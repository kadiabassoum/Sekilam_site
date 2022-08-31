
from multiprocessing import context
from unicodedata import name

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import JsonResponse
from django.template.loader import render_to_string

from store.models import *

# Create your views here.

def Accueil(request):

    product_object = Produit.objects.all()

    ctx={}
    product_name=request.GET.get('q')
    print(product_name)

    if product_name:
        products= Produit.objects.filter(name__icontains=product_name)
    else :
        products = Produit.objects.all()
        
    print(products)
    ctx["searched_products"] = products
    does_req_accept_json = request.accepts("application/json")
    is_ajax_request=request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json

    if is_ajax_request :
        ctx['is_searching']=True
        html =render_to_string(
            template_name="store/search_results.html",
            context={'searched_products': products,'is_searching':True}
        )

        data_dict= {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False) 

    ctx["product_object"]=product_object

    return render(request, 'store/Accueil.html', context=ctx)


# def Search(request):

#     ctx={}
#     product_name=request.GET.get(['q'])
#     print(product_name)

#     if product_name:
#         products= Produit.objects.filter(name__icontains=product_name)
#     else :
#         products = Produit.objects.all()
        
#     ctx["searched_products"] = products
#     does_req_accept_json = request.accepts("application/json")
#     is_ajax_request=request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json

#     print(is_ajax_request)

#     if is_ajax_request :
#         html =render_to_string(
#             template_name="search_results.html",
#             ctx={'searched_products': products}
#         )

#         data_dict= {"html_from_view": html}
#         return JsonResponse(data=data_dict, safe=False) 
#     return render(request, 'store/Search.html',context=ctx)



def vetement(request):
    product_object = Produit.objects.filter(categorie__nom__contains="vêtement")

    return render(request, 'store/vetement.html', {'product_object': product_object})


def Accessoires(request):
    product_object = Produit.objects.filter(categorie__nom__contains="Accessoires")

    return render(request, 'store/Accessoire.html', {'product_object': product_object})



def Chaussures(request):
    product_object = Produit.objects.filter(categorie__nom__contains="chaussures")

    return render(request, 'store/Chaussure.html', {'product_object': product_object})





def produit_detail(request, slug):
    Produit = get_object_or_404(Produit, slug=slug)
    return render(request, 'detail.html', context={"Produit" : Produit})

def add_to_cart(request, slug):
    user = request.user
    Produit = get_object_or_404(Produit, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, 
                                                Produit=Produit)


    if created:
        cart.orders.add(order)
        cart.save()
    
    else:
        order.quantity += 1
        order.save()
    
    return redirect(reverse("Produit", kwargs={"slug": slug}))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)


    return render(request, 'cart.html', context={"orders": cart.orders.all()})


def delete_cart(request):
    if cart := request.user.cart:
        cart.orders.all().delete()
        cart.delete()
    
    return redirect('Accueil')


