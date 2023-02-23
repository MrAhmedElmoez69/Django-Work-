from django.utils import timezone
from django.contrib import admin
from .models import Person
# Register your models here.

# admin.site.register(Person)


class DateJoinedFilter(admin.SimpleListFilter):
    title = 'Date'
    parameter_name = 'date_joined'

    def lookups(self, request, model_admin):
        return (
            ('today', ('Today')),
            ('future', ('Future')),
            ('past', ('Past')),
        )

    def queryset(self, request, queryset):
        today = timezone.now().date()
        if self.value() == 'today':
            return queryset.filter(date_joined=today)
        if self.value() == 'future':
            return queryset.filter(date_joined__gt=today)
        if self.value() == 'past':
            return queryset.filter(date_joined__lt=today)


class PersonAdmin(admin.ModelAdmin):
    list_display = (

        'email',
    )

    list_filter = (
        DateJoinedFilter,
    )
    ordering = ('email',)
    search_fields = [
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
