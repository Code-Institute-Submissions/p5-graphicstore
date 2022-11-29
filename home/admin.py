from django.contrib import admin
from .models import Newsletter

# Register your models here.


class NewsletterAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'date',)

    fields = ('date','email',)

    list_display = ('email', 'date',)

    ordering = ('-date',)


admin.site.register(Newsletter, NewsletterAdmin)