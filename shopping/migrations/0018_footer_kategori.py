# Generated by Django 4.0.6 on 2022-08-11 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0017_remove_footer_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='Kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.kategori'),
        ),
    ]
