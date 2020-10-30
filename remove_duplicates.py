import pandas as pd 
january=['03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
february=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','22']

for i in january:
    data = pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\Jan"+str(i)+".csv")
    data.drop_duplicates(subset ="text", 
                     keep = 'first', inplace = True)
    data.to_csv(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\FinalJan"+str(i)+".csv",index = False)
    
for i in february:
    data = pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\Feb"+str(i)+".csv")
    data.drop_duplicates(subset ="text", 
                     keep = 'first', inplace = True)
    data.to_csv(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\FinalFeb"+str(i)+".csv",index = False)