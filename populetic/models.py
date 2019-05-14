from django.db import models

# Create your models here.
class Gift(models.Model):
    CATEGORIES = (
        ("Family", "Family"),
        ("Love", "Love"),
        ("Faith", "Faith"),
        ("Hobbies", "Hobbies"),
        ("Purpose","Purpose"),
        ("Engraving","Engraving"),
    )
    _d_categories = dict(CATEGORIES)
    gift_number = models.CharField(max_length=8, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=5, choices=CATEGORIES, default="none")