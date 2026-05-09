<template>
  <div class="category-filter" id="category-filter">
    <button
      class="filter-pill"
      :class="{ active: !selectedCategory }"
      @click="$emit('select', null)"
      id="filter-all"
    >All</button>
    <button
      v-for="cat in categories"
      :key="cat.id"
      class="filter-pill"
      :class="{ active: selectedCategory === cat.id }"
      @click="$emit('select', cat.id)"
      :id="'filter-' + cat.id"
    >
      {{ cat.name }}
      <span class="pill-count">{{ cat.product_count }}</span>
    </button>
  </div>
</template>

<script setup>
defineProps({
  categories: { type: Array, default: () => [] },
  selectedCategory: { default: null },
})
defineEmits(['select'])
</script>

<style scoped>
.category-filter {
  display: flex; flex-wrap: wrap; gap: 10px;
  margin-bottom: 40px; padding-bottom: 20px;
}
.filter-pill {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 10px 20px; border-radius: 999px;
  font-size: 0.875rem; font-weight: 500;
  background: var(--color-bg-glass); border: 1px solid var(--color-border);
  color: var(--color-text-secondary); cursor: pointer;
  transition: all 0.2s ease;
}
.filter-pill:hover {
  background: var(--color-bg-glass-hover); border-color: var(--color-border-hover);
  color: var(--color-text-primary);
}
.filter-pill.active {
  background: var(--color-accent); border-color: var(--color-accent);
  color: white;
}
.pill-count {
  font-size: 0.7rem; padding: 2px 6px; border-radius: 999px;
  background: rgba(255,255,255,0.15);
}
.filter-pill.active .pill-count { background: rgba(255,255,255,0.25); }
</style>
