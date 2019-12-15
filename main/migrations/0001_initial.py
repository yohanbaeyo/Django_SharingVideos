# Generated by Django 3.0 on 2019-12-14 15:39

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('thumbnail', models.ImageField(default='no_image.png', upload_to=main.models.user_directory_path)),
            ],
        ),
    ]