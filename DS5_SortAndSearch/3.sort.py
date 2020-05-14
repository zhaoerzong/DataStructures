'''











    二丶选择排序：每遍历一次列表直交换一次数据，也就是进行一次遍历时找到最大的项
        完成遍历后，再把它换到正确的位置

        alist= [26,54,93,17,77,31,44,55,20]
        第一次遍历 [26,54,17,77,31,44,55,20,93]
        第二次遍历 [26,54,20,17,55,31,44,77,93]
        第三次遍历 [26,54,20,17,44,31,55,77,93]
        第四次遍历 [26,31,20,17,44,54,55,77,93]
        第五次遍历 [26,31,20,17,44,54,55,77,93]
        第六次遍历 [26,31,20,17,44,54,55,77,93]
        第七次遍历 [20,17,26,31,44,54,55,77,93]
        第八次遍历 [17,20,26,31,44,54,55,77,93]

'''

def seletcSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionMax = 0

        for location in range(1,fillslot+1):
            if alist[location] > alist[positionMax]:
                positionMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionMax]
        alist[positionMax] = temp


alist = [26,54,93,17,77,31,44,55,20]
seletcSort(alist)
print(alist)
