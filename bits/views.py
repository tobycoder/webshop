from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import bp_pages, bp_products, bp_users, ContactModel
from .forms import ContactForm, ShoppingForm, Login, Registreren
from cart.cart import Cart
# Create your views here.
def get_index(request):
    text = bp_pages.objects.filter(pagina="home")
    former = ContactForm()
    if request.session.has_key('username'):
        username = request.session['username']
        message = "Welkom, %s" % username
    return render(request, 'bits/home.html', context=locals())

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
    query_naam = bp_products.objects.values_list('pr_naam', flat=True).get(id=product_item)
    query_prijs = bp_products.objects.values_list('pr_prijs', flat=True).get(id=product_item)
    if request.method == 'POST':
        form = ShoppingForm(request.POST)
        if form.is_valid():
            product = bp_products.objects.get(id=product_item)
            cart = Cart(request)
            quantity = form.cleaned_data['quantity']
            maat = form.cleaned_data['maat']
            cart.add(product, product.pr_prijs, maat, quantity)
            return HttpResponseRedirect(reverse('bits:add_to_cart'))
    else :
        form = ShoppingForm(initial={'pr_prijs': query_prijs, 'pr_naam': query_naam})
    return render(request, 'bits/solo.html', {'query': query, 'form': form})

def add_to_cart(request):
    return render(request, 'bits/cart.html', dict(cart=Cart(request)))

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
    else:
        form = ContactForm()
    return render(request, 'bits/contact.html', {'form': form})

def authenticate(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if bp_users.objects.filter(username=username).exists() == True:
                if bp_users.objects.filter(password=password).exists() == True:
                    request.session['username']= username
                    url = reverse('bits:get_index')
                    return HttpResponseRedirect(reverse('bits:get_index'))
                else:
                    message = "Fout wachtwoord"
                    return HttpResponseRedirect(reverse('bits:authenticate'))
            else:
                message = "Foute username"
                return HttpResponseRedirect(reverse('bits:authenticate'))
        else:
            message = "Niet alle velden zijn ingevuld"
            return HttpResponseRedirect(reverse('bits:authenticate'))
    else:
        form = Login()
        return render(request, 'bits/login.html', context=locals())

def register(request):
    if request.method == 'POST':
        form = Registreren(request.POST)
        if form.is_valid():
            form.save()
            message = "Gefeliciteerd. U kunt nu inloggen met uw gebruikersnaam en wachtwoord"
            return render(request, 'bits/register.html', context=locals())
        else:
            message = "U bent velden vergeten"
            form = Registreren()
            return render(request, 'bits/register.html', context=locals())
    else:
        form = Registreren()
        return render(request, 'bits/register.html', context=locals())

def logout(request):
    try:
        del request.session['username']
    except:
        pass

    url = reverse('bits:get_index')
    return HttpResponseRedirect(url)


def deleterow(request, product_item):
    product = bp_products.objects.get(id=int(product_item))
    cart = Cart(request)
    cart.remove(product)
    return HttpResponseRedirect(reverse('bits:add_to_cart'))