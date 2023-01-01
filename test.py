def WriteAll(self,Title,SdateTime,EdateTime,detail):
    #f = open('Title.txt','r+')
    #f = open('date_time.txt', 'r+')
    #f = open('Date_time.txt', 'w', encoding = 'UTF-8')
    #for i in f.readlines():

    if SdateTime > EdateTime :
        a = SdateTime 
        SdateTime = EdateTime 
        EdateTime = a 

    f = open('Date_time.txt', 'r')
    now = [] 
    for i in f.readlines():
        now.append(i)
    print(now)
    writed = False

    for i in range(0,len(now),2) :
        if int(EdateTime) < int(now[i+1]) :
            print(int(now[i+1]))
            now.insert(i,SdateTime+'\n')
            now.insert(i+1,EdateTime+'\n')
            place = i // 2  
            writed = True
            break

    if writed == False :
        now.append(SdateTime+'\n')
        now.append(EdateTime+'\n')

    self.NDateTime = [] ;  Tstorage = [] 
    for i in range(len(now)):
        if i % 2 == 0 : 
            Tstorage.append(now[i])
        else :
            Tstorage.append(now[i])
            self.NDateTime.append(Tstorage)
            Tstorage = []

    
    f.close()
    f = open('Date_time.txt','w', encoding = 'UTF-8')

    for i in now :
        f.write(i)
    f.close()

    f = open('Title.txt','r')
    now = [] 
    for i in f.readlines():
        now.append(i)
    if writed == False :
        now.append(Title+'\n')
    else:
        now.insert(place,Title+'\n')
    f.close()

    self.NTitle = []
    for i in now :
        self.NTitle.append(i)



    f = open('Title.txt','w', encoding = 'UTF-8')
    for i in now :
        f.write(i)
    f.close()

    f = open('Detail.txt','r')
    now = [] ; T_detail = ""
    words = f.read()
    for i in words :
        if i != "├" :
            T_detail += i 
        else:
            now.append(T_detail)
            T_detail = ""
    if writed == False :
        now.append(detail)
    else :
        now.insert(place,detail)
    f.close()

    self.NDetail = []
    for i in now :
        self.NDetail.append(i)

    f = open('Detail.txt','w', encoding = 'UTF-8')
    print(now)
    for i in now :
        f.write(i+'├')
    f.close()


def DeleteStroke(self,place):

    del self.NDateTime[place]
    del self.NDetail[place]
    del self.NTitle[place]

    f = open('Date_time.txt', 'w', encoding = 'UTF-8')
    for i in self.NDateTime :
        for j in i :
            f.write(j)
    f.close()

    f = open('Title.txt','w',encoding = 'UTF-8')
    for i in self.NTitle :
        f.write(i)
    f.close()

    f = open('Detail.txt','w',encoding = 'UTF-8')
    for i in self.NDetail:
        f.write(i+'├')
    f.close()