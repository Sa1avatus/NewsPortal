# Generated by Django 4.1.3 on 2022-11-07 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_products_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creation_date',
            new_name='creation',
        ),
    ]
