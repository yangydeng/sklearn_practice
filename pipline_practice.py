# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 19:20:20 2017

@author: Yangyang Deng
@Email: yangydeng@163.com
"""

from sklearn import svm 
from sklearn.datasets import samples_generator
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.pipeline import Pipeline

X,y = samples_generator.make_classification(n_informative=5,n_redundant=0,random_state=0)

anova_filter = SelectKBest(f_regression,k=5)
clf = svm.SVC(kernel='linear')
#
anova_svm = Pipeline([('anova',anova_filter),('svc',clf)])
anova_svm.set_params(anova__k=10,svc__C=0.2,svc__kernel="sigmoid").fit(X,y)


anova_svm.predict(X)
score = anova_svm.score(X,y)

C = anova_svm.named_steps['svc'].get_params