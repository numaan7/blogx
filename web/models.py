from taggit.managers import TaggableManager
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils import timezone
from sqlalchemy import null


# post model
class Categorie(models.Model):
    name=models.CharField(max_length=100,unique=True)
   
    
    
    def __str__(self):
        return self.name

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    

    title = models.CharField(max_length=250)
    
    slug = models.SlugField(max_length=250,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/',default='/media/featured_image/2022/02/28/fi.jpg',blank=True) 
    
    category=models.ForeignKey(Categorie,on_delete=models.CASCADE,null=True,blank=True)
    views=models.IntegerField(default=0)
    body=RichTextUploadingField()
    tags = TaggableManager()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering = ('-publish',)
    
    
    def __str__(self):
        return self.title
    objects = models.Manager() # The default manager.
    published = PublishedManager()
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.slug])

class Conatct(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=1000)
    question=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    class meta:
        ordering=['-date',]
    def __str__(self):
        return "Message from " + self.fname + " " + self.lname + ' - ' + self.email


class Comments(models.Model):
    comment_sno=models.AutoField(primary_key=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    comment=models.TextField()
    parent=models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE,related_name='replies')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.comment
    def get_comments(self):
        return Comments.objects.filter(parent=self).filter(active=True)
class Page(models.Model):

    STATUS_CHOICE = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    ptitle=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    pbody=RichTextUploadingField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICE,default='draft')
    def __str__(self):
        return self.ptitle



