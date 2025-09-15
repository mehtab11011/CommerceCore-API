# ORM – Django REST Framework E-commerce API

## 📌 Overview

**ORM** is a Django project that demonstrates how to expose an already existing **E-commerce database** as RESTful APIs using **Django REST Framework (DRF)**.

Instead of designing a new schema, this project takes the pre-defined models inside `orm_app` (Customer, Product, Order, and OrderItem) and integrates them into the `api` app with **serializers, viewsets, and routers**.

The goal is to show how existing databases can be modernized and made accessible for **mobile apps, frontend frameworks (React, Vue, Angular)**, or even **third-party systems**.

---

## 🏗️ Project Structure

```
orm/                -> Main Django project  
│  
├── orm_app/        -> Contains database models (Customer, Product, Order, OrderItem)  
│   └── models.py   -> Defines E-commerce schema  
│  
├── api/            -> Django REST Framework app  
│   ├── serializers.py -> Converts models into JSON  
│   ├── views.py       -> ViewSets for CRUD operations  
│   └── urls.py        -> Routers for clean endpoints  
│  
└── manage.py
```

---

## 📦 Models (Inside `orm_app/models.py`)

* **Customer** → One-to-One with User model, includes phone and address.
* **Product** → Name, price, and stock management.
* **Order** → Linked to Customer, supports multiple products.
* **OrderItem** → Through model to manage product quantities in each order.

---

## 🔗 API Endpoints (Inside `api/urls.py`)

* `/api_view/user/` – Manage users
* `/api_view/custmer/` – Manage customers
* `/api_view/product/` – Manage products
* `/api_view/order/` – Manage orders
* `/api_view/orderitems/` – Manage order items

All endpoints return **JSON responses**, making the database ready for use in frontend and mobile applications.

---

## 🚀 How It Works

1. Models are defined in `orm_app`.
2. Serializers in `api/serializers.py` convert models into JSON.
3. ViewSets in `api/views.py` provide CRUD operations.
4. Routers in `api/urls.py` create clean API endpoints.
5. The main `urls.py` includes all API routes.

This turns the e-commerce database into a **fully functional API system**.

---
Perfect point Mehtab 👍
Adding **project run commands** in the README makes it super professional and easy for others to set up your repo. Here’s the updated section you can paste:

---

## ⚡ Installation & Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/orm.git
cd orm
```

### 2️⃣ Create and activate virtual environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

The project will now be running at:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

API endpoints will be available under:
👉 [http://127.0.0.1:8000/api\_view/](http://127.0.0.1:8000/api_view/)

---

## 📌 Use Cases

* Mobile apps can fetch products, customers, and orders.
* Web apps (React/Vue) can display and manage store data.
* Businesses can integrate third-party services with their e-commerce system.

---

## 🔮 Next Steps

Planned improvements include:

* 🔑 JWT Authentication
* 📦 Order tracking & statuses
* 💳 Payment gateway integration

---
