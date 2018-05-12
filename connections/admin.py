from django.contrib import admin
from connections.models import ClientTable, ConnectionTable

# Register your models here.
admin.site.register(ClientTable)
admin.site.register(ConnectionTable)