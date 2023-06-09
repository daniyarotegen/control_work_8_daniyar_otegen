from django.db import models
from source import settings


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('CPU', 'Processor'),
        ('GPU', 'Graphics Card'),
        ('MONITOR', 'Monitor'),
        ('MOTHERBOARD', 'Motherboard'),
    )

    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50, verbose_name='Category')
    description = models.TextField(max_length=3000, blank=True, null=True, verbose_name='Description')
    image = models.URLField(null=True, blank=True, verbose_name='Image URL')

    def __str__(self):
        return self.name

    def average_rating(self):
        total_reviews = self.reviews.count()
        if total_reviews > 0:
            total_rating = sum([review.rating for review in self.reviews.all()])
            return round(total_rating / total_reviews, 1)
        return None


class Review(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Author'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Product'
    )
    feedback = models.TextField(
        max_length=3000,
        blank=False,
        null=False,
        verbose_name='Feedback'
    )
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.author.username}'s review of {self.product.name}"
