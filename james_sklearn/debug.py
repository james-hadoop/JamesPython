# encoding:utf-8
from __future__ import print_function
from numpy import *
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))


def loadDataSet(filename):
    dataMat = []  # 创建元祖
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split(",")
        print(curLine)
        fltLine = map(float, curLine)  # 使用map函数将curLine里的数全部转换为float型
        dataMat.append(fltLine)
    return dataMat


def distEclud(vecA, vecB):  # 计算两个向量的欧式距离
    return sqrt(sum(power(vecA - vecB, 2)))


def randCent(dataSet, k):  # 位给定数据集构建一个包含k个随机质心的集合
    n = shape(dataSet)[1]  # shape函数此时返回的是dataSet元祖的列数
    centroids = mat(zeros((k, n)))  # mat函数创建k行n列的矩阵，centroids存放簇中心
    for j in range(n):
        minJ = min(dataSet[:, j])  # 第j列的最小值
        rangeJ = float(max(dataSet[:, j]) - minJ)
        centroids[:, j] = minJ + rangeJ * random.rand(k, 7)  # random.rand(k,1)产生shape(k,1)的矩阵
    return centroids


datMat = loadDataSet('/Users/qjiang/Desktop/20171218/test2.csv')
print(datMat)

y_pred = KMeans(n_clusters=6).fit_predict(datMat)

print("\n")
print(80 * '_')
print(y_pred)

print("\n")
print(80 * '_')

ss = set()
for c in y_pred:
    print(c, ',', end='')
    ss.add(c)

print("\n")
print(80 * '_')
print(ss)
