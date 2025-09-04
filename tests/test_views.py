from django.test import TestCase
from django.urls import reverse
from restaurant.views import MenuItemsView
from restaurant.models import Menu

class MenuItemsViewTest(TestCase):
    def setUp(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item.save()
        
    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "IceCream")
        
            