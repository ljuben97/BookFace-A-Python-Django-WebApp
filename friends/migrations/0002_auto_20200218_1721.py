# Generated by Django 3.0.3 on 2020-02-18 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friend',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='request',
            name='requested_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='request',
            name='requested_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
