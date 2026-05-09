<template>
  <section class="hero" id="hero-section">
    <div class="hero-bg">
      <div class="hero-glow hero-glow-1"></div>
      <div class="hero-glow hero-glow-2"></div>
      <div class="hero-grid"></div>
    </div>

    <div class="container hero-content">
      <div class="hero-text">
        <div class="hero-badge animate-fade-in-up">
          <span class="badge-dot"></span>
          🚀 Free delivery on orders over $20
        </div>

        <h1 class="hero-title animate-fade-in-up" style="animation-delay: 0.1s">
          Delicious Food,
          <br />
          <span class="hero-title-accent">Delivered Fast</span>
        </h1>

        <p class="hero-description animate-fade-in-up" style="animation-delay: 0.2s">
          Order your favorite meals from the best restaurants in town.
          Fresh ingredients, bold flavors, right to your doorstep.
        </p>

        <div class="hero-actions animate-fade-in-up" style="animation-delay: 0.3s">
          <router-link to="/menu" class="btn btn-primary btn-lg" id="hero-order-btn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z"/>
            </svg>
            Order Now
          </router-link>
          <router-link to="/menu" class="btn btn-secondary btn-lg" id="hero-menu-btn">
            Explore Menu
          </router-link>
        </div>

        <div class="hero-stats animate-fade-in-up" style="animation-delay: 0.4s">
          <div class="stat">
            <span class="stat-number">500+</span>
            <span class="stat-label">Happy Customers</span>
          </div>
          <div class="stat-divider"></div>
          <div class="stat">
            <span class="stat-number">50+</span>
            <span class="stat-label">Menu Items</span>
          </div>
          <div class="stat-divider"></div>
          <div class="stat">
            <span class="stat-number">4.9</span>
            <span class="stat-label">Rating ⭐</span>
          </div>
        </div>
      </div>

      <div class="hero-visual animate-fade-in-up" style="animation-delay: 0.3s">
        <div class="hero-image-wrapper">
          <img
            src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&h=600&fit=crop"
            alt="Delicious burger"
            class="hero-image"
          />
          <div class="hero-image-ring"></div>
        </div>

        <!-- Floating food badges -->
        <div class="float-badge float-badge-1">
          <span>🍕</span>
          <div>
            <strong>Pizza</strong>
            <small>From $11.99</small>
          </div>
        </div>
        <div class="float-badge float-badge-2">
          <span>🍔</span>
          <div>
            <strong>Burgers</strong>
            <small>From $8.99</small>
          </div>
        </div>
        <div class="float-badge float-badge-3">
          <span>🥗</span>
          <div>
            <strong>Salads</strong>
            <small>From $6.99</small>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  position: relative;
  min-height: calc(100vh - 72px);
  display: flex;
  align-items: center;
  overflow: hidden;
}

/* Background */
.hero-bg {
  position: absolute;
  inset: 0;
  overflow: hidden;
}

.hero-glow {
  position: absolute;
  border-radius: 50%;
  filter: blur(120px);
  opacity: 0.4;
}

.hero-glow-1 {
  width: 500px;
  height: 500px;
  background: var(--color-accent);
  top: -100px;
  right: 10%;
  opacity: 0.12;
}

.hero-glow-2 {
  width: 400px;
  height: 400px;
  background: #ff8c5a;
  bottom: -50px;
  left: 20%;
  opacity: 0.08;
}

.hero-grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size: 60px 60px;
}

/* Content */
.hero-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  gap: var(--space-16);
  position: relative;
  z-index: 1;
  padding: var(--space-12) 0;
}

/* Text */
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-4);
  background: var(--color-bg-glass);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-full);
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  margin-bottom: var(--space-6);
}

.badge-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-success);
  animation: pulse 2s infinite;
}

.hero-title {
  font-family: var(--font-heading);
  font-size: var(--text-6xl);
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: var(--space-6);
}

.hero-title-accent {
  background: var(--gradient-accent);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-description {
  font-size: var(--text-lg);
  color: var(--color-text-secondary);
  line-height: 1.7;
  max-width: 500px;
  margin-bottom: var(--space-8);
}

.hero-actions {
  display: flex;
  gap: var(--space-4);
  margin-bottom: var(--space-10);
}

/* Stats */
.hero-stats {
  display: flex;
  align-items: center;
  gap: var(--space-6);
}

.stat-number {
  display: block;
  font-family: var(--font-heading);
  font-size: var(--text-2xl);
  font-weight: 700;
  color: var(--color-text-primary);
}

.stat-label {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
}

.stat-divider {
  width: 1px;
  height: 40px;
  background: var(--color-border);
}

/* Visual / Image */
.hero-visual {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-image-wrapper {
  position: relative;
  width: 420px;
  height: 420px;
}

.hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  box-shadow: var(--shadow-xl), 0 0 60px var(--color-accent-glow);
}

.hero-image-ring {
  position: absolute;
  inset: -15px;
  border-radius: 50%;
  border: 2px dashed rgba(255, 107, 53, 0.3);
  animation: spin 30s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Floating badges */
.float-badge {
  position: absolute;
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-4);
  background: rgba(26, 26, 26, 0.9);
  backdrop-filter: blur(20px);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-lg);
  z-index: 2;
}

.float-badge span {
  font-size: 1.5rem;
}

.float-badge strong {
  display: block;
  font-size: var(--text-sm);
  color: var(--color-text-primary);
}

.float-badge small {
  font-size: var(--text-xs);
  color: var(--color-accent);
}

.float-badge-1 {
  top: 10%;
  right: -10px;
  animation: float 4s ease-in-out infinite;
}

.float-badge-2 {
  bottom: 15%;
  left: -20px;
  animation: float 5s ease-in-out infinite 0.5s;
}

.float-badge-3 {
  bottom: 5%;
  right: 10%;
  animation: float 4.5s ease-in-out infinite 1s;
}

/* Responsive */
@media (max-width: 1024px) {
  .hero-content {
    grid-template-columns: 1fr;
    text-align: center;
    gap: var(--space-10);
  }

  .hero-description {
    margin: 0 auto var(--space-8);
  }

  .hero-actions {
    justify-content: center;
  }

  .hero-stats {
    justify-content: center;
  }

  .hero-image-wrapper {
    width: 300px;
    height: 300px;
  }

  .hero-title {
    font-size: var(--text-5xl);
  }
}

@media (max-width: 768px) {
  .hero-visual {
    display: none;
  }

  .hero-title {
    font-size: var(--text-4xl);
  }

  .hero-stats {
    flex-wrap: wrap;
    gap: var(--space-4);
  }

  .stat-divider {
    display: none;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: var(--text-3xl);
  }

  .hero-actions {
    flex-direction: column;
    align-items: stretch;
  }
}
</style>
