# Generated by Django 3.1.5 on 2021-01-18 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210118_0341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['surname', 'first_name']},
        ),
        migrations.RenameField(
            model_name='author',
            old_name='last_name',
            new_name='surname',
        ),
    ]