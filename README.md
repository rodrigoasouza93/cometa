# cometa

## Setup projects

Clone this repo:
    <https://github.com/rodrigoasouza93/cometa>

You must have installed on your machine nodejs and python
<https://nodejs.org/>
<https://www.python.org/>

### Backend Python API - SETUP

Access folder backend(terminal):
    cd backend

Install dependencies(terminal):
    pip install -r requirements.tsx

### Frontend cliente - SETUP

    Access folder frontend(terminal):
        cd frontend

    install dependencies(terminal):
        npm install

## Run Projects

### Backend Python API

    Access folder backend(terminal), if you have not yet accessed:
        cd backend
    Run a command on terminal:
        uvicorn main.server:app
    The server will be running on port 8000, and should be found by accessing the url: http://127.0.0.1:8000 or http://localhost:8000

### Frontend client

    *To run frontend application you should run before backend application*
    Access folder frontend(terminal), if you have not yet accessed:
        cd frontend
    Run a command on terminal:
        npm run dev
    The application will be running on port 5173, and should be found by accessing the url: http://127.0.0.1:5173 or http://localhost:5173

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
