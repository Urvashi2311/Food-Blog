# Generated by Django 4.0.4 on 2022-05-15 07:41

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('content', tinymce.models.HTMLField()),
                ('url', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
