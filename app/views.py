from django.shortcuts import render,reverse
from django.core.exceptions import ObjectDoesNotExist #untuk hendel eror get data ketika tidak ada
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password

from . import serilizer
from . import models

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes,authentication_classes
# Create your views here.


@api_view(['GET'])
def index(request):
    
    context={
        'list':'http://127.0.0.1:8000/user-list/',
        'detail-user':'http://127.0.0.1:8000/datai-user/',
        'kota-list':'http://127.0.0.1:8000/kota-list/',
        'Create-User':'http://127.0.0.1:8000/create-user/',
        'Update-User':'http://127.0.0.1:8000/update-user/id',
        'Delete-User':'http://127.0.0.1:8000/delete-user/id',
        'Detail-User':'http://127.0.0.1:8000/detail-user/id',
    }
    return Response(context)

# user api views
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def userlist(request,format=None):
    user=models.User.objects.filter(is_superuser=False)
    seriliz=serilizer.Userserializer(user,many=True)
    print(len(seriliz.data))
    return Response({'jumlahuser':len(seriliz.data),'data':seriliz.data})

# detail user
@api_view(['GET'])
def detailUser(request,id):
    user=models.User.objects.filter(id=id)
    seriliz=serilizer.Userserializer(user,many=True)
    print(len(seriliz.data))
    return Response({'data':seriliz.data})

# api create user baru
@api_view(['POST'])
def createUser(request):
    # hendel post data 
    serializer=serilizer.Userserializer(data=request.data)
    # ===============
    
    # ambil data from db
    # user=models.User.objects.filter(is_superuser=False)
    # serializ data
    # seriliz=serilizer.Userserializer(user,many=True)
    # =========

    # token 

    if serializer.is_valid():
        account = serializer.save()  
        # data=serializer.data
        # level=models.Leveluser.objects.get(id=int(data['leveluser']))
        # models.User(
        #     nama=data['nama'],
        #     tgl=data['tgl'],
        #     email=data['email'],
        #     username=data['username'],
        #     password=make_password(data['password']),
        #     leveluser=level,
        #     kota=data['kota']
        #     ).save()
        # user=models.User.objects.get(username=data['username'])    
        # token=Token.objects.get(user_id=user.id)
        # print(token.created ) 
        # return Response(token.key)
        token = Token.objects.get(user=account).key

        return Response(token)    
    return Response(serializer.is_valid(raise_exception=True))
         

# api update user
@api_view(['PUT'])
def updateUser(request,id):
    user=models.User.objects.get(id=id)
    serializer=serilizer.Userserializer(instance=user,data=request.data)
    if serializer.is_valid():
        serializer.save()  
        return Response(serializer.data)    
    return Response(serializer.is_valid(raise_exception=True))    

# api delete user
@api_view(['DELETE'])
def deleteUser(request,id):
    try:
        user=models.User.objects.get(id=id)
        user.delete()
        return Response('delete succes') 
    except ObjectDoesNotExist:    
        return Response("user not exis")    
    

#kota api views
@api_view(['GET'])
def kotalist(request):
    kota=models.Kota.objects.all()
    seriliz=serilizer.Kotaserializer(kota,many=True)
    
    return Response(seriliz.data)    




        
