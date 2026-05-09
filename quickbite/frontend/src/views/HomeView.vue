<template>
  <div>
    <HeroSection />

    <!-- Featured Section -->
    <section class="section" id="featured-section">
      <div class="container">
        <h2 class="section-title">Popular Right Now</h2>
        <p class="section-subtitle">Our most loved dishes, hand-picked for you</p>

        <div class="featured-grid stagger-children" v-if="featured.length">
          <FoodCard v-for="product in featured" :key="product.id" :product="product" />
        </div>
        <div class="loading" v-else-if="loading">
          <div class="spinner"></div>
          <p>Loading delicious items...</p>
        </div>

        <div style="text-align:center;margin-top:40px">
          <router-link to="/menu" class="btn btn-secondary btn-lg" id="view-menu-btn">
            View Full Menu →
          </router-link>
        </div>
      </div>
    </section>

    <!-- How it works -->
    <section class="section how-it-works" id="how-it-works">
      <div class="container">
        <h2 class="section-title" style="text-align:center">How It Works</h2>
        <p class="section-subtitle" style="text-align:center">Three simple steps to deliciousness</p>

        <div class="steps-grid stagger-children">
          <div class="step-card glass-card" v-for="(step, i) in steps" :key="i">
            <div class="step-icon">{{ step.icon }}</div>
            <div class="step-number">{{ i + 1 }}</div>
            <h3 class="step-title">{{ step.title }}</h3>
            <p class="step-desc">{{ step.desc }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import HeroSection from '../components/HeroSection.vue'
import FoodCard from '../components/FoodCard.vue'
import api from '../services/api'

const featured = ref([])
const loading = ref(true)

const steps = [
  { icon: '📋', title: 'Browse Menu', desc: 'Explore our diverse selection of gourmet meals and drinks' },
  { icon: '🛒', title: 'Add to Cart', desc: 'Pick your favorites and customize your order' },
  { icon: '🚀', title: 'Fast Delivery', desc: 'Sit back and relax while we deliver to your door' },
]

onMounted(async () => {
  try {
    const res = await api.getFeaturedProducts()
    featured.value = res.data
  } catch (e) {
    console.error('Failed to load featured:', e)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.featured-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px;
}
.loading {
  display: flex; flex-direction: column; align-items: center; gap: 16px;
  padding: 60px 0; color: var(--color-text-muted);
}
.spinner {
  width: 40px; height: 40px; border: 3px solid var(--color-border);
  border-top-color: var(--color-accent); border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* Steps */
.steps-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.step-card { padding: 40px 30px; text-align: center; position: relative; }
.step-icon { font-size: 2.5rem; margin-bottom: 16px; }
.step-number {
  position: absolute; top: 16px; right: 16px;
  width: 30px; height: 30px; border-radius: 50%;
  background: var(--color-accent); color: white;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.8rem; font-weight: 700;
}
.step-title { font-family: var(--font-heading); font-size: 1.2rem; font-weight: 600; margin-bottom: 8px; }
.step-desc { font-size: 0.875rem; color: var(--color-text-secondary); line-height: 1.6; }

@media (max-width: 768px) {
  .steps-grid { grid-template-columns: 1fr; }
}
</style>
