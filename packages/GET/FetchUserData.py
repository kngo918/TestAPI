import requests
import json


# input: REST url
# returns: tuple: (REST response,[list of emails])
def get_all_user_email(url):
    emaillist = []
    dict = {}
    response = requests.get(url)
    # jsonresponse is a dict (json) output
    jsonresponse = json.loads(response.text)

    # condition that jsonresponse['data'] is a list of dictionaries
    if type(jsonresponse['data']) == type(emaillist):
        for record in jsonresponse['data']:
            emaillist.append(record['email'])

    # condition that jsonresponse['data'] value is a string
    elif type(jsonresponse['data']) == type(dict):
        emaillist.append(jsonresponse['data']['email'])

    return response, emaillist  # returns response,list
