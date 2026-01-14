import math
import csv
from collections import defaultdict
from career_map import (
    INTEREST_DOMAINS,
    DOMAIN_SUBJECT_REQUIREMENTS,
    SUBJECT_BLOCKS,
    CAREER_PROFILES,
    CAREER_REQUIREMENTS,
    normalize_interest,   # NEW: import helper from career_map.py
)

CSV_PATH = "training_data.csv"

GRADE_TO_VALUE = {
    'A+': 4.00,
    'A': 4.00,
    'A-': 3.67,
    'B+': 3.33,
    'B': 3.00,
    'B-': 2.67,
    'C+': 2.33,
    'C': 2.00,
    'C-': 1.67,
    'D+': 1.33,
    'D': 1.00,
    'E': 0.67,
    'F': 0.00,
}


def grade_letter_to_value(letter):
    if letter is None:
        return 0.0
    return GRADE_TO_VALUE.get(str(letter).strip().upper(), 0.0)


class CareerRecommender:
    def __init__(self, csv_path: str = CSV_PATH):
        self.csv_path = csv_path
        self.career_profiles = CAREER_PROFILES
        self.career_priors = {}
        self.feature_probabilities = {}
        self.career_requirements = CAREER_REQUIREMENTS

        self.train_naive_bayes()
        print("Naïve Bayes model trained successfully from CSV data!")

    # -----------------------------
    # TRAINING DATA (same behaviour, but interests normalized)
    # -----------------------------
    def create_training_data(self):
        records = []

        with open(self.csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                career_id = int(row['career'])

                interests = []
                for key, val in row.items():
                    if key.startswith('interest_') and val and val.strip():
                        norm = normalize_interest(val)  # map to canonical tag
                        if norm:
                            interests.append(norm)

                courses_grades = {}
                for key, val in row.items():
                    if key == 'career' or key.startswith('interest_'):
                        continue
                    if val and val.strip():
                        courses_grades[key.strip()] = val.strip().upper()

                records.append({
                    'career': career_id,
                    'interests': interests,
                    'courses_grades': courses_grades,
                })

        return records

    # -----------------------------
    # TRAINING (unchanged)
    # -----------------------------
    def train_naive_bayes(self):
        data = self.create_training_data()

        career_counts = defaultdict(int)
        total_records = len(data)

        feature_counts = {
            'interests': defaultdict(lambda: defaultdict(float)),
            'blocks': defaultdict(lambda: defaultdict(float)),
        }

        for record in data:
            c_id = record['career']
            career_counts[c_id] += 1

            # interests
            for interest in record.get('interests', []):
                feature_counts['interests'][c_id][interest] += 1.0

            # aggregate subjects into blocks
            block_sums = defaultdict(float)
            for subject, letter in record.get('courses_grades', {}).items():
                block = SUBJECT_BLOCKS.get(subject)
                if not block:
                    continue
                grade_value = grade_letter_to_value(letter)
                block_sums[block] += grade_value

            for block_name, total_grade in block_sums.items():
                feature_counts['blocks'][c_id][block_name] += total_grade

        # priors
        self.career_priors = {
            c_id: count / total_records for c_id, count in career_counts.items()
        }

        # conditional probabilities with Laplace smoothing
        self.feature_probabilities = {
            'interests': defaultdict(dict),
            'blocks': defaultdict(dict),
        }

        alpha = 1.0

        for c_id in career_counts.keys():
            # interests
            total_int = sum(feature_counts['interests'][c_id].values())
            uniq_int = len(feature_counts['interests'][c_id]) or 1
            for k, count in feature_counts['interests'][c_id].items():
                self.feature_probabilities['interests'][c_id][k] = (
                    (count + alpha) / (total_int + alpha * (uniq_int + 10))
                )

            # blocks
            total_blocks = sum(feature_counts['blocks'][c_id].values())
            uniq_blocks = len(feature_counts['blocks'][c_id]) or 1
            for k, count in feature_counts['blocks'][c_id].items():
                self.feature_probabilities['blocks'][c_id][k] = (
                    (count + alpha) /
                    (total_blocks + alpha * (uniq_blocks + 10))
                )

    # -----------------------------
    # PROBABILITY FOR ONE CAREER
    # -----------------------------
    def calculate_naive_bayes_probability(self, user_data, career_id):
        prob_log = math.log(self.career_priors.get(career_id, 1e-6))

        # 1. BLOCKS / GRADES
        block_sums = defaultdict(float)
        block_counts = defaultdict(int)

        for subject, letter in user_data.get('courses_grades', {}).items():
            block = SUBJECT_BLOCKS.get(subject)
            if not block:
                continue
            grade_value = grade_letter_to_value(letter)
            block_sums[block] += grade_value
            block_counts[block] += 1

        user_block_strengths = {}
        for block, total_grade in block_sums.items():
            avg_grade = total_grade / max(block_counts[block], 1)
            user_block_strengths[block] = avg_grade

        main_blocks = list(self.feature_probabilities['blocks'][career_id].keys())
        main_block = main_blocks[0] if main_blocks else None
        main_block_avg = user_block_strengths.get(
            main_block,
            grade_letter_to_value("C-")
        )

        low_grade_threshold = grade_letter_to_value("C")

        if main_block is not None and main_block_avg < low_grade_threshold:
            prob_log -= 8.0

        # 2. INTERESTS (same NB term; UI interests already normalized in app.py)
        INTEREST_SCALE = 0.5
        for interest in user_data.get('interests', []):
            p = self.feature_probabilities['interests'][career_id].get(interest, 1e-6)
            prob_log += INTEREST_SCALE * math.log(p)

        # 3. BLOCK WEIGHTING
        for block, avg_grade in user_block_strengths.items():
            base_p = self.feature_probabilities['blocks'][career_id].get(block, 1e-6)
            log_base = math.log(base_p)

            if avg_grade <= grade_letter_to_value("C-"):
                weight = - (1.0 - avg_grade / 4.0)
            else:
                weight = avg_grade / 4.0

            prob_log += weight * log_base

        # 4. HARD REQUIREMENT PENALTY (new but simple)
        reqs = self.career_requirements.get(career_id, {}).get("min_grade_subjects", {})
        for subject, min_letter in reqs.items():
            user_letter = user_data.get('courses_grades', {}).get(subject)
            if not user_letter:
                prob_log -= 15.0
                continue
            user_val = grade_letter_to_value(user_letter)
            min_val = grade_letter_to_value(min_letter)
            if user_val < min_val:
                prob_log -= 15.0

        return prob_log

    # -----------------------------
    # DOMAIN ADVISORIES (unchanged)
    # -----------------------------
    def compute_domain_advisories(self, user_data):
        user_interests = {i.strip().lower() for i in user_data.get("interests", [])}
        user_domains = {INTEREST_DOMAINS[i] for i in user_interests if i in INTEREST_DOMAINS}

        if not user_domains:
            return []

        advisories = []
        user_grades = user_data.get("courses_grades", {})

        for domain in user_domains:
            reqs = DOMAIN_SUBJECT_REQUIREMENTS.get(domain, {})
            failed_subjects = []

            for subject, min_letter in reqs.items():
                if subject not in user_grades:
                    continue

                user_letter = user_grades.get(subject)
                user_val = grade_letter_to_value(user_letter)
                min_val = grade_letter_to_value(min_letter)

                if user_val < min_val or user_val <= grade_letter_to_value("C-"):
                    failed_subjects.append((subject, user_letter, min_letter))

            if failed_subjects:
                domain_name = domain.capitalize()
                subjects_list = ", ".join(s for (s, _, _) in failed_subjects)
                advisories.append(
                    f'You have taken interest in {domain_name}-related areas, but your '
                    f'grades in core subject like <strong>{subjects_list}</strong> are below the minimum '
                    f'requirements. It is not advised to pursue {domain_name}-related '
                    f'careers without improving these subjects.'
                )

        return advisories

    # -----------------------------
    # RECOMMEND (unchanged)
    # -----------------------------
    def recommend(self, user_data, top_k=3):
        scores = []
        for c_id in self.career_profiles.keys():
            log_p = self.calculate_naive_bayes_probability(user_data, c_id)
            scores.append((c_id, log_p))

        if not scores:
            return {"careers": [], "advisories": []}

        max_log_p = max(s for _, s in scores)
        normalized = []
        for c_id, log_p in scores:
            p = math.exp(log_p - max_log_p)
            normalized.append((c_id, p))

        total = sum(p for _, p in normalized) or 1.0
        normalized = [(c_id, p / total) for c_id, p in normalized]

        top_list = sorted(normalized, key=lambda x: x[1], reverse=True)[:top_k]

        career_results = []
        for c_id, prob in top_list:
            career_results.append((c_id, prob))

        domain_advisories = self.compute_domain_advisories(user_data)

        return {
            "careers": career_results,
            "advisories": domain_advisories,
        }

    def get_career_info(self, career_id):
        return self.career_profiles.get(career_id, {})

    def get_all_subjects(self):
        subjects = set()
        for profile in self.career_profiles.values():
            for s in profile.get("subjects", []):
                subjects.add(s)
        return sorted(subjects)

    def get_all_interests(self):
        interests = set()
        for profile in self.career_profiles.values():
            for i in profile.get("interests", []):
                interests.add(i)
        return sorted(interests)
