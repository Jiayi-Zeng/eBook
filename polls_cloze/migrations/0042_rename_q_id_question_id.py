# Generated by Django 4.2.5 on 2023-10-09 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0041_rename_id_question_q_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='q_id',
            new_name='id',
        ),
    ]