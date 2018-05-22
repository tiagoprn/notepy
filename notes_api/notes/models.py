import uuid

import reversion

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from markdownx.models import MarkdownxField


@reversion.register()
class Tag(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(),
                            editable=False)
    owner = models.ForeignKey('auth.User', related_name='tags',
                              on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        index_together = [['owner', 'name'],
                          ['owner', 'created']]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        On save, update timestamps.

        It is not considered a good practice to use auto_now and auto_now_add
        anymore, since both stop you from manually setting the value of these
        fields when, e.g., you're manually importing data from another source.
        """
        import ipdb; ipdb.set_trace()
        if not self.id and not self.created:
            self.created = timezone.now()
        if not self.updated:
            self.updated = timezone.now()
        return super().save(*args, **kwargs)


@reversion.register()
class Note(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(),
                            editable=False)
    owner = models.ForeignKey('auth.User', related_name='notes',
                              on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    content = MarkdownxField(blank=True, null=True)
    private = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag,
                                  related_name='notes',
                                  through='NoteTag',
                                  through_fields=('note', 'tag'))

    class Meta:
        ordering = ('-created',)
        unique_together = (('owner', 'name'),)
        index_together = [['owner', 'created'], ]

    def __str__(self):
        return self.name

    def display_tags(self):
        """
        Useful to display the tags on the django admin.

        That is because it does not allow ManyToMany fields on list_display.
        """
        tags = self.tags.all()
        result = ''
        if not tags:
            result = 'N/A'
        else:
            for tag in tags:
                url = reverse("admin:notes_tag_change", args=(tag.uuid, ))
                html = f'<a href={url}>{tag.name}</a>'
                result += f', {html}' if result else f'{html}'
        return mark_safe(result)
    display_tags.short_description = 'TAGS'
    display_tags.allow_tags = True


@reversion.register()
class NoteTag(models.Model):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4(),
                            editable=False)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Link: {}, Tag: {}'.format(self.note.name, self.tag.name)
