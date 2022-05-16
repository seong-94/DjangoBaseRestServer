# Generated by Django 4.0.4 on 2022-05-16 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firexr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactionpoint',
            name='Transform',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transformpos', to='firexr.transform'),
        ),
    ]
