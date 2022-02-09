Acest Sistem de clasificare a deseurilor a fost realizat de Alexandru Botone 
si reprezinta partea practica a lucrarii de diseratie, specializarea SADE.

Utilizarea acestui proiect fara acceptul dezvoltatorului este interzisa.
*******************
Contact

alexbotone@gmail.com

alexandru.botone@econ.ubbcluj.ro
********************
Pentru rularea locala a proiectului trebuiesc instalate toate 
tool-urile prevazute in `requirements.txt`.

**IDE : PyCharm Community

**Python : 3.9

Modele din acest proiect reprezinta rezultatele favorbile din arhitecturiile realizate in dezvoltarea acestui sistem
**************************
**API dezvoltat pentru requesturile UI:

`classifywaste():` (POST)

 Return:  predicted_value, romanian_translation, details,
                    video1, video2, probability 
 
Din dictionarul : util.data

****API dezvoltat pentru requesturile backend:

`classifywaste_api():` (POST)

 Return:  predicted_value, romanian_translation, probability 
 
Din dictionarul : util.data

**************
predicted_value - clasa in care se incadreaza imaginea 

values: 'battery', 'biological', 'brown-glass', 'cardboard', 'clothes', 'e-waste', 'green-glass', 'light-bulbs',
                'metal', 'paper', 'plastic', 'shoes', 'trash', 'white-glass', 'unrated'

romanian_translation - traducerea in romana a clasei

probability - probabilitatea de apartenenta in clasa

video1,video2 - uniqueID de pe platforma youtube.com a videoului embad

details - (text, string) o descriere a clasei in romana pentru afisarea in UI
**************