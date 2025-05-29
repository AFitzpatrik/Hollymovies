from django.db.models import Model, CharField



class Genre(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True) #Zkouška druhé migrace
