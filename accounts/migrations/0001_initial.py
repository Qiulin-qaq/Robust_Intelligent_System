# Generated by Django 4.2.4 on 2023-08-31 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=32, unique=True, verbose_name="用户名"),
                ),
                ("password", models.CharField(max_length=64, verbose_name="密码")),
            ],
        ),
    ]