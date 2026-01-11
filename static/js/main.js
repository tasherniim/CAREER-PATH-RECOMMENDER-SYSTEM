document.addEventListener('DOMContentLoaded', () => {
      // Initialize confetti effect
      function initConfetti() {
        const canvas = document.getElementById('confetti-canvas');
        const ctx = canvas.getContext('2d');
        
        // Set canvas dimensions
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        // Confetti particles
        const particles = [];
        const particleCount = 150;
        
        // Create particles
        for (let i = 0; i < particleCount; i++) {
          particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 10 + 5,
            speedX: Math.random() * 3 - 1.5,
            speedY: Math.random() * 3 + 1,
            color: `hsl(${Math.random() * 360}, 100%, 60%)`,
            shape: Math.random() > 0.5 ? 'circle' : 'rect'
          });
        }
        
        // Animation function
        function animateConfetti() {
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          
          particles.forEach(p => {
            // Update position
            p.x += p.speedX;
            p.y += p.speedY;
            
            // Reset if out of bounds
            if (p.y > canvas.height) {
              p.y = 0;
              p.x = Math.random() * canvas.width;
            }
            if (p.x > canvas.width) p.x = 0;
            if (p.x < 0) p.x = canvas.width;
            
            // Draw particle
            ctx.fillStyle = p.color;
            if (p.shape === 'circle') {
              ctx.beginPath();
              ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
              ctx.fill();
            } else {
              ctx.fillRect(p.x, p.y, p.size, p.size);
            }
          });
          
          requestAnimationFrame(animateConfetti);
        }
        
        // Start animation
        animateConfetti();
        
        // Resize handler
        window.addEventListener('resize', () => {
          canvas.width = window.innerWidth;
          canvas.height = window.innerHeight;
        });
        
        // Trigger burst effect on title hover
        const title = document.querySelector('.title-container h1');
        title.addEventListener('mouseenter', () => {
          confetti({
            particleCount: 50,
            spread: 70,
            origin: { y: 0.6 }
          });
        });
      }
      
      // Start confetti
      setTimeout(initConfetti, 500);
      
      // Rest of the JavaScript code (same as before, but with stats updates)
      const form = document.getElementById('career-form');
      const errorMsg = document.getElementById('error-msg');
      const resultsOverlay = document.getElementById('results-overlay');
      const resultsModal = document.getElementById('results-modal');
      const resultsCloseBtn = document.getElementById('results-close-btn');
      const resultsContent = document.getElementById('results-content');
      const advisoriesBox = document.getElementById('advisories-box');
      const advisoriesList = document.getElementById('advisories-list');
      const submitBtn = document.getElementById('submit-btn');
      const coursesContainer = document.getElementById('courses-container');
      const addCourseBtn = document.getElementById('add-course-btn');
      const interestsChips = document.getElementById('interests-chips');
      const courseCountEl = document.getElementById('course-count');
      const interestCountEl = document.getElementById('interest-count');
      
      
      // Fetch meta options if available
      fetch('/api/meta')
        .then(r => r.ok ? r.json() : null)
        .then(meta => {
          if (meta) {
            if (Array.isArray(meta.subjects) && meta.subjects.length) {
              SUBJECT_OPTIONS = meta.subjects;
            }
            if (Array.isArray(meta.interests) && meta.interests.length) {
              INTEREST_OPTIONS = meta.interests;
            }
          }
          renderInitialUI();
          refreshCourseOptions();
          updateStats();
        })
        .catch(() => {
          renderInitialUI();
          updateStats();
        });
      
      function updateStats() {
        const courseRows = document.querySelectorAll('.course-row').length;
        courseCountEl.textContent = courseRows;
        
        const selectedInterests = interestsChips.querySelectorAll('input[type="checkbox"]:checked').length;
        interestCountEl.textContent = selectedInterests;
      }
      
      function renderInitialUI() {
        addCourseRow();
        renderInterestChips();
      }
      
      function createCourseSelect() {
        const select = document.createElement('select');
        select.className = 'course-select';
        const defaultOpt = document.createElement('option');
        defaultOpt.value = '';
        defaultOpt.textContent = 'Select a course';
        select.appendChild(defaultOpt);
        
        SUBJECT_OPTIONS.forEach(subj => {
          const opt = document.createElement('option');
          opt.value = subj;
          opt.textContent = subj;
          select.appendChild(opt);
        });
        
        select.addEventListener('change', updateStats);
        
        return select;
      }
      
      function createGradeSelect() {
        const select = document.createElement('select');
        select.className = 'grade-select';
        const defaultOpt = document.createElement('option');
        defaultOpt.value = '';
        defaultOpt.textContent = 'Select grade';
        select.appendChild(defaultOpt);
        
        const grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','E','F'];
        grades.forEach(g => {
          const opt = document.createElement('option');
          opt.value = g;
          opt.textContent = g;
          select.appendChild(opt);
        });
        
        return select;
      }
      
      function addCourseRow() {
        const row = document.createElement('div');
        row.className = 'flex-row course-row';
        
        const courseSelect = createCourseSelect();
        courseSelect.classList.add('course-select');
        courseSelect.addEventListener('change', () => {
          refreshCourseOptions();
          updateStats();
        });
        
        const gradeSelect = createGradeSelect();
        gradeSelect.addEventListener('change', updateStats);
        
        const removeBtn = document.createElement('button');
        removeBtn.type = 'button';
        removeBtn.className = 'btn btn-danger';
        removeBtn.innerHTML = '<i class="fas fa-trash-alt"></i> Remove';
        removeBtn.addEventListener('click', () => {
          coursesContainer.removeChild(row);
          refreshCourseOptions();
          updateStats();
          // Add success confetti
          confetti({
            particleCount: 30,
            spread: 60,
            origin: { x: 0.5, y: 0.5 }
          });
        });
        
        row.appendChild(courseSelect);
        row.appendChild(gradeSelect);
        row.appendChild(removeBtn);
        
        coursesContainer.appendChild(row);
        refreshCourseOptions();
        updateStats();
      }
      
      addCourseBtn.addEventListener('click', () => {
        addCourseRow();
        // Add confetti effect
        confetti({
          particleCount: 20,
          spread: 50,
          origin: { x: 0.5, y: 0.5 }
        });
      });
      
      function getUsedSubjects() {
        const used = new Set();
        document.querySelectorAll('.course-row .course-select').forEach(sel => {
          const v = sel.value.trim();
          if (v) used.add(v);
        });
        return used;
      }
      
      function refreshCourseOptions() {
        const used = getUsedSubjects();
        
        document.querySelectorAll('.course-row .course-select').forEach(select => {
          const currentValue = select.value;
          
          Array.from(select.options).forEach(opt => {
            if (!opt.value) { 
              opt.hidden = false;
              opt.disabled = false;
              return;
            }
            
            const isUsed = used.has(opt.value);
            const isCurrent = opt.value === currentValue;
            
            opt.hidden = isUsed && !isCurrent;
            opt.disabled = isUsed && !isCurrent;
          });
        });
      }
      
      function renderInterestChips() {
        interestsChips.innerHTML = '';
        
        INTEREST_OPTIONS.forEach((label, index) => {
          const chip = document.createElement('label');
          chip.className = 'chip';
          
          const checkbox = document.createElement('input');
          checkbox.type = 'checkbox';
          checkbox.value = label;
          
          const text = document.createElement('span');
          text.className = 'chip-label';
          text.textContent = label;
          
          chip.appendChild(checkbox);
          chip.appendChild(text);
          
          chip.addEventListener('click', (e) => {
            e.preventDefault();
            checkbox.checked = !checkbox.checked;
            chip.classList.toggle('selected', checkbox.checked);
            updateStats();
            
            // Add small confetti effect when selecting an interest
            if (checkbox.checked) {
              confetti({
                particleCount: 10,
                spread: 40,
                origin: { x: e.clientX / window.innerWidth, y: e.clientY / window.innerHeight }
              });
            }
          });
          
          interestsChips.appendChild(chip);
        });
      }
      
      function openResultsModal() {
        resultsOverlay.classList.add('open');
        resultsModal.classList.add('open');
        document.body.style.overflow = 'hidden';
        resultsCloseBtn.focus();
        
        // Add confetti celebration
        confetti({
          particleCount: 100,
          spread: 70,
          origin: { y: 0.6 }
        });
      }
      
      function closeResultsModal() {
        resultsModal.classList.remove('open');
        setTimeout(() => {
          resultsOverlay.classList.remove('open');
        }, 300);
        document.body.style.overflow = '';
      }
      
      resultsCloseBtn.addEventListener('click', closeResultsModal);
      
      resultsOverlay.addEventListener('click', (e) => {
        if (e.target === resultsOverlay) {
          closeResultsModal();
        }
      });
      
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && resultsOverlay.classList.contains('open')) {
          closeResultsModal();
        }
      });
      
      form.addEventListener('submit', async function (e) {
        e.preventDefault();
        errorMsg.textContent = '';
        resultsContent.innerHTML = '';
        advisoriesBox.style.display = 'none';
        advisoriesList.innerHTML = '';
        
        const courses_grades = {};
        const rows = document.querySelectorAll('.course-row');
        for (const row of rows) {
          const course = row.querySelector('.course-select').value.trim();
          const grade = row.querySelector('.grade-select').value.trim();
          if (!course && !grade) {
            continue;
          }
          if (!course || !grade) {
            errorMsg.textContent = 'Please select both course and grade for each filled row.';
            return;
          }
          courses_grades[course] = grade;
        }
        
        const interests = [];
        interestsChips.querySelectorAll('input[type="checkbox"]').forEach(cb => {
          if (cb.checked) interests.push(cb.value);
        });
        
        if (Object.keys(courses_grades).length === 0 && interests.length === 0) {
          errorMsg.textContent = 'Please add at least one course and grade, or select some interests.';
          return;
        }
        
        const payload = {
          interests: interests,
          courses_grades: courses_grades
        };
        
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
        
        try {
          const response = await fetch('/api/recommend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          
          if (!response.ok) {
            throw new Error('Server error: ' + response.status);
          }
          
          const data = await response.json();
          
          resultsContent.innerHTML = '';
          advisoriesBox.style.display = 'none';
          advisoriesList.innerHTML = '';
          
          let careers = [];
          let advisories = [];
          
          if (Array.isArray(data)) {
            careers = data;
          } else if (data && typeof data === 'object') {
            careers = Array.isArray(data.careers) ? data.careers : [];
            advisories = Array.isArray(data.advisories) ? data.advisories : [];
          }
          
          if (!careers.length) {
            resultsContent.innerHTML = '<p>No recommendations available yet. Try adding more courses, grades, or interests to get better matches.</p>';
          } else {
            const list = document.createElement('ol');
            careers.forEach((item, index) => {
              const li = document.createElement('li');
              const probPercent = (item.probability * 100).toFixed(1);
              
              const rank = document.createElement('span');
              rank.style.cssText = 'display:inline-block; width:24px; height:24px; background:linear-gradient(45deg,#667eea,#764ba2); color:white; border-radius:50%; text-align:center; line-height:24px; margin-right:10px; font-size:0.8rem;';
              rank.textContent = index + 1;
              
              const nameSpan = document.createElement('span');
              nameSpan.innerHTML = `<strong>${item.name || ('Career ' + item.career_id)}</strong>`;
              
              const pill = document.createElement('span');
              pill.className = 'match-pill';
              pill.textContent = probPercent + '% match';
              
              li.appendChild(rank);
              li.appendChild(nameSpan);
              li.appendChild(pill);
              list.appendChild(li);
            });
            resultsContent.appendChild(list);
          }
          
          if (advisories.length > 0) {
            advisoriesList.innerHTML = '';
            advisories.forEach(msg => {
              const li = document.createElement('li');
              li.innerHTML = msg;
              advisoriesList.appendChild(li);
            });
            advisoriesBox.style.display = 'block';
          }
          
          openResultsModal();
        } catch (err) {
          console.error('Error in /api/recommend handler:', err);
          errorMsg.textContent = 'Failed to get recommendations. Please try again.';
        } finally {
          submitBtn.disabled = false;
          submitBtn.innerHTML = '<i class="fas fa-rocket"></i> Get Recommendations';
        }
      });
    });