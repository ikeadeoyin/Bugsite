# Generated by Django 4.1 on 2023-10-05 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0002_alter_bug_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bug',
            old_name='bug_types',
            new_name='bug_type',
        ),
    ]