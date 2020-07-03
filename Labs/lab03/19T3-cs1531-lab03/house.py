# Author: @abara15 (GitHub)
class House:
    def __init__(self, owner, address, bedrooms):
        self.owner = owner
        self.address = address
        self.last_price = None
        self.number_bedrooms = bedrooms
        self.sale_status = False
    def advertise(self):
        self.sale_status = True
    def sell(self, buyer, price):
        if self.sale_status == True:
            self.owner = buyer
            self.last_price = price
            self.sale_status = False
        elif self.sale_status == False:
            raise Exception
    pass

# Rob built a mansion with 6 bedrooms
mansion = House("Rob", "123 Fake St, Kensington", 6)

# Viv built a 3 bedroom bungalow
bungalow = House("Viv", "42 Wallaby Way, Sydney", 3)

# The bungalow is advertised for sale
bungalow.advertise()

# Hayden tries to buy the mansion but can't
try:
    mansion.sell("Hayden", 3000000)
except Exception:
    print("Hayden is sad")

# He settles for buying the Bungalow instead
bungalow.sell("Hayden", 1000000)
