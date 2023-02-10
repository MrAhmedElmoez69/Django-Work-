from django.contrib import admin
from .models import Event,Participation 
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display =(
        'Title',
        'Category',
        'State',
    )
    list_filter=(
        'Category',
        'State',
    )
    ordering = ('Title',)
    search_fields=[
        'Title',
        'Category'
    ]
    readonly_fields=('CreatedAt','UpdatedAt')


    autocomplete_fields= ['organize']   

    fieldsets = (
        (
            'State',
            {
                'fields': ('State',)
            }
        ),
        (
            'About',
            {
                'classes': ('collapse',),
                'fields': (
                    'Title',
                    'ImageEvent',
                    'Category',
                    'organize',   
                    'NombreParticipants',
                    'Description',
                ),
            }
        ),
        (
            'Dates',
            {
                'fields': (
                    (
                        'DateEvent',
                        'CreatedAt',
                    ),
                )
            }
        ),
    )
admin.site.register(Event,EventAdmin)
admin.site.register(Participation)