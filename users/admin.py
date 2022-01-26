"""Django"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
"""Models"""
from users.models import Profile
from django.contrib.auth.models import User




# Register your models here.


@admin.register(Profile)  # registro la app en el admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # nos lleva al detalle cuando apretamos sobre ellos
    list_display_links = ('pk', 'user',)
    # los hacemos editables, no deben estar en links
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = ('user__username', 'user__email', 'user__first_name',
                     'user__last_name', 'phone_number')  # campo de busqueda
    list_filter = ('user__is_active', 'user__is_staff',
                   'created', 'modified')  # filtros

    fieldsets = ( # info mejor estructurada
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',) # campos que no puedo modificar, solo leer


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
