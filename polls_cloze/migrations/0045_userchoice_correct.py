# Generated by Django 4.2.5 on 2023-10-10 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0044_remove_question_new_choice_publish_pubished_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchoice',
            name='correct',
            field=models.BooleanField(default=False),
        ),
    ]