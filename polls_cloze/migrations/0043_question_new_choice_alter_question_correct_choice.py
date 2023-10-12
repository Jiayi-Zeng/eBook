# Generated by Django 4.2.5 on 2023-10-09 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0042_rename_q_id_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='new_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='newly_selected_for_question', to='polls.choice', verbose_name='New Choice'),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='correct_for_question', to='polls.choice'),
        ),
    ]