# Generated by Django 2.0.13 on 2019-07-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
