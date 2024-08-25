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
        "id": product ID,
        "images": [
            {
                "id": image1 ID,
                "image": "image1 url"
            },
            {
                "id": image2 ID,
                "image": "image2 url"
            }
        ],
        "ad_title": "product title name",
        "description": "product description",
        "price": "product price",
        "date_posted": "date the product was posted",
        "views": number of product views,
        "is_verified": boolean value,
        "owner": product owners ID,
        "category": Category ID,
        "location": Location ID,
        "shop": Shop ID,
        "likes": [
            likes count
        ]
    },
    
   
]
```

## Fetching a Single Product(Product Details)
GET /products/pk/ - Retrieve a single product details

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
    "views": number of views,
    "is_verified": boolean value,
    "owner": product owners ID,
    "category": product category ID,
    "location": Product Geographical Location ID,
    "shop": Product Shop,
    "likes": [
        likes counts
        ]
}
```


## Posting a Product
POST /createproductsapi/ - Create a new product (requires authentication)
### Request Body
The category should be the ID of the categories from the DB

The shop should be the ID of the authenticated users shop

```bash
{
    "category":"Select product category",
    "location":"Location ID",
    "images":[imeage1, image2],
    "ad_title":"product name",
    "price":"520",
    "description":"product description",
    "shop":"shop ID"
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



## Fetching all shops
GET /shop/ - Retrieve a list of all the shops

#### Response

```bash
[
    {
        "id": shop ID,
        "images": [
            {
                "id": image1 ID,
                "image": "image1 url"
            },
            {
                "id": image2 ID,
                "image": "image2 url"
            }
        ],
        "name": "shop name",
        "description": "shop description",
        "registered_o": "date the shop was created",
        "is_verified": boolean value,
        "owner": shop owners ID,
        "category": Category ID,
        "location": Location ID,
    },
    
   
]
```

## Fetching a Single Shop(shop Details)
GET /shop/pk/ - Retrieve a single shop details

### Response

```bash
{
    "id": shop ID,
        "images": [
            {
                "id": image1 ID,
                "image": "image1 url"
            },
            {
                "id": image2 ID,
                "image": "image2 url"
            }
        ],
        "name": "shop name",
        "description": "shop description",
        "registered_o": "date the shop was created",
        "is_verified": boolean value,
        "owner": shop owners ID,
        "category": Category ID,
        "location": Location ID,
}
```


## Posting a Shop
POST /shopcreateapi/ - Create a new shop (requires authentication)
### Request Body
The category should be the ID of the categories from the DB



```bash
{
    "category":"Select product category",
    "location":"Location ID",
    "images":[imeage1, image2],
    "name":"shop name",
    "description":"shop description",
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
    "name": "shop name",
    "description": 'shop description',
    "is_verified": boolean value,
    "owner": id of the shop owner,
    "category": 'category Id the shop belongs',
    "location": 'location ID',
}
```

# Locations

## Fetching all the geographical locations
GET /location/ - Retrieve a list of all the geographical locations


### Response

```bash
[
    {
        "id": 1,
        "name": "laction name"
    },
    {
        "id": 2,
        "name": "location name"
    },
    {
        "id": 3,
        "name": "location name"
    },
    {
        "id": 4,
        "name": "Location name"
    }
]
```


# Category

## Fetching all the product Category

GET /productcategory/ - Retrieve a list of all the product categories

### Response 
```bash
[
    {
        "id": product category ID,
        "name": "product category name",
        "image": "product category icon url"
    }
]
```


## Fetching all the shop Category

GET /shopcategory/ - Retrieve a list of all the shop categories

### Response 
```bash
[
    {
        "id": shop category ID,
        "name": "shop category name",
        "image": "shop category icon url"
    }
]
```
# News Letter
## Creating a newsletter
POST /createnewsletter/ - creating a new newsletter

### Request Body

```bash
{
    'email': 'your email'
}
```

### Response Body

```bash
{
    'id': news letter ID,
    'email': 'your email',
    'time_created': 'time the the letter is created'
}
```



# Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and push your branch to your fork.
Open a pull request with a detailed description of your changes.

# License
This project is licensed under the MIT License. See the LICENSE file for more information.
 
