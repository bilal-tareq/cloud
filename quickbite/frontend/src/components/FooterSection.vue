<template>
  <footer class="footer" id="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo">
            <span>🔥</span>
            <span class="logo-text">Quick<span class="accent">Bite</span></span>
          </div>
          <p class="footer-desc">Delivering happiness one bite at a time. Fresh ingredients, bold flavors, right to your doorstep.</p>
        </div>
        <div class="footer-links">
          <h4>Quick Links</h4>
          <ul>
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/menu">Menu</router-link></li>
            <li><router-link to="/offers">Offers</router-link></li>
            <li><router-link to="/about">About Us</router-link></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Contact</h4>
          <ul>
            <li>📍 123 Food Street, City</li>
            <li>📞 +1 (555) 123-4567</li>
            <li>📧 hello@quickbite.com</li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Hours</h4>
          <ul>
            <li>Mon - Fri: 10AM - 11PM</li>
            <li>Saturday: 11AM - 12AM</li>
            <li>Sunday: 11AM - 10PM</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; {{ new Date().getFullYear() }} QuickBite. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: var(--color-bg-secondary); border-top: 1px solid var(--color-border);
  padding: 60px 0 0;
}
.footer-grid {
  display: grid; grid-template-columns: 1.5fr 1fr 1fr 1fr; gap: 40px;
  padding-bottom: 40px;
}
.footer-logo {
  display: flex; align-items: center; gap: 8px;
  font-family: var(--font-heading); font-size: 1.25rem; font-weight: 700;
  margin-bottom: 16px;
}
.accent { color: var(--color-accent); }
.footer-desc { color: var(--color-text-secondary); font-size: 0.875rem; line-height: 1.7; max-width: 280px; }
.footer-links h4 {
  font-family: var(--font-heading); font-size: 1rem; font-weight: 600;
  margin-bottom: 16px; color: var(--color-text-primary);
}
.footer-links ul { display: flex; flex-direction: column; gap: 10px; }
.footer-links li {
  font-size: 0.875rem; color: var(--color-text-secondary);
  transition: color 0.15s ease;
}
.footer-links a:hover { color: var(--color-accent); }
.footer-bottom {
  border-top: 1px solid var(--color-border); padding: 20px 0;
  text-align: center; font-size: 0.8rem; color: var(--color-text-muted);
}
@media (max-width: 768px) {
  .footer-grid { grid-template-columns: 1fr 1fr; gap: 30px; }
}
@media (max-width: 480px) {
  .footer-grid { grid-template-columns: 1fr; }
}
</style>
