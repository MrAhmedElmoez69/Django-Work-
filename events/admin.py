from django.contrib import admin, messages
from .models import Event, Participation
from django.utils import timezone

# Register your models here.


class ParticipantFilter(admin.SimpleListFilter):
    title = 'Participants'
    parameter_name = 'nombreParticipants'

    def lookups(self, request, model_admin):
        return (
            ('0', ('No Participants')),
            ('more', ('There are Participants'))
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(nombreParticipants__exact=0)
        if self.value() == 'more':
            return queryset.filter(nombreParticipants__gt=0)


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


class EventDateFilter(admin.SimpleListFilter):
    title = 'Date'
    parameter_name = 'dateEvent'

    def lookups(self, request, model_admin):
        return (
            ('today', ('Today')),
            ('future', ('Future')),
            ('past', ('Past')),
        )

    def queryset(self, request, queryset):
        today = timezone.now().date()
        if self.value() == 'today':
            return queryset.filter(dateEvent=today)
        if self.value() == 'future':
            return queryset.filter(dateEvent__gt=today)
        if self.value() == 'past':
            return queryset.filter(dateEvent__lt=today)



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

    unset_state.short_description = "Refuse"
    actions = [set_state, "unset_state", "queryset"]
    actions_on_bottom = True
    actions_on_top = False
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
        ParticipantFilter,
        EventDateFilter,
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
