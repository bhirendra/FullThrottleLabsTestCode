from django.contrib import admin

from users.models import UsersData, UsersActivityPeriodsData


class UsersDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tz', 'created', 'modified']
    search_fields = ['name', 'id']
    list_filter = ['tz']


class UsersActivityPeriodsDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'start_time', 'end_time', 'created', 'modified']
    search_fields = ['user__name', 'user__id']
    autocomplete_fields = ['user']


admin.site.register(UsersData, UsersDataAdmin)
admin.site.register(UsersActivityPeriodsData, UsersActivityPeriodsDataAdmin)
