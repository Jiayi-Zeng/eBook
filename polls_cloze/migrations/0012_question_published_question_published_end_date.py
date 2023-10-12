# Generated by Django 4.2.4 on 2023-09-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_alter_question_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='published_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]