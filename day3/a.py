#!/usr/bin/python

class C :
    def __init__(self) :
        print("Class C is created")
        self.name = "ccc"
        self.age = 0

    def say_hi(self) :
        print("hi")

    def add_age(self, n : int) :
        self.age += n
        
    def __str__(self) :
        return "Call __str__"

    def __repr__(self) :
        return "Call __repr__"

    def __abs__(self) :
        print("Call __abs__")

    def __len__(self) :
        print("Call __len__")

    def __add__(self, other) :
        return self.age + other.age
