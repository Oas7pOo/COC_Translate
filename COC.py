# -*- coding: UTF-8 -*-

# Filename : COC_Translate.py
# author by : 冰冰的大白兔
import re;
import sys;
from colorama import * ;
import time;
import os;

def Read():
    try:
        befSort = open('Translationtable.txt', mode='r',encoding='UTF-8')  #读取txt文件
    except FileNotFoundError:
        print("没有Translationtable.txt翻译表文件！")
        time.sleep(5)
        sys.exit(1)
    for line in befSort.readlines():  # 依次读取每行
        line = re.sub('[\W_]+','',line)  # 去掉每行头尾空白
        Sort.append(line)   #每一行读入列表成为列表元素
#    print(Sort)
    if len(Sort) == 0:
        time.sleep(5)
        sys.exit(1)
    Sort.sort(key = lambda i:len(i),reverse=True)  #将列表内元素按头排序
    for sortLine in Sort:   #逐元素打印列表
        print(sortLine)    #每一行为列表每一元素
    befSort.close() #关闭txt文件

def Write():
    writeSort = open('Translationtable.txt', mode='w',encoding='UTF-8')
    for writLine in Sort:
#        print(writLine)    #每一行为列表每一元素
        writeSort.write(writLine+'\n')
    writeSort.close()

def CutSort():
    m = re.compile("[a-zA-Z]+")#判断是否为字母
    for S in Sort:
        p = m.match(S)
        i = p.end()
        reSor.append(S[0:i])#分割
        reSor.append(S[i:])
#    print(reSor)

def translate():
    untrans = input('开始翻译，请输入需要翻译的字符串\n')  # 接收字符串
    untrans = re.sub('[\W_]+', '', untrans)  # 整理字符串
    j = 1  # 计数
    for j in range(0, len(reSor) - 1, 2):  # 替换字符串
        untrans = re.sub(reSor[j], reSor[j + 1], untrans,flags=re.IGNORECASE)#翻译替换
    print(f'{Fore.MAGENTA}'+f'{Style.BRIGHT}'+untrans)
    print(f'翻译完成{Style.RESET_ALL}')

#def menu():


if __name__ == "__main__":
    os.system("cls")
    print(f'{Fore.YELLOW}等待排序')
    Sort=[] #存储翻译表用的列表
    reSor = []  #翻译表切分
    Read()  #读取翻译表并排序
    Write() #复写排序后翻译表
#    menu()
    CutSort()
    print(f'排序完成{Style.RESET_ALL}')
    while 1 :
        translate()

