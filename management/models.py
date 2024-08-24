from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return f"{self.name} | {self.phone} | {self.address}"
    
    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.name)
        super(Contact, self).save(*args, **kwargs)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=200)
    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile/images')

    
    def __str__(self):
        
        return f"{self.user.username}"
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

class FamilyMember(models.Model):

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/femily', blank=True, null=True)
    relationship = models.CharField(max_length=50)
 

    def __str__(self):
        
        return f"{self.name} | {self.relationship}"
    
class Catagory(models.Model):
    name = models.CharField(max_length=50)
    decription = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return f"{self.name} | {self.decription}"

class Product(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.SET_NULL, blank=True,null=True)
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    decription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return f"{self.catagory} | {self.name} | {self.price}"
