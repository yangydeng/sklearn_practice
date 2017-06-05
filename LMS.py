# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 20:33:31 2017

@author: Administrator
"""

#-------------------------------------------------------------
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

random.seed(2)

def process_data1(w1,w2,M):
    data = [0.1,0.2]
    
    while M:
        M-=1
        data.append(data[-2]*w1+data[-1]*w2+random.normal(0,0.1,1)[0])
        
    
    feature_set = []        
    target_set = []
    
    p3 = len(data)-1
    p2 = p3-1
    p1 = p3-2
    while p1>=0:
        feature_set.append([data[p1],data[p2]])
        target_set.append(data[p3])
        p1,p2,p3 = p1-1,p2-1,p3-1
    
    
    return {'feature_set': np.array(feature_set),
            'target_set': np.array(target_set)}
    
    
def process_data2(w1,w2,M):
    target_set= []
    feature_set = []
    while M:
        M-=1
        tri = sin(float(M)/10*pi)
        noise = random.normal(0,0.5,1)[0]
        feature_set.append([tri,noise])
        target_set.append(w1*tri+w2*noise)
    return {'feature_set': np.array(feature_set),
            'target_set': np.array(target_set)}
    


class LMSI(object):
    """LMS回归算法"""
        
    @staticmethod    
    def draw_w(w0,w1,w2,w3):
        fig0 = plt.figure(0)
        ax = fig0.add_subplot(1,1,1)
        ax.plot(w0,'b'),plt.plot(w1,'r')
        ax.plot(w2,'g'),plt.plot(w3,'y')
        
    @staticmethod
    def draw_learn_curve(E1,E2):
        fig1 = plt.figure(1)
        ax1 = fig1.add_subplot(1,1,1)
        ax1.plot(E1,'g')
        ax1.plot(E2,'y')

    @staticmethod
    def draw_sin(data,pre):
        s = []
        for i in list(data['feature_set']):
            s.append(i[0])
        fig2 = plt.figure(2)
        ax = fig2.add_subplot(1,1,1)
        ax.plot(s,'k')
        
        target = list(data['target_set'])
        fig3 = plt.figure(3)
        ax = fig3.add_subplot(211)
        ax.plot(target,'k')
        
        ax = fig3.add_subplot(212)
        ax.plot(pre,'k')
            

    @staticmethod
    def train(learning_rate):
        data = process_data2(0.6010,-0.3,100)
        theta = np.empty(len(data['feature_set'][0]))        
        
        size = len(theta)
        itertime = 0
        w0 = []
        w1 = []
        E = []
        pre = []
        while itertime < 300:
            itertime += 1
            r = []
            
            fs = data['feature_set']
            ts = data['target_set']
            for i in range(len(fs)):
                predict = np.dot(fs[i], theta)
                error = ts[i] - predict
                r.append(error)
            r = np.array(r)
            delta = []
            for i in range(size):
                
                delta.append(np.dot(r, fs[:,i]))
            delta = learning_rate * np.array(delta)
            theta = theta + delta
            w0.append(theta[0]),w1.append(theta[1]),E.append(error),pre.append(predict)
                
        print theta
        return [w0,w1,E,data,pre]        

if __name__ == '__main__':
    P1 = LMSI.train(0.02)
    P2 = LMSI.train(0.005)
    LMSI.draw_w(P1[0],P1[1],P2[0],P2[1])
    LMSI.draw_learn_curve(P1[2],P2[2])
    LMSI.draw_sin(P1[3],P1[4])