from rest_framework import serializers
from . import models

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=models.User
        fields=[
            'id',
            'nama',
            'tgl',
            'email',
            'username',
            'password',
            'date',
            'leveluser',
            'kota',
            
             ]
        # fields='__all__'


class Kotaserializer(serializers.ModelSerializer):
    class Meta:
        model=models.Kota
        fields='__all__'
        

class Leveluserserializer(serializers.ModelSerializer):
    class Meta:
        model=models.Leveluser
        fields='__all__'


class Comenserializer(serializers.ModelSerializer):
    class Meta:
        model=models.Comment
        fields='__all__'
