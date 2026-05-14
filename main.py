import os
import pandas as pd
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.model_selection import ParameterGrid
#from gutenberg_cleaner import simple_cleaner, super_cleaner

from podela_poglavlja import poglavlja
from sum_words import broj_reci

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB

#poglavlja() 
folders = {
    "Realizam": "chapters_ZIPOVAN/Realizam",
    "Romantizam" : "chapters_ZIPOVAN/Romantizam",
    "Renesansa" : "chapters_ZIPOVAN/Renesansa",
    "Modernizam" : "chapters_ZIPOVAN/Modernizam"
}
epohe = ["Realizam", "Romantizam",  "Renesansa", "Modernizam"]

for epoha in epohe:
    broj_reci(epoha)

texts = []
labels = []

for label, folder_path in folders.items():
    for delo_dir in os.listdir(folder_path):
        print(f"Loading {delo_dir}...", flush=True)
        for filename in os.listdir(os.path.join(folder_path, delo_dir)):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, delo_dir, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()
                    if len(text.split()) > 3:
                        texts.append(text)
                        labels.append(label)

model_params = {
    'naive_byes' : {
        'model' : MultinomialNB(),
        'params' : {   
            'alpha' : [0.0001, 0.01, 0.05, 0.1]
        }
    },
    'random_forest': {
        'model' : RandomForestClassifier(n_jobs = -1, random_state=42),
        'params' : {
            'n_estimators' : [50, 100], # broj drveca
            'max_features' : [10000],
            'max_depth' : [10, 20, 30] #najvise feature (ima previse reci)
            
        }
    },

    'decision trees' :{
        'model' : DecisionTreeClassifier(),
        'params' : {
            'max_depth' : [10, 20, 30], 
            'max_features' : [10000],

        }
    }


}

vectorizer = TfidfVectorizer(stop_words='english', max_features=10000) 
#vectorizer = CountVectorizer(stop_words='english', max_features=10000) 
print(f"max features: 10 000")
X = vectorizer.fit_transform(texts)
y = labels

os.makedirs("bow_folder", exist_ok=True)
with open("bow_folder/matrix.pkl", "wb") as f:
    pickle.dump(X, f)

X_train, X_test, y_train, y_test = train_test_split(
   X, y,
    test_size=0.2,
   random_state=42
)
results = []

for model_name, mp in model_params.items():
    model = mp['model']
    params = mp['params']
    if params:
        grid = ParameterGrid(params) #uzme sve moguce kombinacije
    else:
        grid = [{}]

    print(f"\n=== {model_name} ===")
    for p in grid: #racuna f1 score za svaku kombinaciju parametra
        model.set_params(**p)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        score = f1_score(y_test, y_pred, average= "weighted")
        print(f"Params: {p} => F1: {score:.4f}")
        results.append((model_name, p, score ))


df_results = pd.DataFrame(results, columns= ["Model", "Paramters", "F1 score"])
print("\n=== Svi rezultati ===") 
print(df_results.sort_values(by="F1 score", ascending=False))



