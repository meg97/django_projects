# Generated by Django 3.1.3 on 2020-12-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_item_post_nominals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='ref_num',
            field=models.TextField(unique=True),
        ),
    ]
