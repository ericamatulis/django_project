# Generated by Django 3.1.3 on 2020-12-18 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matrix_name', models.CharField(max_length=200, unique=True)),
                ('matrix_value', models.TextField()),
                ('dimension', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'db_table': 'image',
                'ordering': ['matrix_name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200, unique=True)),
                ('group_summary', models.CharField(blank=True, default='', max_length=200)),
                ('matrices', models.ManyToManyField(blank=True, to='personal.Matrix')),
            ],
            options={
                'verbose_name': 'Image Group',
                'verbose_name_plural': 'Image Groups',
                'db_table': 'image_group',
                'ordering': ['group_name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, unique=True)),
                ('category_summary', models.CharField(blank=True, default='', max_length=200)),
                ('matrices', models.ManyToManyField(blank=True, to='personal.Matrix')),
            ],
            options={
                'verbose_name': 'Image Category',
                'verbose_name_plural': 'Image Categories',
                'db_table': 'image_category',
                'ordering': ['category_name'],
            },
        ),
    ]
