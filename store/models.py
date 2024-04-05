from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.text import slugify
# Create your models here.

class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    
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
    