<template>
  <section class="section" id="offers-page">
    <div class="container">
      <h1 class="section-title">Special Offers</h1>
      <p class="section-subtitle">Don't miss out on these amazing deals</p>

      <div class="offers-grid stagger-children">
        <div class="offer-card glass-card" v-for="offer in offers" :key="offer.id">
          <div class="offer-badge">{{ offer.discount }}</div>
          <div class="offer-icon">{{ offer.icon }}</div>
          <h3 class="offer-title">{{ offer.title }}</h3>
          <p class="offer-desc">{{ offer.description }}</p>
          <div class="offer-code">
            <span>Use code:</span>
            <strong>{{ offer.code }}</strong>
          </div>
          <router-link to="/menu" class="btn btn-primary" style="width:100%;margin-top:16px">
            Order Now
          </router-link>
        </div>
      </div>

      <!-- Banner -->
      <div class="promo-banner glass-card">
        <div class="promo-content">
          <h2>🔥 Free Delivery</h2>
          <p>On all orders over $20. No code needed!</p>
        </div>
        <router-link to="/menu" class="btn btn-primary btn-lg">Order Now</router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
const offers = [
  {
    id: 1, icon: '🍔', discount: '20% OFF',
    title: 'Burger Combo Deal', code: 'BURGER20',
    description: 'Get 20% off on any burger combo meal. Includes fries and a drink!',
  },
  {
    id: 2, icon: '🍕', discount: 'Buy 1 Get 1',
    title: 'Pizza Party', code: 'PIZZA2X',
    description: 'Buy one large pizza and get a second one absolutely free!',
  },
  {
    id: 3, icon: '🥤', discount: 'FREE Drink',
    title: 'Thirsty Thursday', code: 'DRINK0',
    description: 'Every Thursday, get a free drink with any meal order over $10.',
  },
  {
    id: 4, icon: '🎂', discount: '15% OFF',
    title: 'Sweet Treats', code: 'SWEET15',
    description: 'Enjoy 15% off on all desserts. Satisfy your sweet cravings!',
  },
]
</script>

<style scoped>
.offers-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 24px; margin-bottom: 48px; }
.offer-card { padding: 32px; position: relative; overflow: hidden; text-align: center; }
.offer-badge {
  position: absolute; top: 16px; right: 16px;
  padding: 6px 14px; background: var(--color-accent); color: white;
  border-radius: 999px; font-size: 0.75rem; font-weight: 700;
}
.offer-icon { font-size: 3rem; margin-bottom: 16px; }
.offer-title { font-family: var(--font-heading); font-size: 1.25rem; font-weight: 700; margin-bottom: 8px; }
.offer-desc { font-size: 0.875rem; color: var(--color-text-secondary); line-height: 1.6; margin-bottom: 16px; }
.offer-code {
  padding: 10px 16px; background: var(--color-bg-primary); border-radius: 12px;
  font-size: 0.875rem; color: var(--color-text-secondary);
}
.offer-code strong { color: var(--color-accent); margin-left: 8px; }

.promo-banner {
  display: flex; align-items: center; justify-content: space-between;
  padding: 40px 48px; margin-top: 24px;
  background: linear-gradient(135deg, rgba(255,107,53,0.15) 0%, rgba(255,140,90,0.05) 100%);
  border-color: rgba(255,107,53,0.3);
}
.promo-banner h2 { font-family: var(--font-heading); font-size: 1.75rem; font-weight: 700; margin-bottom: 4px; }
.promo-banner p { color: var(--color-text-secondary); }

@media (max-width: 768px) {
  .promo-banner { flex-direction: column; text-align: center; gap: 20px; padding: 32px; }
}
</style>
