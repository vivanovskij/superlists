from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# Create your tests here.

class SmokeTest(TestCase):
    '''тест на токсичность'''

    def test_root_url_resolves_to_home_page_view(self):
        '''тест: корневой url преобразуется в представление'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)
