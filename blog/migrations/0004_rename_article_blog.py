# Generated by Django 4.1 on 2022-09-02 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_remove_article_url_alter_article_date_and_more"),
    ]

    operations = [
        migrations.RenameModel(old_name="Article", new_name="Blog",),
    ]
