# Generated by Django 3.1.7 on 2022-02-24 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220224_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='img/'),
        ),
    ]
