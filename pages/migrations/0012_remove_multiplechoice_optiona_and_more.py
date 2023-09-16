# Generated by Django 4.2.4 on 2023-09-06 07:07

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_multiplechoice_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiplechoice',
            name='optionA',
        ),
        migrations.RemoveField(
            model_name='multiplechoice',
            name='optionB',
        ),
        migrations.RemoveField(
            model_name='multiplechoice',
            name='optionC',
        ),
        migrations.RemoveField(
            model_name='multiplechoice',
            name='optionD',
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='option',
            field=wagtail.fields.StreamField([('option_a', wagtail.blocks.CharBlock(blank=True, max_length=250)), ('option_b', wagtail.blocks.CharBlock(blank=True, max_length=250)), ('option_c', wagtail.blocks.CharBlock(blank=True, max_length=250)), ('option_d', wagtail.blocks.CharBlock(blank=True, max_length=250))], default=0, use_json_field=True),
            preserve_default=False,
        ),
    ]