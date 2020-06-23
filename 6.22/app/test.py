class Main(object):
    def __init__(self):
        self.objects = []
    
    def __call__(self, obj):
        self.objects.append(obj())
    
    def __repr__(self):
        return str(self.objects)


obj = Main()

@obj
def obj1():
    return 'hello'


print(obj)