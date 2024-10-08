# Generated by Django 4.2.16 on 2024-09-28 15:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=512, verbose_name='Название темы по ГО и ЧС')),
                ('t_desciption', models.TextField(blank=True, verbose_name='Краткое описание темы')),
            ],
            options={
                'verbose_name': 'Тема ГО и ЧС',
                'verbose_name_plural': 'Темы ГО и ЧС',
            },
        ),
        migrations.CreateModel(
            name='ImageMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('im_name', models.CharField(max_length=512, verbose_name='название материала картинки')),
                ('im_img', models.ImageField(upload_to='images_materials/', verbose_name='файл кратинки')),
                ('im_date', models.DateField(default=datetime.date.today, verbose_name='Дата публикации')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cde_site.theme', verbose_name='тема ГО и ЧС')),
            ],
            options={
                'verbose_name': 'Материал (Картинка) к теме по ГО и ЧС',
                'verbose_name_plural': 'Материалы (Картинки) к теме по ГО и ЧС',
            },
        ),
        migrations.CreateModel(
            name='DocumentMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dm_name', models.CharField(max_length=512, verbose_name='название материала документа')),
                ('document_path', models.FileField(upload_to='documents_materials/', verbose_name='файл документа')),
                ('dm_date', models.DateField(default=datetime.date.today, verbose_name='Дата публикации')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cde_site.theme', verbose_name='тема ГО и ЧС')),
            ],
            options={
                'verbose_name': 'Материал (Документы) к теме по ГО и ЧС',
                'verbose_name_plural': 'Материалы (Документы) к теме по ГО и ЧС',
            },
        ),
    ]
