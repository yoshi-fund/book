# Generated by Django 4.2.5 on 2023-10-01 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("book_title", models.CharField(max_length=100, verbose_name="タイトル")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="＊任意",
                        null=True,
                        upload_to="",
                        verbose_name="表紙画像",
                    ),
                ),
                (
                    "document_type",
                    models.IntegerField(
                        choices=[(1, "書籍"), (2, "論文"), (3, "ニュース記事"), (4, "その他")],
                        verbose_name="カテゴリ",
                    ),
                ),
                ("text", models.TextField(blank=True, null=True, verbose_name="書評")),
                (
                    "stars",
                    models.IntegerField(
                        choices=[
                            (1, "☆"),
                            (2, "☆☆"),
                            (3, "☆☆☆"),
                            (4, "☆☆☆☆"),
                            (5, "☆☆☆☆☆"),
                        ],
                        verbose_name="評価",
                    ),
                ),
                (
                    "posted_date",
                    models.DateField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="投稿日",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="ユーザー名",
                    ),
                ),
            ],
        ),
    ]
