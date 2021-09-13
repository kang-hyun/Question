from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)
    return render(request, 'questions/index.html', {'current_category':current_category, 'categories':categories,
                                              'products':products})

def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    import random
    if id == 5:

        f = open('Electric Machinery1.txt', mode='r', encoding='utf-8')
        z = f.read()
        f.close()
        y = z.split('Q')
        y.remove('')
        random.shuffle(y)
        x = y[0]
        b = x.split('\n')
        a = b[0]
        c = b[1]
        d = b[2]
        e = b[3]
        f = b[4]
    elif id == 6 :
        f = open('widing.txt', mode='r', encoding='utf-8')
        z = f.read()
        f.close()
        y = z.split('Q')
        y.remove('')
        random.shuffle(y)
        x = y[0]
        b = x.split('\n')
        a = b[0]
        c = b[1]
        d = b[2]
        e = b[3]
        f = b[4]

    else :
        f = open('induced electromotive force.txt', mode='r', encoding='utf-8')
        z = f.read()
        f.close()
        y = z.split('Q')
        y.remove('')
        random.shuffle(y)
        x = y[0]
        b = x.split('\n')
        a = b[0]
        c = b[1]
        d = b[2]
        e = b[3]
        f = b[4]


    return render(request, 'questions/detail.html', {'product': product, 'show': a, 'c':c, 'd':d, 'e':e, 'f':f })
    #return 'questions/detail.html'(a)

def index(request):
    import random

    f = open('test1.txt', mode='r', encoding='utf-8')
    z = f.read()
    f.close()
    y = z.split('Q')
    y.remove('')
    random.shuffle(y)
    print(y)
    print(y[0])
    a = y[0]

    b = a.split('\n')

    return HttpResponse(a)

