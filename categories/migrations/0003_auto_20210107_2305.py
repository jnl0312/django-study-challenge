# Generated by Django 3.1.5 on 2021-01-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20210107_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('action', 'Action'), ('comedy', 'Comedy'), ('thriller', 'Thriller'), ('history', 'History')], max_length=20),
        ),
    ]