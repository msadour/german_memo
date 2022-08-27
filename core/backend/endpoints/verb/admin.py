from django.contrib import admin
from .models import Verb


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Verb)
