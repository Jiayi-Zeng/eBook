# Generated by Django 4.2.4 on 2023-09-14 05:06

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_choice_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.question'),
        ),
    ]
