from django.contrib import admin
from .models import (
    ServiceModel,
    CustomersModel,
    PackageModel,
)
# Register your models here.
@admin.register(PackageModel)
class Pack(admin.ModelAdmin):
    pass


admin.site.register(ServiceModel)
admin.site.register(CustomersModel)
