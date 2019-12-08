from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['url', 'id', 'first_name', 'middle_name', 'last_name', 'email', 'company', 'position', 'type', ]
        read_only_fields = ('id',)



# class UserCreateSerializer(ModelSerializer):
#     password1 = serializers.CharField(write_only=True)
#     password2 = serializers.CharField(write_only=True)
#
#     def create(self, validated_data):
#         user = UserModel.objects.create_user(
#             first_name=validated_data['first_name'],
#             middle_name=validated_data['middle_name'],
#             last_name=validated_data['last_name'],
#             email=validated_data['email'],
#             password1=validated_data['password1'],
#             password2=validated_data['password2'],
#             company=validated_data['company'],
#             position=validated_data['position'],
#
#         )
#         return user
#
#     class Meta:
#         model = UserModel
#         fields = (
#             'first_name',
#             'middle_name',
#             'last_name',
#             'email',
#             'password1',
#             'password2',
#             'company',
#             'position',
#         )
#
#         extra_kwargs = {'password1':
#                             {'write_only': True},
#                         'password2':
#                             {'write_only': True},
#                         }

