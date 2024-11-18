from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    specialist = models.ForeignKey(
        'specialists.Specialist',
        on_delete=models.CASCADE,
        related_name='services_specialist'
    )
    images = models.ImageField(
        upload_to='service_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
