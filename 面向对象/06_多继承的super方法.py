'''
1.super调用父类方法：
1.1  super本身是一个类，super()是一个对象，用于调用父类的绑定方法
1.2  super()只应用在绑定方法中，默认自动传递self对象，（前提是super所在的作用域存在self）
1.3  super的用途：解决复杂的多继承顺序。

2.  super解析：
2.1 super采用mro方法进行计算，计算出多继承的调用顺序
2.2 super语法： 类.mro()    ===>返回的为列表数据
2.3 super会自动根据mro列表返回出来的顺序依次调用
2.4 super作用：专门用于解决复杂的多继承调用顺序关系，依照mro列表

'''


class Pather():
    def pope(self):
        print('<====77=======>')
        print(self)
        print('<====88=======>')

class Father(Pather):
    def pope(self):
        print('<====55=======>')
        super().pope()
        print('<====66=======>')

class Mother(Pather):
    def pope(self):
        print('<====33=======>')
        super().pope()
        print('<====44=======>')

class Son(Father,Mother):
    def pope(self):
        print('<====11=======>')
        super().pope()
        print('<====22=======>')
class myclass():
    pass


sonner = Son()
sonner.pope()       #打印顺序：1-5-3-7-8-4-6-2
print(Son.mro())
'''
分析：为何为：1-5-3-7-8-4-6-2
1.  Son类的mro列表如下：
[<class '__main__.Son'>,
<class '__main__.Father'>, 
<class '__main__.Mother'>, 
<class '__main__.Pather'>, 
<class 'object'>]

2.  先执行Son类，Son子类在执行super().pope的时候查找到Father父类，因此调用Father父类中pope方法

3. 执行到Father中的popo方法的时候，执行到super().pope，则找mro列表，因此调用Mother父类中的pope

4. 执行到Mother中的popo方法的时候，执行到super().pope，则找mro列表，因此调用Pather父类中的pope

5. 此时执行的顺序为：1-5-3-7-8

6. 由于在Mother类中的时候没有执行完，因此执行4，同理在执行6，最后在是2；所以顺序为1-5-3-7-8-4-6-2
'''


'''
issubclass:判断子父类关系（应用在类与类之间）
1.  只要满足在一条继承链上即可；
2.  如果元组中只要一个父类满足，即为真
'''
print(issubclass(Son,Father))                   #True
print(issubclass(Son,(Father,myclass)))         #True
print(issubclass(Son,Pather))                   #True

'''
isinstance:判断对象类型（应用在对象和类之间）
1.  只要满足在一条继承链上即可；
2.  如果元组中只要一个满足，即为真
'''
print(isinstance(sonner,Father))                        #True
print(isinstance(sonner,Pather))                        #True
print(isinstance(sonner,(Mother,myclass)))              #True
print(isinstance(sonner,myclass))                       #False