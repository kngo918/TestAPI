import packages.GET.FetchUserData
from packages.GET import FetchUserData
#Server Host
baseurl="https://reqres.in"

'''
Automated tests using pytest
'''
def test_get_all_user_email():
    list = []

    #tests to validate the functions return
    result = packages.GET.FetchUserData.get_all_user_email(baseurl + '/api/users?page=2')
    assert type(result[1]) == type(list)
    result = packages.GET.FetchUserData.get_all_user_email(baseurl + '/api/users/4')
    assert type(result[1]) == type(list)

