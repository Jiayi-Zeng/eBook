# Generated by Django 4.2.4 on 2023-09-14 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_choice_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
    ]
