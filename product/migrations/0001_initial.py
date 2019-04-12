# Generated by Django 2.1.3 on 2019-04-11 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField(max_length=250)),
                ('pub_date', models.TextField()),
                ('votes_total', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='images/')),
                ('icon', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
