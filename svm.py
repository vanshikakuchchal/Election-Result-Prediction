from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
import pandas as pd
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import matplotlib.pyplot as plt
import csv

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
    plt.title('ROC Curve of SVM')
    plt.show()
    
pipeline = Pipeline(
            [
                ('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(
                    loss='hinge',
                    penalty='l2',
                    alpha=1e-3,
                    random_state=42,
                    max_iter=100,
                    learning_rate='optimal',
                    tol=None,
                )),
            ]
        )
train_df=pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\Dataset\training.csv")
learner = pipeline.fit(train_df['text'],train_df['truth'])
test_df = pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\Dataset\test.csv")
test_df['pred'] = learner.predict(test_df['text'])
test_df.to_csv(r"C:\Users\hp\Desktop\Election\Datewise\Dataset\prediction_of_svm.csv",index = False)

y_test=list()
predict=list()

with open(r"C:\Users\hp\Desktop\Election\Datewise\Dataset\prediction_of_svm.csv","r",encoding='utf-8') as read_obj :
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

