# Generated by Django 3.2.18 on 2023-06-06 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_location', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('image_data', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
