from django.contrib import admin

# Register your models here.
from .models import Questions, Answer




admin.site.register(Questions)
admin.site.register(Answer)
