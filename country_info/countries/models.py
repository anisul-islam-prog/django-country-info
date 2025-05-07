from django.db import models

class Country(models.Model):
    name = models.JSONField()  # Stores full name details
    cca2 = models.CharField(max_length=2, unique=True)
    cca3 = models.CharField(max_length=3, unique=True)
    ccn3 = models.CharField(max_length=3, null=True, blank=True)
    independent = models.BooleanField(default=False)
    status = models.CharField(max_length=50)
    unMember = models.BooleanField(default=False)
    currencies = models.JSONField(null=True, blank=True)  # Stores currency details
    capital = models.JSONField(null=True, blank=True)  # Stores multiple capitals
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100, null=True, blank=True)
    languages = models.JSONField(null=True, blank=True)  # Stores multiple languages
    translations = models.JSONField(null=True, blank=True)  # Stores translated names
    latlng = models.JSONField(null=True, blank=True)  # Stores latitude & longitude
    landlocked = models.BooleanField(default=False)
    borders = models.JSONField(null=True, blank=True)  # Stores neighboring countries
    area = models.FloatField()
    demonyms = models.JSONField(null=True, blank=True)  # Stores gender-based demonyms
    flag = models.CharField(max_length=10)
    maps = models.JSONField(null=True, blank=True)  # Stores map URLs
    population = models.BigIntegerField()
    gini = models.JSONField(null=True, blank=True)  # Stores GINI index
    timezones = models.JSONField()
    continents = models.JSONField()
    flags = models.JSONField()  # Stores flag images
    coatOfArms = models.JSONField(null=True, blank=True)  # Stores coat of arms images
    startOfWeek = models.CharField(max_length=20)
    capitalInfo = models.JSONField(null=True, blank=True)  # Stores capital coordinates
    postalCode = models.JSONField(null=True, blank=True)  # Stores postal code format

    def __str__(self):
        return self.name.get("common", "Unknown Country")
