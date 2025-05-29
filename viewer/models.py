from django.db.models import Model, CharField, DateField, ForeignKey, TextField


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
    country = ForeignKey(Country, null=True, blank=True, on_delete=Model.SET_NULL, related_name="creators")
    biography = TextField(null=True, blank=True)