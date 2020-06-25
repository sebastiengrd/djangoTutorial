from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post) #we can see the Posts on the admin site