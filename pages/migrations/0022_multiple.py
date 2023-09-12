# Generated by Django 4.2.4 on 2023-09-11 12:03

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_delete_multiplechoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multiple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('shortcut', models.CharField(max_length=250)),
                ('question', wagtail.fields.RichTextField()),
                ('option_a', models.CharField(blank=True, max_length=250)),
                ('option_b', models.CharField(blank=True, max_length=250)),
                ('option_c', models.CharField(blank=True, max_length=250)),
                ('option_d', models.CharField(blank=True, max_length=250)),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiple', to='pages.pages')),
            ],
            options={
                'verbose_name_plural': 'MultipleChoice',
            },
        ),
    ]
