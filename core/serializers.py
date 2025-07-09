from rest_framework.serializers import ModelSerializer, CharField
from . import models


# users profiles
class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'


# users
class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)
    profiles = UserProfileSerializer(source='user_profiles', many=True)

    class Meta:
        model = models.Users
        fields = '__all__'


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
