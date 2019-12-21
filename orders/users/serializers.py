from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Contact

UserModel = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['url', 'id', 'first_name', 'middle_name', 'last_name', 'email', 'company', 'position', 'type', ]
        read_only_fields = ('id',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'user', 'phone')
        read_only_fields = ('id',)
        extra_kwargs = {
            'user': {'write_only': True}
        }
