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

### Github Actions
AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY should be provided in Github Secret. Whenever file pushed into `/endpoints` folder, Github Actions will be triggered and a Lambda function that pull code from Github to S3 will be called.
