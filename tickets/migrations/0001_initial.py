# Generated by Django 4.2.18 on 2025-01-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_user', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('branch', models.CharField(max_length=100)),
                ('subject_purchase', models.CharField(max_length=200)),
            ],
        ),
    ]
