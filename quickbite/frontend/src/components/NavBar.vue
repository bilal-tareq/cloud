<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="container navbar-inner">
      <!-- Logo -->
      <router-link to="/" class="navbar-logo" id="navbar-logo">
        <span class="logo-icon">🔥</span>
        <span class="logo-text">Quick<span class="logo-accent">Bite</span></span>
      </router-link>

      <!-- Desktop Navigation -->
      <ul class="navbar-links" id="navbar-links">
        <li v-for="link in navLinks" :key="link.to">
          <router-link :to="link.to" class="nav-link" :id="'nav-' + link.name.toLowerCase()">
            {{ link.name }}
          </router-link>
        </li>
      </ul>

      <!-- Actions -->
      <div class="navbar-actions">
        <button class="btn-icon cart-btn" @click="cart.toggleCart()" id="cart-toggle-btn">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>
            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
          </svg>
          <span class="badge cart-badge" v-if="cart.totalItems > 0">{{ cart.totalItems }}</span>
        </button>

        <!-- Mobile Menu Toggle -->
        <button class="btn-icon mobile-toggle" @click="toggleMobile" id="mobile-menu-toggle">
          <svg v-if="!mobileOpen" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>
          </svg>
          <svg v-else width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
          </svg>
        </button>
      </div>

      <!-- Mobile Menu -->
      <transition name="mobile-menu">
        <div class="mobile-menu" v-if="mobileOpen" id="mobile-menu">
          <ul>
            <li v-for="link in navLinks" :key="link.to">
              <router-link :to="link.to" class="mobile-link" @click="mobileOpen = false">
                {{ link.name }}
              </router-link>
            </li>
          </ul>
        </div>
      </transition>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useCartStore } from '../stores/cart'

const cart = useCartStore()
const isScrolled = ref(false)
const mobileOpen = ref(false)

const navLinks = [
  { name: 'Home', to: '/' },
  { name: 'Menu', to: '/menu' },
  { name: 'Offers', to: '/offers' },
  { name: 'About', to: '/about' },
]

function handleScroll() {
  isScrolled.value = window.scrollY > 20
}

function toggleMobile() {
  mobileOpen.value = !mobileOpen.value
}

onMounted(() => window.addEventListener('scroll', handleScroll))
onUnmounted(() => window.removeEventListener('scroll', handleScroll))
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: var(--z-sticky);
  height: 72px;
  transition: all var(--transition-base);
  background: rgba(13, 13, 13, 0.6);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid transparent;
}

.navbar.scrolled {
  background: rgba(13, 13, 13, 0.92);
  border-bottom-color: var(--color-border);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.navbar-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  position: relative;
}

/* Logo */
.navbar-logo {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-family: var(--font-heading);
  font-size: var(--text-xl);
  font-weight: 700;
  z-index: 10;
}

.logo-icon {
  font-size: 1.5rem;
  animation: float 3s ease-in-out infinite;
}

.logo-accent {
  color: var(--color-accent);
}

/* Nav Links */
.navbar-links {
  display: flex;
  align-items: center;
  gap: var(--space-1);
}

.nav-link {
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-lg);
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--color-text-secondary);
  transition: all var(--transition-fast);
}

.nav-link:hover {
  color: var(--color-text-primary);
  background: var(--color-bg-glass);
}

.nav-link.router-link-active,
.nav-link.router-link-exact-active {
  color: var(--color-accent);
  background: rgba(255, 107, 53, 0.1);
}

/* Actions */
.navbar-actions {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  z-index: 10;
}

.cart-btn {
  position: relative;
  color: var(--color-text-primary);
  background: var(--color-bg-glass);
  border: 1px solid var(--color-border);
  transition: all var(--transition-fast);
}

.cart-btn:hover {
  background: var(--color-bg-glass-hover);
  border-color: var(--color-accent);
  color: var(--color-accent);
}

.cart-badge {
  position: absolute;
  top: -6px;
  right: -6px;
  animation: pulse 2s infinite;
}

.mobile-toggle {
  display: none;
  color: var(--color-text-primary);
}

/* Mobile Menu */
.mobile-menu {
  position: absolute;
  top: 72px;
  left: 0;
  right: 0;
  background: rgba(13, 13, 13, 0.98);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--color-border);
  padding: var(--space-4) var(--space-6);
}

.mobile-link {
  display: block;
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-lg);
  font-size: var(--text-base);
  font-weight: 500;
  color: var(--color-text-secondary);
  transition: all var(--transition-fast);
}

.mobile-link:hover,
.mobile-link.router-link-active {
  color: var(--color-accent);
  background: rgba(255, 107, 53, 0.1);
}

/* Transitions */
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* Responsive */
@media (max-width: 768px) {
  .navbar-links {
    display: none;
  }
  .mobile-toggle {
    display: flex;
  }
}
</style>
