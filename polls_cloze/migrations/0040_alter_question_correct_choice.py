# Generated by Django 4.2.5 on 2023-10-09 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0039_alter_choice_question_alter_question_correct_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_choice',
            field=models.ForeignKey(blank=True, limit_choices_to={'choice_text': models.F('choice_text')}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='correct_for_question', to='polls.choice'),
        ),
    ]
