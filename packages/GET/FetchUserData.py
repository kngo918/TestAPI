import requests
import json

#input: REST url
#returns: touple: (REST response,[list of emails])
def get_all_user_email(url):
    emaillist=[]
    dict={}
    response = requests.get(url)
    #jsonresponse is a dict (json) output
    jsonresponse = json.loads(response.text)

    #jsonresponse['data'] is a list of dictionaries
    if type(jsonresponse['data']) == type(emaillist):
        print (f"Debug: {type(jsonresponse['data'])}")
        for record in jsonresponse['data']:
            emaillist.append(record['email'])

    elif type(jsonresponse['data']) == type(dict):
        #print (f"The type of jsonresponse['data']['email'] is {type(jsonresponse['data']['email'])}")
        emaillist.append(jsonresponse['data']['email']) #returns a string
    #print(emaillist)
    return response,emaillist #returns a list