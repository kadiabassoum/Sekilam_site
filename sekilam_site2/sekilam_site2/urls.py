from django.contrib import admin
from django.urls import path
from sekilam_site2 import settings
from store.views import *
from accounts.views import signup, logout_user, login_user
from django.conf.urls.static import static 
urlpatterns = [
    path('',Accueil, name="Accueil"),
    path('search/',Accueil, name="search"),
    path('admin/', admin.site.urls),
    path('vetement',vetement, name="vetement"),
    path('Accessoire',Accessoires, name="Accessoire"),
    path('chaussures',Chaussures, name="chaussures"),
    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('login/', login_user, name="login"),
    path('cart/', cart, name="cart"),
    path('cart/delete/', delete_cart, name="delete-cart"),

    path('produit/<str:slug>', produit_detail, name="product"),
    path('produit/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



