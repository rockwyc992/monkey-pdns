from django.contrib import admin

from .models import Zone
from .models import Sub_Zone
from .models import Record
from .models import Record_Type

admin.site.register(Zone)
admin.site.register(Sub_Zone)
admin.site.register(Record)
admin.site.register(Record_Type)

