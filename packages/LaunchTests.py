import packages.GET.FetchUserData
from packages.GET import FetchUserData
#Server Host
baseurl="https://reqres.in"

#manual tests
result=packages.GET.FetchUserData.get_all_user_email(baseurl+'/api/users?page=2')
print (type(result[1]))
print(packages.GET.FetchUserData.get_all_user_email(baseurl+'/api/users/4'))


