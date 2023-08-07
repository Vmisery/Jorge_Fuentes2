from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Usuario, AccountAdmin)
admin.site.register(cliente)
admin.site.register(obra)
admin.site.register(carrito)
admin.site.register(productocarrito)
admin.site.register(direccionentrega)


