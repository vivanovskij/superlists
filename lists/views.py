from .models import Item
from django.shortcuts import render, redirect


def home_page(request):
    '''домашняя страница'''
    return render(request, 'home.html')

def view_list(request):
    '''представление списка'''
    items = Item.objects.all()
    return render(request, 'lists.html', {'items': items})

def new_list(request):
    '''новый список'''
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/one-list-in-all-world/')
