# Generated by Django 4.2.5 on 2023-10-10 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0043_question_new_choice_alter_question_correct_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='new_choice',
        ),
        migrations.AddField(
            model_name='publish',
            name='pubished_at',
            field=models.DateTimeField(auto_now_add=True, default='2023-09-15 02:28:19.587328\t'),
            preserve_default=False,
        ),
    ]