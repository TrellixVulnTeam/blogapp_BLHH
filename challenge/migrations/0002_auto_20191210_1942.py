# Generated by Django 2.2.7 on 2019-12-10 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='course',
            new_name='challenge',
        ),
    ]