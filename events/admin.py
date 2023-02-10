from django.contrib import admin, messages
from .models import Event, Participation
# Register your models here.


class ParticipationInline(admin.StackedInline):
    model = Participation
    extra = 1
    classes = ['collapse']
    can_delete = True
    readonly_fields = ('datePart',)


def set_state(ModelAdmin, request, queryset):
    rows = queryset.update(state=True)
    if (rows == 1):
        msg = "One event was "
    else:
        msg = f"{rows} events were "
    messages.success(request, message='%s successfully accepted' % msg)


set_state.short_description = "Accept"


class EventAdmin(admin.ModelAdmin):
    def unset_state(self, request, queryset):
        rows_filter = queryset.filter(state=False)
        if rows_filter.count() > 0:
            messages.error(
                request, message=f"{rows_filter.count()} are already refused")
        else:
            rows = queryset.update(state=False)
            if (rows == 1):
                msg = "One event was"
            else:
                msg = f"{rows} events were"
            messages.success(request, message='%s successfully accepted' % msg)

    actions = [set_state , unset_state]
    inlines = [
        ParticipationInline
    ]

    list_per_page = 20

    list_display = (
        'title',
        'category',
        'state',
    )
    list_filter = (
        'category',
        'state',
    )
    ordering = ('title',)
    search_fields = [
        'title',
        'category'
    ]
    readonly_fields = ('createdAt', 'updatedAt')

    autocomplete_fields = ['organize']

    fieldsets = (
        (
            'State',
            {
                'fields': ('state',)
            }
        ),
        (
            'About',
            {
                'classes': ('collapse',),
                'fields': (
                    'title',
                    'imageEvent',
                    'category',
                    'organize',
                    'nombreParticipants',
                    'description',
                ),
            }
        ),
        (
            'Dates',
            {
                'fields': (
                    (
                        'dateEvent',
                        'createdAt',
                    ),
                )
            }
        ),
    )


admin.site.register(Event, EventAdmin)
admin.site.register(Participation)
