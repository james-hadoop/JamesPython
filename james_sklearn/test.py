# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import numpy as np

final = open('/Users/qjiang/Desktop/20171218/AutoEventsFieldsVector4.csv', 'r')

for line in final:
    print(line)


data = [line.strip().split(',') for line in final]

feature = [[float(x) for x in row[:]] for row in data]

#调用kmeans类
clf = KMeans(n_clusters=9)
s = clf.fit(feature)
print(s)

#9个中心
print(clf.cluster_centers_)

#每个样本所属的簇
print(clf.labels_)

#用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
print(clf.inertia_)

#进行预测
print(clf.predict(feature))

#保存模型
joblib.dump(clf, '/Users/qjiang/Desktop/km.pkl')

#载入保存的模型
clf = joblib.load('/Users/qjiang/Desktop/km.pkl')