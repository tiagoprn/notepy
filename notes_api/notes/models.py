from django.db import models


class Tag(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tags', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        index_together = [['owner', 'name'],
                          ['owner', 'created']]

    def __str__(self):
        return self.name


class Note(models.Model):
    owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
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


class NoteTag(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Link: {}, Tag: {}'.format(self.note.name, self.tag.name)
