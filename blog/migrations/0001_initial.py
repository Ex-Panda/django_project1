# Generated by Django 4.2.6 on 2023-10-29 13:33

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
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('content', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog_image/', verbose_name='превью')),
                ('date_creation', models.DateTimeField(verbose_name='дата создания')),
                ('is_publication', models.BooleanField(verbose_name='признак публикации')),
                ('number_views', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'публикация',
                'verbose_name_plural': 'публикации',
            },
        ),
    ]
