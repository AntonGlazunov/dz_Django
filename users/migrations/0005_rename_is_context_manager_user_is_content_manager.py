# Generated by Django 4.2.15 on 2024-08-11 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_is_context_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_context_manager',
            new_name='is_content_manager',
        ),
    ]
