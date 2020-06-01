
class A:
    def __init__(self):
        a = 1
        self.b = 2
    
    def changer(self):
        self.b += 1

insA = A()

# print(insA.a)
# print(insA.b)

# insA.b = 0
# print(insA.b)

insB = A()
# print(insB.b)

insA.changer()
print(insA.b)
print(insB.b)