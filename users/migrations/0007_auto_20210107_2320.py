# Generated by Django 3.1.5 on 2021-01-07 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20210107_2309'),
        ('users', '0006_auto_20210107_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fav_book_genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_book', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fav_movie_genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_movie', to='categories.category'),
        ),
    ]
