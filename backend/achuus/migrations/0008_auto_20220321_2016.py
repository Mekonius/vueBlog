# Generated by Django 3.1.7 on 2022-03-21 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achuus', '0007_auto_20220301_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achuu_profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='achuus.Achuu_Profile'),
        ),
    ]
