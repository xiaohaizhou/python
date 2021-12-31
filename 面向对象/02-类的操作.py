class  MyDog():
    # 公有属性
    dog = '拉布拉多'

    #私有属性
    __dog_hair = '黑白相间'

    #公有方法
    def jump():
        print('毛为{}的{}喜欢乱跳'.format(MyDog.__dog_hair,MyDog.dog))

    # 私有方法
    def __luanjiao():
        print('{}喜欢乱叫'.format(MyDog.dog))

#1.  类调用属性和方法
#1.1  属性
print(MyDog.dog)                    #拉布拉多

#1.2 方法
MyDog.jump()                        #毛为黑白相间的拉布拉多喜欢乱跳


#2. 类添加属性和方法
#2.1    类添加属性
MyDog.color = '纯黑色'
print(MyDog.color)                  #纯黑色
print(MyDog.__dict__)               #该类的所有成员属性和方法：{'__module__': '__main__', 'dog': '拉布拉多', '_MyDog__dog_hair': '黑白相间', 'jump': <function MyDog.jump at 0x7fd31cea9d08>, '_MyDog__luanjiao': <function MyDog.__luanjiao at 0x7fd31cea9d90>, '__dict__': <attribute '__dict__' of 'MyDog' objects>, '__weakref__': <attribute '__weakref__' of 'MyDog' objects>, '__doc__': None, 'color': '纯黑色'}



#2.2    类添加方法
#方法一：无参数
def func1():
    print('打印的是：类添加无参数的方法，{}'.format(MyDog.color))
MyDog.func_1 = func1
MyDog.func_1()                      #打印的是：类添加无参数的方法，纯黑色

#方法二：有参数的
def func2(name):
    print('打印的是：添加的有参数的方法，{}'.format(name))
MyDog.func_2 = func2
MyDog.func_2('拉布拉多二号')          #打印的是：添加的有参数的方法，拉布拉多二号

#方法三：lambda
MyDog.func_3 = lambda :print('这个类是打印狗狗相关信息的...')
MyDog.func_3()                      #这个类是打印狗狗相关信息的...

'''
总结：
1.  类中的无参数方法只能类来调用，对象无法调用
2.  对象可以调用类中的成员，反过来类不能调用对象中的成员
3.  每创建一个对象都会在内存中占用一份空间，并且对象之间是相互独立的。
4.  在类外也不可以用类的操作去调用私有属性和方法
'''