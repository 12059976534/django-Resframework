from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token



urlpatterns=[
    path('',views.index,name='index'),
    path('user-list/',views.userlist,name='user-list'),
    path('kota-list/',views.kotalist,name='kota-list'),
    path('create-user/',views.createUser,name='create-user'),
    path('update-user/<int:id>',views.updateUser,name='update-user'),
    path('delete-user/<int:id>',views.deleteUser,name='delete-user'),
    path('detail-user/<int:id>',views.detailUser,name='detail-user'),
    # login rest auth
    path('login/',obtain_auth_token,name='login'),
]