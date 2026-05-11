// Nexus AI Landing Page Scripts

document.addEventListener('DOMContentLoaded', () => {
    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(9, 9, 11, 0.9)';
            navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.5)';
            navbar.style.padding = '0.75rem 5%';
        } else {
            navbar.style.background = 'rgba(9, 9, 11, 0.7)';
            navbar.style.boxShadow = 'none';
            navbar.style.padding = '1rem 5%';
        }
    });

    // Smooth Scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Simple reveal animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Apply animation classes to elements
    const animateElements = document.querySelectorAll('.model-card, .bento-item, .price-card, .section-header, .how-step');
    
    animateElements.forEach(el => {
        el.style.opacity = "0";
        el.style.transform = "translateY(30px)";
        el.style.transition = "all 0.6s cubic-bezier(0.4, 0, 0.2, 1)";
        observer.observe(el);
    });

    // Modal Logic
    const modal = document.getElementById('demo-modal');
    const closeBtn = document.querySelector('.close-modal');
    const triggers = document.querySelectorAll('.demo-trigger');

    triggers.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            modal.classList.add('active');
        });
    });

    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            modal.classList.remove('active');
        });
    }

    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });
    }

    // Form submission mock
    const demoForm = document.getElementById('demo-form');
    if (demoForm) {
        demoForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = demoForm.querySelector('button');
            btn.innerHTML = '<i class="fa-solid fa-check"></i> Talebiniz Alındı';
            btn.style.background = 'var(--success-color, #10b981)';
            setTimeout(() => {
                modal.classList.remove('active');
                btn.innerHTML = 'Talebi Gönder';
                btn.style.background = '';
                demoForm.reset();
            }, 2500);
        });
    }

    // ROI Calculator Logic
    const leadsInput = document.getElementById('monthly-leads');
    const valueInput = document.getElementById('avg-value');
    const staffInput = document.getElementById('staff-cost');
    
    if (leadsInput && valueInput && staffInput) {
        const leadsVal = document.getElementById('leads-val');
        const valueVal = document.getElementById('value-val');
        const staffVal = document.getElementById('staff-val');
        
        const savedHours = document.getElementById('saved-hours');
        const extraSales = document.getElementById('extra-sales');
        const totalRoi = document.getElementById('total-roi');

        function calculateROI() {
            const leads = parseInt(leadsInput.value);
            const value = parseInt(valueInput.value);
            const staff = parseInt(staffInput.value);

            // Update Labels
            leadsVal.innerText = leads.toLocaleString('tr-TR');
            valueVal.innerText = value.toLocaleString('tr-TR');
            staffVal.innerText = staff.toLocaleString('tr-TR');

            // Logic:
            // Assuming 15 minutes saved per lead (0.25 hours)
            const hours = Math.round(leads * 0.25);
            // Assuming a 3% increase in conversion rate due to 24/7 instant response
            const sales = Math.round(leads * 0.03);
            // Total ROI = (Saved hours * Staff Cost) + (Extra Sales * Average Value)
            const roi = (hours * staff) + (sales * value);

            // Update Results
            savedHours.innerText = hours.toLocaleString('tr-TR');
            extraSales.innerText = sales.toLocaleString('tr-TR');
            totalRoi.innerText = roi.toLocaleString('tr-TR');
        }

        // Add event listeners
        [leadsInput, valueInput, staffInput].forEach(input => {
            input.addEventListener('input', calculateROI);
        });

        // Initial calculation
        calculateROI();
    }
});
