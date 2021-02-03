import json
import logging
import traceback
imporfts psycopg2

version='1.0.6'

def lambda_handler(event, context):
  return {
            'statusCode': 200,
            'body' : 'Hello'
        }
