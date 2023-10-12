# Generated by Django 4.2.5 on 2023-10-10 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0046_alter_userchoice_choice_clozequestion_clozepublish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userchoice',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.choice'),
        ),
        migrations.CreateModel(
            name='ClozeUserChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=200)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('correct', models.BooleanField(default=False)),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.publish')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
