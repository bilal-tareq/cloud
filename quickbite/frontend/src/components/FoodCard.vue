<template>
  <div class="food-card glass-card" :id="'food-card-' + product.id">
    <div class="card-image-wrapper">
      <img :src="product.image" :alt="product.name" class="card-image" loading="lazy" />
      <div class="card-overlay">
        <button class="btn btn-primary btn-sm" @click="handleAddToCart">+ Add</button>
      </div>
      <span class="card-badge" v-if="product.is_featured">⭐ Featured</span>
    </div>
    <div class="card-body">
      <span class="card-category">{{ product.category_name }}</span>
      <h3 class="card-title">{{ product.name }}</h3>
      <p class="card-description">{{ product.description }}</p>
      <div class="card-footer">
        <span class="card-price">${{ parseFloat(product.price).toFixed(2) }}</span>
        <button class="btn btn-primary btn-sm" @click="handleAddToCart" :id="'add-btn-' + product.id">
          Add to Cart
        </button>
      </div>
    </div>
    <transition name="feedback">
      <div class="cart-feedback" v-if="showFeedback">✓ Added!</div>
    </transition>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCartStore } from '../stores/cart'

const props = defineProps({ product: { type: Object, required: true } })
const cart = useCartStore()
const showFeedback = ref(false)

function handleAddToCart() {
  cart.addItem(props.product)
  showFeedback.value = true
  setTimeout(() => { showFeedback.value = false }, 1200)
}
</script>

<style scoped>
.food-card { position: relative; overflow: hidden; display: flex; flex-direction: column; }
.card-image-wrapper { position: relative; height: 200px; overflow: hidden; }
.card-image { width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease; }
.food-card:hover .card-image { transform: scale(1.08); }
.card-overlay {
  position: absolute; inset: 0; background: rgba(0,0,0,0.5);
  display: flex; align-items: center; justify-content: center;
  opacity: 0; transition: opacity 0.25s ease;
}
.food-card:hover .card-overlay { opacity: 1; }
.card-badge {
  position: absolute; top: 12px; left: 12px;
  padding: 4px 12px; background: rgba(0,0,0,0.7); backdrop-filter: blur(10px);
  border-radius: 999px; font-size: 0.75rem; font-weight: 600; color: var(--color-warning);
}
.card-body { padding: 20px; flex: 1; display: flex; flex-direction: column; }
.card-category {
  font-size: 0.75rem; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.05em; color: var(--color-accent); margin-bottom: 4px;
}
.card-title { font-family: var(--font-heading); font-size: 1.125rem; font-weight: 600; margin-bottom: 8px; }
.card-description {
  font-size: 0.875rem; color: var(--color-text-secondary); line-height: 1.5; flex: 1;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
}
.card-footer {
  display: flex; align-items: center; justify-content: space-between;
  margin-top: 16px; padding-top: 16px; border-top: 1px solid var(--color-border);
}
.card-price { font-family: var(--font-heading); font-size: 1.25rem; font-weight: 700; color: var(--color-accent); }
.cart-feedback {
  position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%);
  padding: 12px 24px; background: rgba(52,211,153,0.95); color: white;
  font-weight: 700; font-size: 0.875rem; border-radius: 999px; z-index: 10; pointer-events: none;
}
.feedback-enter-active { transition: all 0.3s ease; }
.feedback-leave-active { transition: all 0.2s ease; }
.feedback-enter-from { opacity: 0; transform: translate(-50%,-50%) scale(0.8); }
.feedback-leave-to { opacity: 0; transform: translate(-50%,-60%); }
</style>
