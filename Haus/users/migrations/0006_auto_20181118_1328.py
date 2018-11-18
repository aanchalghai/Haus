# Generated by Django 2.1 on 2018-11-18 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_auto_20180822_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='PgListings',
            fields=[
                ('title', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('price', models.CharField(max_length=10, null=True)),
                ('bedrooms', models.CharField(max_length=2, null=True)),
                ('bathrooms', models.CharField(max_length=2, null=True)),
                ('area', models.CharField(max_length=4, null=True)),
                ('locality', models.CharField(max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=10, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True, unique=True)),
                ('pictures', models.ImageField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RentListings',
            fields=[
                ('title', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('price', models.CharField(max_length=10, null=True)),
                ('bedrooms', models.CharField(max_length=2, null=True)),
                ('bathrooms', models.CharField(max_length=2, null=True)),
                ('area', models.CharField(max_length=4, null=True)),
                ('locality', models.CharField(max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=10, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True, unique=True)),
                ('pictures', models.ImageField(blank=True,)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellListings',
            fields=[
                ('title', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('price', models.CharField(max_length=10, null=True)),
                ('bedrooms', models.CharField(max_length=2, null=True)),
                ('bathrooms', models.CharField(max_length=2, null=True)),
                ('area', models.CharField(max_length=4, null=True)),
                ('locality', models.CharField(max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=10, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True, unique=True)),
                ('pictures', models.ImageField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='listings',
            name='user',
        ),
        migrations.DeleteModel(
            name='Listings',
        ),
    ]
