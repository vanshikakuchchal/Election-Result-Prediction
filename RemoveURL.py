
import re
import csv 

january=['03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
february=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','22']

for i in january:
    write_obj=open( r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\FinalJanWithoutURL"+str(i)+".csv","w",encoding='utf-8',newline='')
    csv_writer=csv.writer(write_obj)
    with open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\FinalJan"+str(i)+".csv", 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            thestring = row[2]
            URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', thestring)
            row[2]=URLless_string.lower()
            csv_writer.writerow(row)
    
for i in february:
    write_obj=open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\FinalFebWithoutURL"+str(i)+".csv","w",encoding='utf-8',newline='')
    csv_writer=csv.writer(write_obj)
    with open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\FinalFeb"+str(i)+".csv", 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            thestring = row[2]
            URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', thestring)
            row[2]=URLless_string.lower()
            csv_writer.writerow(row)
        
     
        
read_obj.close()
write_obj.close()
        
       