# Generated by Django 4.2.6 on 2023-12-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.CharField(blank=True, max_length=100, null=True, verbose_name='slug')),
                ('content', models.CharField(max_length=250, verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='изображение')),
                ('date_create', models.DateTimeField(verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='признак публикации')),
                ('count_views', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
