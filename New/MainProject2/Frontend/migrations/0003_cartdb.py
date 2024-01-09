# Generated by Django 4.2.5 on 2023-11-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_userregdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=30, null=True)),
                ('Prod_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Total_price', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
