<template>
  <section class="section" id="about-page">
    <div class="container">
      <div class="about-hero">
        <h1 class="section-title" style="text-align:center">About QuickBite</h1>
        <p class="section-subtitle" style="text-align:center;max-width:600px;margin:0 auto 48px">
          We're on a mission to deliver the best food experience right to your doorstep
        </p>
      </div>

      <div class="about-grid stagger-children">
        <div class="about-card glass-card" v-for="item in values" :key="item.title">
          <div class="about-icon">{{ item.icon }}</div>
          <h3>{{ item.title }}</h3>
          <p>{{ item.desc }}</p>
        </div>
      </div>

      <div class="story-section">
        <div class="story-content">
          <h2 class="section-title">Our Story</h2>
          <p>QuickBite started with a simple idea: everyone deserves access to delicious, quality food without the hassle. What began as a small kitchen in 2023 has grown into a beloved food delivery service.</p>
          <p>We partner with the best local chefs and use only fresh, premium ingredients to craft meals that bring joy to every bite. Our team is passionate about food, speed, and making your day a little brighter.</p>
          <div class="story-stats">
            <div class="stat-item">
              <span class="stat-num">500+</span>
              <span class="stat-lbl">Happy Customers</span>
            </div>
            <div class="stat-item">
              <span class="stat-num">50+</span>
              <span class="stat-lbl">Menu Items</span>
            </div>
            <div class="stat-item">
              <span class="stat-num">15min</span>
              <span class="stat-lbl">Avg Delivery</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const values = [
  { icon: '🥇', title: 'Quality First', desc: 'We use only the freshest ingredients sourced from trusted local suppliers.' },
  { icon: '⚡', title: 'Lightning Fast', desc: 'Average delivery time of 15 minutes. Hot food, delivered hot.' },
  { icon: '💚', title: 'Eco Friendly', desc: 'All our packaging is biodegradable. We care about our planet.' },
  { icon: '🤝', title: 'Community', desc: 'We support local farmers and businesses, strengthening our community.' },
]
</script>

<style scoped>
.about-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 24px; margin-bottom: 60px; }
.about-card { padding: 32px; text-align: center; }
.about-icon { font-size: 2.5rem; margin-bottom: 16px; }
.about-card h3 { font-family: var(--font-heading); font-size: 1.1rem; font-weight: 600; margin-bottom: 8px; }
.about-card p { font-size: 0.875rem; color: var(--color-text-secondary); line-height: 1.6; }

.story-section { max-width: 700px; margin: 0 auto; }
.story-content p {
  color: var(--color-text-secondary); font-size: 1rem; line-height: 1.8; margin-bottom: 16px;
}
.story-stats { display: flex; gap: 40px; margin-top: 32px; }
.stat-item { text-align: center; }
.stat-num { display: block; font-family: var(--font-heading); font-size: 1.75rem; font-weight: 700; color: var(--color-accent); }
.stat-lbl { font-size: 0.8rem; color: var(--color-text-muted); }

@media (max-width: 768px) {
  .story-stats { flex-wrap: wrap; gap: 24px; }
}
</style>
