from django.contrib import admin
from .models import Post


# Need to register each Model object here?
admin.site.register(Post)