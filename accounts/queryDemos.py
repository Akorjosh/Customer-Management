from itertools import product
from unicodedata import category, name

from django.test import tag
from accounts.models import*

#***(1) Returns all customers from customer Table
customers = Customer.objects.all()

#***(2) Returns first customer in table
firstCustomer = Customer.objects.first()

#***(3) Returns last customer in table 
lastCustomer = Customer.objects.last()

#***(4) Single Customer by name
customerByName = Customer.objects.get(name='John Doe')

#***(5) Single Customer by name
customerByName = Customer.objects.get(id=4)

#***(6) returns all orders related to customer 
firstCustomer.order_set.all()

#***(7) returns orders customer name
order = Orders.objects.first()
parentName = order.customer.name

#***(8) returns products from product table with the value of "out door" in category attribute
products = Product.objects.filter(category="Outdoor")

#***(9) order sort objects by id 
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

#(10) returns all products with the tag of sports 
productsFiltered = Product.objects.filter(tags__name = "Sports")

#(11)Bonus
#Q: If the customer has more than 1 ball, how would you reflect that in the DB?
#A: Because there are many different products and this value changes constantly you 
# would most likely not want to store the value int he database but rather jsut make
# this a function we can run each time we load the customers profile#

#returns the total count for number of times a "ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product__name = "Ball").count() 

#Returns total count for each product ordered
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1


#Related Example
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()






