import os
import random
with open('/Users/tcy/code/dicty/3500words.txt','r',encoding='UTF-8-sig') as file:
    content = file.read()
dicty = {}
dataList = []   #已记录单词列表
keyList = []    #全局已保存单词的key
freqList = []   #词频列表
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
    global freqList 
    dataList = []
    with open('/Users/tcy/code/dicty/data.txt','r+',encoding='UTF-8-sig') as file:
        data = file.readlines()
    # print(data)
    if len(data) != 0:
        for i in data[0].split(','):
            if i != '':
                dataList.append(int(i))
    if len(data) >= 2:
        for i in data[1].split(','):
            if i != '':
                freqList.append(int(i))
    print(freqList)
    print(dataList)
    # print(keyList)
    
def clear():
    os.system('clear')

def review():
    count = 0
    global keyList
    global dataList_tem
    global keyList_tem
    global showlist
    keyList_tem = []
    dataList_tem = []
    keyList = []
    for i in range(len(dataList)):
        keyList.append(list(dicty.keys())[dataList[i]])
    
    while True:
        try:
            fre = int(input("请输入需要查看的等级(默认为5):"))
            if fre >= 0 and fre <= 9:
                break
        except:
            continue
    #接口
    # showlist = random.sample([i for i in range(0,len(dataList))],len(dataList))
    showlist = choose(len(dataList),fre)
    # print(showlist)
    
    for i in showlist:
        word = keyList[i]
        count += 1
        dataList_tem.append(dataList[i])
        keyList_tem.append(word)
        print("%-15s\t"%(str(count)+'.'+word),end='')
        if count % 5 == 0:
            print()
        if count == 10:
            count = 0
            break

    while True:
        print()
        print("{:-^50s}".format(''))
        print("1.查询释义\t2.标记单词\t3.退出")
        print("{:-^50s}".format(''))
        try:
            chos1 = int(input("请选择下一步操作(1/2/3):"))
            if chos1 == 1:
                search()
                input("继续")
            elif chos1 == 2:
                markfreq()
                input("继续")
            elif chos1 == 3:
                break
        except:
            print("Error")
            print()
            continue

def search():
    global showList_re
    while True:
        chos = list(input("请选择需要查看释义的单词(词前序号):").split())
        if len(chos) != 0:
            for i in chos:
                try:
                    print(dicty[keyList_tem[int(i)-1]]) 
                    print()
                except:
                    print("包含非法输入")
                    break
        else:
            break

def markfreq():
    global freqList
    global dataList_tem
    global keyList
    global keyList_tem
    global showlist
    print("-a:提升等级\t-d:降低等级(默认为提升)")
    while True:
        chos = list(input("请选择需要标记的单词(词前序号):").split())
        if len(chos) == 0:
            break
        if len(chos) >= 1:
            if chos[-1] == "-a" or chos[-1] == "-d":
                com = chos[-1]
                chos.pop()
            else:
                com = "-a"
            for i in chos:
                try:
                    print(keyList_tem[int(i)-1])
                    print(dicty[keyList_tem[int(i)-1]]) 
                    print()
                    if com == "-a":
                        freqList[showlist[int(i)-1]] += 1
                    elif com == "-d":
                        freqList[showlist[int(i)-1]] -= 1
                except:
                    print("包含非法输入")
                    break
        else:
            continue

def addNew():
    count = 0
    showList = [] #储存显示的单词编号
    global freqList
    global dataList
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
    #写入datalist
    if len(showList) != 0:
        while True:
            chos = list(input("请选择需要记录的单词(词前序号):").split())
            if len(chos) != 0:
                for i in chos:
                    try:
                        dataList.append(showList[int(i)-1])
                        freqList.append(5)
                    except:
                        print("包含非法输入")
                        break
                print (dataList)
            else:
                break
    else:
        print("无")

def writein():
    global dataList
    global freqList
    print("正在保存...")
    with open('/Users/tcy/code/dicty/data.txt','r+',encoding='UTF-8-sig') as file:
        for i in dataList:
            file.write(","+str(i))
        file.write("\n")
        for i in freqList:
            file.write(","+str(i))
            
        print("保存成功")
        # print(freqList)
def choose(length,fre):
    global keyList
    global dataList
    global freqList
    choiList = []
    for i in range(len(freqList)):
        if freqList[i] == int(fre):
            choiList.append(i)
    random.shuffle(choiList)
    if len(choiList) >= length:
        return random.sample(choiList,length)
    else:
        return random.sample(choiList,len(choiList))

def main():
    global dataList
    global freqList
    while True:
        print("已保存%d个单词"%(len(dataList)))
        print("{:-^50s}".format(''))
        print("1.复习\t2.浏览新单词\t3.退出")
        print("{:-^50s}".format(''))
        try:
            chos1 = int(input("请选择下一步操作(1/2/3):"))
            if chos1 == 1:
                clear()
                review()
                clear()
                input("继续")
            elif chos1 == 2:
                clear()
                addNew()
                clear()
                input("继续")
            elif chos1 == 3:
                clear()
                writein()
                break
        except:
            print("Error")
            print()
            continue

clear()
init()
print("正在初始化...")
main()