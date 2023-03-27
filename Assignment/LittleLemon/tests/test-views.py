from django.tests import TestCase

class MenuViewTest(TestCase):
    
    def setup(self):
        pass

    def test_getall(self):
        return Menu.objects.all()