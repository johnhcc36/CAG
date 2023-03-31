Requirements
- Python 3.x
- AWS CLI
- AWS account
- SQLite 3 (for testing)


Setup
1. Clone this repository to your local machine.

2. Install the required Python packages:
	pip install -r requirements.txt
	
	
3. Set up an AWS API Gateway and Lambda function:

 - Follow the instructions in the AWS documentation to create a new API Gateway and Lambda function.

 - In the Lambda function, copy and paste the code from the "Task1_code.py" file.

4. Modify the Task1_code.py file to connect to your database:

 - Modify the DB_FILE variable to point to the location of your SQLite database file.

 - Modify the DB_TABLE variable to match the name of your database table.

5. Deploy the Lambda function:

 - Zip the Task1_code.py file and any required packages into a single archive. For example:
	zip function.zip Task1_code.py sqlite3.py

 - Use the AWS CLI to upload the zip file to your Lambda function:
	aws lambda update-function-code --function-name <function-name> --zip-file fileb://function.zip

6. Test the Lambda function:

	- Use the AWS API Gateway test feature to test the Lambda function with the following JSON input:
		
	{
		"name": "Notebook",
		"category": "Stationary",
		"price": 5.5
	}
	
	
7. Run unit tests:

	- Run the following command to execute the unit tests:
	  python Task1.UnitTest.py


Usage

To use the API, send an HTTP POST request to the URL of your API Gateway endpoint with a JSON payload containing the item details. 
  
 For example for Task1:

 curl -X POST https://<api-gateway-endpoint>/path/to/lambda-function \
     -H 'Content-Type: application/json' \
     -d '{
             "name": "Notebook",
             "category": "Stationary",
             "price": 5.5
         }'

The response will contain a JSON object with a new id field assigned by the server:
  {
    "id": 1
  }

