# Generated by Django 3.0.8 on 2020-11-04 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0006_auto_20201103_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='default.png', upload_to='Profile_images'),
        ),
    ]
