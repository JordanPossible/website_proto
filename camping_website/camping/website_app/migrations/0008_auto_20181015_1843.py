# Generated by Django 2.1.2 on 2018-10-15 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0007_auto_20181015_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(max_length=255, upload_to='media/upload/'),
        ),
    ]