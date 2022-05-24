from django.contrib import admin
from .models import BookstoreUser, UserRoles

# Register your models here.
admin.site.register(BookstoreUser)
admin.site.register(UserRoles)
