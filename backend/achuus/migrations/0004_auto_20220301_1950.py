# Generated by Django 3.1.7 on 2022-03-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achuus', '0003_auto_20220228_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achuu_profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='achuus.AchuuProfile'),
        ),
    ]
