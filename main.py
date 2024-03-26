import mysql.connector as sqltor
import csv
import requests
import os
import cv2
import numpy as np
import face_recognition
from datetime import datetime

mycon = sqltor.connect(host='localhost',user='root',passwd='<your passwd>',database='<your db name>')
cursor=mycon.cursor()

if mycon.is_connected():
    print("Succesfully connected to mysql database")

#create table
try:
    cursor.execute("create table info(id int,force_no int(20),name varchar(20),age int,INOUT_resident varchar(20),Address varchar(50))")
    # print("Table created successfully")
except:
    cursor.execute("drop table info")
    # print("Table deleted Successfully")
    cursor.execute("create table info(id int,force_no int(20),name varchar(20),age int,INOUT_resident varchar(20),Address varchar(50))")
    # print("Table created successfully")

#Opened csv file
with open("<your path .fd1.csv>",'r') as nf:
    x=csv.reader(nf)
    lis=[]
    line=0
    data=[]
    for row in x:
        if line==0:
            pass
        else:
            # print(row)
            lis.append([int(row[4]),row[2],int(row[3]),row[6],row[5]])
            data.append({"name":row[2],"url":row[7]})
        line+=1


def download_image():
    os.chdir("<folder of images path/Images>")
    for y in data:
        res=requests.get(y["url"])
        name=y["name"]
        file = open(f'{name}.png','wb')
        file.write(res.content)
        file.close()

def display():
    cursor.execute("Select * from info")
    x=cursor.fetchall()
    for i in x:
        print(i)

def insert_values(coun,force_no,name,age,i_o,address):
    cursor.execute("Insert into info values({},{},'{}',{},'{}','{}')".format(coun,force_no,name,age,i_o,address))
    # print("Data added succesfully")


def lst_in_o():
    print("Inside campus residents!")
    cursor.execute("select * from info where INOUT_resident = 'In Campus'")
    for k in cursor.fetchall():
        print(k)
        
    print("Outside campus residents!")
    cursor.execute("select * from info where INOUT_resident = 'Outside Campus'")
    for j in cursor.fetchall():
        print(j)

def display_data():
    c=int(input("Enter your id number: "))
    st="Select * from info where force_no={}".format(c)
    cursor.execute(st)
    for j in cursor.fetchall():
        print(j)

count=1
for i in lis:
    # print(i)
    force=i[0]
    nam=i[1]
    ag=i[2]
    i_0=i[3]
    ad=i[4]
    insert_values(count,force,nam,ag,i_0,ad)
    mycon.commit()
    count+=1
# download_image()
print("Images downloaded successfully")
display()
lst_in_o()
# mycon.close()


path = 'R:\\Python\\Database_\\Images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    with open("R:\\Python\\Database_\\Main\\Attendence.csv", 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines("\n")
            f.writelines(f'{name},{dtString}')

encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if faceDis[matchIndex]< 0.50:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)
            cursor.execute("select * from info where name = '{}'".format(name))
            for d in cursor.fetchall():
                print(d)
                break
            # print(name)
        else:
            name = 'Unknown'
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            # markAttendance((name))

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
