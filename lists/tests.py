from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from superlists.settings import SECRET_KEY

from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):
    '''тест домашней страницы'''

    def test_root_url_resolves_to_home_page_view(self):
        '''тест: корневой url преобразуется в представление'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_secret_key(self):
        '''тест: соответствие SECRET_KEY'''
        self.assertEqual( \
             'django-insecure-7)6!^4h%xv&z$&@bl6g)rj5zy^+7*z&!*3+h73k5tf$zs0w1if', \
             SECRET_KEY)

    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
