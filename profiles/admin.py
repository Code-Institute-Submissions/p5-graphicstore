from django.contrib import admin
from .models import Ticket

# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'body',)

    fields = ('title', 'body',)

    list_display = ('title', 'body',)

    ordering = ('-date',)


admin.site.register(Ticket, TicketAdmin)
