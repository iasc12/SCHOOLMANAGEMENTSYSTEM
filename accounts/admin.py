from django.contrib import admin
from django .contrib.auth.admin import UserAdmin
from .models import CustomUser 

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Role', {'fields': ('role',)}),


)

    add_fieldssets = UserAdmin.add_fieldsets + (('Role', {'fields': ('role',)}),
)
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')

# Register your models here.