from django.db import models
from django.utils.text import slugify



class Category(models.Model):
    name = models.CharField(max_length=90, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateField(null=True)
    slug = models.SlugField(default='', editable=False, max_length=100)

    def save(self, *args, **kwargs):
        value = slugify(self.title)
        self.slug = value
        return self.super(args, kwargs)

    class Meta:
        db_table = "posts_categories"

class Post(models.Model):
    title = models.CharField(max_length=90, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateField(null=True)
    slug = models.SlugField(default='', editable=False, max_length=100)

    def save(self, *args, **kwargs):
        value = slugify(self.title)
        self.slug = value
        return self.super(args, kwargs)
    
    class Meta:
        db_table = "posts"

