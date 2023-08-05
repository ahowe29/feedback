from django.db import models


class Review(models.Model):
    user_name = models.CharField(max_length=100)  # no need for max length cause the form validates this, but needed for db efficency
    review_text = models.TextField()
    rating = models.IntegerField()
