from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    alpha_2 = models.CharField(max_length=2, db_index=True)
    alpha_3 = models.CharField(max_length=3, db_index=True)
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name