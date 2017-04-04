from django.contrib import admin

from .models import Zone
from .models import Sub_Zone
from .models import Record
from .models import Record_Type

class Record_Admin(admin.ModelAdmin):
    list_display = ('prefix', 'zone', 'type', 'context')

    def get_queryset(self, request):
        query = super(Record_Admin, self).get_queryset(request)

        # If super-user, show all comments
        if request.user.is_superuser:
            return query

        return query.filter(zone__owner=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'zone':
            kwargs['queryset'] = Sub_Zone.objects.filter(owner=request.user)
        return super(Record_Admin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Zone)
admin.site.register(Sub_Zone)
admin.site.register(Record, Record_Admin)
admin.site.register(Record_Type)

