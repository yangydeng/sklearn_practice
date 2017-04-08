# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:03:54 2017

@author: Yangyang Deng
@Email: yangydeng@163.com
"""

from numpy import array,tile
import matplotlib.pyplot as plt 
import operator

def createDataSet():
    group = array([[1.,1.1],[1.,1.],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

group,labels = createDataSet()

inX,dataSet,labels,k = [0,0],group,labels,3  #inX: new sample to be predict; 

dataSetSize = dataSet.shape[0]    #number of samples
diffMat = tile(inX,(dataSetSize,1)) - dataSet  #calculate the different of each element
sqDiffMat = diffMat**2
sqDistances = sqDiffMat.sum(axis=1)
distances = sqDistances**0.5
sortedDistIndicies = distances.argsort()  # the index of distances, smaller -- bigger
classCount = {}
for i in range(k):
    voteIlabel = labels[sortedDistIndicies[i]]
    classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
sortedDistIndicies = sorted(classCount.items(),key=operator.itemgetter(1),reverse = True)

print(sortedDistIndicies[0][0]) 



#--------------------------pyplot scatter test------------------------
data = array([[1,1,1],[2,2,2],[3,3,3],[4,4,4]])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(data[:,1],data[:,2],[10,10,30,30],['r','r','b','b'])  #1st parameter is x-label, 2nd is the second label;
                                                                 #3rd the size of point, 4th the color
plt.show()                    