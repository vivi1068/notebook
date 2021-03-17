# Generated by Django 3.1.7 on 2021-03-17 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('content', models.TextField(max_length=5000, verbose_name='文章内容')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('date_joined', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('date_last_change', models.DateTimeField(auto_now=True, verbose_name='最后一次修改时间')),
            ],
        ),
    ]
