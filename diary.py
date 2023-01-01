# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys;
from sys import argv
from datetime import datetime
from PyQt5.QtCore import QTimer
import json 

'''with open('ToDoList.json') as todo :
    data = json.load(todo)'''

year = int(datetime.today().strftime("%Y"))
month = int(datetime.today().strftime("%m"))


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 1480, 760)
        self.setWindowTitle("diary")
        self.Fday = 0
        self.hour = 0
        self.day = 0
        self.initUI()

    def initUI(self):
        global year, month
        self.year = int(datetime.today().strftime("%Y"))
        self.month = int(datetime.today().strftime("%m"))
        self.num = []
        self.years = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 0 1 2 3 4 5 6 7 8 9 10 11 12
        self.lyears = [31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 0 1 2 3 4 5 6 7 8 9 10 11 12
        self.NTitle = [] 
        self.NDetail = [] 
        self.NDateTime = [] 

        if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
            self.T = 1
            self.T_s = self.lyears

        else:
            self.T = 0
            self.T_s = self.years

        self.T_storage = datetime(year=year, month=month, day=1, hour=1, minute=1, second=1)

        self.space = self.T_storage.isoweekday()

        for i in range(self.space - 1):
            self.num.append(str(self.T_s[month - 1] - (self.space - 1) + i + 1))

        for i in range(self.T_s[month]):
            self.num.append(str(i + 1))

        for i in range(10):
            self.num.append(str(i + 1))

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText("Monday")
        self.label_1.move(189, 100)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText("Tuesday")
        self.label_2.move(331, 100)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setText("Wednesday")
        self.label_3.move(473, 100)

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setText("Thursday")
        self.label_4.move(615, 100)

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setText("Friday")
        self.label_5.move(757, 100)

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setText("Saturday")
        self.label_6.move(899, 100)

        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setText("Sunday")
        self.label_7.move(1041, 100)

        self.label_Year = QtWidgets.QLabel(self)
        self.label_Year.setText(str(year))
        self.label_Year.move(585, 40)
        self.label_Year.setStyleSheet(''' font-size: 24px; ''')

        self.label_Month = QtWidgets.QLabel(self)
        self.label_Month.setText(str(month))
        self.label_Month.move(685, 40)
        self.label_Month.setStyleSheet(''' font-size: 24px; ''')

        self.label_list = QtWidgets.QLabel(self)
        self.label_list.setText("To do list")
        self.label_list.move(1250, 40)
        self.label_list.setStyleSheet(''' font-size: 24px; ''')

        self.BYear_up = QtWidgets.QPushButton(self)
        self.BYear_up.setGeometry(595, 10, 25, 25)
        self.BYear_up.setText("⬆")
        self.BYear_up.clicked.connect(self.BYear_up_Clicked)

        self.BMonth_up = QtWidgets.QPushButton(self)
        self.BMonth_up.setGeometry(685, 10, 25, 25)
        self.BMonth_up.setText("⬆")
        self.BMonth_up.clicked.connect(self.BMonth_up_Clicked)

        self.BYear_down = QtWidgets.QPushButton(self)
        self.BYear_down.setGeometry(595, 70, 25, 25)
        self.BYear_down.setText("⬇")
        self.BYear_down.clicked.connect(self.BYear_down_Clicked)

        self.BMonth_down = QtWidgets.QPushButton(self)
        self.BMonth_down.setGeometry(685, 70, 25, 25)
        self.BMonth_down.setText("⬇")
        self.BMonth_down.clicked.connect(self.BMonth_down_Clicked)

        self.B1 = QtWidgets.QPushButton(self)
        self.B1.setGeometry(142, 120, 142, 120)
        self.B1.setText(self.num[0])
        self.B1.clicked.connect(self.label_1Clicked)

        self.B2 = QtWidgets.QPushButton(self)
        self.B2.setGeometry(284, 120, 142, 120)
        self.B2.setText(self.num[1])
        self.B2.clicked.connect(self.label_2Clicked)

        self.B3 = QtWidgets.QPushButton(self)
        self.B3.setGeometry(426, 120, 142, 120)
        self.B3.setText(self.num[2])
        self.B3.clicked.connect(self.label_3Clicked)

        self.B4 = QtWidgets.QPushButton(self)
        self.B4.setGeometry(568, 120, 142, 120)
        self.B4.setText(self.num[3])
        self.B4.clicked.connect(self.label_4Clicked)

        self.B5 = QtWidgets.QPushButton(self)
        self.B5.setGeometry(710, 120, 142, 120)
        self.B5.setText(self.num[4])
        self.B5.clicked.connect(self.label_5Clicked)

        self.B6 = QtWidgets.QPushButton(self)
        self.B6.setGeometry(852, 120, 142, 120)
        self.B6.setText(self.num[5])
        self.B6.clicked.connect(self.label_6Clicked)

        self.B7 = QtWidgets.QPushButton(self)
        self.B7.setGeometry(994, 120, 142, 120)
        self.B7.setText(self.num[6])
        self.B7.clicked.connect(self.label_7Clicked)

        self.B8 = QtWidgets.QPushButton(self)
        self.B8.setGeometry(142, 240, 142, 120)
        self.B8.setText(self.num[7])
        self.B8.clicked.connect(self.label_8Clicked)

        self.B9 = QtWidgets.QPushButton(self)
        self.B9.setGeometry(284, 240, 142, 120)
        self.B9.setText(self.num[8])
        self.B9.clicked.connect(self.label_9Clicked)

        self.B10 = QtWidgets.QPushButton(self)
        self.B10.setGeometry(426, 240, 142, 120)
        self.B10.setText(self.num[9])
        self.B10.clicked.connect(self.label_10Clicked)

        self.B11 = QtWidgets.QPushButton(self)
        self.B11.setGeometry(568, 240, 142, 120)
        self.B11.setText(self.num[10])
        self.B11.clicked.connect(self.label_11Clicked)

        self.B12 = QtWidgets.QPushButton(self)
        self.B12.setGeometry(710, 240, 142, 120)
        self.B12.setText(self.num[11])
        self.B12.clicked.connect(self.label_12Clicked)

        self.B13 = QtWidgets.QPushButton(self)
        self.B13.setGeometry(852, 240, 142, 120)
        self.B13.setText(self.num[12])
        self.B13.clicked.connect(self.label_13Clicked)

        self.B14 = QtWidgets.QPushButton(self)
        self.B14.setGeometry(994, 240, 142, 120)
        self.B14.setText(self.num[13])
        self.B14.clicked.connect(self.label_14Clicked)

        self.B15 = QtWidgets.QPushButton(self)
        self.B15.setGeometry(142, 360, 142, 120)
        self.B15.setText(self.num[14])
        self.B15.clicked.connect(self.label_15Clicked)

        self.B16 = QtWidgets.QPushButton(self)
        self.B16.setGeometry(284, 360, 142, 120)
        self.B16.setText(self.num[15])
        self.B16.clicked.connect(self.label_16Clicked)

        self.B17 = QtWidgets.QPushButton(self)
        self.B17.setGeometry(426, 360, 142, 120)
        self.B17.setText(self.num[16])
        self.B17.clicked.connect(self.label_17Clicked)

        self.B18 = QtWidgets.QPushButton(self)
        self.B18.setGeometry(568, 360, 142, 120)
        self.B18.setText(self.num[17])
        self.B18.clicked.connect(self.label_18Clicked)

        self.B19 = QtWidgets.QPushButton(self)
        self.B19.setGeometry(710, 360, 142, 120)
        self.B19.setText(self.num[18])
        self.B19.clicked.connect(self.label_19Clicked)

        self.B20 = QtWidgets.QPushButton(self)
        self.B20.setGeometry(852, 360, 142, 120)
        self.B20.setText(self.num[19])
        self.B20.clicked.connect(self.label_20Clicked)

        self.B21 = QtWidgets.QPushButton(self)
        self.B21.setGeometry(994, 360, 142, 120)
        self.B21.setText(self.num[20])
        self.B21.clicked.connect(self.label_21Clicked)

        self.B22 = QtWidgets.QPushButton(self)
        self.B22.setGeometry(142, 480, 142, 120)
        self.B22.setText(self.num[21])
        self.B22.clicked.connect(self.label_22Clicked)

        self.B23 = QtWidgets.QPushButton(self)
        self.B23.setGeometry(284, 480, 142, 120)
        self.B23.setText(self.num[22])
        self.B23.clicked.connect(self.label_23Clicked)

        self.B24 = QtWidgets.QPushButton(self)
        self.B24.setGeometry(426, 480, 142, 120)
        self.B24.setText(self.num[23])
        self.B24.clicked.connect(self.label_24Clicked)

        self.B25 = QtWidgets.QPushButton(self)
        self.B25.setGeometry(568, 480, 142, 120)
        self.B25.setText(self.num[24])
        self.B25.clicked.connect(self.label_25Clicked)

        self.B26 = QtWidgets.QPushButton(self)
        self.B26.setGeometry(710, 480, 142, 120)
        self.B26.setText(self.num[25])
        self.B26.clicked.connect(self.label_26Clicked)

        self.B27 = QtWidgets.QPushButton(self)
        self.B27.setGeometry(852, 480, 142, 120)
        self.B27.setText(self.num[26])
        self.B27.clicked.connect(self.label_27Clicked)

        self.B28 = QtWidgets.QPushButton(self)
        self.B28.setGeometry(994, 480, 142, 120)
        self.B28.setText(self.num[27])
        self.B28.clicked.connect(self.label_28Clicked)

        self.B29 = QtWidgets.QPushButton(self)
        self.B29.setGeometry(142, 600, 142, 120)
        self.B29.setText(self.num[28])
        self.B29.clicked.connect(self.label_29Clicked)

        self.B30 = QtWidgets.QPushButton(self)
        self.B30.setGeometry(284, 600, 142, 120)
        self.B30.setText(self.num[29])
        self.B30.clicked.connect(self.label_30Clicked)

        self.B31 = QtWidgets.QPushButton(self)
        self.B31.setGeometry(426, 600, 142, 120)
        self.B31.setText(self.num[30])
        self.B31.clicked.connect(self.label_31Clicked)

        self.B32 = QtWidgets.QPushButton(self)
        self.B32.setGeometry(568, 600, 142, 120)
        self.B32.setText(self.num[31])
        self.B32.clicked.connect(self.label_32Clicked)

        self.B33 = QtWidgets.QPushButton(self)
        self.B33.setGeometry(710, 600, 142, 120)
        self.B33.setText(self.num[32])
        self.B33.clicked.connect(self.label_33Clicked)

        self.B34 = QtWidgets.QPushButton(self)
        self.B34.setGeometry(852, 600, 142, 120)
        self.B34.setText(self.num[33])
        self.B34.clicked.connect(self.label_34Clicked)

        self.B35 = QtWidgets.QPushButton(self)
        self.B35.setGeometry(994, 600, 142, 120)
        self.B35.setText(self.num[34])
        self.B35.clicked.connect(self.label_35Clicked)

        self.Start_year = QtWidgets.QLabel(self)
        self.Start_year.setText(str(self.year))
        self.Start_year.move(240, 100)
        self.Start_year.setStyleSheet(''' font-size: 24px; ''')

        self.Start_month = QtWidgets.QLabel(self)
        self.Start_month.setText(str(self.month))
        self.Start_month.move(360, 100)
        self.Start_month.setStyleSheet(''' font-size: 24px; ''')

        self.Start_day = QtWidgets.QLabel(self)
        self.Start_day.setText(str(self.day))
        self.Start_day.move(450, 100)
        self.Start_day.setStyleSheet(''' font-size: 24px; ''')

        self.Start_hour = QtWidgets.QLabel(self)
        self.Start_hour.setText(str(self.hour))
        self.Start_hour.move(560, 100)
        self.Start_hour.setStyleSheet(''' font-size: 24px; ''')

        self.Mlabel = QtWidgets.QLabel(self)
        self.Mlabel.setText("to")
        self.Mlabel.move(720, 100)
        self.Mlabel.setStyleSheet(''' font-size: 24px; ''')

        self.Start_hour_L = QtWidgets.QPushButton(self)
        self.Start_hour_L.setGeometry(530, 100, 25, 25)
        self.Start_hour_L.setText("⇦")
        self.Start_hour_L.clicked.connect(self.Start_hour_L_Clicked)

        self.Start_hour_R = QtWidgets.QPushButton(self)
        self.Start_hour_R.setGeometry(590, 100, 25, 25)
        self.Start_hour_R.setText("⇨")
        self.Start_hour_R.clicked.connect(self.Start_hour_R_Clicked)

        self.Start_year_L = QtWidgets.QPushButton(self)
        self.Start_year_L.setGeometry(210, 100, 25, 25)
        self.Start_year_L.setText("⇦")
        self.Start_year_L.clicked.connect(self.Start_year_L_Clicked)

        self.Start_year_R = QtWidgets.QPushButton(self)
        self.Start_year_R.setGeometry(295, 100, 25, 25)
        self.Start_year_R.setText("⇨")
        self.Start_year_R.clicked.connect(self.Start_year_R_Clicked)

        self.Start_month_L = QtWidgets.QPushButton(self)
        self.Start_month_L.setGeometry(330, 100, 25, 25)
        self.Start_month_L.setText("⇦")
        self.Start_month_L.clicked.connect(self.Start_month_L_Clicked)

        self.Start_month_R = QtWidgets.QPushButton(self)
        self.Start_month_R.setGeometry(390, 100, 25, 25)
        self.Start_month_R.setText("⇨")
        self.Start_month_R.clicked.connect(self.Start_month_R_Clicked)

        self.Start_day_L = QtWidgets.QPushButton(self)
        self.Start_day_L.setGeometry(420, 100, 25, 25)
        self.Start_day_L.setText("⇦")
        self.Start_day_L.clicked.connect(self.Start_day_L_Clicked)

        self.Start_day_R = QtWidgets.QPushButton(self)
        self.Start_day_R.setGeometry(480, 100, 25, 25)
        self.Start_day_R.setText("⇨")
        self.Start_day_R.clicked.connect(self.Start_day_R_Clicked)
        ############

        x = 640
        self.Fyear = self.year
        self.Fmonth = self.month
        self.Fhour = self.hour

        self.End_year = QtWidgets.QLabel(self)
        self.End_year.setText(str(self.Fyear))
        self.End_year.move(x + 240, 100)
        self.End_year.setStyleSheet(''' font-size: 24px; ''')

        self.End_month = QtWidgets.QLabel(self)
        self.End_month.setText(str(self.Fmonth))
        self.End_month.move(x + 360, 100)
        self.End_month.setStyleSheet(''' font-size: 24px; ''')

        self.End_day = QtWidgets.QLabel(self)
        self.End_day.setText(str(self.Fday))
        self.End_day.move(x + 450, 100)
        self.End_day.setStyleSheet(''' font-size: 24px; ''')

        self.End_hour = QtWidgets.QLabel(self)
        self.End_hour.setText(str(self.Fhour))
        self.End_hour.move(x + 560, 100)
        self.End_hour.setStyleSheet(''' font-size: 24px; ''')

        self.End_hour_L = QtWidgets.QPushButton(self)
        self.End_hour_L.setGeometry(x + 530, 100, 25, 25)
        self.End_hour_L.setText("⇦")
        self.End_hour_L.clicked.connect(self.End_hour_L_Clicked)

        self.End_hour_R = QtWidgets.QPushButton(self)
        self.End_hour_R.setGeometry(x + 590, 100, 25, 25)
        self.End_hour_R.setText("⇨")
        self.End_hour_R.clicked.connect(self.End_hour_R_Clicked)

        self.End_year_L = QtWidgets.QPushButton(self)
        self.End_year_L.setGeometry(x + 210, 100, 25, 25)
        self.End_year_L.setText("⇦")
        self.End_year_L.clicked.connect(self.End_year_L_Clicked)

        self.End_year_R = QtWidgets.QPushButton(self)
        self.End_year_R.setGeometry(x + 295, 100, 25, 25)
        self.End_year_R.setText("⇨")
        self.End_year_R.clicked.connect(self.End_year_R_Clicked)

        self.End_month_L = QtWidgets.QPushButton(self)
        self.End_month_L.setGeometry(x + 330, 100, 25, 25)
        self.End_month_L.setText("⇦")
        self.End_month_L.clicked.connect(self.End_month_L_Clicked)

        self.End_month_R = QtWidgets.QPushButton(self)
        self.End_month_R.setGeometry(x + 390, 100, 25, 25)
        self.End_month_R.setText("⇨")
        self.End_month_R.clicked.connect(self.End_month_R_Clicked)

        self.End_day_L = QtWidgets.QPushButton(self)
        self.End_day_L.setGeometry(x + 420, 100, 25, 25)
        self.End_day_L.setText("⇦")
        self.End_day_L.clicked.connect(self.End_day_L_Clicked)

        self.End_day_R = QtWidgets.QPushButton(self)
        self.End_day_R.setGeometry(x + 480, 100, 25, 25)
        self.End_day_R.setText("⇨")
        self.End_day_R.clicked.connect(self.End_day_R_Clicked)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(585, 150, 300, 40))
        self.lineEdit.setObjectName("lineEdit")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QtCore.QRect(240, 240, 1000, 400))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.LineTitle = QtWidgets.QLabel(self)
        self.LineTitle.setText("Title : ")
        self.LineTitle.move(425, 150)
        self.LineTitle.setStyleSheet(''' font-size: 24px; ''')

        self.detal = QtWidgets.QLabel(self)
        self.detal.setText("detal : ")
        self.detal.move(240, 200)
        self.detal.setStyleSheet(''' font-size: 24px; ''')

        self.Confirm = QtWidgets.QPushButton(self)
        self.Confirm.setGeometry(1345, 600, 70, 25)
        self.Confirm.setText("confirm")
        self.Confirm.clicked.connect(self.label_Confirm_Clicked)

        self.Cancel = QtWidgets.QPushButton(self)
        self.Cancel.setGeometry(1270, 600, 70, 25)
        self.Cancel.setText("cancel")
        self.Cancel.clicked.connect(self.label_Cancel_Clicked)

        
        self.ToDoList1 = QtWidgets.QPushButton(self)
        self.ToDoList1.setGeometry(1210, 120, 230, 95)
        self.showlist(1)
        self.ToDoList1.setText(self.w)

        self.ToDoList2 = QtWidgets.QPushButton(self)
        self.ToDoList2.setGeometry(1210, 220, 230, 95)
        self.showlist(2)
        self.ToDoList2.setText(self.w)

        self.ToDoList3 = QtWidgets.QPushButton(self)
        self.ToDoList3.setGeometry(1210, 320, 230, 95)
        self.showlist(3)
        self.ToDoList3.setText(self.w)

        self.ToDoList4 = QtWidgets.QPushButton(self)
        self.ToDoList4.setGeometry(1210, 420, 230, 95)
        self.showlist(4)
        self.ToDoList4.setText(self.w)

        self.ToDoList5 = QtWidgets.QPushButton(self)
        self.ToDoList5.setGeometry(1210, 520, 230, 95)
        self.showlist(5)
        self.ToDoList5.setText(self.w)

        self.ToDoList6 = QtWidgets.QPushButton(self)
        self.ToDoList6.setGeometry(1210, 620, 230, 95)
        self.showlist(6)
        self.ToDoList6.setText(self.w)

        #self.NTitle[i].clicked.connect(self.NTitle[i]_Clicked)
        self.all_button = [self.ToDoList1,self.ToDoList2,self.ToDoList3,self.ToDoList4,self.ToDoList5,self.ToDoList6] 

        self.lineEdit.hide()
        self.plainTextEdit.hide()
        self.LineTitle.hide()
        self.detal.hide()
        self.Confirm.hide()
        self.Cancel.hide()

        self.Start_year.hide()
        self.Start_day.hide()
        self.Start_month.hide()
        self.Start_hour.hide()
        self.Start_year_L.hide()
        self.Start_year_R.hide()
        self.Start_month_R.hide()
        self.Start_month_L.hide()
        self.Start_day_L.hide()
        self.Start_day_R.hide()
        self.Start_hour_L.hide()
        self.Start_hour_R.hide()

        self.End_year.hide()
        self.End_day.hide()
        self.End_month.hide()
        self.End_hour.hide()
        self.End_year_L.hide()
        self.End_year_R.hide()
        self.End_month_R.hide()
        self.End_month_L.hide()
        self.End_day_L.hide()
        self.End_day_R.hide()
        self.End_hour_L.hide()
        self.End_hour_R.hide()

        self.Mlabel.hide()

    def showlist(self,n):
        if len(self.NTitle) < n :
            self.w = ''
        else :
            print(n,self.NDateTime)
            self.w = str(self.NDateTime[n-1][0] + ':' + str(self.NDateTime[n-1][1]) + '\n' + str(self.NTitle[n-1]) )


    def WriteAll(self,Title,SdateTime,EdateTime,detail):

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




    def BYear_down_Clicked(self):
        self.year = int(self.year)
        self.year += 1
        self.label_Year.setText(str(self.year))
        self.T_storage = datetime(year=self.year, month=self.month, day=1, hour=1, minute=1, second=1)
        self.main(month)

    def BYear_up_Clicked(self):
        self.year = int(self.year)
        if self.year != 1:
            self.year -= 1 
            self.label_Year.setText(str(self.year))
            self.T_storage = datetime(year=self.year, month=self.month, day=1, hour=1, minute=1, second=1)
            self.main(month)

    def BMonth_down_Clicked(self):
        self.month = int(self.month)
        if self.month != 12:
            self.month += 1
            self.label_Month.setText(str(self.month))
            self.T_storage = datetime(year=self.year, month=self.month, day=1, hour=1, minute=1, second=1)
            self.main(month)

    def BMonth_up_Clicked(self):
        self.month = int(self.month)
        if self.month != 1:
            self.month -= 1
            self.label_Month.setText(str(self.month))
            self.T_storage = datetime(year=self.year, month=self.month, day=1, hour=1, minute=1, second=1)
            self.main(month)

    def Start_year_L_Clicked(self):
        self.year -= 1
        self.Start_year.setText(str(self.year))

    def Start_year_R_Clicked(self):
        self.year += 1
        self.Start_year.setText(str(self.year))

    def Start_month_L_Clicked(self):
        if self.month == 1:
            self.month = 12
        else:
            self.month -= 1
        self.Start_month.setText(str(self.month))

    def Start_month_R_Clicked(self):
        if self.month == 12:
            self.month = 1
        else:
            self.month = self.month + 1
        self.Start_month.setText(str(self.month))

    def Start_day_L_Clicked(self):
        if self.day == 1:
            self.day = self.lyears[self.month]
        else:
            self.day = int(self.day) - 1
        self.Start_day.setText(str(self.day))

    def Start_day_R_Clicked(self):
        if int(self.day) >= (self.lyears[self.month]):
            self.day = 1
        else:
            self.day = int(self.day) + 1
        self.Start_day.setText(str(self.day))

    def Start_hour_L_Clicked(self):
        if self.hour == 0:
            self.hour = 24
        else:
            self.hour -= 1
        self.Start_hour.setText(str(self.hour))

    def Start_hour_R_Clicked(self):
        if self.hour == 23:
            self.hour = 0
        else:
            self.hour += 1
        self.Start_hour.setText(str(self.hour))

    def End_year_L_Clicked(self):
        if self.Fyear != 0:
            self.Fyear -= 1
        self.End_year.setText(str(self.Fyear))

    def End_year_R_Clicked(self):
        self.Fyear += 1
        self.End_year.setText(str(self.Fyear))

    def End_month_R_Clicked(self):
        if self.Fmonth == 12:
            self.Fmonth = 1
        else:
            self.Fmonth = self.Fmonth + 1
        self.End_month.setText(str(self.Fmonth))

    def End_month_L_Clicked(self):
        if self.Fmonth == 1:
            self.Fmonth = 12
        else:
            self.Fmonth -= 1
        self.End_month.setText(str(self.Fmonth))

    def End_day_L_Clicked(self):
        if self.Fday == 1:
            self.Fday = self.lyears[self.month]
        else:
            self.Fday = int(self.Fday) - 1
        self.End_day.setText(str(self.Fday))

    def End_day_R_Clicked(self):
        if int(self.Fday) >= (self.lyears[self.month]):
            self.Fday = 1
        else:
            self.Fday = int(self.Fday) + 1
        self.End_day.setText(str(self.Fday))

    def End_hour_L_Clicked(self):
        if self.Fhour == 0:
            self.Fhour = 24
        else:
            self.Fhour -= 1
        self.End_hour.setText(str(self.Fhour))

    def End_hour_R_Clicked(self):
        if self.Fhour == 23:
            self.Fhour = 0
        else:
            self.Fhour += 1
        self.End_hour.setText(str(self.Fhour))

    def label_Confirm_Clicked(self):
        self.ShowMain(0)
        Title = str(self.lineEdit.text())
        detal = str(self.plainTextEdit.toPlainText())

        Fyear = str(self.Fyear) 
        year = str(self.year)

        if int(self.month) < 10 :
            month = '0' + str(self.month)
        else:
            month = str(self.month)

        if int(self.Fmonth) < 10 :
            Fmonth = '0' + str(self.Fmonth)
        else :
            Fmonth = str(self.Fmonth)

        if int(self.day) < 10 :
            day = '0' + str(self.day)
        else:
            day = str(self.day)

        if int(self.Fday) < 10 :
            Fday = '0' + str(self.Fday)
        else:
            Fday = str(self.Fday)

        if int(self.hour) < 10:
            hour = '0' + str(self.hour)
        else :
            hour = str(self.hour)

        if int(self.Fhour) < 10 :
            Fhour = '0' + str(self.Fhour)
        else :
            Fhour = str(self.Fhour)

        S = str(year) + str(month) + str(day) + str(hour) 
        E = str(Fyear) + str(Fmonth) + str(Fday) + str(Fhour)

        self.WriteAll(Title,S,E,detal)
        self.lineEdit.clear()
        self.plainTextEdit.clear()

        
        for i in range(6):
            self.showlist(i+1)
            self.all_button[i].setText(self.w)
        
        
    def label_Cancel_Clicked(self):
        self.ShowMain(0)
        self.plainTextEdit.clear()
        self.lineEdit.clear()
        
    def main(self, month):
        self.num = []
        if (int(self.year) % 4) == 0 and (int(self.year) % 100) != 0 or (int(self.year) % 400) == 0:
            self.T = 1
            self.T_s = self.lyears
        else:
            self.T = 0
            self.T_s = self.years
        self.T_storage = datetime(year=int(self.year), month=int(self.month), day=1, hour=1, minute=1, second=1)
        self.space = self.T_storage.isoweekday()
        for i in range(self.space - 1):
            self.num.append(str(self.T_s[month - 1] - (self.space - 1) + i + 1))
        for i in range(self.T_s[month]):
            self.num.append(str(i + 1))
        for i in range(10):
            self.num.append(str(i + 1))
        self.run()

    def run(self):
        self.B1.setText(self.num[0])
        self.B2.setText(self.num[1])
        self.B3.setText(self.num[2])
        self.B4.setText(self.num[3])
        self.B5.setText(self.num[4])
        self.B6.setText(self.num[5])
        self.B7.setText(self.num[6])
        self.B8.setText(self.num[7])
        self.B9.setText(self.num[8])
        self.B10.setText(self.num[9])
        self.B11.setText(self.num[10])
        self.B12.setText(self.num[11])
        self.B13.setText(self.num[12])
        self.B14.setText(self.num[13])
        self.B15.setText(self.num[14])
        self.B16.setText(self.num[15])
        self.B17.setText(self.num[16])
        self.B18.setText(self.num[17])
        self.B19.setText(self.num[18])
        self.B20.setText(self.num[19])
        self.B21.setText(self.num[20])
        self.B22.setText(self.num[21])
        self.B23.setText(self.num[22])
        self.B24.setText(self.num[23])
        self.B25.setText(self.num[24])
        self.B26.setText(self.num[25])
        self.B27.setText(self.num[26])
        self.B28.setText(self.num[27])
        self.B29.setText(self.num[28])
        self.B30.setText(self.num[29])
        self.B31.setText(self.num[30])
        self.B32.setText(self.num[31])
        self.B33.setText(self.num[32])
        self.B34.setText(self.num[33])
        self.B35.setText(self.num[34])

    def changeMonth(self):
        self.Start_month.setText(str(self.month))
        self.Fmonth = self.month
        self.End_month.setText(str(self.Fmonth))

    def label_1Clicked(self):  # 可刪除num參數
        self.HideMain(self.num[0])
        self.Start_day.setText(str(self.num[0]))
        self.End_day.setText(str(self.num[0]))
        self.Fday = self.day = self.num[0]
        self.changeMonth()

    def label_2Clicked(self):
        self.HideMain(self.num[1])
        self.Start_day.setText(str(self.num[1]))
        self.End_day.setText(str(self.num[1]))
        self.Fday = self.day = self.num[1]
        self.changeMonth()

    def label_3Clicked(self):
        self.HideMain(self.num[2])
        self.Start_day.setText(str(self.num[2]))
        self.End_day.setText(str(self.num[2]))
        self.Fday = self.day = self.num[2]
        self.changeMonth()

    def label_4Clicked(self):
        self.HideMain(self.num[3])
        self.Start_day.setText(str(self.num[3]))
        self.End_day.setText(str(self.num[3]))
        self.Fday = self.day = self.num[3]
        self.changeMonth()

    def label_5Clicked(self):
        self.HideMain(self.num[4])
        self.Start_day.setText(str(self.num[4]))
        self.End_day.setText(str(self.num[4]))
        self.Fday = self.day = self.num[4]
        self.changeMonth()

    def label_6Clicked(self):
        self.HideMain(self.num[5])
        self.Start_day.setText(str(self.num[5]))
        self.End_day.setText(str(self.num[5]))
        self.Fday = self.day = self.num[5]
        self.changeMonth()

    def label_7Clicked(self):
        self.HideMain(self.num[6])
        self.Start_day.setText(str(self.num[6]))
        self.End_day.setText(str(self.num[6]))
        self.Fday = self.day = self.num[6]
        self.changeMonth()

    def label_8Clicked(self):
        self.HideMain(self.num[7])
        self.Start_day.setText(str(self.num[7]))
        self.End_day.setText(str(self.num[7]))
        self.Fday = self.day = self.num[7]
        self.changeMonth()

    def label_9Clicked(self):
        self.HideMain(self.num[8])
        self.Start_day.setText(str(self.num[8]))
        self.End_day.setText(str(self.num[8]))
        self.Fday = self.day = self.num[8]
        self.changeMonth()

    def label_10Clicked(self):
        self.HideMain(self.num[9])
        self.Start_day.setText(str(self.num[9]))
        self.End_day.setText(str(self.num[9]))
        self.Fday = self.day = self.num[9]
        self.changeMonth()

    def label_11Clicked(self):
        self.HideMain(self.num[10])
        self.Start_day.setText(str(self.num[10]))
        self.End_day.setText(str(self.num[10]))
        self.Fday = self.day = self.num[10]
        self.changeMonth()

    def label_12Clicked(self):
        self.HideMain(self.num[11])
        self.Start_day.setText(str(self.num[11]))
        self.End_day.setText(str(self.num[11]))
        self.Fday = self.day = self.num[11]
        self.changeMonth()

    def label_13Clicked(self):
        self.HideMain(self.num[12])
        self.Start_day.setText(str(self.num[12]))
        self.End_day.setText(str(self.num[12]))
        self.Fday = self.day = self.num[12]
        self.changeMonth()

    def label_14Clicked(self):
        self.HideMain(self.num[13])
        self.Start_day.setText(str(self.num[13]))
        self.End_day.setText(str(self.num[13]))
        self.Fday = self.day = self.num[13]
        self.changeMonth()

    def label_15Clicked(self):
        self.HideMain(self.num[14])
        self.Start_day.setText(str(self.num[14]))
        self.End_day.setText(str(self.num[14]))
        self.Fday = self.day = self.num[14]
        self.changeMonth()

    def label_16Clicked(self):
        self.HideMain(self.num[15])
        self.Start_day.setText(str(self.num[15]))
        self.End_day.setText(str(self.num[15]))
        self.Fday = self.day = self.num[15]
        self.changeMonth()

    def label_17Clicked(self):
        self.HideMain(self.num[16])
        self.Start_day.setText(str(self.num[16]))
        self.End_day.setText(str(self.num[16]))
        self.Fday = self.day = self.num[16]
        self.changeMonth()

    def label_18Clicked(self):
        self.HideMain(self.num[17])
        self.Start_day.setText(str(self.num[17]))
        self.End_day.setText(str(self.num[17]))
        self.Fday = self.day = self.num[17]
        self.changeMonth()

    def label_19Clicked(self):
        self.HideMain(self.num[18])
        self.Start_day.setText(str(self.num[18]))
        self.End_day.setText(str(self.num[18]))
        self.Fday = self.day = self.num[18]
        self.changeMonth()

    def label_20Clicked(self):
        self.HideMain(self.num[19])
        self.Start_day.setText(str(self.num[19]))
        self.End_day.setText(str(self.num[19]))
        self.Fday = self.day = self.num[19]
        self.changeMonth()

    def label_21Clicked(self):
        self.HideMain(self.num[20])
        self.Start_day.setText(str(self.num[20]))
        self.End_day.setText(str(self.num[20]))
        self.Fday = self.day = self.num[20]
        self.changeMonth()

    def label_22Clicked(self):
        self.HideMain(self.num[21])
        self.Start_day.setText(str(self.num[21]))
        self.End_day.setText(str(self.num[21]))
        self.Fday = self.day = self.num[21]
        self.changeMonth()

    def label_23Clicked(self):
        self.HideMain(self.num[22])
        self.Start_day.setText(str(self.num[22]))
        self.End_day.setText(str(self.num[22]))
        self.Fday = self.day = self.num[22]
        self.changeMonth()

    def label_24Clicked(self):
        self.HideMain(self.num[23])
        self.Start_day.setText(str(self.num[23]))
        self.End_day.setText(str(self.num[23]))
        self.Fday = self.day = self.num[23]
        self.changeMonth()

    def label_25Clicked(self):
        self.HideMain(self.num[24])
        self.Start_day.setText(str(self.num[24]))
        self.End_day.setText(str(self.num[24]))
        self.Fday = self.day = self.num[24]
        self.changeMonth()

    def label_26Clicked(self):
        self.HideMain(self.num[25])
        self.Start_day.setText(str(self.num[25]))
        self.End_day.setText(str(self.num[25]))
        self.Fday = self.day = self.num[25]
        self.changeMonth()

    def label_27Clicked(self):
        self.HideMain(self.num[26])
        self.Start_day.setText(str(self.num[26]))
        self.End_day.setText(str(self.num[26]))
        self.Fday = self.day = self.num[26]
        self.changeMonth()

    def label_28Clicked(self):
        self.HideMain(self.num[27])
        self.Start_day.setText(str(self.num[27]))
        self.End_day.setText(str(self.num[27]))
        self.Fday = self.day = self.num[27]
        self.changeMonth()

    def label_29Clicked(self):
        self.HideMain(self.num[28])
        self.Start_day.setText(str(self.num[28]))
        self.End_day.setText(str(self.num[28]))
        self.Fday = self.day = self.num[28]
        self.changeMonth()

    def label_30Clicked(self):
        self.HideMain(self.num[29])
        self.Start_day.setText(str(self.num[29]))
        self.End_day.setText(str(self.num[29]))
        self.Fday = self.day = self.num[29]
        self.changeMonth()

    def label_31Clicked(self):
        self.HideMain(self.num[30])
        self.Start_day.setText(str(self.num[30]))
        self.End_day.setText(str(self.num[30]))
        self.Fday = self.day = self.num[30]
        self.changeMonth()

    def label_32Clicked(self):
        self.HideMain(self.num[31])
        self.Start_day.setText(str(self.num[31]))
        self.End_day.setText(str(self.num[31]))
        self.Fday = self.day = self.num[31]
        self.changeMonth()

    def label_33Clicked(self):
        self.HideMain(self.num[32])
        self.Start_day.setText(str(self.num[32]))
        self.End_day.setText(str(self.num[32]))
        self.Fday = self.day = self.num[32]
        self.changeMonth()

    def label_34Clicked(self):
        self.HideMain(self.num[33])
        self.Start_day.setText(str(self.num[33]))
        self.End_day.setText(str(self.num[33]))
        self.Fday = self.day = self.num[33]
        self.changeMonth()

    def label_35Clicked(self):
        self.HideMain(self.num[34])
        self.Start_day.setText(str(self.num[34]))
        self.End_day.setText(str(self.num[34]))
        self.Fday = self.day = self.num[34]
        self.changeMonth()

    def HideMain(self, day):
        self.B1.hide()
        self.B2.hide()
        self.B3.hide()
        self.B4.hide()
        self.B5.hide()
        self.B6.hide()
        self.B7.hide()
        self.B8.hide()
        self.B9.hide()
        self.B10.hide()
        self.B11.hide()
        self.B12.hide()
        self.B13.hide()
        self.B14.hide()
        self.B15.hide()
        self.B16.hide()
        self.B17.hide()
        self.B18.hide()
        self.B19.hide()
        self.B20.hide()
        self.B21.hide()
        self.B22.hide()
        self.B23.hide()
        self.B24.hide()
        self.B25.hide()
        self.B26.hide()
        self.B27.hide()
        self.B28.hide()
        self.B29.hide()
        self.B30.hide()
        self.B31.hide()
        self.B32.hide()
        self.B33.hide()
        self.B34.hide()
        self.B35.hide()
        self.label_1.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_Year.hide()
        self.label_Month.hide()
        self.label_list.hide()
        self.BYear_up.hide()
        self.BYear_down.hide()
        self.BMonth_down.hide()
        self.BMonth_up.hide()
        for i in self.all_button:
            i.hide()

        self.Start_month_L.show()
        self.Start_month_R.show()
        self.Start_year.show()
        self.Start_day.show()
        self.Start_month.show()
        self.Start_year_L.show()
        self.Start_year_R.show()
        self.Start_hour.show()
        self.Start_day_L.show()
        self.Start_day_R.show()
        self.Start_hour_L.show()
        self.Start_hour_R.show()
        self.Mlabel.show()

        self.End_year.show()
        self.End_day.show()
        self.End_month.show()
        self.End_hour.show()
        self.End_year_L.show()
        self.End_year_R.show()
        self.End_month_R.show()
        self.End_month_L.show()
        self.End_day_L.show()
        self.End_day_R.show()
        self.End_hour_L.show()
        self.End_hour_R.show()

        self.lineEdit.show()
        self.plainTextEdit.show()
        self.LineTitle.show()
        self.detal.show()
        self.Confirm.show()
        self.Cancel.show()

    def ShowMain(self, day):
        self.B1.show()
        self.B2.show()
        self.B3.show()
        self.B4.show()
        self.B5.show()
        self.B6.show()
        self.B7.show()
        self.B8.show()
        self.B9.show()
        self.B10.show()
        self.B11.show()
        self.B12.show()
        self.B13.show()
        self.B14.show()
        self.B15.show()
        self.B16.show()
        self.B17.show()
        self.B18.show()
        self.B19.show()
        self.B20.show()
        self.B21.show()
        self.B22.show()
        self.B23.show()
        self.B24.show()
        self.B25.show()
        self.B26.show()
        self.B27.show()
        self.B28.show()
        self.B29.show()
        self.B30.show()
        self.B31.show()
        self.B32.show()
        self.B33.show()
        self.B34.show()
        self.B35.show()
        self.label_1.show()
        self.label_2.show()
        self.label_3.show()
        self.label_4.show()
        self.label_5.show()
        self.label_6.show()
        self.label_7.show()
        self.label_Year.show()
        self.label_Month.show()
        self.label_list.show()
        self.BYear_up.show()
        self.BYear_down.show()
        self.BMonth_down.show()
        self.BMonth_up.show()
        for i in self.all_button:
            i.show()


        self.Start_month_L.hide()
        self.Start_month_R.hide()
        self.Start_year.hide()
        self.Start_day.hide()
        self.Start_month.hide()
        self.Start_year_L.hide()
        self.Start_year_R.hide()
        self.Start_hour.hide()
        self.Start_day_L.hide()
        self.Start_day_R.hide()
        self.Start_hour_L.hide()
        self.Start_hour_R.hide()
        self.Mlabel.hide()

        self.End_year.hide()
        self.End_day.hide()
        self.End_month.hide()
        self.End_hour.hide()
        self.End_year_L.hide()
        self.End_year_R.hide()
        self.End_month_R.hide()
        self.End_month_L.hide()
        self.End_day_L.hide()
        self.End_day_R.hide()
        self.End_hour_L.hide()
        self.End_hour_R.hide()

        self.lineEdit.hide()
        self.plainTextEdit.hide()
        self.LineTitle.hide()
        self.detal.hide()
        self.Confirm.hide()
        self.Cancel.hide()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
