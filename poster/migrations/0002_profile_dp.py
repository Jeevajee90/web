# Generated by Django 4.2.3 on 2023-08-28 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import poster.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_dp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=poster.models.getImagename)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
