# Generated by Django 4.2.4 on 2023-09-13 11:57

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_remove_clozequestion_page_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiplechoice',
            name='page_ptr',
        ),
        migrations.AddField(
            model_name='clozequestion',
            name='page',
            field=modelcluster.fields.ParentalKey(default=11, on_delete=django.db.models.deletion.CASCADE, related_name='clozeQuestion', to='pages.pages'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='id',
            field=models.BigAutoField(auto_created=True, default=11, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='page',
            field=modelcluster.fields.ParentalKey(default=11, on_delete=django.db.models.deletion.CASCADE, related_name='multipleChoice', to='pages.pages'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
