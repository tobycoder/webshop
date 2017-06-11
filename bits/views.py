from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import bp_pages, bp_products, bp_users, ContactModel, ShopCart
from .forms import ContactForm, ShoppingForm
from django.db.models import Sum, F
from django.template.loader import get_template, render_to_string
from django.template import Template, Context
from django.core.mail import EmailMessage, send_mail, BadHeaderError
# Create your views here.
def get_index(request):
    text = bp_pages.objects.filter(pagina="home")
    former = ContactForm()
    return render(request, 'bits/home.html', {'text': text, 'form': former})

def get_product(request, shop_item):
    query = bp_products.objects.filter(pr_cat=shop_item)[:3]
    query_all = bp_products.objects.filter(pr_cat=shop_item)
    return render(request, 'bits/product.html', {'query': query, 'query_all': query_all})

def get_product_by_sub(request, shop_item, shop_subitem):
    query = bp_products.objects.filter(pr_cat=shop_item, pr_subcat=shop_subitem)[:3]
    query_all = bp_products.objects.filter(pr_cat=shop_item, pr_subcat=shop_subitem)
    return render(request, 'bits/product.html', {'query': query, 'query_all': query_all})

def get_product_by_new(request, shop_item):
    new = 'NEW'
    query = bp_products.objects.filter(pr_cat=shop_item, new=new)[:3]
    query_all = bp_products.objects.filter(pr_cat=shop_item, new=new)
    return render(request, 'bits/product.html', {'query': query, 'query_all': query_all})

def get_product_by_new_solo(request):
    new = 'NEW'
    query = bp_products.objects.filter(new=new)[:3]
    query_all = bp_products.objects.filter(new=new)
    return render(request, 'bits/product.html', {'query': query, 'query_all': query_all})

def get_product_solo(request, product_item):
    query = bp_products.objects.filter(id=product_item)
    if request.method == 'POST':
        form = ShoppingForm(request.POST)
        if form.is_valid():
            url = reverse('bits:cart_overview')
            obj = ShopCart()
            obj.q = form.cleaned_data['q']
            nameobject = bp_products.objects.get(id=product_item)
            obj.name = nameobject.pr_naam
            obj.maat = form.cleaned_data['maat']
            obj.price = nameobject.pr_prijs
            obj.save()
            return HttpResponseRedirect(url)
    else :
        form = ShoppingForm()
    return render(request, 'bits/solo.html', {'query': query, 'form': form})

def contact_request(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = ContactModel()
            obj.voornaam = form.cleaned_data['voornaam']
            obj.onderwerp = form.cleaned_data['onderwerp']
            obj.email = form.cleaned_data['email']
            obj.text = form.cleaned_data['text']
            obj.save()

    return render(request, 'bits/contact.html', {'form': form})

def cart_overview(request):
    query = ShopCart.objects.all()
    subtotal = ShopCart.objects.aggregate(subtotaal=Sum(F('price') * F('q')))['subtotaal']
    btw = int(subtotal) * 0.21
    total = int(subtotal) + int(btw)
    return render(request, 'bits/cart.html', context=locals())