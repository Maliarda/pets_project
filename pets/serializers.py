import base64

from django.core.files.base import ContentFile

from rest_framework import serializers

from .models import Pet, User


class PetShortSerializer(serializers.ModelSerializer):
    """
    Serializer for representing a short version of the Pet model.
    """

    class Meta:
        model = Pet
        fields = ["name", "kind"]


class UserSerializer(serializers.ModelSerializer):
    pets = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "pets"]
        ref_name = "CustomUser"

    def get_pets(self, obj):
        pet = Pet.objects.filter(owner=obj,)
        serializer = PetShortSerializer(pet, many=True,)
        return serializer.data


class Base64ImageField(serializers.ImageField):
    """
    A custom image field for handling base64-encoded images.
    """

    def to_internal_value(self, data):
        """
        If the data is a base64-encoded image string,
        it decodes the image data and saves it to a file.
        """
        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(";base64,")
            ext = format.split("/")[-1]
            data = ContentFile(base64.b64decode(imgstr), name="temp." + ext,)

        return super().to_internal_value(data)


class PetSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False, allow_null=True,)

    class Meta:
        model = Pet
        fields = ["id", "name", "kind", "photo", "owner"]
        read_only_fields = ("owner",)
