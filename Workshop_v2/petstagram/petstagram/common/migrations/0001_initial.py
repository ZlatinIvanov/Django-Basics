# Generated by Django 5.0.1 on 2024-02-04 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('pet_photo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='photos.petphoto')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_photo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='photos.petphoto')),
            ],
        ),
    ]
