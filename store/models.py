from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.text import slugify
# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author=models.CharField(max_length=50,null=True)
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
    