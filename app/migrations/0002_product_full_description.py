# Generated by Django 4.0 on 2021-12-31 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='full_description',
            field=models.TextField(null=True),
        ),
    ]