# Generated by Django 4.2.4 on 2023-09-14 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_userchoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchoice',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
            preserve_default=False,
        ),
    ]
