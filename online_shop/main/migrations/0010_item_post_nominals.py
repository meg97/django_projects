# Generated by Django 3.1.3 on 2020-11-30 19:12

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_item_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='post_nominals',
            field=django_mysql.models.ListCharField(models.CharField(max_length=10), default=['product'], max_length=66, size=6),
        ),
    ]
