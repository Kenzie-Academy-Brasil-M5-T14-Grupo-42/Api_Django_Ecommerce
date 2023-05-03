from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset = User.objects.all(), message = "A user with that username already exists.")
        ],
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset = User.objects.all())
        ],
    )

    def create(self, instance: User, validated_data: dict) -> User:
        if validated_data.get("role") == "Administrador":
            return User.objects.create_superuser(**validated_data)
        
        else:
            return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)

                continue
            setattr(instance, key, value)

        instance.save()

        return instance
    
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "role", "username", "email", "password"]
        read_only_fields = ["id","is_superuser"]
        extra_kwargs = {"password": {"write_only": "True"}}