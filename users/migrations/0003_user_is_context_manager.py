# Generated by Django 4.2.15 on 2024-08-11 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_user_avatar_user_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_context_manager',
            field=models.BooleanField(default=False, verbose_name='Контекст-менеджер'),
        ),
    ]
