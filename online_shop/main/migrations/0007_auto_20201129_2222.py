# Generated by Django 3.1.3 on 2020-11-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201129_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='/models/no_image.jpg', upload_to='media'),
        ),
    ]
