# Generated by Django 3.0.3 on 2020-10-11 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0006_auto_20201011_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
