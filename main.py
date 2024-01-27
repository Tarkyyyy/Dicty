import json
import time
import os
import random
with open('/Users/tcy/code/dicty/3500words.txt','r',encoding='UTF-8-sig') as file:
    content = file.read()
dicty = {}
dataList = []
keyList = []
# print(content)
print("{:-^50s}".format(''))
for line in content.split("\n"):
    if line:
        key,value = line.split('：')
        # print(key,value)
        dicty[key] = value
# print(dicty)
print("词库获取成功")
#初始化
def init():
    global dataList
    global keyList  #全局已保存单词的key
    dataList = []
    keyList = []
    with open('/Users/tcy/code/dicty/data.txt','r+',encoding='UTF-8-sig') as file:
        data = file.readline()
    # print(data)
    for i in data.split(','):
        if i != '':
            dataList.append(int(i))
    # print(dataList)
    for i in range(len(dataList)):
        keyList.append(list(dicty.keys())[dataList[i]])
    # print(keyList)
    
def clear():
    os.system('clear')

def review():
    count = 0
    snum = 0
    showList = []
    for i in keyList:
        count += 1
        showList.append(i)
        print("%-15s\t"%(str(count)+'.'+i),end='')
        if count % 5 == 0:
            print()
        snum += 1
    print()
    print("{:-^50s}".format(''))
    while True:
        chos = list(input("请选择需要查看释义的单词(词前序号):").split())
        if len(chos) != 0:
            for i in chos:
                try:
                    print(dicty[showList[int(i)-1]]) 
                    print()
                except:
                    print("包含非法输入")
                    break
        else:
            break

def addNew():
    count = 0
    showList = []
    writeList = []
    for i in range(10):
        ranum = random.randint(0,len(dicty))
        word = list(dicty.keys())[ranum]
        if word not in keyList:
            count += 1
            print("%-15s\t"%(str(count)+'.'+word),end='')
            showList.append(ranum)
            if count % 5 == 0:
                print()
            if count == 10:
                count = 0
                break
    # print(showList)
    print()
    print("{:-^50s}".format(''))
    if len(showList) != 0:
        while True:
            chos = list(input("请选择需要记录的单词(词前序号):").split())
            if len(chos) != 0:
                for i in chos:
                    try:
                        writeList.append(showList[int(i)-1])
                    except:
                        print("包含非法输入")
                        break
                print (writeList)
                with open('/Users/tcy/code/dicty/data.txt','a+',encoding='UTF-8-sig') as file:
                    for i in writeList:
                        file.write(","+str(i))
                        print("保存成功")
            else:
                break
    else:
        print("无")

def main():
    while True:
        init()
        print("已保存%d个单词"%(len(dataList)))
        print("{:-^50s}".format(''))
        print("1.复习\t2.浏览新单词\t3.退出")
        print("{:-^50s}".format(''))
        chos1 = int(input("请选择下一步操作(1/2/3):"))
        if chos1 == 1:
            clear()
            review()
            input("继续")
        elif chos1 == 2:
            clear()
            addNew()
            input("继续")
        elif chos1 == 3:
            break
        else:
            print("Error")
        

print("正在初始化...")
main()