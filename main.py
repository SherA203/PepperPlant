class Car:
    models = {
        "Some model"       : 0,
        "Some other model" : 1
    }            #You don't need to space the line out like this, I just like doing it like this.
    model = None #None is the python equivalent of null
    colors = {
        "Lorem" : 0,
        "Ipsum" : 1
    }
    color = None

    def __init__(self, model, color):
        #__init is the name of all constructors in python
        #self has to be the first input in a python function within a class.
        self.model = model
        self.color = color

c = Car(1, 0)
print(c.models)
print(c.model)
print(c.colors)
print(c.color)
