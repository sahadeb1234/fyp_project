# Generated by Django 4.0.1 on 2022-03-06 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cartproduct_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]