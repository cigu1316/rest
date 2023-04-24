# Generated by Django 4.1.3 on 2023-04-23 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Subcategoria', 'verbose_name_plural': 'Subcategorias'},
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='measureunit',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]