# Generated by Django 5.0.4 on 2024-05-23 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WorkList', '0003_rename_id_examen_examenradiologique_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageradiologique',
            old_name='id_image',
            new_name='id',
        ),
    ]
