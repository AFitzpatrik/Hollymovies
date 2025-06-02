from django.db import models
from django.db.models import Model, CharField, DateField, ForeignKey, TextField, DateTimeField, ManyToManyField


class Genre(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True) #Zkouška druhé migrace

    class Meta:
        ordering = ["name"]

    def __repr__(self): # převádí na string, určena více pro programátory, než uživatele
       return f"Genre(name={self.name})"

    def __str__(self): #převádí na string, určena více pro uživatele, než programátory
        return self.name


class Country(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Countries"

    def __repr__(self):
        return f"Country(name={self.name})"

    def __str__(self):
        return self.name


class Creator(Model):
    name = CharField(max_length=32, null=True, blank=True)
    surname = CharField(max_length=32, null=True, blank=True)
    artistic_name = CharField(max_length=32, null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
    date_of_death = DateField(null=True, blank=True)
    country = ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL, related_name="creators")
    biography = TextField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ["surname", "name", "artistic_name", "date_of_birth"]


        def __repr__(self):
            return f"Creator(name={self.name}, surname={self.surname}, artistic_name={self.artistic_name})"

        def __str__(self):
            if self.date_of_birth:
                return f"{self.name} {self.surname} ({self.date_of_birth.year})"
            return f"{self.name} {self.surname}"


class Movie(Model):
    title_orig = CharField(max_length=64, null=False, blank=False)
    title_cz = CharField(max_length=64, null=True, blank=True)
    genre = ManyToManyField(Genre, blank=True, related_name="movies")
    directors = ManyToManyField(Creator, blank=True, related_name="directing")
    actors = ForeignKey(Creator,null=True, blank=True, on_delete=models.SET_NULL, related_name="acting_movies")
    composers = ForeignKey(Creator,null=True, blank=True, on_delete=models.SET_NULL, related_name="composed_movies")
    length = ForeignKey(Creator,null=True, blank=True, on_delete=models.SET_NULL, related_name="length_movies")
    description = TextField(null=True, blank=True)
    year = DateField(null=True, blank=True)
    countries = ForeignKey(Creator, null=True, blank=True, on_delete=models.SET_NULL, related_name="movies")

    class Meta:
        ordering = ["title_orig", "title_cz", "genre", "directors", "actors", "composers", "length", "year", "countries"]


        def __repr__(self):
            return f"Movie(title_orig={self.title_orig}, title_cz={self.title_cz}, genre={self.genre})"

        def __str__(self):
            return f"{self.title_orig} {self.title_cz} ({self.genre})"