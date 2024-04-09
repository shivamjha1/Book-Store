from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"

class Address(models.Model):
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField()
    
    def address(self):
        return f"{self.street},{self.city}"
    def __str__(self) -> str:
        return self.address()
    class Meta:
        verbose_name_plural="Adrress_Entries"
    
    
class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()
    
class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author=models.ForeignKey(Author,on_delete=models.CASCADE, null=True,related_name="books")
    is_bestselling=models.BooleanField(default=True)
    slug=models.SlugField(default="",blank=True, null=False,db_index=True)#harry-potter
    countries_published=models.ManyToManyField(Country,null=True)
    
    def __str__(self):
        return f"{self.title}:{self.rating}"
    
    # def save(self,*args,**kwargs):
    #     self.slug=slugify(self.title)
    #     super().save(*args,**kwargs)
    
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_id=models.IntegerField()
    isbookissued=models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.roll_id},{self.name}"
    