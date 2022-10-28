from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# uuid - slug instead of the DB ID
class Meal(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.meal} {self.stars}"

    class Meta:
        unique_together = [("user", "meal")]
        index_together = [("user", "meal")]
