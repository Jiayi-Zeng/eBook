# Generated by Django 4.2.6 on 2023-10-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_cloze', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clozequestion',
            name='correct',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
