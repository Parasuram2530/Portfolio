document.addEventListener('DOMContentLoaded', () => {
    // Initialize AOS
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            mirror: false
        });
    }

    // Theme Toggle Logic
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }

    // Mobile Toggle Logic
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navLinksContainer = document.querySelector('.nav-links');
    const navLinksItems = document.querySelectorAll('.nav-link');

    if (mobileToggle && navLinksContainer) {
        mobileToggle.addEventListener('click', () => {
            navLinksContainer.classList.toggle('active');
            const icon = mobileToggle.querySelector('i');
            if (navLinksContainer.classList.contains('active')) {
                icon.className = 'fa-solid fa-xmark';
            } else {
                icon.className = 'fa-solid fa-bars-staggered';
            }
        });

        // Close menu when clicking a link
        navLinksItems.forEach(link => {
            link.addEventListener('click', () => {
                navLinksContainer.classList.remove('active');
                const icon = mobileToggle.querySelector('i');
                if (icon) {
                    icon.className = 'fa-solid fa-bars-staggered';
                }
            });
        });
    }



    // Navbar Scroll Effect
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Current Year for Footer
    const yearSpan = document.getElementById('current-year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // Active link highlighting via IntersectionObserver
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    if (sections.length > 0 && navLinks.length > 0) {
        const observerOptions = {
            root: null,
            rootMargin: '-50% 0px -50% 0px',
            threshold: 0
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');
                    navLinks.forEach(link => {
                        link.classList.remove('active');
                        if (link.getAttribute('href').includes(`#${id}`)) {
                            link.classList.add('active');
                        }
                    });
                }
            });
        }, observerOptions);

        sections.forEach(section => {
            observer.observe(section);
        });
    }





    // Skills Filter Logic
    const filterBtns = document.querySelectorAll('.cat-pill');
    const skillCards = document.querySelectorAll('.skill-card');

    if (filterBtns.length > 0 && skillCards.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class from all
                filterBtns.forEach(b => b.classList.remove('active'));
                // Add to clicked
                btn.classList.add('active');

                const filterValue = btn.getAttribute('data-filter');

                skillCards.forEach(card => {
                    if (filterValue === 'all' || card.getAttribute('data-category') === filterValue) {
                        card.style.display = 'flex';
                        // Trigger reflow
                        void card.offsetWidth;
                        card.classList.remove('hidden');
                    } else {
                        card.classList.add('hidden');
                        setTimeout(() => {
                            if (card.classList.contains('hidden')) {
                                card.style.display = 'none';
                            }
                        }, 250);
                    }
                });
            });
        });
    }

    // Skills Progress Ring Animation using Intersection Observer
    const progressRings = document.querySelectorAll('.progress-ring__circle');

    if (progressRings.length > 0 && skillCards.length > 0) {
        const radius = 36;
        const circumference = radius * 2 * Math.PI;

        progressRings.forEach(ring => {
            ring.style.strokeDasharray = `${circumference} ${circumference}`;
            ring.style.strokeDashoffset = circumference;
        });

        const animateProgress = (entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const card = entry.target;
                    const ring = card.querySelector('.progress-ring__circle');
                    const text = card.querySelector('.progress-text');
                    
                    if (ring && text && !card.classList.contains('animated')) {
                        const targetProgress = parseInt(ring.getAttribute('data-progress')) || 0;
                        
                        // Animate SVG stroke
                        const offset = circumference - (targetProgress / 100) * circumference;
                        ring.style.strokeDashoffset = offset;

                        // Animate number
                        let current = 0;
                        const duration = 1400; // 1.4s
                        const increment = targetProgress / (duration / 16);
                        
                        const updateCounter = () => {
                            current += increment;
                            if (current < targetProgress) {
                                text.textContent = Math.floor(current);
                                requestAnimationFrame(updateCounter);
                            } else {
                                text.textContent = targetProgress;
                            }
                        };
                        
                        requestAnimationFrame(updateCounter);
                        card.classList.add('animated');
                    }
                    observer.unobserve(card);
                }
            });
        };

        const progressObserver = new IntersectionObserver(animateProgress, {
            root: null,
            threshold: 0.1
        });

        skillCards.forEach(card => {
            progressObserver.observe(card);
        });
    }

    // Projects Filter Logic
    const projFilterBtns = document.querySelectorAll('.proj-filter-btn');
    const allProjCards = document.querySelectorAll('.all-proj-card');

    if (projFilterBtns.length > 0 && allProjCards.length > 0) {
        projFilterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                projFilterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filterValue = btn.getAttribute('data-filter');

                allProjCards.forEach(card => {
                    if (filterValue === 'all' || card.getAttribute('data-category') === filterValue) {
                        card.classList.remove('hidden');
                    } else {
                        card.classList.add('hidden');
                    }
                });
            });
        });
    }

    // Project Modal Logic
    const modal = document.getElementById('projectModal');
    const modalClose = document.getElementById('modalClose');
    const triggers = document.querySelectorAll('.project-card-trigger');

    if (modal && triggers.length > 0) {
        triggers.forEach(trigger => {
            trigger.addEventListener('click', (e) => {
                // Prevent trigger if clicking on links within card
                if (e.target.closest('a') || e.target.closest('.bento-icon') || e.target.closest('.all-proj-icons')) return;

                const title = trigger.getAttribute('data-title');
                const tagline = trigger.getAttribute('data-tagline');
                const desc = trigger.getAttribute('data-desc');
                const tech = trigger.getAttribute('data-tech');
                const status = trigger.getAttribute('data-status');
                const dates = trigger.getAttribute('data-dates');
                const github = trigger.getAttribute('data-github');
                const live = trigger.getAttribute('data-live');

                document.getElementById('modalTitle').textContent = title;
                document.getElementById('modalTagline').textContent = tagline;
                document.getElementById('modalDesc').textContent = desc || "No description provided.";
                document.getElementById('modalDates').textContent = dates;

                // Status Badge
                const statusEl = document.getElementById('modalStatus');
                statusEl.className = `status-badge status-${status.toLowerCase().replace(' ', '-')}`;
                statusEl.innerHTML = status === 'Ongoing' ? `🔴 ${status}` : `✅ ${status}`;

                // Tech Pills
                const techEl = document.getElementById('modalTech');
                techEl.innerHTML = '';
                if (tech) {
                    tech.split(',').forEach(t => {
                        const span = document.createElement('span');
                        span.className = 'tech-pill-small';
                        span.textContent = t.trim();
                        techEl.appendChild(span);
                    });
                }

                // Actions
                const actionsEl = document.getElementById('modalActions');
                actionsEl.innerHTML = '';
                if (github) {
                    const a = document.createElement('a');
                    a.href = github;
                    a.target = '_blank';
                    a.className = 'btn-outline';
                    a.innerHTML = '<i class="fa-brands fa-github"></i> GitHub';
                    actionsEl.appendChild(a);
                }
                if (live) {
                    const a = document.createElement('a');
                    a.href = live;
                    a.target = '_blank';
                    a.className = 'btn-primary';
                    a.innerHTML = '<i class="fa-solid fa-arrow-up-right-from-square"></i> Live Demo';
                    actionsEl.appendChild(a);
                }

                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        });

        const closeModal = () => {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        };

        modalClose.addEventListener('click', closeModal);
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal();
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modal.classList.contains('active')) closeModal();
        });
    }

    // Tabs Logic
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    if (tabBtns.length > 0 && tabPanes.length > 0) {
        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active from all
                tabBtns.forEach(b => b.classList.remove('active'));
                tabPanes.forEach(p => p.classList.remove('active'));

                // Add active to clicked
                btn.classList.add('active');
                const targetId = btn.getAttribute('data-target');
                document.getElementById(targetId).classList.add('active');
            });
        });
    }

    // Toast System
    window.showToast = function(msg, type = 'success') {
        const container = document.getElementById('toastContainer');
        if (!container) return;

        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        
        let icon = 'fa-circle-check';
        if (type === 'error') icon = 'fa-circle-xmark';
        if (type === 'info') icon = 'fa-circle-info';

        toast.innerHTML = `
            <div class="toast-icon"><i class="fa-solid ${icon}"></i></div>
            <div class="toast-content">${msg}</div>
        `;
        
        container.appendChild(toast);
        
        // Trigger reflow for animation
        setTimeout(() => toast.classList.add('show'), 10);
        
        // Remove after 3.2s
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300); // Wait for transition
        }, 3200);
    };

    // Click to copy
    const copyTriggers = document.querySelectorAll('.copy-trigger');
    copyTriggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const textToCopy = trigger.getAttribute('data-copy');
            navigator.clipboard.writeText(textToCopy).then(() => {
                const icon = trigger.querySelector('.copy-icon');
                icon.className = 'fa-solid fa-check copy-icon';
                icon.style.color = 'var(--accent)';
                window.showToast('Email copied to clipboard!', 'success');
                
                setTimeout(() => {
                    icon.className = 'fa-regular fa-copy copy-icon';
                    icon.style.color = '';
                }, 2000);
            });
        });
    });

    // CSRF Cookie Helper
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Contact Form AJAX
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const submitBtn = document.getElementById('submitBtn');
            const btnText = submitBtn.querySelector('.btn-text');
            const btnSpinner = submitBtn.querySelector('.btn-spinner');
            
            // Loading state
            submitBtn.disabled = true;
            btnText.classList.add('hidden');
            btnSpinner.classList.remove('hidden');

            const formData = new FormData(this);
            const csrftoken = getCookie('csrftoken');

            fetch('/contact/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'Accept': 'application/json'
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.showToast("Message sent! I'll get back within 24 hours 🚀", 'success');
                    contactForm.reset();
                } else {
                    window.showToast(data.message || "Something went wrong.", 'error');
                }
            })
            .catch(error => {
                window.showToast("Network error. Please try again.", 'error');
            })
            .finally(() => {
                // Reset button state
                submitBtn.disabled = false;
                btnText.classList.remove('hidden');
                btnSpinner.classList.add('hidden');
            });
        });
    }
    // Typewriter Effect
    const typewriterElement = document.querySelector('.typewriter-text');
    if (typewriterElement) {
        const roles = ["GenAI Developer", "AI/ML Engineer", "Backend Developer", "Python Enthusiast"];
        let roleIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        let typeSpeed = 100;

        function type() {
            const currentRole = roles[roleIndex];
            
            if (isDeleting) {
                typewriterElement.textContent = currentRole.substring(0, charIndex - 1);
                charIndex--;
                typeSpeed = 50;
            } else {
                typewriterElement.textContent = currentRole.substring(0, charIndex + 1);
                charIndex++;
                typeSpeed = 100;
            }

            if (!isDeleting && charIndex === currentRole.length) {
                isDeleting = true;
                typeSpeed = 2000; // Pause at end
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                roleIndex = (roleIndex + 1) % roles.length;
                typeSpeed = 500; // Pause before next role
            }

            setTimeout(type, typeSpeed);
        }

        type();
    }
});
