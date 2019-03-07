from django.urls import path,re_path
from user_management import views as user_management_views

urlpatterns = [
	#登录注册注销的Url
	path('user_login/',user_management_views.user_login,name='user_login'),
	path('user_registration/',user_management_views.user_registration,name='user_registration'),
    path('user_logout/',user_management_views.user_logout,name='user_logout'),

    #个人信息的Url
    path('personal_information_modification/',user_management_views.personal_information_modification,name = 'personal_information_modification'),

]