import { db } from './firebase-config.js';
import { doc, setDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

// ── Theme ──

function initTheme() {
    const saved = localStorage.getItem('logiclab_theme');
    if (saved === 'dark') {
        document.documentElement.classList.add('dark-mode');
        document.body.classList.add('dark-mode');
    } else if (saved === 'light') {
        document.documentElement.classList.remove('dark-mode');
        document.body.classList.remove('dark-mode');
    } else {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.classList.add('dark-mode');
            document.body.classList.add('dark-mode');
        }
    }
    updateLogo();
}

let _basePath = null;

function getBasePath() {
    if (_basePath !== null) return _basePath;
    const logo = document.querySelector('.logo');
    if (!logo) return '';
    const src = logo.getAttribute('src');
    const lastSlash = src.lastIndexOf('/');
    _basePath = lastSlash >= 0 ? src.substring(0, lastSlash + 1) : '';
    return _basePath;
}

function updateLogo() {
    const logo = document.querySelector('.logo');
    if (!logo) return;
    const base = getBasePath();
    const isDark = document.body.classList.contains('dark-mode');
    logo.src = isDark ? base + 'AppIconDark.png' : base + 'Logo.png';
}

let isSwitching = false;

function toggleTheme() {
    const logo = document.querySelector('.logo');
    if (isSwitching) return;
    isSwitching = true;

    if (logo) {
        logo.classList.remove('loaded');
        logo.classList.add('switching');
    }

    setTimeout(() => {
        document.documentElement.classList.toggle('dark-mode');
        document.body.classList.toggle('dark-mode');
        const isDark = document.body.classList.contains('dark-mode');
        localStorage.setItem('logiclab_theme', isDark ? 'dark' : 'light');
        updateLogo();
    }, 300);

    setTimeout(() => {
        if (logo) {
            logo.classList.remove('switching');
            logo.classList.add('loaded');
        }
        isSwitching = false;
    }, 1100);
}

// ── Scroll animations ──

function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.2 });

    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
}

// ── Logo load ──

function initLogo() {
    const logo = document.querySelector('.logo');
    const badge = document.querySelector('.hero-badge');
    if (!logo) return;

    logo.addEventListener('click', toggleTheme);
    logo.style.cursor = 'pointer';

    if (logo.complete) {
        logo.classList.add('loaded');
        if (badge) badge.classList.add('loaded');
    } else {
        logo.addEventListener('load', () => {
            logo.classList.add('loaded');
            if (badge) badge.classList.add('loaded');
        });
    }
}

// ── Pricing selection ──

let selectedPlan = 'free';

function initPricing() {
    const cards = document.querySelectorAll('.pricing-card, .plan-option');
    const continueBtn = document.getElementById('continue-btn');
    cards.forEach(card => {
        card.addEventListener('click', () => {
            cards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            selectedPlan = card.dataset.plan;
            if (continueBtn) {
                continueBtn.textContent = selectedPlan === 'free' ? 'PRÓBÁLD KI' : 'INGYENES PRÓBA INDÍTÁSA';
            }
            // GA4 event: plan selected
            if (typeof gtag === 'function') {
                gtag('event', 'plan_selected', {
                    plan_type: selectedPlan,
                    intent_of_payment: selectedPlan !== 'free'
                });
            }
        });
    });
}

// ── Modal ──

function openModal() {
    const overlay = document.getElementById('checkout-overlay');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
    setTimeout(() => {
        document.getElementById('modal-email').focus();
    }, 300);
}

function closeModal() {
    const overlay = document.getElementById('checkout-overlay');
    if (!overlay.classList.contains('active')) return;
    overlay.classList.remove('active');
    document.body.style.overflow = '';
}

function initContinueButton(source) {
    const continueBtn = document.getElementById('continue-btn');
    if (!continueBtn) return;

    continueBtn.addEventListener('click', () => {
        if (!selectedPlan) selectedPlan = 'free';
        // GA4 event: checkout button clicked
        if (typeof gtag === 'function') {
            gtag('event', 'checkout_click', {
                plan_type: selectedPlan,
                intent_of_payment: selectedPlan !== 'free',
                source: source
            });
        }
        openModal();
    });

    // Close modal
    document.getElementById('modal-close').addEventListener('click', closeModal);
    document.getElementById('checkout-overlay').addEventListener('click', (e) => {
        if (e.target === e.currentTarget) closeModal();
    });
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModal();
    });

    // Submit email
    const submitBtn = document.getElementById('modal-submit');
    const emailInput = document.getElementById('modal-email');
    const statusEl = document.getElementById('modal-status');

    submitBtn.addEventListener('click', () => handleSubmit(source, emailInput, submitBtn, statusEl));
    emailInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') handleSubmit(source, emailInput, submitBtn, statusEl);
    });
}

async function handleSubmit(source, emailInput, submitBtn, statusEl) {
    const email = emailInput.value.trim().toLowerCase();
    const emailRegex = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/;

    if (!email) {
        statusEl.textContent = 'EMAIL REQUIRED';
        return;
    }
    if (!emailRegex.test(email)) {
        statusEl.textContent = 'INVALID FORMAT';
        return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = 'SAVING...';
    statusEl.textContent = '';

    try {
        const docId = `${source}_${email}`;
        await setDoc(doc(db, 'kids-waitlist', docId), {
            email: email,
            plan: selectedPlan,
            source: source,
            lang: document.documentElement.lang || 'en',
            timestamp: serverTimestamp()
        });
    } catch (error) {
        if (error.code !== 'permission-denied') {
            console.error(error);
        }
    }

    // GA4 event: waitlist signup
    if (typeof gtag === 'function') {
        gtag('event', 'waitlist_signup', {
            plan_type: selectedPlan,
            intent_of_payment: selectedPlan !== 'free',
            email_domain: email.split('@')[1]
        });
    }

    // Success
    const planLabels = { free: 'Ingyenes próbaidőszak', monthly: '€9.99/hó', yearly: '€79/év' };
    const modalBody = document.querySelector('.modal-body');
    modalBody.innerHTML = `
        <div class="reveal-container">
            <h2 class="reveal-title">Benne vagy.</h2>
            <p class="reveal-detail">Értesítjük a <strong>${email}</strong> címet, amint a LogicLab Kids elindul.</p>
            <br>
            <p class="reveal-small">Választott csomag: ${planLabels[selectedPlan] || planLabels.free}</p>
        </div>
    `;
}

// ── FAQ ──

function initFaq() {
    document.querySelectorAll('.faq-item').forEach(item => {
        item.addEventListener('click', () => {
            const wasOpen = item.classList.contains('open');
            document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
            if (!wasOpen) item.classList.add('open');
        });
    });
}

// ── Init ──

export function initKidsPage(source) {
    initTheme();
    initLogo();
    initScrollAnimations();
    initPricing();
    initContinueButton(source);
    initFaq();
}

export function setSelectedPlanUI(plan) {
    selectedPlan = plan;
    const cards = document.querySelectorAll('.pricing-card, .plan-option');
    cards.forEach(c => {
        if (c.dataset.plan === plan) {
            c.classList.add('selected');
        } else {
            c.classList.remove('selected');
        }
    });
    const continueBtn = document.getElementById('continue-btn');
    if (continueBtn) {
        continueBtn.textContent = selectedPlan === 'free' ? 'PRÓBÁLD KI' : 'INGYENES PRÓBA INDÍTÁSA';
    }
}
