from django.contrib import admin
from .models import Article, CustomUser, Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(CustomUser)
admin.site.register(Comment)