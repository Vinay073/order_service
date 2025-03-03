# **Product API Documentation**

This project implements a backend system for managing and processing orders in an e-commerce platform. It includes
RESTful APIs, asynchronous order processing using an in-memory queue, and metrics reporting.

## **Table of Contents**

1. [Prerequisites](#prerequisites)
2. [How to Run the Application](#how-to-run-the-application)
3. [API Endpoints](#api-endpoints)
    - [Create an Order](#create-an-order)
    - [Check Order Status](#check-order-status)
    - [Fetch Metrics](#fetch-metrics)

---

## **prerequisites**

- Clone the repository using below command

```bash
    git clone https://github.com/Vinay073/order_service.git
```

- Python 3.10 Version
- `pip` (Python package installer)
- Create a virtual env using below command s

```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
```

---

## **how-to-run-the-application**

```bash
    cd order_service
    python app.py
    
```

## **Overview**

The Current repo i have implemented the following functionality:

- Accepting new orders via a RESTful API.
- Simulating asynchronous order processing using an in-memory queue.
- Providing APIs to check the status of orders and fetch system metrics.
- The database i have used is SQLite for simplicity, and the application is built using Python Flask.

## **API Endpoints**

### **Create an Order**

- **Request**:
  ```bash
  curl -X POST https://order-service-ra6t.onrender.com/order \
  -H "Content-Type: application/json" \
  -d '{
    "order_id": "12345",
    "user_id": "user_001",
    "item_ids": ["item_001", "item_002", "item_003"],
    "total_amount": 150.75
  }'

### **Check order status**

```bash
      curl -X GET  https://order-service-ra6t.onrender.com/order/456
```

### **Fetch Metrics**

```bash
      curl -X GET https://order-service-ra6t.onrender.com/metrics
```
