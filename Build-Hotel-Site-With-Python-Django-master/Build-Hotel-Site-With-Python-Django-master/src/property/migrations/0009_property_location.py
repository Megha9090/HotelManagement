# Generated by Django 2.1.5 on 2019-01-12 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
