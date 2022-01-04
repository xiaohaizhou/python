'''
什么是继承：
    ---一个类除了自身所拥有的的属性和方法外，还获取了另一个类的属性和方法;是一种继承关系，被继承的类称为父类
（基类或超类），继承的类称为子类（衍生类）

继承分类：单继承，多继承。

1. 单继承：
    1.1 子父继承之后，子类可以调用父类的公有属性和方法;
    1.2 子父继承之后，子类不能调用父类的私有成员;
    1.3 子父继承之后，子类可以重写父类的公有方法;
        1.3.1   重写父类的方法实际上是在子类中重新定义了一个与父类中名称相同的方法。
        1.3.2   实例对象在调用属性和方法时，调用顺序为：对象--子类--父类-- 都没有则报错
'''
class   Family():
    husband = 'xhz'

    __wife = 'flf'

    def father(self):
        print('我的父亲是{}'.format(self.husband))

    def __mother(self):
        print('我的母亲是{}'.format(self.__wife))

class Myhouse(Family):
    #调用父类属性和方法
    def house(self):
        self.father()
        print(self.husband)
        # print(self.__wife)            #error

    #重写父类方法：
    def father(self):
        print('我的父亲不是你了，换人了')


zz = Myhouse()
#1.  调用父类中的成员属性和方法
zz.house()
zz.father()                     #我的父亲是xhz
'''
打印信息：
我的父亲是xhz
xhz
error
'''

#2.  重写父类方法
zz.father()                 #我的父亲不是你了，换人了





'''
1.  多继承：
    1.1 用类调用：
        语法： 类名.方法/属性
    
    1.2 用对象调用
        调用顺序：对象本身--类--父类（继承的先后顺序）

'''
class  Chian():
    def first_line_citys(self):
        print('一线城市有：北上广深')

    def second_line_citys(self):
        print('二线城市有：武汉，成都，重庆')

class   Usa():
    def first_line_citys(self):
        print('一线城市有：纽约')

    def second_line_citys(self):
        print('二线城市有：芝加哥')

class  Ct(Chian,Usa):
    pass

class Qt(Usa,Chian):
    pass

#对象调用(调用顺序：对象本身--类--父类（继承的先后顺序）)
qq = Ct()
qq.first_line_citys()       #一线城市有：北上广深
qq.second_line_citys()      #二线城市有：武汉，成都，重庆

ww = Qt()
ww.first_line_citys()       #一线城市有：纽约
ww.second_line_citys()      #二线城市有：芝加哥




