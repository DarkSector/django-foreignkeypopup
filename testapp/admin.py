from django.contrib import admin
from models import ParentModel, ChildClass


# Register your models here.
admin.site.register(ParentModel)
admin.site.register(ChildClass)
