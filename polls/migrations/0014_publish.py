# Generated by Django 4.2.5 on 2023-09-15 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_userchoice_submitted_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('are_you_sure', models.BooleanField(default=False, help_text='Are you sure you want to schedule the publication?')),
                ('delay_duration', models.DurationField(help_text='Duration to wait before the question should be published.')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='publish', to='polls.question')),
            ],
            options={
                'verbose_name': 'Publication Schedule',
                'verbose_name_plural': 'Publication Schedules',
            },
        ),
    ]
