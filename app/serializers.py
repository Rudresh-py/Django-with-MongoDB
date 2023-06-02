from django.contrib.auth.models import User
from app.models import User, Product
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user


class ProductSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Product
        fields = ['name', 'attributes', 'user']
