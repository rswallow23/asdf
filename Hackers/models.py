from django.db import models
from django.utils import timezone
from django.utils.text import slugify 
from django.contrib.auth.models import User
from django.contrib import auth 


# Create your models here.
class Posts(models.Model):
	title = models.CharField(max_length=60)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
	slug = models.SlugField(max_length=60, unique=True)
	user = models.ForeignKey(User,blank=True,null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		self.updated_at = timezone.now()
		if not self.id:
			self.created_at = timezone.now()
		return super(Posts, self).save(*args, **kwargs)

	def __str__(self):
		return self.title 

	def to_json(self):
		return{
		"title":self.title,
		"content":self.content,
		"created_at":self.created_at,
		"updated_at":self.updated_at,
		"user":self.user.username,
		"slug":self.slug,
		}

