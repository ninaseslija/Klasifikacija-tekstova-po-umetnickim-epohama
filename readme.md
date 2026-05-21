optimizacija random foresta




iteracija 0:
'n_estimators' : [50, 100], 
'max_features' : [10 000], 
'max_depth' : [10, 20, 30]
tacnost ne najbolja, max_features 10 000 je previse

iteracija 1:
TF-IDF
parametri: 
 'n_estimators' : [50, 100], 
'max_features' : [50, 100, 200, 300, 500, 1000], 
'max_depth' : [10, 20, 30]

oko 100 - 200 najbolja tacnost, uzimamo parametre tu izmedju
povecavamo max_depth

iteracija 1: 
TF-IDF
parametri: 
 'n_estimators' : [50, 100], 
'max_features' : [50, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 500, 1000],
'max_depth' : [10, 20, 30, 35, 40, 45, 50]

max_depth daje bolje rezultate sto je dubina visa
100 daje bolje rezultate -> prelazimo na samo 100
max_features najbolji oko 180-200 
generisemo grafik, jedan za features, drugi za depth

dokument: 80_rezultati.txt (C:\Users\ninas\OneDrive\Documents\Klasifikacija\TFIDF)



iteracija 2:
BoW
menjamo samo broj drveca - fiksno 100: 
 'n_estimators' : [100], 
'max_features' : [50, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 500, 1000],
'max_depth' : [10, 20, 30, 35, 40, 45, 50]

dokument: rezultati1.txt (C:\Users\ninas\OneDrive\Documents\Klasifikacija\BoW) 

pitanje: bow daje bolju tacnost? 
  -> malo je bolji 


iteracija 3:
isprobavamo 70-30 NA OBA VEKTORIZATORA 
n_estimators = 100 

  iteracija 3.1:
  TFIDF
  dokument: 70_rezultati_tfidf.txt
  iteracija 3.2:
  BOW
  dokument: 70_rezultati_tfidf.txt


-> 70-30 losije: vracamo se na 80

? pitanje: da li 70-30 daje bolje rezultate? 
  -> ne, vracamo se na 80

iteracija 4:
uradjena je analiza podataka, gde je najveca vrednost, a gde opada.
nova iteracija ima sledece parametre:
BoW
80-20
parametri: 
'n_estimators' : [100, 150, 200],
'max_features' : [50, 100, 140, 180, 220, 300],  
'max_depth' : [30, 40, 50, 60, 70, 80]


-uraditi grafik greske 
-dodati jos dubine dok ne postane losije 
-max_features da bude 50 i 100 -> uraditi cross validation
