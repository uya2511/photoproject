# Generated by Django 4.1 on 2023-11-17 01:06

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
            name="Category",
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
                ("title", models.CharField(max_length=20, verbose_name="カテゴリ")),
            ],
        ),
        migrations.CreateModel(
            name="PhotoPost",
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
                ("title", models.CharField(max_length=200, verbose_name="タイトル")),
                ("comment", models.TextField(verbose_name="コメント")),
                ("image1", models.ImageField(upload_to="photoa", verbose_name="イメージ1")),
                (
                    "image2",
                    models.ImageField(
                        blank=True, null=True, upload_to="photos", verbose_name="イメージ2"
                    ),
                ),
                (
                    "posted_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="投稿日時"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="photo.category",
                        verbose_name="カテゴリ",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="ユーザー",
                    ),
                ),
            ],
        ),
    ]
