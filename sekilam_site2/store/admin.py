from django.contrib import admin

from store.models import Cart, Order, Produit, Client, Categorie, Facture

# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('name','slug','price','stock','thumbnail','description','categorie')
admin.site.register(Produit, ProduitAdmin)



class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'produit', 'quantite','ordered','ordered_date')
admin.site.register(Order, OrderAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('client',)
admin.site.register(Cart, CartAdmin)




class ClientAdmin(admin.ModelAdmin):
    list_display = ('tel', 'adresse', 'prenom', 'nom','email')
admin.site.register(Client, ClientAdmin)

admin.site.register(Categorie)


class FactureAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_facture', 'adresse_facture')
admin.site.register(Facture, FactureAdmin)


