# Generated by Django 2.1.7 on 2019-04-02 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(default='no name', max_length=30)),
                ('post_name_id', models.IntegerField()),
                ('post_note', models.CharField(default='no note', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PostsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(default='no name', max_length=30)),
                ('post_contents', models.CharField(default='no contents', max_length=200)),
                ('post_like_cout', models.IntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postitem_set', to='Posts.Posts')),
            ],
        ),
    ]
