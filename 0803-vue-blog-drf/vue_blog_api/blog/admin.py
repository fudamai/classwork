from django.contrib import admin
from .models import Comments, Blogs

# Register your models here.
admin.site.register(Blogs)
admin.site.register(Comments)