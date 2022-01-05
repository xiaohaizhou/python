'''
什么是多态？
    不同的子类对象，调用相同的父类方法，产生不同的执行结果。
    （简而言之：不同的子类中都重写了父类的方法和属性。）

'''
class Arym():
    def attack(self):
        print('海陆空，全军出击....')

    def back(self):
        print('海陆空，全军撤退....')

class Air_force(Arym):
    def attack(self):
        print('我是空军，我要进攻.')

    def back(self):
        print('我是空军，我要撤退了.')

class Navy(Arym):
    def attack(self):
        print('我是海军，我要进攻.')

    def back(self):
        print('我是海军，我要撤退了.')

class Army_jun(Arym):
    def attack(self):
        print('我是路军，我要进攻.')

    def back(self):
        print('我是路军，我要撤退了.')

#创建对象
obj1 = Air_force()
obj2 = Navy()
obj3 = Army_jun()
obj2.attack()

list1 = [obj1,obj2,obj3]
starvar = '''
1. 全军出击
2. 全军撤退
3. 海军出击，其他撤退
'''
num = int(input('请输入序号：'))
for i in list1:
    if num == 1:
        i.attack()
    elif num == 2:
        i.back()
    elif num == 3:
        if isinstance(i,Navy):
            i.attack()
        else:
            i.back()

'''
单态：同一个类，无论实例化多少次，都有且只有一个对象。

每创建一个对象，都会在内存中多占用一份空间，为了节省空间，提升执行效率，使用单态模式。
场景：只是单纯调用类中的成员，而不会额外为当前对象添加成员
'''

#实现单态的方式：
class Myclass():
    __obj = None
    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self,name):
        self.name = name

obj1 = Myclass('xhz')

obj2 = Myclass('flf')
print(obj1.name)                    #flf
print(obj2.name)                    #flf
'''
解析：
1.  第一次，在实例化对象的时候触发__new__魔术方法；
     if cls.__obj is None 的条件成立，object.__new__(cls)创建一个对象给私有成员属性__obj
2.  第二次，在实例化对象的时候，触发魔术方法__new__，此时if cls.__obj is None的条件不成立，因此直接
    return cls.__obj。

3.  第三次，第四次...都通二一样，因此每次实例对象都是相同的。
4.  所以obj1.name和obj2.name的返回信息均为flf
'''