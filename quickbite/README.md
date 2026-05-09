# QuickBite — Food Delivery Website

A full-stack food ordering website built with **Vue 3** and **Django REST Framework**.

## 🚀 Quick Start

### Backend (Django)

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py seed        # Load sample data
python manage.py runserver   # Starts on http://127.0.0.1:8000
```

### Frontend (Vue 3)

```bash
cd frontend
npm install
npm run dev    # Starts on http://localhost:5173
```

### Admin Panel

Visit `http://127.0.0.1:8000/admin/` to manage products, categories, and orders.

Create a superuser first:
```bash
cd backend
python manage.py createsuperuser
```

## 📁 Project Structure

```
quickbite/
├── backend/          # Django REST API
│   ├── api/          # Models, views, serializers
│   ├── quickbite/    # Django settings
│   └── manage.py
├── frontend/         # Vue 3 SPA
│   ├── src/
│   │   ├── components/   # Reusable UI components
│   │   ├── views/        # Page views
│   │   ├── stores/       # Pinia state management
│   │   ├── services/     # API service
│   │   └── router/       # Vue Router config
│   └── index.html
└── README.md
```

## ✨ Features

- 🎨 Premium dark theme with glassmorphism
- 📱 Fully responsive (mobile, tablet, desktop)
- 🛒 Add to cart with slide-in sidebar
- 📦 Order placement with delivery details
- 🔍 Category filtering on menu page
- ⭐ Featured products on homepage
- 🎁 Special offers page
- ⚡ Fast page transitions

## 🛠 Tech Stack

| Layer    | Technology              |
|----------|------------------------|
| Frontend | Vue 3, Vite, Pinia     |
| Backend  | Django, DRF            |
| Database | SQLite                 |
| Styling  | Vanilla CSS            |
