from django.contrib import admin
from connections.models import ClientTable, ConnectionTable

# Register your models here.
#admin.site.register(ClientTable)
#admin.site.register(ConnectionTable)



#Client Admin Section
class ClientTableAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'client_name', 'f4f_code')

admin.site.register(ClientTable, ClientTableAdmin)


#Connection Admin Section
class ConnectionTableAdmin(admin.ModelAdmin):
    list_display = ('user', 'message_type', 'direction', 'client', 'status')

admin.site.register(ConnectionTable, ConnectionTableAdmin)