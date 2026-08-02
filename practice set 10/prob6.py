import random
random.randint(222,555)# or from random import randint

class train:

    def __init__(slf,trainno):
        slf.trainno=trainno

    def book(self,trainno,fro,to):
        print(f"ticket is booked in train number {trainno} from {fro} to {to}")

    def getstatus(self):
        print(f"train number {self.trainno} is running on time")

    def getfare(self, trainno,fro,to):
        print(f"fare for train number {trainno} from {fro} to {to} is {random.randint(222,555)}")


t = train(12345)
t.book(12345,"delhi","mumbai")
t.getstatus()
t.getfare(12345,"delhi","mumbai")#no change in output because self is just a convention, we can use any name instead of self