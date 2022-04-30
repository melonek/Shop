from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=99999, decimal_places=2)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    class Producer(models.Model):
        def __str__(self):
            return self.nazwa

        name = models.CharField(max_length=60)
        description = models.TextField(blank=True)

        class Meta:
            verbose_name = "Producer"
            verbose_name_plural = "Producers"

