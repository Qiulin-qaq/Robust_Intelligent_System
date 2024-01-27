# Generated by Django 4.2.4 on 2023-09-02 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdminInfo",
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
