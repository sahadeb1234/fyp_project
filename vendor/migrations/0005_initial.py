# Generated by Django 4.0.1 on 2022-04-07 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0004_delete_preregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=100)),
                ('companyStartdate', models.DateField()),
                ('company_register_number', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Province No. 1', 'Province No. 1'), ('Madhesh Province', 'Madhesh Province'), ('Bagmati Province', 'Bagmati Province'), ('Gandaki Province', 'Gandaki Province'), ('Lumbini Province', '\tLumbini Province'), ('Karnali Province', 'Karnali Province'), ('Sudurpashchim Province', 'Sudurpashchim Province')], max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.PositiveBigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('businesstype', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(upload_to='products')),
                ('company_register_document', models.FileField(upload_to='document')),
            ],
        ),
    ]