# Generated by Django 3.1 on 2020-08-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0018_auto_20200806_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='icon',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
