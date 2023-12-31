# Generated by Django 4.2.5 on 2023-10-10 16:36

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('md_pages', '0002_alter_mdpages_body'),
        ('polls', '0045_userchoice_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userchoice',
            name='choice',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='ClozeQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=200)),
                ('published', models.BooleanField(default=False)),
                ('correct_choice', models.CharField(max_length=200)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='cloze_questions', to='md_pages.mdpages')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='ClozePublish',
            fields=[
                ('publish_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('pubished_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.clozequestion')),
            ],
        ),
    ]
