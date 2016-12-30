from logr import loadDataSet,gradAscent
dataArr,labelArr = loadDataSet()
# print dataArr
# print labelArr
m = gradAscent(dataArr,labelArr)
print m
