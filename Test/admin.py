from django.contrib import admin

# Register your models here.

from .models import Manager, Client


class ManagerAdmin(admin.ModelAdmin):
    list_display = ("manager", "mail")
    search_fields = ("manager",)


class ClientAdmin(admin.ModelAdmin):
    list_display = ("client", "address", "manager")
    search_fields = ("client", "address")
    raw_id_fields = ("manager",)


admin.site.register(Manager, ManagerAdmin)
admin.site.register(Client, ClientAdmin)
