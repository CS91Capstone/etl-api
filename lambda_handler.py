import os
import json
import pymysql

# https://stackify.com/aws-lambda-with-python-a-complete-getting-started-guide/
# https://docs.aws.amazon.com/lambda/latest/dg/python-image.html
# https://pypi.org/project/PyMySQL/#documentation


MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_PORT = os.environ['MYSQL_PORT']
MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASS = os.environ['MYSQL_PASS']


def query_mysql() -> dict:
    result: dict = None
    destination_table: str = "recreationgov_base_v1"
    
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
            cursor.execute(f"SELECT * FROM {destination_table} LIMIT 10")
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
        data['id'] = record[0]
        data['last_modified'] = record[1].strftime('%Y-%m-%dT%H:%M:%SZ') 
        data['campsite_id'] = record[2]
        data['facility_id'] = record[3] 
        data['campsite_name'] = record[4] 
        data['campsite_type'] = record[5] 
        data['type_of_use'] = record[6] 
        data['campsite_accessible'] = record[7] 
        data['campsite_reservable'] = record[8] 
        data['campsite_longitude'] = record[9] 
        data['campsite_latitude'] = record[10]  
        transform_data.append(data)
    return transform_data


def handler(event, context):
    query_result: dict = query_mysql()   
    transformed_result: list = transform(records=query_result)
 
    return {
        'statusCode': 200,
        'body': transformed_result,
        "headers": {
            'Content-Type': 'application/json'
        }
    }