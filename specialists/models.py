from django.db import models


class Specialist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    services = models.ForeignKey(
        'services.Service',
        on_delete=models.CASCADE,
        related_name='specialists_service'
    )
    lust_meter = models.IntegerField(
        default=50, choices=[(i, i) for i in range(0, 101)])
    image = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
