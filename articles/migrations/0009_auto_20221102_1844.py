# Generated by Django 3.2.13 on 2022-11-02 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_merge_0005_alter_article_hits_0007_article_modify_dt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hits',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='like_users',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated_at',
        ),
    ]
