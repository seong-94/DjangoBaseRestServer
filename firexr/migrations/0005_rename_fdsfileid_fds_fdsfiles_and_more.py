# Generated by Django 4.0.4 on 2022-05-16 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firexr', '0004_alter_interactionpoint_localtransform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fds',
            old_name='FDSFileID',
            new_name='FDSFiles',
        ),
        migrations.RenameField(
            model_name='separatedscenario',
            old_name='FDS',
            new_name='LocalFDS',
        ),
    ]
