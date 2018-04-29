from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import Tag, Note, NoteTag


@admin.register(Tag)
class TagAdmin(VersionAdmin):
    actions_on_top = True
    actions_on_bottom = True

    list_filter = ('created', 'name')


@admin.register(Note)
class NoteAdmin(VersionAdmin):
    actions_on_top = True
    actions_on_bottom = True

    list_filter = ('created', 'name', 'content', 'tags')


@admin.register(NoteTag)
class NoteTagAdmin(VersionAdmin):
    pass
