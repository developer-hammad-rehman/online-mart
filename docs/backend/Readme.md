# Online Mart App

## Overview

The Online Mart App is a microservices-based application designed to provide a seamless online shopping experience. The app is composed of several independent services that handle different aspects of the shopping process. These services communicate with each other to manage user authentication, inventory, payments, notifications, products, and orders.

## Microservices Architecture

The application is divided into the following microservices:

### 1. User-Service (Auth Service)
- **Purpose**: Manages user registration, authentication, and profile management.
- **Endpoints**: User login, logout, registration, and profile update.

### 2. Inventory Service
- **Purpose**: Manages product inventory, including stock levels and availability.
- **Endpoints**: Inventory check, stock update, and inventory listing.

### 3. Payment Service
- **Purpose**: Handles all payment-related operations, including payment processing and transaction management.
- **Endpoints**: Payment processing, payment status, and transaction history.

### 4. Notification Service
- **Purpose**: Sends notifications to users regarding order status, promotions, and other relevant information.
- **Endpoints**: Email notifications, SMS notifications, and push notifications.

### 5. Product Service
- **Purpose**: Manages product details, including product listings, descriptions, pricing, and categories.
- **Endpoints**: Product listing, product detail, and product search.

### 6. Order Service
- **Purpose**: Handles order creation, management, and tracking.
- **Endpoints**: Order creation, order status, and order history.

## Technologies Used

- **Docker**: For containerizing the microservices.
- **Azure Container Apps**: For deploying and managing containers in the cloud.
- **FastAPI**: As the web framework for building the microservices.
- **PostgreSQL**: For relational database management.
- **Kafka**: For event streaming and communication between microservices.
- **API Management Service**: For managing and securing APIs.

## Getting Started

### Prerequisites
- Docker
- Azure account
- PostgreSQL
- Kafka

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/developer-hammad-rehman/online-mart-app.git
   cd online-mart-app
