#Imports
import json

class Parcel:
    def __init__(self):
        self.name=""
        self.dimension=0
        self.size=""
        self.cost=0

    def create_parcel(self, myName, myDimension):
        self.name=myName
        self.dimension=myDimension
        if(self.dimension<10): 
            self.size="s"
        elif(self.dimension>10 and self.dimension<50): 
            self.size="m"
        elif(self.dimension>50 and self.dimension<100):
            self.size="l"
        elif(self.dimension>=100):
            self.size="xl"
        else:
            raise ValueError("Dimensions cannot be negative")
        self.cost=self.sizeTocost(self.size)

    def sizeTocost(self, a):
        switch={
            "s":3,
            "m":8,
            "l":15,
            "xl":25
        }
        return switch.get(a,0)

class Order:
    def __init__(self):
        self.total_cost=0
        self.List_of_parcels=[]

    def get_my_order(self, parcels, speedy_shipping):
        for p in parcels:
            myParcel=Parcel()
            myParcel.create_parcel(p, parcels[p])
            self.List_of_parcels.append(myParcel)
            self.total_cost+=myParcel.cost
        if(speedy_shipping==True):
            self.total_cost=self.total_cost*2
        return(self.List_of_parcels)
