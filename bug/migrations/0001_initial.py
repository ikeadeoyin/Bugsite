# Generated by Django 4.1 on 2023-10-04 16:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('bug_types', models.CharField(choices=[('error', 'error'), ('new_feature', 'new feature'), ('improvement', 'improvement'), ('test_case', 'test case')], max_length=20)),
                ('report_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('to_do', 'to do'), ('assigned', 'assigned'), ('in_progress', 'in progress'), ('under_review', 'under review'), ('done', 'Done')], max_length=20)),
            ],
        ),
    ]
