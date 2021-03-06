# Generated by Django 2.1 on 2018-08-21 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('title', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('R', 'Rent'), ('S', 'Sale')], max_length=1, null=True)),
                ('price', models.CharField(max_length=5, null=True)),
                ('bedrooms', models.CharField(max_length=2, null=True)),
                ('bathrooms', models.CharField(max_length=2, null=True)),
                ('area', models.CharField(max_length=4, null=True)),
                ('locality', models.CharField(max_length=10, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=10, null=True)),
                ('country', models.CharField(max_length=10, null=True)),
                ('pin_code', models.CharField(max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True, unique=True)),
                ('pictures', models.ImageField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
