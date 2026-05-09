<template>
  <section class="section" id="menu-page">
    <div class="container">
      <h1 class="section-title">Our Menu</h1>
      <p class="section-subtitle">Explore our full selection of delicious meals</p>

      <div class="search-section">
        <div class="search-box glass-card">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="search-icon">
            <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
          </svg>
          <input 
            type="text" 
            v-model="searchQuery" 
            @input="handleSearch" 
            placeholder="Search for your favorite food..." 
            class="search-input"
          />
        </div>
      </div>

      <CategoryFilter
        v-if="!searchQuery"
        :categories="categories"
        :selectedCategory="selectedCategory"
        @select="selectCategory"
      />
      <div v-else class="search-results-info">
        Showing results for "{{ searchQuery }}"
        <button @click="clearSearch" class="btn-text">Clear</button>
      </div>

      <div class="menu-grid stagger-children" v-if="products.length">
        <FoodCard v-for="product in products" :key="product.id" :product="product" />
      </div>

      <div class="loading" v-else-if="loading">
        <div class="spinner"></div>
        <p>Loading menu...</p>
      </div>

      <div class="empty" v-else>
        <span style="font-size:3rem">🍽️</span>
        <p>No items found in this category</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import CategoryFilter from '../components/CategoryFilter.vue'
import FoodCard from '../components/FoodCard.vue'
import api from '../services/api'

const categories = ref([])
const products = ref([])
const selectedCategory = ref(null)
const searchQuery = ref('')
const loading = ref(true)
let searchTimeout = null

async function loadProducts(categoryId = null, search = '') {
  loading.value = true
  try {
    const res = search 
      ? await api.searchProducts(search)
      : await api.getProducts(categoryId)
    products.value = res.data
  } catch (e) {
    console.error('Failed to load products:', e)
  } finally {
    loading.value = false
  }
}

function handleSearch() {
  clearTimeout(searchTimeout)
  searchTimeout = setTimeout(() => {
    selectedCategory.value = null
    loadProducts(null, searchQuery.value)
  }, 500)
}

function clearSearch() {
  searchQuery.value = ''
  loadProducts()
}

function selectCategory(catId) {
  selectedCategory.value = catId
  searchQuery.value = ''
  loadProducts(catId)
}

onMounted(async () => {
  try {
    const res = await api.getCategories()
    categories.value = res.data
  } catch (e) {
    console.error('Failed to load categories:', e)
  }
  loadProducts()
})
</script>

<style scoped>
.menu-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px;
}

/* Search Styles */
.search-section {
  margin-bottom: 30px;
}
.search-box {
  display: flex;
  align-items: center;
  padding: 5px 20px;
  max-width: 600px;
  margin: 0 auto;
}
.search-icon {
  color: var(--color-text-muted);
  margin-right: 15px;
}
.search-input {
  background: transparent;
  border: none;
  color: var(--color-text-primary);
  padding: 15px 0;
  width: 100%;
  font-size: 1.1rem;
}
.search-input::placeholder {
  color: var(--color-text-muted);
}
.search-results-info {
  margin-bottom: 30px;
  color: var(--color-text-secondary);
  display: flex;
  align-items: center;
  gap: 15px;
}
.btn-text {
  color: var(--color-accent);
  background: none;
  border: none;
  cursor: pointer;
  font-weight: 600;
  text-decoration: underline;
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
.empty {
  display: flex; flex-direction: column; align-items: center;
  gap: 12px; padding: 60px 0; color: var(--color-text-muted);
}
</style>
