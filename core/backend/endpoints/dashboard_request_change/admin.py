from django.contrib import admin
from .models import WordRequest, VerbRequest


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(WordRequest)
admin.site.register(VerbRequest)
