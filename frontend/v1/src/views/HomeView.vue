<script setup>
import { onMounted } from 'vue'
import Navbar from '@/components/Navbar.vue'

const steps = [
  {
    n: '01',
    title: 'Add your products',
    body: 'Snap a photo with your phone, set a price, hit save. Your shelf fills up as you go.',
  },
  {
    n: '02',
    title: 'Share your shop',
    body: 'The moment you open your shelf, it gets its own page you can share on WhatsApp, Facebook, wherever your customers already are.',
  },
  {
    n: '03',
    title: 'Get paid, restock',
    body: 'Orders land in your phone. Payment lands in Airtel Money or TNM Mpamba. Mark it sold, add the next item.',
  },
]

const features = [
  {
    title: 'Built for your phone',
    body: 'Set up your whole shop from the phone you already carry. No laptop, no code, no waiting on a developer.',
  },
  {
    title: 'Paid the way you get paid',
    body: 'Airtel Money and TNM Mpamba are built in from day one — not a plug-in you have to hunt for later.',
  },
  {
    title: 'Price it your way',
    body: 'Kwacha, dollars, rand — set prices in whatever currency your customers actually pay you in.',
  },
]

const waitlistFormId = '6a5c4e9aa1d322fcbd76a1ad'
const waitlistHost = 'https://rrqgalro.forms.app'
let waitlistWidget = null
let waitlistScriptLoaded = false

const loadWaitlistForm = () => {
  if (waitlistScriptLoaded || document.querySelector('script[src="https://cdn.forms.app/embed.js"]')) {
    waitlistScriptLoaded = true
    return
  }

  const script = document.createElement('script')
  script.src = 'https://cdn.forms.app/embed.js'
  script.type = 'text/javascript'
  script.async = true
  script.defer = true
  script.onload = () => {
    waitlistScriptLoaded = true
  }
  document.body.appendChild(script)
}

const openWaitlistForm = () => {
  loadWaitlistForm()

  if (!window.formsapp) {
    window.location.href = waitlistHost
    return
  }

  if (!waitlistWidget) {
    waitlistWidget = new window.formsapp(
      waitlistFormId,
      'standard',
      { width: '100vw', height: '600px' },
      waitlistHost,
    )
  }

  if (typeof waitlistWidget.open === 'function') {
    waitlistWidget.open()
  } else {
    window.location.href = waitlistHost
  }
}

onMounted(() => {
  const revealEls = document.querySelectorAll('[data-reveal]')
  if (!('IntersectionObserver' in window) || revealEls.length === 0) {
    revealEls.forEach((el) => el.classList.add('is-visible'))
    return
  }
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible')
          observer.unobserve(entry.target)
        }
      })
    },
    { threshold: 0.2 },
  )
  revealEls.forEach((el) => observer.observe(el))
  loadWaitlistForm()
})
</script>

<template>
  <div class="page">
    <Navbar :on-waitlist="openWaitlistForm" />

    <main id="top">
      <section class="hero">
        <div class="hero__copy">
          <p class="eyebrow">A shop from Ocickle</p>
          <h1>Create your storefront in minutes.</h1>
          <p class="hero__sub">
            Add your products, open a shop that looks like the real thing, and get paid straight
            to Airtel Money or TNM Mpamba. No website skills. No fee to start.
          </p>
          <div class="hero__actions">
            <a class="btn btn--amber btn--lg" href="#" @click.prevent="openWaitlistForm">Join the waitlist</a>
            <a class="btn btn--ghost btn--lg" href="#" @click.prevent="openWaitlistForm">Get early access</a>
          </div>
        </div>

        <div class="hero__art" aria-hidden="true">
          <div class="shelf-scene">
            <div class="card card--1">
              <span class="card__swatch swatch--a"></span>
              <span class="card__tag">MWK 4,500</span>
            </div>
            <div class="card card--2">
              <span class="card__swatch swatch--b"></span>
              <span class="card__tag">USD 15</span>
            </div>
            <div class="card card--3">
              <span class="card__swatch swatch--c"></span>
              <span class="card__tag">MWK 12,000</span>
            </div>
            <div class="card card--4">
              <span class="card__swatch swatch--d"></span>
              <span class="card__tag">ZAR 180</span>
            </div>
            <div class="plank"></div>
            <div class="bracket bracket--left"></div>
            <div class="bracket bracket--right"></div>
          </div>
        </div>
      </section>

      <section id="features" class="features" data-reveal>
        <h2>Why sellers stock their shop here</h2>
        <div class="features__grid">
          <article class="feature" v-for="f in features" :key="f.title">
            <h3>{{ f.title }}</h3>
            <p>{{ f.body }}</p>
          </article>
        </div>
      </section>

      <section id="how" class="how" data-reveal>
        <h2>Three things, and you're open</h2>
        <ol class="how__list">
          <li class="how__step" v-for="s in steps" :key="s.n">
            <span class="how__n">{{ s.n }}</span>
            <div>
              <h3>{{ s.title }}</h3>
              <p>{{ s.body }}</p>
            </div>
          </li>
        </ol>
      </section>

      <section class="quote" data-reveal>
        <blockquote>
          "I used to type out prices one customer at a time on WhatsApp. Now I just point people
          to my shop."
        </blockquote>
        <p class="quote__attr">Chimwemwe, shop owner</p>
      </section>

      <section id="start" class="cta" data-reveal>
        <h2>Simple to start. Built to grow.</h2>
        <p>Your shelf is free to open. Bring what you sell — we'll bring the shop.</p>
        <a class="btn btn--amber btn--lg" href="#" @click.prevent="openWaitlistForm">Join the waitlist</a>
      </section>
    </main>

    <footer class="footer">
      <div class="footer__inner">
        <div class="footer__brand">
          <img src="/icon-192.png" alt="" width="22" height="22" />
          <span>Ocickle Shelf</span>
        </div>
        <p>A product of Ocickle</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.page {
  overflow-x: clip;
}

/* ---------- Buttons ---------- */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  font-weight: 700;
  border: 2px solid var(--ink);
  transition:
    transform 0.1s ease,
    box-shadow 0.1s ease;
  white-space: nowrap;
}

.btn--sm {
  padding: 8px 16px;
  font-size: 0.86rem;
}

.btn--lg {
  padding: 13px 24px;
  font-size: 1rem;
}

.btn--amber {
  background: var(--amber);
  color: var(--ink);
  box-shadow: var(--shadow-flat);
}

.btn--amber:hover {
  transform: translate(-2px, -2px);
  box-shadow: 7px 7px 0 rgba(36, 28, 19, 0.12);
}

.btn--amber:active {
  transform: translate(1px, 1px);
  box-shadow: 2px 2px 0 rgba(36, 28, 19, 0.12);
}

.btn--ghost {
  background: transparent;
  border-color: var(--ink-faint);
  color: var(--ink);
}

.btn--ghost:hover {
  border-color: var(--ink);
}

/* ---------- Hero ---------- */
.hero {
  max-width: var(--container);
  margin: 0 auto;
  padding: 64px 24px 40px;
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 40px;
  align-items: center;
}

.eyebrow {
  font-family: var(--mono);
  font-size: 0.78rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--clay-deep);
  margin-bottom: 16px;
}

.hero h1 {
  font-family: var(--display);
  font-weight: 800;
  font-size: clamp(2.3rem, 4.6vw, 3.4rem);
  line-height: 1.08;
  letter-spacing: -0.01em;
  color: var(--ink);
}

.hero__sub {
  margin-top: 20px;
  max-width: 46ch;
  font-size: 1.06rem;
  color: var(--ink-soft);
}

.hero__actions {
  margin-top: 30px;
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}

@media (max-width: 880px) {
  .hero {
    grid-template-columns: 1fr;
    padding-top: 44px;
  }
}

/* ---------- Shelf illustration (signature element) ---------- */
.shelf-scene {
  position: relative;
  height: 320px;
  display: grid;
  place-items: end center;
}

.plank {
  position: absolute;
  bottom: 64px;
  left: 4%;
  right: 4%;
  height: 20px;
  border-radius: 3px;
  background: var(--clay);
  border-bottom: 5px solid var(--clay-deep);
}

.bracket {
  position: absolute;
  bottom: 28px;
  width: 13px;
  height: 38px;
  background: var(--clay-deep);
  border-radius: 0 0 3px 3px;
}

.bracket--left {
  left: 12%;
}

.bracket--right {
  right: 12%;
}

.card {
  position: absolute;
  bottom: 82px;
  width: 106px;
  padding: 9px;
  border-radius: 8px;
  background: var(--paper-deep);
  border: 2px solid var(--ink);
  box-shadow: var(--shadow-flat);
  opacity: 0;
  transform: translateY(10px) rotate(var(--rot, 0deg));
  animation: cardIn 0.5s ease forwards;
}

.card__swatch {
  display: block;
  width: 100%;
  height: 62px;
  border-radius: 5px;
  margin-bottom: 8px;
  border: 1.5px solid var(--ink-faint);
}

.card__tag {
  font-family: var(--mono);
  font-size: 0.7rem;
  color: var(--ink);
  font-weight: 500;
}

.swatch--a {
  background: var(--amber);
}
.swatch--b {
  background: #4f7a78;
}
.swatch--c {
  background: var(--clay);
}
.swatch--d {
  background: #c99a3e;
}

.card--1 {
  left: 4%;
  --rot: -5deg;
  animation-delay: 0.05s;
}
.card--2 {
  left: 27%;
  bottom: 98px;
  --rot: 3deg;
  animation-delay: 0.15s;
}
.card--3 {
  left: 51%;
  --rot: -3deg;
  animation-delay: 0.25s;
}
.card--4 {
  left: 74%;
  bottom: 94px;
  --rot: 4deg;
  animation-delay: 0.35s;
}

@keyframes cardIn {
  to {
    opacity: 1;
    transform: translateY(0) rotate(var(--rot, 0deg));
  }
}

@media (max-width: 880px) {
  .shelf-scene {
    height: 250px;
  }
  .card {
    width: 82px;
  }
  .card__swatch {
    height: 46px;
  }
}

/* ---------- Reveal-on-scroll ---------- */
[data-reveal] {
  opacity: 0;
  transform: translateY(14px);
  transition:
    opacity 0.5s ease,
    transform 0.5s ease;
}

[data-reveal].is-visible {
  opacity: 1;
  transform: translateY(0);
}

/* ---------- Features ---------- */
.features {
  max-width: var(--container);
  margin: 88px auto 0;
  padding: 0 24px;
}

.features h2,
.how h2,
.cta h2 {
  font-family: var(--display);
  font-weight: 700;
  font-size: clamp(1.6rem, 2.8vw, 2.1rem);
  color: var(--ink);
  text-align: center;
  margin-bottom: 40px;
}

.features__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.feature {
  background: var(--paper-deep);
  border: 2px solid var(--ink);
  border-radius: var(--radius);
  padding: 24px 22px;
  box-shadow: var(--shadow-flat);
}

.feature h3 {
  font-family: var(--display);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--clay-deep);
  margin-bottom: 9px;
}

.feature p {
  color: var(--ink-soft);
  font-size: 0.95rem;
}

@media (max-width: 880px) {
  .features__grid {
    grid-template-columns: 1fr;
  }
}

/* ---------- How it works ---------- */
.how {
  max-width: 740px;
  margin: 100px auto 0;
  padding: 0 24px;
}

.how__list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.how__step {
  display: grid;
  grid-template-columns: 52px 1fr;
  gap: 18px;
  align-items: start;
  padding-bottom: 28px;
  border-bottom: 2px dashed var(--ink-faint);
}

.how__step:last-child {
  border-bottom: none;
}

.how__n {
  font-family: var(--mono);
  font-size: 1.25rem;
  font-weight: 500;
  color: var(--clay-deep);
}

.how__step h3 {
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.08rem;
  margin-bottom: 6px;
  color: var(--ink);
}

.how__step p {
  color: var(--ink-soft);
}

/* ---------- Quote ---------- */
.quote {
  max-width: 660px;
  margin: 100px auto 0;
  padding: 0 24px;
  text-align: center;
}

.quote blockquote {
  font-family: var(--display);
  font-weight: 600;
  font-size: clamp(1.2rem, 2.4vw, 1.5rem);
  line-height: 1.42;
  color: var(--ink);
}

.quote__attr {
  margin-top: 16px;
  font-family: var(--mono);
  font-size: 0.84rem;
  color: var(--clay-deep);
}

/* ---------- CTA ---------- */
.cta {
  max-width: 620px;
  margin: 110px auto 0;
  padding: 48px 32px;
  text-align: center;
  background: var(--paper-deep);
  border: 2px solid var(--ink);
  border-radius: 20px;
  box-shadow: var(--shadow-flat);
}

.cta p {
  color: var(--ink-soft);
  margin-bottom: 24px;
}

/* ---------- Footer ---------- */
.footer {
  margin-top: 100px;
  border-top: 2px solid var(--ink);
}

.footer__inner {
  max-width: var(--container);
  margin: 0 auto;
  padding: 28px 24px 44px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
}

.footer__brand {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--display);
  font-weight: 700;
  color: var(--ink);
}

.footer p {
  color: var(--ink-soft);
  font-size: 0.86rem;
}
</style>
