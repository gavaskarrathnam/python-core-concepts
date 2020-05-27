import os
from model import Product as prod


class Controller():
    def product_list(self):
        return prod.getProduct(self)


control = Controller()
print(" output:  " + control.product_list() )

