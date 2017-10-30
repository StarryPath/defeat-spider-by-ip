#coding=utf-8

from django.shortcuts import HttpResponse
import time

class Stack(object):
    def __init__(self):
        self.AllIP_list=[]   # 储存全部可重复 ip + 时间
        self.Ip_list1=[]         #存储全部不重复ip+个数
        self.Ip_list2=[]
        self.BlackIp_list=[]     #存储被禁ip
        self.dict1={}               #队列中的单个元素
        self.dict2={}             #储存单个ip+个数
    def process_request(self, request):
        if request.META['REMOTE_ADDR'] in self.BlackIp_list:
            return HttpResponse('<h1>Forbidden</h1>')
        while self.AllIP_list!=[]:
            if (time.time()-(self.AllIP_list[0].values()[0]))>10:
                del self.AllIP_list[0]
                del self.Ip_list1[0]
            else:
                break

        self.dict1={request.META['REMOTE_ADDR']:time.time()}
        self.AllIP_list.append(self.dict1)

        self.Ip_list1.append(request.META['REMOTE_ADDR'])
        self.dict2 = {request.META['REMOTE_ADDR']:self.Ip_list1.count(request.META['REMOTE_ADDR'])}
        if self.dict2.values()[0]>50:
            self.BlackIp_list.append(self.dict2.keys()[0])
        print self.AllIP_list,self.dict2,time.time()-(self.AllIP_list[0].values()[0])



