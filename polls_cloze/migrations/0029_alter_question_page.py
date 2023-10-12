# Generated by Django 4.2.5 on 2023-10-08 22:52

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('md_pages', '0002_alter_mdpages_body'),
        ('polls', '0028_question_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories2', to='md_pages.mdpages'),
        ),
    ]