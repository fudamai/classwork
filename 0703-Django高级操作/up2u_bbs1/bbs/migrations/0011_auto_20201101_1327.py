# Generated by Django 3.0.3 on 2020-11-01 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0010_reply_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='reply_text',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_description',
            field=models.TextField(max_length=2000),
        ),
    ]
