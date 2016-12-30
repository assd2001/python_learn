from logr import loadDataSet,gradAscent,plotBestFit
dataArr,labelArr = loadDataSet()
# print dataArr
# print labelArr
m = gradAscent(dataArr,labelArr)
# print m
plotBestFit(m)

