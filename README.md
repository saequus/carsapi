# Carsapi

## Preparation

Note: poetry should already be installed on the system.

### Local setup
~~~
make shell
make install
make migrate
make up
~~~

### Logging into admin

Credentials will be sent to you after request to __slava@spetsyian.com__.

## API

### Swagger
~~~
/redoc/
/swagger/
~~~

### Sending requests

---
1. Flush db before use (just to be sure no previous data is present)
~~~
curl --location --request GET 'http://3ckster.com/api/v2/flush-db/'
~~~
Response
~~~ json
{
    "status": "flushed"
}
~~~

---
2. Post data to retrieve car
~~~

curl --location --request POST 'http://3ckster.com/api/cars/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": "Civic",
    "make": "Honda"
}'
~~~
Response
~~~ json
{
    "model": "Civic",
    "make": "Honda"
}
~~~

---
3. Post rating data
~~~
curl --location --request POST 'http://3ckster.com/api/rate/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "car_id": 1,
    "rating": 5
}'
~~~
Response
~~~ json
{
    "rating": 5,
    "car_id": 1
}
~~~

---
4. Get aggregated cars data
~~~
curl --location --request GET 'http://3ckster.com/api/cars/'
~~~
Response
~~~ json
[
    {
        "id": 1,
        "make": "HONDA",
        "model": "Civic",
        "avg_rating": 5.0
    }
]
~~~

---
5. Get information on which cars are popular by their rates number
~~~
curl --location --request GET 'http://3ckster.com/api/popular/'
~~~
Response
~~~ json
[
    {
        "id": 1,
        "make": "HONDA",
        "model": "Civic",
        "rates_number": 1
    }
]
~~~



