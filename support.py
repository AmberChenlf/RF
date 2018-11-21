#_*_coding:utf-8_*_
import re

def delete_space(string):
    return string.replace(" ","").replace("\t","").strip()

def statistic(string):
    #返回参数statisticList[i]的列表内容：rx-pkts,rx-bytes,jumbo(oversinze),undersize,discard,fcsError,mtuExceeded,fragments,tx-pkts,tx-bytes
    statistcList = list()
    list1 = string.split("eth")
    del list1[0]

    for i in range(len(list1)):
        statistcList = list1[i].split(" ")
        del statistcList[0]
        while "" in statistcList:
            statistcList.remove("")

    return statistcList

def Changeabs(number):
    return    abs(number)

