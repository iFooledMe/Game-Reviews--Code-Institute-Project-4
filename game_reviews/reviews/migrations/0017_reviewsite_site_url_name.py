# Generated by Django 3.1 on 2020-08-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0016_auto_20200812_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewsite',
            name='site_url_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
