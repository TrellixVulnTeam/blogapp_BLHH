# Generated by Django 2.2.7 on 2019-12-10 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slug', models.SlugField()),
                ('Title', models.CharField(max_length=120)),
                ('Description', models.TextField(max_length=320)),
                ('College', models.CharField(max_length=120)),
                ('Duration', models.DurationField()),
                ('Active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slug', models.SlugField()),
                ('Title', models.CharField(max_length=120)),
                ('Type', models.CharField(max_length=120)),
                ('Desciption', models.TextField(max_length=320)),
                ('sample_inputs', models.TextField()),
                ('sample_output', models.TextField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='challenge.Challenge')),
            ],
        ),
    ]