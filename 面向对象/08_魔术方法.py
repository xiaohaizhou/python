'''
__new__魔术方法：
1.  触发时机：实例化类生成对象的时候触发，（触发时机在__init__之前）
2.  功能：控制对象的创建过程
3.  参数：至少有一个cls接受当前类，其他根据情况来定
4.  返回值：通常返回对象或None


__init__方法和__new__方法注意事项：
1.  如果__new__没有返回对象或者返回的是其他类的对象，不会调用构造方法
2.  __new__和__init__的参数要保持一致
'''
#1. 基本使用 :
# 在使用了__new__魔法方法后，但是在不定义对象的话，返回值为None；我们在平时不用__new__魔法方法的时候，实际上默认父类object已经创建了
class  Myclass1():
    def __new__(cls, *args, **kwargs):
        pass
obj1 = Myclass1()
print(obj1)             #None


#2. 返回本类对象
class Myclass2():
    def __new__(cls, *args, **kwargs):
        obj2 =  object.__new__(cls)
        return obj2

obj2 = Myclass2()
print(obj2)                     #<__main__.Myclass2 object at 0x7f9eb9b9ff28>

#3. 返回其他类的对象
class Myclass3():
    def __new__(cls, *args, **kwargs):
        return obj2
obj3 = Myclass3()
print(obj3)                       #返回的对象2：<__main__.Myclass2 object at 0x7fd3b65a1a90>


'''
__del__魔术方法（构析方法）
触发时机：当对象内存被回收时自动触发，页面执行完毕回收所有变量；所有对象被del时候也会触发
功能：对象使用完毕之后资源回收
参数：一个self接收对象。
返回值：无
'''
#1. 基本语法
class Myslass():
    def __init__(self,name):
        self.name = name

    def xx(self):
        print('我的名字是{}'.format(self.name))

    def __del__(self):
        print('构析方法被触发....')
#触发方式一：页面执行完毕回收所有变量
obj4 = Myslass('xhz')
# obj4.xx()
'''我的名字是xhz
构析方法被触发....'''

#触发方式二：所有对象被del时候也会触发
obj5 = obj4
print('<===start====>')
del obj4                    #此时还存在obj5,因此不会触发__del__
del obj5
print('<===end====>')
#注意：当前对象引用计数为2，只有引用计数为0的时候，该对象才会被真正删除



'''
__str__魔术方法：
    触发时机：使用print（对象）或者str（对象）的时候触发
    功能： 查看对象
    参数：一个self接受当前对象
    返回值：必须返回字符串
    
'''
class Cat():
    gift = '抓老鼠'
    def __init__(self,name):
        self.name = name

    def cat_gift(self):
        return  '猫的名字是{}，猫会{}'.format(self.name,self.gift)

    def __str__(self):
        return self.cat_gift()
tom = Cat('汤姆')
print(str(tom))

'''
__repr__魔术方法：
    触发时机：使用repr（对象）的时候触发
    功能： 查看对象,与__str__相似
    参数：一个self接受当前对象
    返回值：必须返回字符串

'''
class Mouse():
    gift = '偷吃'
    def __init__(self,name):
        self.name = name

    def cat_gift(self):
        print('老鼠的名字是{}，老鼠会{}'.format(self.name,self.gift))

    def __str__(self):
        return self.cat_gift()
jerry = Mouse('杰瑞')
res = repr(jerry)
print(res)