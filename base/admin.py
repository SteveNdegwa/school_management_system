from django.contrib import admin

from base.models import State, Role, Permission, RolePermission


# Register your models here.


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created', 'date_modified')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'state', 'date_created', 'date_modified')


class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'state', 'date_created', 'date_modified')


class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('role', 'permission', 'state', 'date_created', 'date_modified')


admin.register(State, StateAdmin)
admin.register(Role, RoleAdmin)
admin.register(Permission, PermissionAdmin)
admin.register(RolePermission, RolePermissionAdmin)
