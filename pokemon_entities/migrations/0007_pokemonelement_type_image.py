# Generated by Django 3.1.8 on 2021-04-21 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20210421_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonelement_type',
            name='image',
            field=models.ImageField(null=True, upload_to='element_pic', verbose_name='изображение элемента'),
        ),
    ]
