# Generated by Django 5.0.4 on 2024-04-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='mpaaRatingLabel',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='mpaaRatingType',
        ),
        migrations.AddField(
            model_name='movie',
            name='mpaaRating',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
