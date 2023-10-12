# Generated by Django 4.2.5 on 2023-10-08 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0032_alter_question_correct_choice_alter_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_choice',
            field=models.ForeignKey(blank=True, limit_choices_to={'question': models.F('id')}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='correct_for_question', to='polls.choice'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]