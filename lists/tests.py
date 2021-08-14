from lists.models import Item, List
from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):
    '''тест домашней страницы'''

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ListAndItemModelsTest(TestCase):
    '''тест модели элемента списка'''

    def test_saving_and_retrieving_items(self):
        '''тест сохранения и получения элементов списка'''
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)


class ListViewTest(TestCase):
    '''тест представление списка'''

    def test_uses_list_template(self):
        '''тест: используется шаблон списка'''
        response = self.client.get('/lists/one-list-in-all-world/')
        self.assertTemplateUsed(response, 'lists.html')

    def test_displays_all_items(self):
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/lists/one-list-in-all-world/')

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')


class NewListTest(TestCase):
    '''тест нового списка'''

    def test_can_save_a_POST_request(self):
        '''тест: можно сохранить post-request'''
        response = self.client.post( '/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')


    def test_redirects_after_POST(self):
        '''тест: переадресует после post-запроса'''
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/one-list-in-all-world/')


class ListViewTest(TestCase):
    '''тест представления списка'''

    def test_displays_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='itemy 1', list=list_)
        Item.objects.create(text='itemy 2', list=list_)
