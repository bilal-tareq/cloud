<template>
  <transition name="sidebar">
    <div class="sidebar-overlay" v-if="cart.isOpen" @click="cart.closeCart" id="cart-overlay">
      <div class="sidebar" @click.stop id="cart-sidebar">
        <div class="sidebar-header">
          <h2 class="sidebar-title">Your Cart</h2>
          <button class="btn-icon" @click="cart.closeCart" id="cart-close-btn" style="background:var(--color-bg-glass);border:1px solid var(--color-border);color:var(--color-text-primary)">
            ✕
          </button>
        </div>

        <div class="sidebar-body" v-if="cart.items.length > 0">
          <div class="cart-item" v-for="item in cart.items" :key="item.id">
            <img :src="item.image" :alt="item.name" class="item-image" />
            <div class="item-info">
              <h4 class="item-name">{{ item.name }}</h4>
              <span class="item-price">${{ item.price.toFixed(2) }}</span>
              <div class="item-qty">
                <button class="qty-btn" @click="cart.updateQuantity(item.id, item.quantity - 1)">−</button>
                <span class="qty-value">{{ item.quantity }}</span>
                <button class="qty-btn" @click="cart.updateQuantity(item.id, item.quantity + 1)">+</button>
              </div>
            </div>
            <button class="remove-btn" @click="cart.removeItem(item.id)">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"/>
              </svg>
            </button>
          </div>
        </div>

        <div class="sidebar-empty" v-else>
          <span style="font-size:3rem">🛒</span>
          <p>Your cart is empty</p>
          <button class="btn btn-secondary" @click="cart.closeCart">Browse Menu</button>
        </div>

        <div class="sidebar-footer" v-if="cart.items.length > 0">
          <div class="total-row">
            <span>Total</span>
            <span class="total-price">${{ cart.totalPrice.toFixed(2) }}</span>
          </div>
          <router-link to="/cart" class="btn btn-primary btn-lg" style="width:100%" @click="cart.closeCart" id="checkout-btn">
            Proceed to Checkout
          </router-link>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { useCartStore } from '../stores/cart'
const cart = useCartStore()
</script>

<style scoped>
.sidebar-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.6);
  z-index: var(--z-overlay); backdrop-filter: blur(4px);
}
.sidebar {
  position: fixed; top: 0; right: 0; bottom: 0; width: 400px; max-width: 90vw;
  background: var(--color-bg-secondary); border-left: 1px solid var(--color-border);
  display: flex; flex-direction: column; z-index: var(--z-modal);
  animation: slideInRight 0.3s ease;
}
.sidebar-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 20px 24px; border-bottom: 1px solid var(--color-border);
}
.sidebar-title { font-family: var(--font-heading); font-size: 1.25rem; font-weight: 700; }
.sidebar-body { flex: 1; overflow-y: auto; padding: 16px 24px; }
.cart-item {
  display: flex; align-items: center; gap: 12px;
  padding: 16px 0; border-bottom: 1px solid var(--color-border);
}
.item-image { width: 60px; height: 60px; border-radius: 12px; object-fit: cover; }
.item-info { flex: 1; }
.item-name { font-size: 0.875rem; font-weight: 600; margin-bottom: 4px; }
.item-price { font-size: 0.875rem; color: var(--color-accent); font-weight: 600; }
.item-qty { display: flex; align-items: center; gap: 8px; margin-top: 8px; }
.qty-btn {
  width: 28px; height: 28px; border-radius: 8px;
  background: var(--color-bg-glass); border: 1px solid var(--color-border);
  color: var(--color-text-primary); font-size: 1rem;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; transition: all 0.15s ease;
}
.qty-btn:hover { background: var(--color-bg-glass-hover); border-color: var(--color-accent); }
.qty-value { font-weight: 600; min-width: 20px; text-align: center; }
.remove-btn {
  color: var(--color-text-muted); cursor: pointer; padding: 4px;
  transition: color 0.15s ease; background: none; border: none;
}
.remove-btn:hover { color: var(--color-danger); }
.sidebar-empty {
  flex: 1; display: flex; flex-direction: column;
  align-items: center; justify-content: center; gap: 16px;
  color: var(--color-text-muted);
}
.sidebar-footer {
  padding: 20px 24px; border-top: 1px solid var(--color-border);
  background: var(--color-bg-primary);
}
.total-row {
  display: flex; justify-content: space-between; margin-bottom: 16px;
  font-size: 1rem; font-weight: 600;
}
.total-price { color: var(--color-accent); font-size: 1.25rem; font-family: var(--font-heading); }

.sidebar-enter-active, .sidebar-leave-active { transition: opacity 0.3s ease; }
.sidebar-enter-from, .sidebar-leave-to { opacity: 0; }
</style>
