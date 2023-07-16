import json

import pytest
from django.urls import reverse
from rest_framework import status

from pets.models import Pet


@pytest.mark.django_db
def test_list_pets(api_client):
    url = reverse("pet-list")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_create_pet(auth_api_client, user):
    url = reverse("pet-list")
    data = {"name": "New Pet", "kind": "cat"}

    response = auth_api_client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name"] == data["name"]
    assert response.data["kind"] == data["kind"]
    assert response.data["owner"] == user.id


@pytest.mark.django_db
def test_create_update_delete_pet(auth_api_client, user):
    # Создание питомца
    create_url = reverse("pet-list")
    create_data = {"name": "New Pet", "kind": "cat"}
    create_response = auth_api_client.post(create_url, data=create_data)

    assert create_response.status_code == status.HTTP_201_CREATED
    assert create_response.data["name"] == create_data["name"]
    assert create_response.data["kind"] == create_data["kind"]

    # Обновление питомца
    pet_id = create_response.data["id"]
    update_url = reverse("pet-detail", args=[pet_id])
    update_data = {"name": "Updated Pet"}
    update_response = auth_api_client.patch(
        update_url,
        data=json.dumps(update_data),
        content_type="application/json",
    )

    assert update_response.status_code == status.HTTP_200_OK
    assert update_response.data["name"] == update_data["name"]

    # Удаление питомца
    delete_url = reverse("pet-detail", args=[pet_id])
    delete_response = auth_api_client.delete(delete_url)

    assert delete_response.status_code == status.HTTP_204_NO_CONTENT
    assert not Pet.objects.filter(id=pet_id).exists()
