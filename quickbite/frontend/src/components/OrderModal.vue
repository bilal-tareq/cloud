<template>
  <transition name="modal">
    <div class="modal-overlay" v-if="show" @click="$emit('close')" id="order-modal-overlay">
      <div class="modal-content glass-card" @click.stop id="order-modal">
        <div class="modal-icon">{{ success ? '🎉' : '❌' }}</div>
        <h2 class="modal-title">{{ success ? 'Order Placed!' : 'Order Failed' }}</h2>
        <p class="modal-message">{{ message }}</p>
        <p class="modal-order-id" v-if="orderId">Order #{{ orderId }}</p>
        <button class="btn btn-primary btn-lg" @click="$emit('close')" style="margin-top:20px">
          {{ success ? 'Continue Shopping' : 'Try Again' }}
        </button>
      </div>
    </div>
  </transition>
</template>

<script setup>
defineProps({
  show: Boolean,
  success: { type: Boolean, default: true },
  message: { type: String, default: '' },
  orderId: { default: null },
})
defineEmits(['close'])
</script>

<style scoped>
.modal-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.7);
  display: flex; align-items: center; justify-content: center;
  z-index: var(--z-modal); backdrop-filter: blur(8px);
}
.modal-content {
  padding: 48px; text-align: center; max-width: 420px; width: 90%;
}
.modal-icon { font-size: 4rem; margin-bottom: 16px; }
.modal-title { font-family: var(--font-heading); font-size: 1.75rem; font-weight: 700; margin-bottom: 8px; }
.modal-message { color: var(--color-text-secondary); font-size: 0.95rem; line-height: 1.6; }
.modal-order-id { color: var(--color-accent); font-weight: 700; font-size: 1.1rem; margin-top: 8px; }
.modal-enter-active, .modal-leave-active { transition: opacity 0.3s ease; }
.modal-enter-from, .modal-leave-to { opacity: 0; }
</style>
