import kata
import unittest

class Test_the_orders(unittest.TestCase):
    def test_simple_order(self):        
        
        # Create an Order
        Order_list={
            "Boots":"l",
            "Trousers":"m",
            "T-shirt":"s"
        }
        Price_list=[]
        Price_list.append(15)
        Price_list.append(8)
        Price_list.append(3)

        #Initialize Order
        myOrder=kata.Order()

        #Get the Order
        result=myOrder.get_my_order(Order_list)
        
        #Run the Tests
        i=0
        for p in result:
            self.assertEqual(p.name, list(Order_list.keys())[i])
            self.assertEqual(p.size, list(Order_list.values())[i])
            self.assertEqual(p.cost, list(Price_list)[i])
            i+=1
        self.assertEqual(myOrder.total_cost, 26)

if __name__ == '__main__':
    unittest.main()