# Generated by Django 4.2.4 on 2023-09-04 08:43

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_blogpagegalleryimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpagegalleryimage',
            old_name='caption',
            new_name='answer',
        ),
        migrations.RemoveField(
            model_name='blogpagegalleryimage',
            name='image',
        ),
        migrations.AddField(
            model_name='blogpagegalleryimage',
            name='question',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blogpagegalleryimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='pages.pages'),
        ),
    ]