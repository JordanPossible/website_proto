# Generated by Django 2.1.2 on 2018-10-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0004_auto_20181009_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titrte', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(max_length=255, upload_to='static/img/')),
            ],
        ),
    ]