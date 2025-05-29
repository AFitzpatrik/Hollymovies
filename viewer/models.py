from django.db.models import Model, CharField



class Genre(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True) #Zkouška druhé migrace

    class meta:
        ordering = ["name"]

    def __repr__(self): # převádí na string, určena více pro programátory, než uživatele
       return f"Genre(name={self.name})"

    def __str__(self): #převádí na string, určena více pro uživatele, než programátory
        return self.name
