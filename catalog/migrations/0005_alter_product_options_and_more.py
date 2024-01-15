# Generated by Django 4.2.6 on 2024-01-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('set_is_published', 'Может менять статус публикации'), ('set_description', 'Может изменять описание'), ('set_category', 'Может изменять категорию')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='last_date_chance',
            new_name='last_date_change',
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='признак публикации'),
        ),
    ]