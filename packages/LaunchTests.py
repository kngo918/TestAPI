import packages.GET.FetchUserData
from packages.GET import FetchUserData
#Server Host
baseurl="https://reqres.in"


print(packages.GET.FetchUserData.get_all_user_email(baseurl+'/api/users?page=2'))
print(packages.GET.FetchUserData.get_all_user_email(baseurl+'/api/users/4'))
#todo:
#assert packages.GET.FetchUserData.get_all_user_email(baseurl+'/api/users/4')[0] == "Response [200]"
#assert type(ackages.GET.FetchUserData.get_all_user_email(baseurl+'/api/users/4')[1] == type(list)

