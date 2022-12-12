# Generated by Django 4.0.6 on 2022-10-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_lab'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Lab2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_txt1', models.CharField(max_length=100)),
                ('d_txt1', models.TextField()),
                ('image1', models.ImageField(upload_to='media/media')),
                ('h_txt2', models.CharField(max_length=100)),
                ('d_txt2', models.TextField()),
                ('image2', models.ImageField(upload_to='media/media')),
            ],
        ),
        migrations.DeleteModel(
            name='About_Lab',
        ),
    ]