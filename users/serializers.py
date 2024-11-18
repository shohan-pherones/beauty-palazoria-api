from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(
        max_length=15, required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    image = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = get_user_model()
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password',
            'phone_number', 'address', 'image'
        ]

    def create(self, validated_data):
        user_data = {key: validated_data.pop(key) for key in [
            'username', 'email', 'password', 'first_name', 'last_name']}
        user = get_user_model().objects.create_user(**user_data)

        CustomUser.objects.create(
            user=user,
            phone_number=validated_data.get('phone_number', ''),
            address=validated_data.get('address', ''),
            image=validated_data.get('image', None),
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = get_user_model().objects.filter(
            username=attrs['username']).first()
        if user and user.check_password(attrs['password']):
            try:
                custom_user = user.customuser
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError(
                    "Associated custom user does not exist.")
            return {'user': custom_user}
        raise serializers.ValidationError('Invalid credentials')


class CustomUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = CustomUser
        fields = ('id', 'user', 'first_name', 'last_name',
                  'phone_number', 'address', 'image')
