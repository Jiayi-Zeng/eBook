# Generated by Django 4.2.4 on 2023-08-30 09:05

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_blogpage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
