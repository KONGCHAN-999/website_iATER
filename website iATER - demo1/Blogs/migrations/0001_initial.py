# Generated by Django 4.0.6 on 2022-10-25 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogs_TxtH', models.CharField(max_length=150)),
                ('blogs_Txt', models.TextField()),
                ('blogs_Image', models.ImageField(upload_to='media/media')),
            ],
        ),
    ]