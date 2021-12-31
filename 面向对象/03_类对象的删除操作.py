class Family():
    #公有属性
    name = 'xhz'
    # 私有属性
    __wife_name = 'flf'
    #公有有参方法（）
    def famiy_head(self):
        print('{}的妻子是{}'.format(self.name,self.__wife_name))

    # 私有有参方法（）
    def __boss_of_family(self):
        print('家中的boos是{}'.format(self.__wife_name))
    #公有无参方法
    def house_wife():
        print('家庭主妇是{}'.format(Family.__wife_name))
    #私有无参方法
    def __chef_family():
        print('家中的厨师是{}'.format(Family.name))

    #用于访问私有成员的公有方法
    def chengyuan(self):
        print(Family.__wife_name)
        print(Family.__chef_family())

'''实例化对象'''
happy_family = Family()

# 1.  类外访问私有化成员（属性和方法）
'''方法一：访问私有成员'''
#python的私有话实际上是采用了改名策略：_类名 + 私有属性;（在其他的语言之中实际上是真的无法获取到私有属性的）
print(happy_family._Family__wife_name)          #flf
happy_family._Family__boss_of_family()          #家中的boos是flf

'''方法二：访问私有成员(使用类中的公有方法去访问)--推荐该方法'''
print('========')
happy_family.chengyuan()        #flf     家中的厨师是xhz

#2. 使用类对象的删除相应的成员
'''删除对象成员属性'''
happy_family.name = 'xswl'
print(happy_family.name)            #xswl
del happy_family.name
print(happy_family.name)            #xhz
#del del happy_family.name          error(报错）

'''删除对象成员方法'''
happy_family.fangfa = lambda :print('这个是类的成员访问')
happy_family.fangfa()
del happy_family.fangfa
#happy_family.fangfa()          #error找不到该方法

'''删除类中的成员属性'''
del Family.name
'''删除类中的成员属性'''
del Family.famiy_head

'''
总结：
1.  对象可以访问类中公有的成员，但是不能删除或者修改类中的成员
2.  对象在访问成员时，优先访问该对象自己的成员，如果没有在访问类的，类中也没有的话就报错
'''



