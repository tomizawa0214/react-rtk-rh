# Generated by Django 3.0.7 on 2021-05-02 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
