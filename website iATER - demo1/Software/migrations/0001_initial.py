# Generated by Django 4.0.6 on 2022-10-25 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sw_head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sw_h', models.CharField(max_length=150)),
                ('sw_t', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='sw_txtbody1_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bd_h_txt1', models.TextField()),
                ('bd_txt1', models.TextField()),
                ('image1', models.ImageField(upload_to='media/media')),
            ],
        ),
        migrations.CreateModel(
            name='sw_txtbody2_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bd_h_txt1', models.TextField()),
                ('bd_txt1', models.TextField()),
                ('image1', models.ImageField(upload_to='media/media')),
            ],
        ),
    ]
