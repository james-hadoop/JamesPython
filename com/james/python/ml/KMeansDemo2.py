# -*- coding: UTF-8 -*-
import numpy
import random
import codecs
import copy
import re
import matplotlib.pyplot as plt

def calcuDistance(vec1, vec2):
    # 计算向量vec1和向量vec2之间的欧氏距离
    return numpy.sqrt(numpy.sum(numpy.square(vec1 - vec2)))

def loadDataSet(inFile):
    # 载入数据测试数据集
    # 数据由文本保存，为二维坐标
    inDate = codecs.open(inFile, 'r', 'utf-8').readlines()
    dataSet = list()
    for line in inDate:
        line = line.strip()
        strList = re.split('[ ]+', line)  # 去除多余的空格
        # print strList[0], strList[1]
        numList = list()
        for item in strList:
            num = float(item)
            numList.append(num)
            # print numList
        dataSet.append(numList)

    return dataSet      # dataSet = [[], [], [], ...]

def initCentroids(dataSet, k):
    # 初始化k个质心，随机获取
    return random.sample(dataSet, k)  # 从dataSet中随机获取k个数据项返回

def minDistance(dataSet, centroidList):
    # 对每个属于dataSet的item，计算item与centroidList中k个质心的欧式距离，找出距离最小的，
    # 并将item加入相应的簇类中

    clusterDict = dict()                 # 用dict来保存簇类结果
    for item in dataSet:
        vec1 = numpy.array(item)         # 转换成array形式
        flag = 0                         # 簇分类标记，记录与相应簇距离最近的那个簇
        minDis = float("inf")            # 初始化为最大值

        for i in range(len(centroidList)):
            vec2 = numpy.array(centroidList[i])
            distance = calcuDistance(vec1, vec2)  # 计算相应的欧式距离
            if distance < minDis:
                minDis = distance
                flag = i                          # 循环结束时，flag保存的是与当前item距离最近的那个簇标记

        if flag not in clusterDict.keys():   # 簇标记不存在，进行初始化
            clusterDict[flag] = list()
            # print flag, item
        clusterDict[flag].append(item)       # 加入相应的类别中

    return clusterDict                       # 返回新的聚类结果

def getCentroids(clusterDict):
    # 得到k个质心
    centroidList = list()
    for key in clusterDict.keys():
        centroid = numpy.mean(numpy.array(clusterDict[key]), axis = 0)  # 计算每列的均值，即找到质心
        # print key, centroid
        centroidList.append(centroid)

    return numpy.array(centroidList).tolist()

def getVar(clusterDict, centroidList):
    # 计算簇集合间的均方误差
    # 将簇类中各个向量与质心的距离进行累加求和

    sum = 0.0
    for key in clusterDict.keys():
        vec1 = numpy.array(centroidList[key])
        distance = 0.0
        for item in clusterDict[key]:
            vec2 = numpy.array(item)
            distance += calcuDistance(vec1, vec2)
        sum += distance

    return sum

def showCluster(centroidList, clusterDict):
    # 展示聚类结果

    colorMark = ['or', 'ob', 'og', 'ok', 'oy', 'ow']      # 不同簇类的标记 'or' --> 'o'代表圆，'r'代表red，'b':blue
    centroidMark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw']   # 质心标记 同上'd'代表棱形
    for key in clusterDict.keys():
        plt.plot(centroidList[key][0], centroidList[key][1], centroidMark[key], markersize = 12)  # 画质心点
        for item in clusterDict[key]:
            plt.plot(item[0], item[1], colorMark[key]) # 画簇类下的点

    plt.show()

if __name__ == '__main__':

    inFile = "/home/james/workspace/JamesPython/AutoEventsFieldsVector_clear2.csv"            # 数据集文件
    dataSet = loadDataSet(inFile)                      # 载入数据集
    centroidList = initCentroids(dataSet, 4)           # 初始化质心，设置k=4
    clusterDict = minDistance(dataSet, centroidList)   # 第一次聚类迭代
    newVar = getVar(clusterDict, centroidList)         # 获得均方误差值，通过新旧均方误差来获得迭代终止条件
    oldVar = -0.0001                                   # 旧均方误差值初始化为-1
    print '***** 第1次迭代 *****'
    print
    print '簇类'
    for key in clusterDict.keys():
        print key, ' --> ', clusterDict[key]
    print 'k个均值向量: ', centroidList
    print '平均均方误差: ', newVar
    print
    showCluster(centroidList, clusterDict)             # 展示聚类结果

    k = 2
    while abs(newVar - oldVar) >= 0.0001:              # 当连续两次聚类结果小于0.0001时，迭代结束
        centroidList = getCentroids(clusterDict)          # 获得新的质心
        clusterDict = minDistance(dataSet, centroidList)  # 新的聚类结果
        oldVar = newVar
        newVar = getVar(clusterDict, centroidList)

        print '***** 第%d次迭代 *****' % k
        print
        print '簇类'
        for key in clusterDict.keys():
            print key, ' --> ', clusterDict[key]
        print 'k个均值向量: ', centroidList
        print '平均均方误差: ', newVar
        print
        showCluster(centroidList, clusterDict)            # 展示聚类结果

        k += 1
