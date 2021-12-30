class MyCar():
    # 定义一个共有属性
    log = '布加迪威龙'
    # 定义一个私有属性
    __price = '该车的价格为2000w'

    # 定义一个共有方法
    def running(self):
        print('百公里耗油300L，log={},price={}'.format(self.log,self.__price))
'''
为什么函数中要加self：
    因为当对象去调用类中的成员方法时，系统会默认吧该对象当做参数传递给方法，而self就是接受这个对象参数的
'''

    # 定义一个私有方法
    def __info(self):
        print('车主信息保密,log={},price={}'.format(self.log,self.__price))

#实例化对象
car = MyCar()

#1. 实例化对象访问<公有>属性和方法
#1.1  属性
print(car.log)       #布加迪威龙

# 1.2  方法
car.running()        #百公里耗油300L，log=布加迪威龙


#2. 实例化对象访问<私有>属性和方法
#2.1 私有属性
#print(car.__price)      error报错:AttributeError: 'MyCar' object has no attribute '__price'

#2.2 私有方法
#car.__info             error报错

'''
总结：
私有属性和方法：在本类的内部可以访问（被调用），外部不可用访问
公有属性和方法：在本类的内部和外部都可以被访问
'''




#3 实例化对象动态添加公有属性
#3.1    属性
car.color = '黄色的'
print(car.color)                    #黄色的
print(car.__dict__)                 #{'color': '黄色的'}


#3.2  方法
#3.2.1  无参数
def dahuangfeng():
    print('我是大黄蜂')
car.xhz = dahuangfeng
car.xhz()                           #我是大黄蜂



#3.2.2   有参数
def qingtianzhu(name):
    print('我是{}'.format(name))
car.xhz1 = qingtianzhu
car.xhz1('擎天柱')                            #我是擎天柱


#3.2.3
def flf(car,name):
    print('我是{}，color={},log={},'.format(name,car.color,car.log))
car.xhz2 = flf
car.xhz2(car,'付丽芳')                     #我是付丽芳，color=黄色的,log=布加迪威龙,

# 3.2.4
import types
'''
创建绑定方法，系统自动把该对象当成参数传递给方法
types.MethodType(方法,对象)      ===>绑定方法
'''
def flf1(car,name):
    print('我是{}，color={},log={},'.format(name,car.color,car.log))
car.xhz3 = types.MethodType(flf1,car)
car.xhz3('xhz')                                   #  我是xhz，color=黄色的,log=布加迪威龙,


