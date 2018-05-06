import uuid

from django.db import models


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


class Note(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(),
                            editable=False)
    owner = models.ForeignKey('auth.User', related_name='notes',
                              on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
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
        return ', '.join([tag.name for tag in self.tags.all()]) \
            if self.tags.all() else 'N/A'
    display_tags.short_description = 'Tags'
    display_tags.allow_tags = True


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
