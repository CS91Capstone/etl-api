# ETL API

Lambda code used with API Gateway

### Software packages
All we used was pymysql to connect to our mysql database.

### Endpoints
Each of the endpoints are located inside of the endpoints folder. These endpoints are then deployed to AWS. Once they are in AWS they can be deployed in API Gateway for clients to use. This API does not require clients to have any kind of API key to use. 

### Swagger Documentation
You can import the file openapi.yaml into [swagger.io](https://editor.swagger.io/) editor. This gives you some documentation on the API and what endpoints require what information. 

### Postman
In the postman folder we have a collection that you can use/test our endpoints.
