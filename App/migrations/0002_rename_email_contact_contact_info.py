# Generated by Django 4.2.4 on 2023-09-16 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='contact_info',
        ),
    ]
