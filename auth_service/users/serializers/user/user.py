from rest_framework import serializers
from users.models.user import CustomUser
from typing import Any, Dict


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for representing user information, including followers and following counts.
    
    This serializer fetches and displays user profile data along with the 
    number of followers and following.
    """
    class Meta:
        model = CustomUser
        fields = [
            "email", 
            "first_name", 
            "last_name",
            "bio", 
            "profile_picture", 
            "slug", 
        ]
   

class UpdateProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for updating a user's profile information.
    
    This serializer validates and processes user profile updates, including
    optional fields such as first name, last name, bio, and profile picture.
    """
    first_name = serializers.CharField(
        max_length=30, 
        required=False,
        allow_blank=True
    )
    last_name = serializers.CharField(
        max_length=30, 
        required=False,
        allow_blank=True
    )
    bio = serializers.CharField(
        max_length=500, 
        required=False, 
        allow_blank=True
    )
    profile_picture = serializers.ImageField(
        required=False
    )

    class Meta:
        model = CustomUser
        fields = [
            "first_name", 
            "last_name", 
            "bio", 
            "profile_picture"
        ]

    def update(self, instance: CustomUser, validated_data: Dict[str, Any]) -> CustomUser:
        """
        Updates the user profile instance with the provided validated data.
        
        Args:
            instance (CustomUser): The user instance to be updated.
            validated_data (Dict[str, Any]): The validated data to update the instance.
        
        Returns:
            CustomUser: The updated user instance.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance