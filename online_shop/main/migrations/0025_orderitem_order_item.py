# Generated by Django 3.1.3 on 2020-12-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20201205_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order_item',
            field=models.ManyToManyField(blank=True, null=True, to='main.Item'),
        ),
    ]
