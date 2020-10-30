# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:59:06 2020

@author: Mayank$AGGARWAL
"""
import csv
import re
def clean(tweet):
    return ' '.join(re.sub("(@+|(\w+:\/\/\S+))|(#[A-Za-z0-9_+]+)|(&amp)|(http[A-Za-z0-9_+]+)", " ", tweet).split())
def cleanpunc(tweet):
    return ' '.join(re.sub("([-`,/])|([_'! * ?:%&;|¦~<>=])", " ", tweet).split())
def correctdot(tweet):
    return ' '.join(re.sub("([.])", ". ", tweet).split())

january=['03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
february=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','22']

for i in january:
    write_objaap=open( r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\\cleanaap.csv","w",encoding='utf-8',newline='')
    csv_writeraap=csv.writer(write_objaap)
    write_objbjp=open( r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\\cleanbjp.csv","w",encoding='utf-8',newline='')
    csv_writerbjp=csv.writer(write_objbjp)
    write_objinc=open( r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\\cleaninc.csv","w",encoding='utf-8',newline='')
    csv_writerinc=csv.writer(write_objinc)
    with open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\\aap.csv", 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            thestring = row[2]
            URLless_string = correctdot(cleanpunc(clean(thestring)))
            row[2]=URLless_string
            csv_writeraap.writerow(row)
    with open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\\bjp.csv", 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            thestring = row[2]
            URLless_string = correctdot(cleanpunc(clean(thestring)))
            row[2]=URLless_string
            csv_writerbjp.writerow(row)
    with open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\\inc.csv", 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            thestring = row[2]
            URLless_string = correctdot(cleanpunc(clean(thestring)))
            row[2]=URLless_string
            csv_writerinc.writerow(row)
    
for i in february:
    write_objaap=open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\\cleanaap.csv","w",encoding='utf-8',newline='')
    csv_writeraap=csv.writer(write_objaap)
    write_objbjp=open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\\cleanbjp.csv","w",encoding='utf-8',newline='')
    csv_writerbjp=csv.writer(write_objbjp)
    write_objinc=open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\\cleaninc.csv","w",encoding='utf-8',newline='')
    csv_writerinc=csv.writer(write_objinc)
    with open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\\aap.csv", 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            thestring = row[2]
            URLless_string = correctdot(cleanpunc(clean(thestring)))
            row[2]=URLless_string
            csv_writeraap.writerow(row)
    with open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\\bjp.csv", 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            thestring = row[2]
            URLless_string = correctdot(cleanpunc(clean(thestring)))
            row[2]=URLless_string
            csv_writerbjp.writerow(row)
    with open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\\inc.csv", 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            thestring = row[2]
            URLless_string = correctdot(cleanpunc(clean(thestring)))
            row[2]=URLless_string
            csv_writerinc.writerow(row)
        
     
        
read_obj.close()
write_objaap.close()
write_objbjp.close()
write_objinc.close()