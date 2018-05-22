from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from rangefilter.filter import DateRangeFilter
from reversion.admin import VersionAdmin

from .models import Tag, Note, NoteTag


class NoteTagInline(admin.TabularInline):
    model = Note.tags.through
    extra = 1


class VersionAdminWithOwnerAutofill(VersionAdmin):
    history_latest_first = True

    def get_changeform_initial_data(self, request):
        get_data = super().get_changeform_initial_data(request)
        get_data['owner'] = request.user.pk
        return get_data


@admin.register(Tag)
class TagAdmin(VersionAdminWithOwnerAutofill):
    list_per_page = 10

    list_display = ['name', 'uuid', 'created', 'updated']
    list_filter = ('created', ('created', DateRangeFilter), 'updated', ('updated', DateRangeFilter), )
    search_fields = ('uuid', 'created', 'name', )


@admin.register(Note)
class NoteAdmin(VersionAdminWithOwnerAutofill, MarkdownxModelAdmin):
    list_per_page = 10

    inlines = [NoteTagInline, ]

    list_display = ['name', 'display_tags', 'uuid', 'created', 'updated', 'private']
    list_filter = ('created', ('created', DateRangeFilter), 'updated', ('updated', DateRangeFilter), 'private')
    search_fields = ('uuid', 'created', 'name', 'content', 'private', 'tags__name', )
