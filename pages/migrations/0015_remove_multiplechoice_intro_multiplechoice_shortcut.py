# Generated by Django 4.2.4 on 2023-09-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_remove_multiplechoice_body_multiplechoice_optiona_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiplechoice',
            name='intro',
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='shortcut',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
