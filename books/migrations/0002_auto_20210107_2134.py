# Generated by Django 3.1.5 on 2021-01-07 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.person'),
        ),
    ]
