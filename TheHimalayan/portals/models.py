from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=24, unique_for_date='publish')
    #author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='news_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    
    
    class Meta:
        ordering=('-publish',)
        
    def __str__(self):
       return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])


class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=32)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return 'commented by {} on {}'.format(self.name,self.post)
    
class Contact(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)

    
    def __str__(self):
        return self.firstname
    


class PoliticalNewsPost(Post):
  pass

class SportsNewsPost(Post):
  pass

class InternationalNewsPost(Post):
  pass

class ScienceNewsPost(Post):
  pass

class BreakingNewsPost(Post):
   pass



