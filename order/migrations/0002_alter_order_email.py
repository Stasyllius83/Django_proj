# Generated by Django 4.2.6 on 2023-12-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=150, verbose_name='почта'),
        ),
    ]
