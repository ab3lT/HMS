from django.db import models

class Room(models.Model):
    ROOM_CATAGORIES = (('YAC', 'AC'),
    ('NAC', 'NON-AC'),
    ('DEL', 'DELUXE'),
    ('kIN', 'KING'),
    ('QUE', 'QUEEN'),
    )
    number = models.IntegerField()
    catagory = models.CharField(max_length=3, choices=ROOM_CATAGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()


    def __str__(self):
        return f' {self.number}, {self.catagory}   with  {self.beds} for  {self.capacity} people'


