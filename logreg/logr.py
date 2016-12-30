#coding:utf-8
from numpy import loadtxt,where,reshape,transpose,zeros,mat,shape,ones,exp,array
from pylab import scatter,show,legend,xlabel,ylabel
from math import e,log

# data = loadtxt('C:\\git\\python_learn\\logreg\\data1.txt',delimiter=',')
# # 读取txt 返回array
#
# X = data[:, 0:2] #取array中的前两位 坐标信息
# y = data[:, 2] #取最后一位  标志信息
#
# pos = where(y == 1) #找出y中1的index
# neg = where(y == 0) #找出y中0的index
#
# scatter(X[pos, 0], X[pos, 1], marker='o', c='b') #绘制散点 取左边中第0和第1两值，标志为o 绘制1的点
# scatter(X[neg, 0], X[neg, 1], marker='x', c='r') #绘制0的点
# xlabel('x')
# ylabel('y')
# legend(['Fail', 'Pass'])
# show()

def loadDataSet():
    dataMat = [];labelMat = []
    fr = open('C:\\git\\python_learn\\logreg\\data1.txt')
    for line in fr.readlines():
        lineArr = line.strip().split(',')
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1 + exp(-inX))

def gradAscent(dataMatIN,classLabels):
    dataMatrix = mat(dataMatIN)
    labelMatrix = mat(classLabels).transpose()
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycle = 500
    weight = ones((n,1))
    for k in range(maxCycle):
        h = sigmoid(dataMatrix*weight)
        error = (labelMatrix - h )
        weight = weight + alpha * dataMatrix.transpose() * error
    return weight

def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat,labelMet = loadDataSet()
    dataArr= array(dataMat)
    n = shape(dataArr)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    for i in range(n):
        if int(labelMet[i]) == 1:
            xcord1.append(dataArr[i,1]);ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i, 1]);ycord2.append(dataArr[i, 2])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(ycord2,ycord2,s=30,c='green')
    x = range(-3.0,3.0,0.1)
    print weights
    y = (-weights[0] -weights[1]*x)/weights[2]
    print x
    print y
    print '111111111'
    print len(y)
    ax.plot(x,y)
    plt.xlabel('X1');plt.ylabel('X2');
    plt.show()





def compute_cost(theta, X, y):
    m = X.sha[0]  # 训练样本的行数
    theta = reshape(theta, (len(theta), 1))

    J = (1. / m) * (-transpose(y).dot(log(sigmoid(X.dot(theta)))) - transpose(1 - y).dot(log(1 - sigmoid(X.dot(theta)))))

    grad = transpose((1. / m) * transpose(sigmoid(X.dot(theta)) - y).dot(X))
    # optimize.fmin expects a single value, so cannot return grad
    return J[0][0]  # ,grad

def compute_grad(theta, X, y):
    '''''compute gradient'''
    m = X.shape[0]  # 训练样本的行数
    theta.shape =(1,3)
    grad = zeros(3)
    h = sigmoid(X.dot(theta.T))
    delta = h - y
    l = grad.size
    for i in range(l):
        sumdelta = delta.T.dot(X[:, i])
        grad[i]=(1.0/ m)* sumdelta *-1
    theta.shape =(3,)
    return  grad