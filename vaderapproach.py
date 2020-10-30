# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:05:54 2020

@author: Mayank$AGGARWAL
"""




'''
Vader
'''
import csv
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


def roccurve(Y_test,Pred):
    
    fpr, tpr, threshold = roc_curve(Y_test,Pred)
    print("True Positive Rate",tpr[1])
    print("False Positive Rate",fpr[1])
    roc_auc = auc(fpr, tpr)
    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label = 'AUC = %0.4f' % roc_auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.title('ROC Curve of Vader')
    plt.show()
    
def lexiconrate(s):
        score = analyser.polarity_scores(s)
        # if(score['compound']>0):
        #     score['compound']=0.8*score['compound']
        return score['compound']
    
def bigramapproach(text):
    senti=0
    count=0
    for i in text:
        pos=nltk.pos_tag(i)
        if((pos[0][1]=='RB' or pos[0][1]=='RBR' or pos[0][1]=='RBS') and (pos[1][1]=='JJ' or pos[1][1]=='JJR' or pos[1][1]=='JJS')):
            s1=pos[0][0]+" "+pos[1][0]
            senti=senti+lexiconrate(s1)
            count=count+1
        if(pos[0][1]=='JJ' or pos[0][1]=='JJR' or pos[0][1]=='JJS' or pos[1][1]=='JJ' or pos[1][1]=='JJR' or pos[1][1]=='JJS'):
            s2=pos[0][0]+" "+pos[1][0]
            senti=senti+lexiconrate(s2)
            count=count+1
    if(count==0):
        return senti
    else:
        return (senti/count)

def getsentiment(text):
    sentencetokenize=sent_tokenize(text)
    senti = 0
    count =0
    for i in sentencetokenize:
       # wordstokenize=word_tokenize(i.lower())
        #wordstokenize=list(ngrams(wordstokenize, 2))
        senti = senti + lexiconrate(i)
        count+=1
    if(count==0):
        return senti
    else:
        return (senti/count)




wrong =0
avotes=0
pvotes=0
write_obj=open( r"C:\Users\hp\Desktop\Election\Datewise\Dataset\vader.csv","w",encoding='utf-8',newline='')
csv_writer=csv.writer(write_obj)
with open(r"C:\Users\hp\Desktop\Election\Datewise\Dataset\training.csv", 'r',encoding="utf8") as read_obj:
    csv_reader = csv.reader(read_obj)
    for row in csv_reader:
        text = row[0]
        p=getsentiment(text)
        
        if row[1] == '1':
            avotes=avotes+1
        if p > 0.1:
            row.append("1")
            if row[1] == '1':
                pvotes=pvotes+1 
            else:
                wrong=wrong+1
        else:
            row.append("0")
        csv_writer.writerow(row)
y_test=list()
predict=list()
with open(r"C:\Users\hp\Desktop\Election\Datewise\Dataset\vader.csv","r",encoding='utf-8') as read_obj :
    csv_reader = csv.reader(read_obj)
    TP=0
    FP=0
    TN=0
    FN=0
    for row in csv_reader:
        y_test.append(int(row[1]))
        predict.append(int(row[2]))
        if row[1]==row[2]=="1":
            TP += 1
        if row[2]=='1' and row[1]!=row[2]:
            FP += 1
        if row[1]==row[2]=="0":
            TN += 1
        if row[2]=='0' and row[1]!=row[2]:
            FN += 1
    print("True positive ",TP)
    print("True negative ",TN)
    print("False positive ",FP)
    print("False negative ",FN)
    recall=TP/(TP+FN)
    precision=TP/(TP+FP)
    print("Recall",recall)
    print("Precision",precision)
    roccurve(y_test,predict)

read_obj.close()
write_obj.close()
        
