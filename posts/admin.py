from django.contrib import admin
from .models import Posts, Category
from . import models
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp", "featured_post"]
    list_display_links = ["title"]

    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]

admin.site.register(Posts, PostModelAdmin)
admin.site.register(Category)
