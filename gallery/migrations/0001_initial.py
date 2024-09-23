# Generated by Django 5.1.1 on 2024-09-22 20:00

import django.db.models.deletion
import gallery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('gallery_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Antenna',
            fields=[
                ('gallery_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='gallery.gallery')),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('type', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('gallery.gallery', models.Model),
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('gallery_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='gallery.gallery')),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('gallery.gallery', models.Model),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=gallery.models.upload_to_gallery)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='gallery.gallery')),
            ],
            options={
                'ordering': ['order', '-created_at'],
                'unique_together': {('gallery', 'order')},
            },
        ),
    ]