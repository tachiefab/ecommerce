from django.conf import settings
from django.db.models.signals import pre_save
from django.db import models
from categories.models import Category
from tmstoreapi.utils import unique_slug_generator


def upload_product_image(instance, filename):
    return "product/{slug}/{filename}".format(slug=instance.slug, filename=filename)


class ProductQuerySet(models.QuerySet):
    pass


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)


class Product(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    description     = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99, null=True,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                        null=True, blank=True, 
                                        related_name='product_category'
                                        )
    image       = models.ImageField(upload_to=upload_product_image, null=True, blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-timestamp',]

    @property
    def owner(self):
        return self.user

    @property
    def product_category(self):
        return self.category.name


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver, sender=Product)





