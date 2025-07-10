from rest_framework.serializers import ModelSerializer, CharField
from . import models
from django.contrib.auth.hashers import make_password


# users profiles
class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'


# users
class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)
    profiles = UserProfileSerializer(
        source='user_profiles', many=True, read_only=True)

    class Meta:
        model = models.Users
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.password = make_password(password)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


# levels
class LevelSerializer(ModelSerializer):
    class Meta:
        model = models.levels
        fields = '__all__'


# books
class BookSerializer(ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'


# logins
class LoginSerializer(ModelSerializer):
    class Meta:
        model = models.Logins
        fields = '__all__'
