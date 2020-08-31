import kata
import unittest

class Test_the_orders(unittest.TestCase):
    def test_simple_order(self):        
        
        # Create an Order
        parcel_list=[]
        parcel_list.append({"name":"Boots", "dimension":55, "weight":1})
        parcel_list.append({"name":"Trousers", "dimension":15, "weight":1})
        parcel_list.append({"name":"T-shirt", "dimension":1, "weight":1})

        Price_list=[]
        Price_list.append(15)
        Price_list.append(8)
        Price_list.append(3)

        #Initialize Order
        myOrder=kata.Order()

        #Get the Order
        result=myOrder.get_my_order(parcel_list, False)
        
        #Run the Tests
        i=0
        for p in result:
            self.assertEqual(p.name, parcel_list[i]["name"])
            self.assertEqual(p.dimension, parcel_list[i]["dimension"])
            self.assertEqual(p.cost, list(Price_list)[i])
            i+=1
        self.assertEqual(myOrder.total_cost, 26)

    def test_speedy_shipping(self):
        
        # Create an Order
        parcel_list=[]
        parcel_list.append({"name":"Boots", "dimension":55, "weight":1})
        parcel_list.append({"name":"Trousers", "dimension":15, "weight":1})
        parcel_list.append({"name":"T-shirt", "dimension":1, "weight":1})

        Price_list=[]
        Price_list.append(15)
        Price_list.append(8)
        Price_list.append(3)

        #Initialize Order
        myOrder=kata.Order()

        #Get the Order
        result=myOrder.get_my_order(parcel_list, True)
        
        #Run the Tests
        i=0
        for p in result:
            self.assertEqual(p.name, parcel_list[i]["name"])
            self.assertEqual(p.dimension, parcel_list[i]["dimension"])
            self.assertEqual(p.cost, list(Price_list)[i])
            i+=1
        self.assertEqual(myOrder.total_cost, 52)

    def test_weighty_parcels_with_speedy_shipping(self):
        # Create an Order
        parcel_list=[]
        parcel_list.append({"name":"Boots", "dimension":55, "weight":8})
        parcel_list.append({"name":"Trousers", "dimension":15, "weight":5})
        parcel_list.append({"name":"T-shirt", "dimension":1, "weight":1})

        Price_list=[]
        Price_list.append(19)
        Price_list.append(12)
        Price_list.append(3)

        #Initialize Order
        myOrder=kata.Order()

        #Get the Order
        result=myOrder.get_my_order(parcel_list, True)
        
        #Run the Tests
        i=0
        for p in result:
            self.assertEqual(p.name, parcel_list[i]["name"])
            self.assertEqual(p.dimension, parcel_list[i]["dimension"])
            self.assertEqual(p.cost, list(Price_list)[i])
            i+=1
        self.assertEqual(myOrder.total_cost, 68)

    def test_Heavy_Parcel(self):
        # Create an Order
        parcel_list=[]
        parcel_list.append({"name":"Bricks", "dimension":1, "weight":60})

        Price_list=[]
        Price_list.append(60)

        #Initialize Order
        myOrder=kata.Order()

        #Get the Order
        result=myOrder.get_my_order(parcel_list, False)
        
        #Run the Tests
        i=0
        for p in result:
            self.assertEqual(p.name, parcel_list[i]["name"])
            self.assertEqual(p.dimension, parcel_list[i]["dimension"])
            self.assertEqual(p.cost, list(Price_list)[i])
            i+=1
        self.assertEqual(myOrder.total_cost, 60)

if __name__ == '__main__':
    myTests=Test_the_orders()
    myTests.test_simple_order()
    myTests.test_speedy_shipping()
    myTests.test_weighty_parcels_with_speedy_shipping()
    myTests.test_Heavy_Parcel()
    print("All tests have passed successfully")

