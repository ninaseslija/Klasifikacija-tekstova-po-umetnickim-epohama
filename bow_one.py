# BAG OF WORDS ZA JEDAN TEKST

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


with open("Zlocin i kazna.txt", "r", encoding="utf-8") as f:
    text = f.read()


vectorizer = CountVectorizer(stop_words='english') #pretvori text u listu reci (tokenizacija)
                                                    #stop words sklanja reci poput the, an...
                                                    
X = vectorizer.fit_transform([text]) #FIT:
                                    #macka -> 0
                                    #  pas -> 1
                                    #----------
                                    #TRANSFORM:
                                    #pretvara tekst u sparse matricu, u njoj se nalazi broj 
                                    #pojavljivanja svake reci

                    
vocab = vectorizer.get_feature_names_out()  #vocab niz svih reci u tekstu

freqs = X.toarray()[0] #freqs je koliko se koja rec pojavljuje, ali sada kao obican niz (lakse)

df = pd.DataFrame({
    "Word": vocab,
    "Frequency": freqs
})

df = df.sort_values(by="Frequency", ascending=False).reset_index(drop=True)
pd.set_option("display.max_rows", None)  # prikaži sve redove
print(df)


top_n = 20 
top_idx = freqs.argsort()[::-1][:top_n]
print("\nTop", top_n, "reč(i) i broj pojavljivanja:")
for idx in top_idx:
    print(vocab[idx], int(freqs[idx]))

