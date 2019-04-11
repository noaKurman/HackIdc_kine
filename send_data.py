#! /usr/bin/python3.7
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import requests
import boto3
import datetime

host = 'search-kine-project-xgu3iblcsmpalo7cw3ksno7bie.us-east-2.es.amazonaws.com' # For example, my-test-domain.us-east-1.es.amazonaws.com
region = 'us-east-2' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(access_key, secret_key, region, service)

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)
document = {
    "Comment number": 888,
    "id": 10156903362466670,
    "authorProfileId": 1648450909,
    "max_exp": 3089348,
    "sentiment": 0.5,
    "tag": "REAL_PROFILE",
    "type": "Comment" }
#document = {
#    "id": 5,
#    "timestamp": datetime.datetime.now(),
#    "title": "testing 3",
#    "test_body": "testing testing",
#    "year": "2020"
#}

es.index(index="test", doc_type="_doc", id="9", body=document)
