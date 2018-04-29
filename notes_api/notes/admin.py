from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from reversion.admin import VersionAdmin

from .models import Tag, Note, NoteTag


class NoteTagInline(admin.TabularInline):
    model = Note.tags.through
    extra = 1


class VersionAdminWithOwnerAutofill(VersionAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super().get_changeform_initial_data(request)
        get_data['owner'] = request.user.pk
        return get_data


@admin.register(Tag)
class TagAdmin(VersionAdminWithOwnerAutofill):
    list_per_page = 10

    list_display = ['name', 'created']
    list_filter = ('created', ('created', DateRangeFilter), )
    search_fields = ('created', 'name', )


@admin.register(Note)
class NoteAdmin(VersionAdminWithOwnerAutofill):
    list_per_page = 10

    inlines = [NoteTagInline, ]

    list_display = ['name', 'created']
    list_filter = ('created', ('created', DateRangeFilter), )
    search_fields = ('created', 'name', 'content', 'tags__name', )



@admin.register(NoteTag)
class NoteTagAdmin(VersionAdminWithOwnerAutofill):
    list_per_page = 10

    list_display = ['__str__', 'created']
    list_filter = ('created', ('created', DateRangeFilter), )
    search_fields = ('created', 'note__name', 'tag__name',)
