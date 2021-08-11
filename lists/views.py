from .models import Item
from django.shortcuts import render, redirect


def home_page(request):
    '''домашняя страница'''
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    else:
        new_item_text = ''

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
