import os
import json

# https://stackify.com/aws-lambda-with-python-a-complete-getting-started-guide/
# https://docs.aws.amazon.com/lambda/latest/dg/python-image.html
# https://pypi.org/project/PyMySQL/#documentation


MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_PORT = os.environ['MYSQL_PORT']
MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASS = os.environ['MYSQL_PASS']

def query_mysql(campsite_id) -> dict:
    result: dict = None
    destination_table: str = "Campsites_Access"
    
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        port=int(MYSQL_PORT),
        passwd=MYSQL_PASS,
        db=MYSQL_DATABASE,
        connect_timeout=5
    )
    try:
        with conn.cursor() as cursor:
            # cursor.execute(f"SELECT campsite_id FROM {destination_table} WHERE campsite_accessible = 1")
            cursor.execute(f"SELECT campsite_accessible FROM {destination_table} WHERE campsite_id = {campsite_id} ")
            result = cursor.fetchall()

    except Exception as e:
        print(e)

    finally:
        if(conn is not None and conn.open):
            conn.close()

    return result

def transform(records: list) -> list:
    transform_data: list = []
    for record in records:
        data: dict = {}
        data['campsite_accessible'] = record[0]
        transform_data.append(data)
    return transform_data


def lambda_handler(event, context):
    campsite_id: str = event['campsite_id']
    query_result: dict = query_mysql(campsite_id)
    transformed_result: list = transform(records=query_result)
    # TODO implement
    return {
        'statusCode': 200,
        'body': transformed_result,
        "headers": {
            'Content-Type': 'application/json'
        }
    }
