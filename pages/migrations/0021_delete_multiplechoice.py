# Generated by Django 4.2.4 on 2023-09-11 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_alter_multiplechoice_answer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MultipleChoice',
        ),
    ]