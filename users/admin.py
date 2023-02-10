from django.contrib import admin
from .models import Person
# Register your models here.

#admin.site.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display =(

        'email',
    )
    ordering = ('email',)
    search_fields=[
        'CIN',
        'email',
    ]
    fieldsets = (
        (
            'Personal Info',
            {
                'fields': (
                    'CIN',
                    'email',
                    'username',
                    

                ),
            }
        ),
    )

admin.site.register(Person, PersonAdmin)