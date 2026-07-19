<script setup>
const props = defineProps({
  onWaitlist: {
    type: Function,
    default: null,
  },
})

const handleWaitlistClick = (event) => {
  if (props.onWaitlist) {
    event.preventDefault()
    props.onWaitlist()
  }
}
</script>

<template>
  <header class="nav">
    <div class="nav__inner">
      <a href="#top" class="brand">
        <img src="/icon-192.png" alt="Shelf" class="brand__mark" width="34" height="34" />
        <span class="brand__prefix">Ocickle Shelf</span>
      </a>
      <nav class="nav__links" aria-label="Primary">
        <a href="#features">Features</a>
        <a href="#how">How it works</a>
      </nav>
      <a class="btn btn--amber btn--sm" href="#" @click="handleWaitlistClick">Join waitlist</a>
    </div>
  </header>
</template>

<style scoped>
.nav {
  position: sticky;
  top: 0;
  z-index: 20;
  background: var(--paper-deep);
  border-bottom: 2px solid var(--ink);
}

.nav__inner {
  max-width: var(--container);
  margin: 0 auto;
  padding: 14px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 6px;
}

.brand__prefix {
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--ink);
}

.brand__mark {
  margin-left: -2px;
}

.nav__links {
  display: flex;
  gap: 28px;
  font-weight: 600;
  font-size: 0.95rem;
}

.nav__links a {
  opacity: 0.75;
  transition: opacity 0.15s ease;
}

.nav__links a:hover {
  opacity: 1;
}

@media (max-width: 720px) {
  .nav__links {
    display: none;
  }
}
</style>
