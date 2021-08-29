from django.contrib import admin
from posts import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']

@admin.register(models.Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'slug', 'category']
