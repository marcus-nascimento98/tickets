# Generated by Django 4.2.18 on 2025-01-28 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_alter_quote_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='description_quotes',
            new_name='description',
        ),
    ]
