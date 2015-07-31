import os.path
import uuid
from django.conf import settings
from django.db import models


class RenameFilesModel(models.Model):
    """Abstract model for two-phase saving to rename filename after saving.

    This allows the final filenames to contain information like the primary key of the model.
    Normally it is used with `FileField` and `ImageField`.

    Adapted from https://djangosnippets.org/snippets/1129/

    Example:

        class Photo(RenameFilesModel):
            file = models.ImageField(upload_to='uploads/temp')

            RENAME_FILES = {
                'file': {
                    'dest': 'uploads/photos',
                    'keep_ext': True,
                    'blank': True,
                }
            }

        >>> photo = Photo(file='uploads/temp/photo.jpg')
        >>> photo.pk

        >>> photo.save()
        >>> photo.pk
        1
        >>> photo.file
        <ImageFieldFile: uploads/photos/1.jpg>

    If the 'dest' option is a callable, it will be called with the model
    instance (guaranteed to be saved) and the currently saved filename, and
    must return the new filename.  Otherwise, the filename is determined by
    'dest' and the model's primary key.

    If a file already exists at the resulting path, it is deleted.  This is
    desirable if the filename should always be the primary key, for instance.
    To avoid this behavior, write a 'dest' handler that results in a unique
    filename.

    If 'keep_ext' is True (the default), the extension of the previously saved
    filename will be appended to the primary key to construct the filename.
    The value of 'keep_ext' is not considered if 'dest' is a callable.

    """
    RENAME_FILES = {}

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False):
        rename_files = getattr(self, 'RENAME_FILES', None)
        if rename_files:
            super(RenameFilesModel, self).save(force_insert, force_update)
            force_insert, force_update = False, True

            for field_name, options in rename_files.items():
                field = getattr(self, field_name)
                # Ignore blank field
                # We don't check since Django Field should do that in advance.
                if not field:
                    continue
                file_name = str(field)
                name, ext = os.path.splitext(file_name)
                keep_ext = options.get('keep_ext', False)
                final_dest = options['dest']
                if callable(final_dest):
                    final_name = final_dest(self, file_name)
                else:
                    final_name = os.path.join(final_dest, 'organized/%s' % (self.pk,))
                    if keep_ext:
                        final_name += ext
                if file_name != final_name:
                    field.storage.delete(final_name)
                    field.storage.save(final_name, field)
                    field.storage.delete(file_name)
                    setattr(self, field_name, final_name)

        super(RenameFilesModel, self).save(force_insert, force_update)


class Sample(RenameFilesModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=2048, help_text=(
        'Name of the sample. Max 2048 characters'
    ))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owned_samples')

    def upload_to(self, filename):
        uuid = self.pk
        return 'samples/%s' % str(uuid)

    def temp_upload_to(self, filename):
        '''Temporarily store the file in storage. Assume self has not been committed.'''
        return 'samples/unorganized/%Y-%m-%d_{:s}'.format(filename)

    sample_file = models.FileField(upload_to=temp_upload_to, max_length=1024, blank=True)
    RENAME_FILES = {
        'sample_file': {'dest': upload_to, 'keep_ext': False}
    }
