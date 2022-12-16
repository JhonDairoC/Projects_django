from django.contrib import admin
from .models import Produc

# Register your models here.
class ProducAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "clasific",
        "name",
        "price",
        "image",
        "supplier",
    )
admin.site.register(Produc, ProducAdmin)