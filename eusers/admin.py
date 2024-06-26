from django.contrib import admin

from .models import Guardian, Student, EUser


# Register your models here.

class GuardianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'other_name', 'dob', 'id_no', 'phone_number', 'other_phone_number',
                    'email', 'state', 'date_created', 'date_modified')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('admission_no', 'first_name', 'last_name', 'other_name', 'dob', 'guardian', 'other_guardian',
                    'state', 'date_created', 'date_modified')


class EUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'other_name', 'dob', 'id_no', 'phone_number',
                    'other_phone_number', 'email', 'role', 'state', 'date_created', 'date_modified')


admin.site.register(Guardian, GuardianAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(EUser, EUserAdmin)
