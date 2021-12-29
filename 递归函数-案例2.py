'''
计算文件家的总大小是一个典型的递归案例：
递归函数：自己调用自己的函数被称为递归函数；

什么时候触发递归？
1. 当最后一层栈帧空间执行结束的时候，触发递归
2. 当遇到return返回值的时候，终止当前函数触发递归。
'''

'''
listvar = [1,2,3,4,5,6,7,8,9] （用zip函数实现listvar1，listvar2，listvar3）
n = 2
listvar1 = [[1,2],[3,4],[5,6],[7,8]]
n = 3
listvar2 = [[1,2,3],[4,5,6],[7,8,9]]
n = 4
listvar3 = [[1,2,3,4],[5,6,7,8]
'''
'''
1. 分析：
zip(list1,list2,list3...),是将传入的列表参数中，各个列表中的元素相同的下标组成新的列表：
如：
zip([1,2,3,5],[4,5,6])         ===>  ((1,4),(2,5),(3,6))

2. listvar1 = [[1,2],[3,4],[5,6],[7,8]]   可以变为如下列表用zip组成：
当n = 2时：
list1 = [1,3,5,7,9]  ===>list1 = listvar[0::2]
list2 = [2,4,6,8]    ===>list2 = listvar[1::2]

当n=3时：
listvar2 = [[1,2,3],[4,5,6],[7,8,9]]
list1 = [1,4,7]     ===>list1 = listvar[0::3]
list2 = [2,5,8]     ===>list2 = listvar[1::3]
list3 = [3,6,9]     ===>list3 = listvar[2::3]

n = 4
listvar = [[1,2,3,4],[5,6,7,8]
list1 = [1,5,9]     ===>list1 = listvar[0::4]
list2 = [2,6]       ===>list2 = listvar[1::4]
list3 = [3,7]       ===>list3 = listvar[2::4]
list3 = [5,8]       ===>list3 = listvar[3::4]

3. 总结：
3.1  经过上述规律，listvar切片时，lisvar=[range(n)::n]


'''
list1 = []
listvar = [1,2,3,4,5,6,7,8,9]
#基本思路
for n in  [ listvar[i::3 ]for i in range(3) ]:
    list1.append(n)
print(list1)
print(list(zip(list1[0],list1[1])))

#简化
print('<======>')
fnc = lambda n :zip(*[ listvar[i::n ]for i in range(n) ])
print(list(fnc(3)))


# 2.青蛙跳台阶  (递归实现)
'''
一只青蛙要跳上n层高的台阶
一次能跳一级,也可以跳两级
请问这只青蛙有多少种跳上这个n层高台阶的方法?
'''
'''
分析：
1.  当n=1时： 跳跃方式  (1)                                        1种
2.  当n=2时： 跳跃方式  （1，1） (2)                               2种
3.  当n=3时： 跳跃方式  （1，1，1） (1，2)  （2，1）                 3种
4.  当n=4时： 跳跃方式  （1，1，1，1） (1，1，2) （1，2，1）（2，1，1）（2，2）               5种
5.  当n=5时： 跳跃方式  （1，1，1，1，1） (1，2，1，1) （1，1，2，1）（1，1，1，2）（2，1，1，1）
                      （1，2，2） （2，1，2）（2，2，1）            8种
6.  当n=6时： 跳跃方式  （1，1，1，1，1，1） (1，2，1，1，1) （1，1，2，1，1）（1，1，1，2，1）（2，1，1，1，1）（1，1，1，1，2）
                      （2，2，1，1） （2，1，2，1）（2，1，1，2） 
                      （1，2，2，1） （1，2，1，2） 
                      （1，1，2，2）（2，2，2）                  13种
                      
即：
n=1    m=1
n=2    m=2
n=3    m=3   1+2
n=4    m=5   2+3
n=5    m=8   3+5
n=6    m=13  5+8
'''
def fnc(n):
    if n <=2:
        return n
    return fnc(n-1) + fnc(n-2)
print(fnc(7))


# 3.递归反转字符串 "将14235 反转成53241" (递归实现)
#方法一：
#反向取字符
number = '14235'
def fnc1(lth,list11=[]):
    if lth == 0:
        return list11
    res = number[lth-1]
    list11.append(res)
    return fnc1(lth-1)
lth = len(number)
print(list(fnc1(lth)))

#方法二：
#正项去字符创
def fnc2(star):
    if len(star) == 1:
        return star
    return fnc2(star[1:]) + fnc2(star[0])
star = '14235'
print(list(fnc2(star)))


# 4.斐波那契数列用尾递归实现
#斐波那契数列就是改组数列： 1，1，2，3，5，8，13，21
def fnc3(n):
    if n == 1 or n == 2:
        return 1
    return fnc3(n-2) + fnc3(n-1)
print(fnc3(7))

