# Generated by Django 4.2.4 on 2023-09-12 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_multiplechoice_clozequestion_page_delete_multiple'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clozequestion',
            name='page',
        ),
        migrations.RemoveField(
            model_name='multiplechoice',
            name='page',
        ),
    ]