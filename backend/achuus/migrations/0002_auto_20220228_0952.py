# Generated by Django 3.1.7 on 2022-02-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achuus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achuu_profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followd_by', to='achuus.AchuuProfile'),
        ),
    ]
