# Generated by Django 5.0.2 on 2024-04-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_country_alter_address_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='countries_published',
            field=models.ManyToManyField(null=True, to='store.country'),
        ),
    ]