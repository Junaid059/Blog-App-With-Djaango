from rest_framework.serializers import ModelSerializer
from .models import NewUser


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['email', 'fullname', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = NewUser(**validated_data)
        user.username = validated_data['email']  # AbstractUser requires username
        if password is not None:
            user.set_password(password)
        user.save()
        return user