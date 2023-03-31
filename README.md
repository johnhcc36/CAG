1) Setting up AWS DynamoDB:

- Go to the AWS Management Console and navigate to DynamoDB.
- Create a new table with "id" as the primary key.
- Add additional fields for "name", "category", "price", and "last_updated_dt".

2) Install necessary dependencies:

- boto3: AWS SDK for Python

3) Running the code locally:
- Ensure that you have AWS credentials set up in your local environment.
- Install the necessary dependencies by running pip install boto3.
- Run the unit tests by executing python -m unittest Task1_UnitTest.py.
- You can also run the function locally by importing it in another Python script and passing in the item details as a dictionary to the insert_item() function.