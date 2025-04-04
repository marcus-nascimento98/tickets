# Generated by Django 4.2.18 on 2025-02-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_alter_quote_description_quotes_alter_quote_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='description_quotes',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='status',
            field=models.IntegerField(blank=True, default=0, editable=False, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='value',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='branch',
            field=models.CharField(choices=[('Niterói', 'Niterói'), ('Petrópolis', 'Petrópolis'), ('Rio das Ostras', 'Rio das Ostras'), ('Teresópolis', 'Teresópolis'), ('Centro de Reparos', 'Centro de Reparos')], max_length=100, verbose_name='Filial'),
        ),
    ]
