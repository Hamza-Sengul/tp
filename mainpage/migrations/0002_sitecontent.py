# Generated by Django 5.0.6 on 2024-08-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divider_image_1', models.ImageField(blank=True, null=True, upload_to='site_images/')),
                ('divider_image_2', models.ImageField(blank=True, null=True, upload_to='site_images/')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='site_images/')),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('about_us', models.TextField(blank=True, null=True)),
                ('vision', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
