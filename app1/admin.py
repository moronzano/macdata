from django.contrib import admin
from .models import SwModels, Switches, DhcpTable, StoreMac

admin.site.register(SwModels)
admin.site.register(Switches)
admin.site.register(DhcpTable)
admin.site.register(StoreMac)
