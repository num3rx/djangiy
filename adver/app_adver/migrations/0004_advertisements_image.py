# Generated by Django 4.2.3 on 2023-08-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adver', '0003_advertisements_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='image',
            field=models.ImageField(default='', upload_to='', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]