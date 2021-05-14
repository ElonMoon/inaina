# Generated by Django 2.2.2 on 2019-06-29 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mina", "0002_auto_20170812_0122"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="minapost",
            options={"ordering": ("-created_date",), "verbose_name": "민아 포스트", "verbose_name_plural": "민아 포스트 목록"},
        ),
        migrations.AlterField(
            model_name="minapost",
            name="user",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="유저"
            ),
        ),
    ]
