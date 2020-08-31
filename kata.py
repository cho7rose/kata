#Imports
import json

class Parcel:
    def __init__(self):
        self.name=""
        self.dimension=0
        self.size=""
        self.cost=0
        self.weight=0

    def create_parcel(self, myName, myDimension, myWeight):
        self.name=myName
        self.dimension=myDimension
        self.weight=myWeight
        self.get_size()
        self.cost=self.sizeTocost(self.size)
        self.addOverweight()

    def get_size(self):
        if(self.weight>50):
            self.size="Heavy"
        elif(self.dimension<10): 
            self.size="s"
        elif(self.dimension>10 and self.dimension<50): 
            self.size="m"
        elif(self.dimension>50 and self.dimension<100):
            self.size="l"
        elif(self.dimension>=100):
            self.size="xl"
        else:
            raise ValueError("Dimensions cannot be negative")
    
    def sizeTocost(self, a):
        switch={
            "s":3,
            "m":8,
            "l":15,
            "xl":25,
            "Heavy":50
        }
        return switch.get(a,0)

    def addOverweight(self):
        if(self.size=="s" and self.weight>1):
            self.cost+=(self.weight-1)*2
        elif(self.size=="m" and self.weight>3):
            self.cost+=(self.weight-3)*2
        elif(self.size=="l" and self.weight>6):
            self.cost+=(self.weight-6)*2
        elif(self.size=="xl" and self.weight>10):
            self.cost+=(self.weight-10)*2
        elif(self.size=="Heavy" and self.weight>50):
            self.cost+=(self.weight-50)

class Order:
    def __init__(self):
        self.total_cost=0
        self.List_of_parcels=[]

    def get_my_order(self, parcels, speedy_shipping):
        for p in parcels:
            myParcel=Parcel()
            myParcel.create_parcel(p["name"], p["dimension"], p["weight"])
            self.List_of_parcels.append(myParcel)
            self.total_cost+=myParcel.cost
        if(speedy_shipping==True):
            self.total_cost=self.total_cost*2
        return(self.List_of_parcels)
