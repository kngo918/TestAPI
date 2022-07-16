import packages.GET.FetchUserData
from packages.GET import FetchUserData
#Server Host
baseurl="https://reqres.in"

'''
Automated tests using pytest
usage: In the .\TestAPI directory, run 'pytest' command to find
       test_*.py, *_test.py files and functions named test_* or *_test 
'''
def test_get_all_user_email():
    list = []

    #tests to validate the functions return
    result = packages.GET.FetchUserData.get_all_user_email(baseurl + '/api/users?page=2')
    assert type(result[1]) == type(list)
    result = packages.GET.FetchUserData.get_all_user_email(baseurl + '/api/users/4')
    assert type(result[1]) == type(list)

def test_expect_get_fail():
    dict = {}

    #tests to validate the functions return
    result = packages.GET.FetchUserData.get_all_user_email(baseurl + '/api/users/4')
    assert type(result[1]) == type(dict) #expect assertion failure