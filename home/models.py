from django.db import models

# return '%s' %self.user
#  Create your models here.
from datetime import datetime

from django.utils.text import slugify
from django.contrib.auth.models import User

from django.db.models.signals import post_save




class cluns(models.Model):

    name = models.CharField(max_length=1000,verbose_name=("الاسم"))
    phon = models.CharField(max_length=1000,verbose_name=("رقم الهاتف"),null=True,blank=True)
    email = models.CharField(max_length=1000,verbose_name=("الاميل"),null=True,blank=True)
    image = models.ImageField(upload_to='photos/',verbose_name=("الصورة الشخصية"),default='R.png')
    time= models.DateTimeField(default=datetime.now)
    slug = models.SlugField(max_length=255, unique=True,null=True,blank=True, allow_unicode=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE ,unique=True,null=True,)
    def save(self, *args, **kwargs):
        super(cluns, self).save(*args, **kwargs)
        self.slug = slugify(str(self.id))
        return super(cluns, self).save(*args, **kwargs)
    def __str__(self) :
        return self.name
    
    
class massgee(models.Model):
    name=models.CharField(max_length=100)
    phon=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    massge=models.TextField(max_length=10000)
    
class images(models.Model):
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/work/',verbose_name=("اعملنا "),default='R.png')
    def __str__(self) :
        return self.name
    

