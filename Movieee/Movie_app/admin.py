from django.contrib import admin
from .models import MovieInfo
from .models import User

# Register your models here.

admin.site.register(MovieInfo)
admin.site.register(User)
