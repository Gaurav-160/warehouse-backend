from django.db import models

# Godown model to represent sections and subsections


class Godown(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    parent_godown = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Item model to represent items stored in the godowns


class Item(models.Model):
    item_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    price = models.FloatField()
    status = models.CharField(max_length=50)
    godown = models.ForeignKey(
        Godown, related_name='items', on_delete=models.CASCADE)
    brand = models.CharField(max_length=255)
    attributes = models.JSONField()  # Store item attributes as JSON
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return self.name
