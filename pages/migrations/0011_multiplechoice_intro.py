# Generated by Django 4.2.4 on 2023-09-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_multiplechoice_options_delete_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoice',
            name='intro',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
