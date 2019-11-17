# Generated by Django 2.2 on 2019-11-17 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_auto_20191117_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ('-name',), 'verbose_name': 'Магазин', 'verbose_name_plural': 'Список магазинов'},
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='trademark_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='official_name',
        ),
    ]
