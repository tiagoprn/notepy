from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from reversion.admin import VersionAdmin

from .models import Tag, Note, NoteTag


class NoteTagInline(admin.TabularInline):
    model = Note.tags.through
    extra = 1


@admin.register(Tag)
class TagAdmin(VersionAdmin):
    actions_on_top = True
    actions_on_bottom = True

    list_filter = ('created', ('created', DateRangeFilter), )
    search_fields = ('created', 'name',)


@admin.register(Note)
class NoteAdmin(VersionAdmin):
    actions_on_top = True
    actions_on_bottom = True

    inlines = [NoteTagInline,]
    list_filter = ('created', ('created', DateRangeFilter), )
    search_fields = ('created', 'name', 'content', 'tags__name',)


@admin.register(NoteTag)
class NoteTagAdmin(VersionAdmin):
    actions_on_top = True
    actions_on_bottom = True

    list_filter = ('created', ('created', DateRangeFilter), )
    search_fields = ('created', 'note__name', 'tag__name',)