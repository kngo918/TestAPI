import requests
import json

"""
POST Method: to Create a new resource on the server
"""
# input: REST url
# returns: tuple: (REST response,[list of emails])
def create_userdata(url,request_json):
    http_response = requests.post(url,request_json)
    json_response = json.loads(http_response.text)
    return http_response,json_response