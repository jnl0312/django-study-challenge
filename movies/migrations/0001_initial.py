# Generated by Django 3.1.5 on 2021-01-07 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_auto_20210107_2134'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('year', models.DateField()),
                ('cover_image', models.ImageField(blank=True, upload_to='')),
                ('rating', models.IntegerField()),
                ('cast', models.ManyToManyField(blank=True, related_name='kind_cast', to='people.Person')),
                ('category', models.ManyToManyField(blank=True, to='categories.Category')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kind_director', to='people.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
