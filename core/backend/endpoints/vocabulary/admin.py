from django.contrib import admin
from .models import Word


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Word)
