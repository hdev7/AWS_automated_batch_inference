import subprocess
import sys

filePath = sys.argv[1]
print('filePath: ' ,  filePath)

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
	
install("pandas")
install("sklearn")

from sklearn.externals import joblib
import pandas as pd

test_df = pd.read_csv('test.csv')

vect = joblib.load('tfidfvectorizer.pkl')
model = joblib.load('model.pkl')

test_tfidf = vect.transform(test_df.text)
y_pred = model.predict(test_tfidf)

y_df = pd.DataFrame(y_pred, columns=['target'])

final_df = pd.concat([test_df,y_df],axis = 1)

final_df.to_csv('scored_data.csv')




