# Generated by Django 4.0.6 on 2022-08-04 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.FileField(blank=True, null=True, upload_to='cards', verbose_name='card resmi')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=150)),
            ],
        ),
    ]
