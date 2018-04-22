from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import Tag, Note, NoteTag


@admin.register(Tag)
class TagAdmin(VersionAdmin):
    pass


@admin.register(Note)
class NoteAdmin(VersionAdmin):
    pass


@admin.register(NoteTag)
class NoteTagAdmin(VersionAdmin):
    pass
