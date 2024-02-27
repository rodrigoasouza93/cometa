# cometa

## Setup projects

### Backend Python API - SETUP

Clone this repo:
    <https://github.com/rodrigoasouza93/cometa>

Access folder backend(terminal):
    cd backend

Install dependencies(terminal):
    pip install -r requirements.tsx

### Frontend cliente - SETUP

    TODO

## Run Projects

### Backend Python API

    Access folder backend(terminal), if you have not yet accessed:
        cd backend  
    Run this commands on terminal:
        python3 -m venv venv or python -m venv venv
        source venv/bin/activate
        uvicorn main.server:app
    The server will be running on port 8000, and should be found by accessing the url: http://127.0.0.1:8000 or http://localhost:8000

### Frontend client

    TODO

## Consume API

    You can check a list os APIs available accessing http://127.0.0.1:8000/docs or http://localhost:8000/docs;
    You can follow the next examples:
        * GET A LIST OF BEERS - attention the list of beers change if you restar the application
        ```shell
        curl --request GET \
            --url http://127.0.0.1:8000/beers
        ```
        * PLACE AN ORDER
        ```shell
        curl --request POST \
            --url http://127.0.0.1:8000/orders \
            --data '{
            "customer_name": "maria",
            "beer_id": "3e41fecb-eb90-4935-8b9a-808ed0f08ca0"
            }'
        ```
        * GET BILLING INFOS
        ```shell
        curl --request GET \
            --url http://127.0.0.1:8000/orders/billing
        ```
        * PROCESS PAYMENT
        ```shell
        curl --request POST \
            --url http://127.0.0.1:8000/orders/payment \
            --data '{
                "customer_name": "maria"
            }'
        ```
