from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg
from django.conf import settings

"""Choices for product gender"""
GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]

"""Choices for shoe type"""
TYPE_CHOICES = [
    ('sport', 'sport'),
    ('skateboarding', 'skateboarding'),
    ('sneakers', 'sneakers'),
    ('lifestyle', 'lifestyle')
]


class Product(models.Model):
    """Product model"""
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    type = models.CharField(choices=TYPE_CHOICES, max_length=30, blank=True, null=True, default=None)
    price = models.FloatField(default=0)
    colors = ArrayField(models.CharField(max_length=20), blank=True, null=True, default=list)
    sizes = ArrayField(models.IntegerField(), blank=True, null=True, default=list)
    discount_price = models.FloatField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    desc = models.TextField(default=None, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, blank=True, null=True, max_length=10)
    for_kids = models.BooleanField(blank=True, null=True)

    @property
    def average_rating(self):
        """Calculate average rating of the product based on Rating model"""
        if hasattr(self, '_average_rating'):
            return self._average_rating

    @property
    def first_color(self):
        """Return product's first color, used for preview version of the project"""
        return self.colors[0]


class ProductPictures(models.Model):
    """Pictures for products"""
    model = models.ForeignKey(Product, related_name='pictures', on_delete=models.CASCADE, blank=True, null=True)
    color = models.CharField(max_length=30, default=None, null=True, blank=True)
    picture = models.ImageField(upload_to="pictures/product_pictures")
    primary_placeholder = models.BooleanField(default=False)
    color_placeholder = models.BooleanField(default=False)
    #
    # def __str__(self):
    #     return self.color


class Rating(models.Model):
    """Product rating"""
    model = models.ForeignKey(Product, related_name='rating', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    message = models.TextField(max_length=350)
    rate = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """User cannot rate same product twice"""
        unique_together = ['user', 'model']
        
    def __str__(self):
        return self.message


