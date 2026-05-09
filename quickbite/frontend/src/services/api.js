import axios from 'axios'

const API_BASE = '/api'

const api = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json',
  },
})

export default {
  // Categories
  getCategories() {
    return api.get('/categories/')
  },

  // Products
  getProducts(categoryId = null) {
    const params = {}
    if (categoryId) params.category = categoryId
    return api.get('/products/', { params })
  },

  getFeaturedProducts() {
    return api.get('/products/featured/')
  },

  searchProducts(query) {
    return api.get('/products/', { params: { search: query } })
  },

  // Orders
  placeOrder(orderData) {
    return api.post('/orders/', orderData)
  },

  getOrder(orderId) {
    return api.get(`/orders/${orderId}/`)
  },
}
