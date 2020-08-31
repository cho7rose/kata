#Imports
import json

class Parcel:
    def __init__(self):
        self.name=""
        self.size=""
        self.cost=0

    def create_parcel(self, myName, mySize):
        self.name=myName
        self.size=mySize
        self.cost=self.sizeTocost(mySize)

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
