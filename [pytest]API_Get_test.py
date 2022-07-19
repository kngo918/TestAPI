import packages.GET.FetchUserData
import packages.POST.CreateUserData
import json
import requests

from packages.GET import FetchUserData
#Server Host
baseurl="https://reqres.in"

'''
Automated tests using pytest
usage: In the TestAPI directory, run 'pytest' command to find
       test_*.py, *_test.py files and functions named test_* or *_test 
'''
def test_GET_functional():
    list = []

    #tests to validate the functions return
    result = packages.GET.FetchUserData.get_all_user_email(baseurl + '/api/users?page=2')
    assert type(result[1]) == type(list)
    result = packages.GET.FetchUserData.get_all_user_email(baseurl + '/api/users/4')
    assert type(result[1]) == type(list)
    http_response = requests.get(baseurl+'/api/users/5')
    assert http_response.status_code == 200


def test_expect_get_fail():
    #tests to validate the functions return
    #We expect (e-fail) this test to fail the assertion and result in a test failure
    result = packages.GET.FetchUserData.get_all_user_email(baseurl + '/api/users/4')
    assert type(result[1]) == type(dict) #expect assertion failure

def test_POST_functional():
    #test cases to validate a new user 'Jon Doe' with job 'QA' can be created
    request_json = json.loads('{"name":"Jon Doe","job":"QA"}')
    http_response = requests.post(baseurl + '/api/users',request_json)
    json_response = json.loads(http_response.text)
    assert http_response.status_code == 201
    assert json_response['name'] == "Jon Doe"
    assert json_response['job'] == "QA"

def test_PUT_functional():
    request_json = json.loads('{"name":"Jonathan Doe","job":"QA Manager"}')
    http_response = requests.post(baseurl + '/api/users/2',request_json)
    json_response = json.loads(http_response.text)
    assert http_response.status_code == 201
    assert json_response['name'] == "Jonathan Doe"
    assert json_response['job'] == "QA Manager"