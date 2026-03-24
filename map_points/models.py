from django.db import models

# Create your models here.
class MapPoint(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Принято'),
        (STATUS_APPROVED, 'Одобрено'),
        (STATUS_REJECTED, 'Отказ'),
    ]

    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name='Широта'
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name='Долгота'
    )

    image = models.ImageField(
        upload_to='points/',
        blank=True,
        null=True,
        verbose_name='Фотография'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        verbose_name='Статус'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )

    def __str__(self):
        return f'{self.title} ({self.get_status_display()})'
