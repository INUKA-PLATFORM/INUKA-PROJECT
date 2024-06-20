# Generated by Django 4.2.13 on 2024-06-20 17:31

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='applicants_contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='financial_statements',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file'),
        ),
        migrations.AddField(
            model_name='user',
            name='guardian_contacts',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='letter_of_recommendation',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file'),
        ),
        migrations.AddField(
            model_name='user',
            name='national_id',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file'),
        ),
        migrations.AddField(
            model_name='user',
            name='passport_photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='user',
            name='reason_for_application',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='year_of_study',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file'),
        ),
    ]
