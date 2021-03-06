import json
import packages.GET.FetchUserData
import packages.POST.CreateUserData
import packages.PUT.UpdateUserData
#Server Host
baseurl="https://reqres.in"

#manual tests
'''
objective: Validate GET /api/users return user details when providing specific user ID or returns all users 
if asked.  

Test Steps: Run REST GET to /api/users?page=2 to get list of all users
Run REST Get to /api/users/4 to get details for specific user. 
Test should include values that do not exist, conditions for overflow, and check for invalid syntax. 

Expected Results: 
1) list of users and user details
2) expect response 200 for valid endpoint and verify response for invalid IDs. 
3) validate responses (200 series, 300 series, 400 series, 500 series)
'''
###############
print('\nGET Methods Tests')
###############
result=packages.GET.FetchUserData.get_all_user_email(baseurl+'/api/users?page=2')
#Manual test to check response of the API call is a list of all email address
print (f'The response type of the API is: {type(result[1])}')

#Manual Test to check userid=4 returns email address
print(packages.GET.FetchUserData.get_all_user_email(baseurl+'/api/users/4'))

#Manual Test to check all email addresses are returned.
print (packages.GET.FetchUserData.get_all_user_email(baseurl + '/api/users?page=2'))

###############
print ('\nPOST Methods Tests')
###############
#Generate the json payload
request_json = json.loads('{"name":"Jon Doe","job":"QA"}')
result=packages.POST.CreateUserData.create_userdata((baseurl + '/api/users'), request_json)
#Manual Test to verify HTTP Response == 201
print (f'The HTTP Status is: {result[0]}')
#Manual Test to verify server created a user (and display user id) and timestamp of the opperation
print (f'The HTTP Response is {result[1]}')

###############
print ('\nPUT Methods Tests')
###############
#Generate the json payload
request_json = json.loads('{"name":"Jonathan Doe","job":"QA Manager"}')
result=packages.PUT.UpdateUserData.update_userdata(baseurl + '/api/users/2', request_json)
print (f'The HTTP Status is: {result[0]}')
print (f'The HTTP Response is: {result[1]}')

