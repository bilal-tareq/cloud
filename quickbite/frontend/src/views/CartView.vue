<template>
  <section class="section" id="cart-page">
    <div class="container">
      <h1 class="section-title">Checkout</h1>
      <p class="section-subtitle">Review your order and place it</p>

      <div class="checkout-layout" v-if="cart.items.length > 0">
        <!-- Cart Items -->
        <div class="cart-items-panel glass-card">
          <h2 class="panel-title">Your Items ({{ cart.totalItems }})</h2>
          <div class="cart-list">
            <div class="cart-row" v-for="item in cart.items" :key="item.id">
              <img :src="item.image" :alt="item.name" class="row-img" />
              <div class="row-info">
                <h4>{{ item.name }}</h4>
                <span class="row-price">${{ item.price.toFixed(2) }}</span>
              </div>
              <div class="row-qty">
                <button class="qty-btn" @click="cart.updateQuantity(item.id, item.quantity - 1)">−</button>
                <span>{{ item.quantity }}</span>
                <button class="qty-btn" @click="cart.updateQuantity(item.id, item.quantity + 1)">+</button>
              </div>
              <span class="row-subtotal">${{ (item.price * item.quantity).toFixed(2) }}</span>
              <button class="remove-btn" @click="cart.removeItem(item.id)">✕</button>
            </div>
          </div>
        </div>

        <!-- Checkout Form -->
        <div class="checkout-panel glass-card">
          <h2 class="panel-title">Delivery Details</h2>
          <form @submit.prevent="submitOrder">
            <div class="form-group">
              <label class="form-label">Full Name</label>
              <input class="form-input" v-model="form.customer_name" placeholder="John Doe" required id="input-name" />
            </div>
            <div class="form-group">
              <label class="form-label">Phone Number</label>
              <input class="form-input" v-model="form.customer_phone" placeholder="+1 555 123 4567" required id="input-phone" />
            </div>
            <div class="form-group">
              <label class="form-label">Delivery Address</label>
              <textarea class="form-input" v-model="form.customer_address" placeholder="123 Food Street, Apt 4" rows="3" required id="input-address"></textarea>
            </div>
            <div class="form-group">
              <label class="form-label">Notes (optional)</label>
              <textarea class="form-input" v-model="form.notes" placeholder="Extra ketchup, no onions..." rows="2" id="input-notes"></textarea>
            </div>

            <div class="order-summary">
              <div class="summary-row"><span>Subtotal</span><span>${{ cart.totalPrice.toFixed(2) }}</span></div>
              <div class="summary-row"><span>Delivery</span><span class="free">Free</span></div>
              <div class="summary-row total"><span>Total</span><span>${{ cart.totalPrice.toFixed(2) }}</span></div>
            </div>

            <button type="submit" class="btn btn-primary btn-lg" style="width:100%" :disabled="submitting" id="place-order-btn">
              {{ submitting ? 'Placing Order...' : 'Place Order' }}
            </button>
          </form>
        </div>
      </div>

      <!-- Empty State -->
      <div class="empty-cart" v-else>
        <span style="font-size:4rem">🛒</span>
        <h2>Your cart is empty</h2>
        <p>Add some delicious items from our menu!</p>
        <router-link to="/menu" class="btn btn-primary btn-lg">Browse Menu</router-link>
      </div>

      <OrderModal
        :show="modal.show"
        :success="modal.success"
        :message="modal.message"
        :orderId="modal.orderId"
        @close="handleModalClose"
      />
    </div>
  </section>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '../stores/cart'
import OrderModal from '../components/OrderModal.vue'
import api from '../services/api'

const cart = useCartStore()
const router = useRouter()
const submitting = ref(false)

const form = reactive({
  customer_name: '',
  customer_phone: '',
  customer_address: '',
  notes: '',
})

const modal = reactive({
  show: false,
  success: true,
  message: '',
  orderId: null,
})

async function submitOrder() {
  submitting.value = true
  try {
    const orderData = {
      ...form,
      items: cart.items.map(item => ({
        product: item.id,
        product_name: item.name,
        quantity: item.quantity,
        price: item.price.toFixed(2),
      })),
    }
    const res = await api.placeOrder(orderData)
    modal.success = true
    modal.message = 'Your order has been placed successfully! We will prepare it right away.'
    modal.orderId = res.data.id
    modal.show = true
    cart.clearCart()
  } catch (e) {
    modal.success = false
    modal.message = 'Something went wrong. Please try again.'
    modal.show = true
    console.error('Order failed:', e)
  } finally {
    submitting.value = false
  }
}

function handleModalClose() {
  modal.show = false
  if (modal.success) {
    router.push('/')
  }
}
</script>

<style scoped>
.checkout-layout { display: grid; grid-template-columns: 1.2fr 1fr; gap: 24px; align-items: start; }
.cart-items-panel, .checkout-panel { padding: 28px; }
.panel-title { font-family: var(--font-heading); font-size: 1.2rem; font-weight: 700; margin-bottom: 20px; }
.cart-row {
  display: flex; align-items: center; gap: 12px;
  padding: 16px 0; border-bottom: 1px solid var(--color-border);
}
.row-img { width: 56px; height: 56px; border-radius: 12px; object-fit: cover; }
.row-info { flex: 1; }
.row-info h4 { font-size: 0.9rem; font-weight: 600; margin-bottom: 2px; }
.row-price { font-size: 0.8rem; color: var(--color-accent); }
.row-qty { display: flex; align-items: center; gap: 8px; }
.qty-btn {
  width: 28px; height: 28px; border-radius: 8px;
  background: var(--color-bg-glass); border: 1px solid var(--color-border);
  color: var(--color-text-primary); cursor: pointer;
  display: flex; align-items: center; justify-content: center;
}
.qty-btn:hover { border-color: var(--color-accent); }
.row-subtotal { font-weight: 600; min-width: 60px; text-align: right; }
.remove-btn {
  background: none; border: none; color: var(--color-text-muted);
  cursor: pointer; font-size: 1rem; padding: 4px;
}
.remove-btn:hover { color: var(--color-danger); }

.order-summary { margin: 24px 0; padding: 20px; background: var(--color-bg-primary); border-radius: 12px; }
.summary-row { display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 0.9rem; color: var(--color-text-secondary); }
.summary-row.total { border-top: 1px solid var(--color-border); padding-top: 12px; margin-top: 12px; margin-bottom: 0; font-size: 1.1rem; font-weight: 700; color: var(--color-text-primary); }
.summary-row.total span:last-child { color: var(--color-accent); }
.free { color: var(--color-success); font-weight: 600; }

.empty-cart { text-align: center; padding: 80px 0; }
.empty-cart h2 { font-family: var(--font-heading); margin: 16px 0 8px; }
.empty-cart p { color: var(--color-text-muted); margin-bottom: 24px; }

button:disabled { opacity: 0.6; cursor: not-allowed; }

@media (max-width: 768px) {
  .checkout-layout { grid-template-columns: 1fr; }
}
</style>
