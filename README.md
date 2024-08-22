# MadukaShop Backend API Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Installation](#installation)
4. [Usage](#usage)
    - [Start Django Server](#1-start-django-server)
5. [API Endpoints](#api-endpoints)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction
This documentation provides an overview of the usage of the MadukaShop marketplace APIs.

## Project Overview
MadukaShop is a marketplace platform that allows users to buy and sell products. This backend API handles user authentication, product listings, and order management.

## Installation

Make sure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

## 1 Start Django Server
Visit http://localhost:8000 in your browser to access the application.

# API Endpoints
## Authentication

### Login
POST /users/token/ - Get User Token and Refresh Token for authentication

#### request Body
```bash
{
    "email": "your email",
    "password": "your password"
}
```
#### Response
```bash
{
    "refresh": "your refresh tok",
    "access": "your access token"
}
```

### Register
POST /users/register/ - Register a new user

#### Request Body

```bash
{
    "email":"your email",
    "first_name":"your first name",
    "last_name":"your last name"
    "phone_number":"your phone number",
    "password":"your password"
}
```
#### Email OTP Request Authentuication
POST /users/sendOtp/ - Email verification

#### Request Body

```bash
{
    "email":"your email"
}
```

#### Response

```bash
{
    "success"
}
```

### VErify OTP
Verifying with the OTP code sent to the Email

POST /users/verifyotp/ - Email verification

#### Request Body

```bash
{
    "email":"your email",
    "otp_number":"otp code sent to your email"
}
```

If success, a 200 response is returned
#### Response

```bash
{
    "message":"OTP verification successful."
}
```

if the verification expired, a 400 bad request is returned with a message

```bash
{
    "message":"'OTP code has expired, request a new one."
}
```

### Getting token Using the Refresh Token

POST /userstoken/refresh/   

#### Request Body

```bash
{
    "refresh":"refresh token"
}
```

#### Response

if token is valid, you get a 200 status of ok

Response Body
```bash
{
    "access": "eyJhbGciOiJIUzI1Ni",
    "refresh": "eyJhbGciOiJIUz"
}
```

if token is invalid, you get a 401 error status 

Response Body
```bash
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
```

nb: `Access Token expires after 5 minutes while Refresh Token expires after 1 day`

# Products

## Fetching all products
GET /products/ - Retrieve a list of all the products

#### Response

```bash
[
    {
        "id": 1,
        "images": [
            {
                "id": 1,
                "image": "https://res.cloudinary.com/dndmmeamv/raw/upload/v1/images/product_images/425275967_350963471252612_8093914443767549707_n_kyxpki.jpg"
            },
            {
                "id": 5,
                "image": "https://res.cloudinary.com/dndmmeamv/raw/upload/v1/images/product_images/7io30qysok731_eygd50.jpg"
            }
        ],
        "ad_title": "Coffee Table",
        "description": "Built with the best wood",
        "price": "12000.00",
        "date_posted": "2024-03-25T12:58:18.543721Z",
        "views": 112,
        "is_verified": true,
        "owner": 1,
        "category": 1,
        "location": 1,
        "shop": 1,
        "likes": [
            1
        ]
    },
    {
        "id": 2,
        "images": [
            {
                "id": 2,
                "image": "https://res.cloudinary.com/dndmmeamv/raw/upload/v1/images/product_images/maxim-shklyaev-1oGP7-k3zvI-unsplash_gsjrwu.jpg"
            },
            {
                "id": 3,
                "image": "https://res.cloudinary.com/dndmmeamv/raw/upload/v1/images/product_images/patrick-langwallner-jWUrHPZjtoQ-unsplash_qytngl.jpg"
            },
            {
                "id": 4,
                "image": "https://res.cloudinary.com/dndmmeamv/raw/upload/v1/images/product_images/martin-sanchez-PnD5d2XTkl4-unsplash_hfmwa2.jpg"
            }
        ],
        "ad_title": "King Size Bed",
        "description": "The best bed with 6x6 king size bed",
        "price": "25000.00",
        "date_posted": "2024-03-25T14:32:46.036975Z",
        "views": 250,
        "is_verified": true,
        "owner": 1,
        "category": 1,
        "location": 2,
        "shop": 1,
        "likes": [
            1,
            2
        ]
    },
   
]
```

## Fetching a Single Product(Product Details)
GET /products/pk/ - Retrieve a list of all the products

### Response

```bash
{
    "id": 3,
    "images": [
        {
            "id": "image1 ID",
            "image": "image1 url"
        },
        {
            "id": "image2 ID",
            "image": "image2 url"
        },
    ],
    "ad_title": "Name of the product",
    "description": "product descripton",
    "price": "product price",
    "date_posted": "the date the product was posted",
    "views": 3,
    "is_verified": true,
    "owner": 1,
    "category": 1,
    "location": 4,
    "shop": 1,
    "likes": []
}
```


## Posting a Product
POST /createproductsapi/ - Create a new product (requires authentication)
### Request Body
The category should be the ID of the categories from the DB


The shop should be the ID of the authenticated users shop

```bash
{
    "category":"1",
    "location": "Nairobi",
    "images":[imeage1, image2],
    "ad_title":"HP Pavilion",
    "price":"520",
    "description":"very good, and it refurbished",
    "shop":"1"
}
```

### Response

```bash
{
    "id": 3,
    "images": [
        {
            "id": image1 ID,
            "image": "image1 url"
        },
        {
            "id": image2 ID,
            "image": "image2 url"
        },
    ],
    "ad_title": "Queen size bed",
    "description": 'product description',
    "date_posted": "product data",
    "views": 'number of views the product has',
    "is_verified": 'true or false',
    "owner": 'id of the products authos',
    "category": 'category Id the product belongs',
    "location": 'location ID',
    "shop": 'shop ID the product was posted in',
    "likes": ['number of likes the product has']
}
```


## Liking And Unlikeing a product

POST /productlike/pk/ - Like product (requires authentication)

### Request Body

```bash
{
    "user_who_liked":"userId",
}
```

### Response

the response for success is a 200 ok


#### response if user has not already liked the product
```bash
{
    "has_likes": True
}
```

### Unliking product
POST /productunlike/ - UnLike product (requires authentication)

#### request body

```bash
{
    "pk":"product_id",
    "user_id":"users_id"
}
```

### Response
the response for success is a 200 ok

```bash
{
    "message":"Like removed successfully!"
}
```

# Shops



Orders

GET /api/orders/ - Retrieve a list of orders (requires authentication)
POST /api/orders/ - Create a new order (requires authentication)
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and push your branch to your fork.
Open a pull request with a detailed description of your changes.
# License
This project is licensed under the MIT License. See the LICENSE file for more information.


### Additional Tips
- **Consistent Formatting**: Ensure consistent use of headings, code blocks, and list formatting.
- **Detailed API Information**: Include examples of requests and responses if applicable.
- **Links to Related Resources**: Provide links to any related documentation or resources that might be helpful to the user.

Feel free to adapt this template to fit the specific details and requirements of your project. 
