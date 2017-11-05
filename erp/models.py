from django.db import models


class Bread(models.Model):
    """ Bread class """

    name = models.CharField(max_length=30, unique=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def new_price(self, price):
        self.price = price


class Stock(models.Model):
    """ Stock class """

    bread = models.ForeignKey(Bread, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.quantity, self.bread.name)

    # how to "throw away" (i.e. turn quantity to 0) lines create the day before?


# class Sale(models.Model):
#     """ Sale class """
#
#     def __str__(self):
#         return "{} {} sold on {}".format(self.quantity, self.bread.name,
#                                             self.date)
