SUBJECT_OPTIONS = [
    "Big Data Analytics and Development",
    "Computational Intelligence",
    "Computer and Network Security",
    "Computer Graphics and Visualisation",
    "Computer Networks",
    "Computer Organisation and Architecture",
    "Cryptography",
    "Data Structures",
    "Database Systems",
    "Digital Forensics",
    "E-Commerce",
    "File System Forensics",
    "Fundamentals of Programming",
    "Human-Computer Interaction",
    "Information Security Management",
    "Introduction to Data Analytics",
    "Network Forensics",
    "Object-oriented Programming",
    "Operating Systems",
    "Software Engineering and Design",
    "Statistics",
    "Web Programming and Development",
    "Wireless Network Security"
      ]
      
INTEREST_OPTIONS = [
    # software / coding / web
    "software development",
    "web development",
    "coding",
    "mobile development",
    "game development",

    # data / AI / analytics / research
    "data",
    "machine learning",
    "statistics",
    "data engineering",
    "business intelligence",
    "research and academia",

    # network / security / forensics
    "network",
    "security",
    "cybersecurity",
    "forensics",

    # ui/ux / product / digital
    "UI/UX",
    "product management",
    "digital marketing",

    # cloud / devops / reliability
    "cloud",
    "devops",
    "site reliability",

    # business / domain-focused
    "ecommerce and fintech",
]

INTEREST_DOMAINS = {
    # software
    "software development": "software",
    "web development": "software",
    "coding": "software",
    "mobile development": "software",
    "game development": "software",

    # data
    "data": "data",
    "machine learning": "data",
    "statistics": "data",
    "data engineering": "data",
    "business intelligence": "data",
    "research and academia": "data",

    # security / network
    "network": "security",
    "security": "security",
    "cybersecurity": "security",
    "forensics": "security",

    # ui/ux / product / digital
    "UI/UX": "uiux",
    "product management": "uiux",
    "digital marketing": "uiux",

    # cloud / devops / reliability
    "cloud": "cloud",
    "devops": "cloud",
    "site reliability": "cloud",

    # business / domain
    "ecommerce and fintech": "business",
}

DOMAIN_SUBJECT_REQUIREMENTS = {
    # strong in programming / software engineering
    "software": {
        "Fundamentals of Programming": "C",
        "Object-oriented Programming": "C",
        "Data Structures": "C",
        "Software Engineering and Design": "C-",
    },

    # strong in statistics + analytics + big data
    "data": {
        "Statistics": "C",
        "Introduction to Data Analytics": "C",
        "Big Data Analytics and Development": "C-",
    },

    # strong in networks + security fundamentals
    "security": {
        "Computer Networks": "C",
        "Computer and Network Security": "C-",
        "Information Security Management": "C-",
    },

    # strong in HCI / UX
    "uiux": {
        "Human-Computer Interaction": "C-",
    },

    # strong in OS + networks + security (for cloud/devops)
    "cloud": {
        "Operating Systems": "C",
        "Computer Networks": "C",
        "Computer and Network Security": "C-",
    },

    # strong in web + DB + basic analytics (for business/e‑commerce)
    "business": {
        "E-Commerce": "C",
        "Database Systems": "C-",
        "Introduction to Data Analytics": "C-",
    },
}

# INTERNAL: multi-tag version (for you to maintain)
SUBJECT_BLOCK_TAGS = {
    "Fundamentals of Programming": ["programming"],
    "Object-oriented Programming": ["programming"],
    "Data Structures": ["programming"],
    "Software Engineering and Design": ["programming"],
    "Web Programming and Development": ["programming", "web"],
    "Computer Organisation and Architecture": ["programming"],

    "Statistics": ["data"],
    "Introduction to Data Analytics": ["data", "business"],
    "Big Data Analytics and Development": ["data", "data engineering"],
    "Computational Intelligence": ["data", "ai"],

    "Computer Networks": ["security", "cloud"],
    "Operating Systems": ["security", "cloud", "infrastructure"],
    "Computer and Network Security": ["security", "cloud"],
    "Information Security Management": ["security", "business"],
    "Wireless Network Security": ["security", "cloud"],
    "Cryptography": ["security"],

    "Digital Forensics": ["security", "forensics"],
    "File System Forensics": ["security", "forensics"],
    "Network Forensics": ["security", "forensics"],

    "Database Systems": ["web", "data", "business"],
    "Human-Computer Interaction": ["web", "uiux"],
    "Computer Graphics and Visualisation": ["web", "uiux"],
    "E-Commerce": ["web", "business"],
}

# Public: single main block per subject for the Naive Bayes model
SUBJECT_BLOCKS = {
    subject: tags[0] if isinstance(tags, list) and tags else tags
    for subject, tags in SUBJECT_BLOCK_TAGS.items()
}



CAREER_PROFILES = {
    1: {
        'name': 'Software Engineer',
        'description': 'Design, develop and maintain software systems and applications',
        'subjects': [
            'Fundamentals of Programming',
            'Object-oriented Programming',
            'Data Structures',
            'Software Engineering and Design',
            'Database Systems',
            'Web Programming and Development',
        ],
        'interests': [
            'software development',
            'web development',
            'coding',
            'applications',
            'problem solving',
        ],
    },
    2: {
        'name': 'Data Scientist',
        'description': 'Analyze data and build predictive models',
        'subjects': [
            'Statistics',
            'Discrete Mathematics',
            'Introduction to Data Analytics',
            'Big Data Analytics and Development',
            'Computational Intelligence',
        ],
        'interests': [
            'data',
            'analytics',
            'machine learning',
            'statistics',
            'research',
        ],
    },
    3: {
        'name': 'Network Security Engineer',
        'description': 'Design and secure computer networks',
        'subjects': [
            'Computer Networks',
            'Operating Systems',
            'Computer and Network Security',
            'Wireless Network Security',
            'Cryptography',
        ],
        'interests': [
            'network',
            'security',
            'infrastructure',
        ],
    },
    4: {
        'name': 'Cybersecurity Analyst',
        'description': 'Investigate and prevent cyber attacks',
        'subjects': [
            'Computer and Network Security',
            'Information Security Management',
            'Digital Forensics',
            'Ethical Hacker',
            'File System Forensics',
            'Network Forensics',
        ],
        'interests': [
            'security',
            'cybersecurity',
            'forensics',
        ],
    },
    5: {
        'name': 'Web Developer',
        'description': 'Build and maintain web applications',
        'subjects': [
            'Fundamentals of Programming',
            'Web Programming and Development',
            'Database Systems',
            'Human-Computer Interaction',
            'E-Commerce',
        ],
        'interests': [
            'web development',
            'frontend',
            'backend',
            'ui/ux',
        ],
    },
    6: {
        'name': 'Mobile Application Developer',
        'description': 'Develop and maintain mobile applications for Android and iOS',
        'subjects': [
            'Fundamentals of Programming',
            'Object-oriented Programming',
            'Data Structures',
            'Software Engineering and Design',
            'Web Programming and Development',
        ],
        'interests': [
            'software development',
            'mobile development',
            'coding',
            'web development',
        ],
    },
    7: {
        'name': 'Full-Stack Developer',
        'description': 'Develop both frontend and backend of web applications',
        'subjects': [
            'Fundamentals of Programming',
            'Object-oriented Programming',
            'Data Structures',
            'Web Programming and Development',
            'Database Systems',
            'Human-Computer Interaction',
        ],
        'interests': [
            'software development',
            'web development',
            'coding',
            'ui/ux',
        ],
    },
    8: {
        'name': 'Software QA Engineer',
        'description': 'Design and execute tests to ensure software quality',
        'subjects': [
            'Fundamentals of Programming',
            'Software Engineering and Design',
            'Web Programming and Development',
            'Database Systems',
        ],
        'interests': [
            'software development',
            'coding',
            'devops',
        ],
    },
    9: {
        'name': 'Systems Analyst',
        'description': 'Analyze requirements and design effective IT systems',
        'subjects': [
            'Software Engineering and Design',
            'Database Systems',
            'Web Programming and Development',
            'E-Commerce',
        ],
        'interests': [
            'software development',
            'product management',
            'ecommerce and fintech',
        ],
    },
    10: {
        'name': 'Game Developer',
        'description': 'Create interactive games and simulations',
        'subjects': [
            'Fundamentals of Programming',
            'Object-oriented Programming',
            'Data Structures',
            'Computer Graphics and Visualisation',
        ],
        'interests': [
            'game development',
            'software development',
            'coding',
        ],
    },
    11: {
        'name': 'Data Analyst',
        'description': 'Analyze and visualize data to support decisions',
        'subjects': [
            'Statistics',
            'Introduction to Data Analytics',
            'Big Data Analytics and Development',
            'Database Systems',
        ],
        'interests': [
            'data',
            'statistics',
            'business intelligence',
        ],
    },
    12: {
        'name': 'Business Intelligence Analyst',
        'description': 'Build dashboards and reports for business stakeholders',
        'subjects': [
            'Statistics',
            'Introduction to Data Analytics',
            'Big Data Analytics and Development',
            'Database Systems',
            'E-Commerce',
        ],
        'interests': [
            'business intelligence',
            'data',
            'statistics',
        ],
    },
    13: {
        'name': 'Data Engineer',
        'description': 'Design and maintain data pipelines and infrastructure',
        'subjects': [
            'Introduction to Data Analytics',
            'Big Data Analytics and Development',
            'Database Systems',
            'Computer Networks',
        ],
        'interests': [
            'data engineering',
            'data',
            'cloud',
        ],
    },
    14: {
        'name': 'Machine Learning Engineer',
        'description': 'Build and deploy machine learning models',
        'subjects': [
            'Statistics',
            'Introduction to Data Analytics',
            'Big Data Analytics and Development',
            'Computational Intelligence',
            'Fundamentals of Programming',
        ],
        'interests': [
            'machine learning',
            'data',
            'statistics',
            'research and academia',
        ],
    },
    15: {
        'name': 'Information Security Analyst',
        'description': 'Protect systems and data from cyber threats',
        'subjects': [
            'Computer Networks',
            'Operating Systems',
            'Computer and Network Security',
            'Information Security Management',
        ],
        'interests': [
            'security',
            'cybersecurity',
            'network',
        ],
    },
    16: {
        'name': 'SOC Analyst',
        'description': 'Monitor and respond to security incidents in a SOC environment',
        'subjects': [
            'Computer Networks',
            'Computer and Network Security',
            'Information Security Management',
            'Digital Forensics',
            'Network Forensics',
        ],
        'interests': [
            'security',
            'cybersecurity',
            'forensics',
            'network',
        ],
    },
    17: {
        'name': 'Digital Forensics Investigator',
        'description': 'Investigate digital evidence for security incidents',
        'subjects': [
            'Digital Forensics',
            'File System Forensics',
            'Network Forensics',
            'Computer and Network Security',
        ],
        'interests': [
            'forensics',
            'security',
            'cybersecurity',
        ],
    },
    18: {
        'name': 'Network Engineer',
        'description': 'Design and manage computer networks',
        'subjects': [
            'Computer Networks',
            'Operating Systems',
            'Wireless Network Security',
            'Computer and Network Security',
        ],
        'interests': [
            'network',
            'security',
            'cloud',
        ],
    },
    19: {
        'name': 'Cloud Engineer',
        'description': 'Design and maintain cloud infrastructure and services',
        'subjects': [
            'Computer Networks',
            'Operating Systems',
            'Computer and Network Security',
            'Web Programming and Development',
        ],
        'interests': [
            'cloud',
            'devops',
            'software development',
            'network',
        ],
    },
    20: {
        'name': 'DevOps Engineer',
        'description': 'Automate deployment and infrastructure for software systems',
        'subjects': [
            'Computer Networks',
            'Operating Systems',
            'Computer and Network Security',
            'Web Programming and Development',
        ],
        'interests': [
            'cloud',
            'devops',
            'software development',
            'network',
        ],
    },
    21: {
        'name': 'UI/UX Designer',
        'description': 'Design user interfaces and user experiences for digital products',
        'subjects': [
            'Human-Computer Interaction',
            'Computer Graphics and Visualisation',
            'Web Programming and Development',
            'E-Commerce',
        ],
        'interests': [
            'ui/ux',
            'web development',
            'product management',
            'digital marketing',
        ],
    },
    22: {
        'name': 'Product Manager',
        'description': 'Define product vision and coordinate cross-functional delivery',
        'subjects': [
            'Software Engineering and Design',
            'Web Programming and Development',
            'Database Systems',
            'E-Commerce',
            'Introduction to Data Analytics',
        ],
        'interests': [
            'product management',
            'software development',
            'ecommerce and fintech',
            'business intelligence',
        ],
    },
    23: {
        'name': 'E-Commerce Specialist',
        'description': 'Manage and optimize e-commerce platforms and digital sales',
        'subjects': [
            'E-Commerce',
            'Web Programming and Development',
            'Database Systems',
            'Introduction to Data Analytics',
        ],
        'interests': [
            'ecommerce and fintech',
            'web development',
            'digital marketing',
        ],
    },
    24: {
        'name': 'Digital Marketing Technologist',
        'description': 'Use technology and data to run and optimize digital campaigns',
        'subjects': [
            'E-Commerce',
            'Introduction to Data Analytics',
            'Database Systems',
        ],
        'interests': [
            'digital marketing',
            'business intelligence',
            'ecommerce and fintech',
        ],
    },
}

CAREER_REQUIREMENTS = {
    1: {  # Software Engineer
        "min_grade_subjects": {
            "Fundamentals of Programming": "C",
            "Object-oriented Programming": "C",
            "Data Structures": "C",
            "Software Engineering and Design": "A",
        }
    },
    2: {  # Data Scientist
        "min_grade_subjects": {
            "Statistics": "C",
            "Introduction to Data Analytics": "C",
            "Big Data Analytics and Development": "C-",
        }
    },
    3: {  # Network Security Engineer
        "min_grade_subjects": {
            "Computer Networks": "C",
            "Operating Systems": "C-",
            "Computer and Network Security": "C-",
        }
    },
    4: {  # Cybersecurity Analyst
        "min_grade_subjects": {
            "Computer and Network Security": "C",
            "Information Security Management": "C",
            "Digital Forensics": "C-",
        }
    },
    5: {  # Web Developer
        "min_grade_subjects": {
            "Fundamentals of Programming": "C",
            "Web Programming and Development": "C",
            "Database Systems": "C-",
            "Human-Computer Interaction": "C-",
        }
    },
    6: {  # Mobile Application Developer
        "min_grade_subjects": {
            "Fundamentals of Programming": "C",
            "Object-oriented Programming": "C",
            "Data Structures": "C-",
        }
    },
    7: {  # Full-Stack Developer
        "min_grade_subjects": {
            "Fundamentals of Programming": "C",
            "Web Programming and Development": "C",
            "Database Systems": "C-",
        }
    },
    8: {  # Software QA Engineer
        "min_grade_subjects": {
            "Fundamentals of Programming": "C-",
            "Software Engineering and Design": "C",
        }
    },
    9: {  # Systems Analyst
        "min_grade_subjects": {
            "Software Engineering and Design": "C",
            "Database Systems": "C-",
        }
    },
    10: {  # Game Developer
        "min_grade_subjects": {
            "Fundamentals of Programming": "C",
            "Computer Graphics and Visualisation": "C-",
        }
    },
    11: {  # Data Analyst
        "min_grade_subjects": {
            "Statistics": "C",
            "Introduction to Data Analytics": "C",
        }
    },
    12: {  # Business Intelligence Analyst
        "min_grade_subjects": {
            "Statistics": "C",
            "Introduction to Data Analytics": "C",
            "Database Systems": "C-",
        }
    },
    13: {  # Data Engineer
        "min_grade_subjects": {
            "Introduction to Data Analytics": "C",
            "Big Data Analytics and Development": "C-",
        }
    },
    14: {  # Machine Learning Engineer
        "min_grade_subjects": {
            "Statistics": "C",
            "Computational Intelligence": "C",
        }
    },
    15: {  # Information Security Analyst
        "min_grade_subjects": {
            "Operating Systems": "C-",
            "Computer and Network Security": "C",
        }
    },
    16: {  # SOC Analyst
        "min_grade_subjects": {
            "Computer and Network Security": "C",
            "Information Security Management": "C",
            "Digital Forensics": "C-",
        }
    },
    17: {  # Digital Forensics Investigator
        "min_grade_subjects": {
            "Digital Forensics": "C",
            "File System Forensics": "C-",
        }
    },
    18: {  # Network Engineer
        "min_grade_subjects": {
            "Computer Networks": "C",
            "Operating Systems": "C-",
        }
    },
    19: {  # Cloud Engineer
        "min_grade_subjects": {
            "Computer Networks": "C",
            "Operating Systems": "C",
        }
    },
    20: {  # DevOps Engineer
        "min_grade_subjects": {
            "Operating Systems": "C",
            "Software Engineering and Design": "C",
        }
    },
    21: {  # UI/UX Designer
        "min_grade_subjects": {
            "Human-Computer Interaction": "C",
        }
    },
    22: {  # Product Manager
        "min_grade_subjects": {
            "Software Engineering and Design": "B-",
            "E-Commerce": "C-",
        }
    },
    23: {  # E-Commerce Specialist
        "min_grade_subjects": {
            "E-Commerce": "C",
            "Web Programming and Development": "C-",
        }
    },
    24: {  # Digital Marketing Technologist
        "min_grade_subjects": {
            "E-Commerce": "C-",
            "Introduction to Data Analytics": "C-",
        }
    },

}
