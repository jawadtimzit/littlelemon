from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

# TestCase class
class TestMenuItemsView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="Pizza", price=12, inventory=20)
        self.item2 = Menu.objects.create(title="Burger", price=8, inventory=15)

    def test_get_all_menu_items(self):
        response = self.client.get("/restaurant/menu/")
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)