# Django Python Assignment

## Introduction

This is a Django project that provides a RESTful API for managing invoices and associated details.

## Prerequisites

- Python 3.x
- Django
- Django REST framework

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/PhaleshM/Assignment_Django_Python
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```bash
    cd DjangoAssignment
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the API at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API Endpoints

- `GET /invoices/`: Get a list of all invoices.
- `POST /invoices/`: Create a new invoice.
- `GET /invoices/{invoice_id}/`: Get details of a specific invoice.
- `PUT /invoices/{invoice_id}/`: Update a specific invoice.
- `DELETE /invoices/{invoice_id}/`: Delete a specific invoice.

## Payload Format

The payload for creating or updating an invoice should be in the following format:

```json
{
    "customer_name": "Customer Name",
    "date": "YYYY-MM-DD", ##optional
    "details": {
        "description": "Invoice Description",
        "quantity": 5,
        "unit_price": 20
    }
}
