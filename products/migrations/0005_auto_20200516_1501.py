# Generated by Django 3.0.5 on 2020-05-16 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200516_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='something', max_length=100),
            preserve_default=False,
        ),
    ]
