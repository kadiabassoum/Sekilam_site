from random import random
from django.db import models
import random
from sekilam_site2.settings import AUTH_USER_MODEL

def create_new_ref_number():
    return str(random.randint(1000000000, 9999999999))


class Client(models.Model):
    tel = models.CharField(max_length=50)
    adresse = models.CharField(max_length=300)
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    email = models.CharField(max_length=50,blank=True,null=True)
    

    def __str__(self):
        return self.prenom

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'




class Categorie(models.Model):
    nom = models.CharField(max_length=128,primary_key=True)


    def __str__(self):
        return self.nom

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'





class Produit(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="produits", blank = True, null = True)
    categorie  = models.ForeignKey(Categorie, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} ({self.stock})"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'



class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.produit.name} ({self.quantite})"



class Cart(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order,related_name="ligne_commande")


    def __str__(self):
        return f"{self.client.prenom}"


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'


class Facture(models.Model):
    name = models.CharField(max_length=10, blank=True, unique=True,editable=False,default=create_new_ref_number)
    date_facture = models.DateTimeField(auto_now=False, auto_now_add=False)
    adresse_facture = models.CharField(max_length=300)

    
def __str__(self):
    return self.name

class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Facture'
        verbose_name_plural = 'Factures'