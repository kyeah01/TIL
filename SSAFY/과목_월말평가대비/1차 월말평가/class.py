# class Time:
#     """ 시간을 표현하기 위한 클래스,
#         속성으로는 hour, minute, second """
#     def print_time(self):
#         print(self.hour,':',self.minute,':',self.second)


# time = Time()
# time.hour = 11
# time.minute = 59
# time.second = 30
# time.print_time()


class Person:
    def __init__(self, name, cell, pocket):
        self.name = name
        self.cell = cell
        self.pocket = pocket
    def greeting(self):
        print(f'안녕 나는 {self.name}이야.')
    def in_my_pocket(self, item, how_many):
        # if item in self.pocket:
        #     self.pocket.update({item : self.pocket[item]+how_many})
        # else:
        #     self.pocket.update({item:how_many})
        self.pocket.update({item:self.pocket.get(item)+how_many})
    def get_my_pocket(self):
        return self.pocket
    
name = 'yewon'
cell = '1212'
item = {'clip':1, 'earphone':1, 'money':2}
im = Person(name, cell, item)
im.greeting()
im.in_my_pocket('c',1)
print(im.get_my_pocket())