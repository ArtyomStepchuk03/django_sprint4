from django.db import models


class TimeStampedModel(models.Model):
    """Базовая абстрактная модель: дата создания и флаг публикации."""

    is_published = models.BooleanField(
        verbose_name="Публиковать",
        default=True,
        help_text="Отключите, чтобы скрыть объект от отображения.",
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )

    class Meta:
        abstract = True
