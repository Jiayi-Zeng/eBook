# Generated by Django 4.2.6 on 2023-11-14 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls_cloze', '0003_alter_clozequestion_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clozequestion',
            options={'ordering': ['question_text'], 'verbose_name': '填空题', 'verbose_name_plural': '填空题'},
        ),
    ]
