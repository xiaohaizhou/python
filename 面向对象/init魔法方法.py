'''
__init__构造方法：
1.  触发时机：实例化对象，初始化时触发
2. 功能：为对象创建成员
3. 参数：参数不固定，至少一个self参数
'''

class   Myclass():
    def __init__(self,name,skin):
        print('我是构造方法：__init__')
        self.name = name
        self.skin = skin

    def Info(self):
        print('小孩子的名字是{}，小孩子的肤色是{}'.format(self.name,self.skin))

xhz = Myclass('hello word','黑色的')
xhz.Info()
'''
打印信息：
我是构造方法：__init__         （只要类被实例化就会打印）
小孩子的名字是hello word，小孩子的肤色是黑色的
'''