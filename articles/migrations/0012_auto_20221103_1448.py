# Generated by Django 3.2.13 on 2022-11-03 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_comment_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.comment'),
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
    ]
