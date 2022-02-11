import logging

import numpy as np
import tensorflow as tf

data = {
    "battery":
        [
            "baterie",
            "Reciclarea bateriilor are ca scop eliminarea acestora din celelalte deseuri solide, deoarece aceste "
            "contin o serie de metale grele si substane chimice toxice si greu de eliminat. Aceste substante "
            "contamineaza solul si vegetalele ce cresc pe acesta, fara posibilitate de tratare. Desi este foarte "
            "scumpa reciclarea bateriilor aceasta este benefica deoarece materialele metalice se reutilizeaza la "
            "crearea de noi baterii, iar carbonul este utilizat la topirea metalelor.<br><br> Stiati ca Nichel-Cadmiu "
            "utilizat în baterii se retrateaza si se poate refolosi de pana la 5 ori?",
            "bHbgCvNBFW0", "Jw-hinWmFwE"],
    "biological":
        [
            "biologic",
            "Deseurile biologice se stocheaza in gropi de gunoi separat pentru descompunere sau pentru crearea de "
            "compost, benefic pentru imbogatirea solului. Inca din cele mai vechi timpuri oamenii foloseau compostul "
            "ca ingrasamant natural si il stocau de obicei in apropiere de gradina de legume. De obicei toate "
            "deseurile biologice se descompun total in 2-3 ani, iar volumul scade cu aproximativ 65%, "
            "astfel ca gropile de deseuri biodegradabile se pot refolosi, acestea se pot considera fabrici de "
            "ingrasamant gratuit.<br><br> Stiati ca din compost se poate realiza un sistem de incalzire alternativa "
            "pentru case? ",
            "GjATfgctCog", "1F34RkGF89M"],
    "brown-glass":
        [
            "sticla maro",
            "Reciclarea sticlei este un proces foarte simplu, mai usor decat crearea de sticla noua. Prin zdrobirea "
            "in particule mici a deseului din sticla si retopirea ei, clarificarea si re-turnarea, sticla a terminat "
            "procesul de reciclare. Desigur pentru a produce sticla de o culoare anume aceasta trebuie selectata "
            "separat, uzual in 3 categorii: translarenta si alba, verde, maro si neagra. Inainte de reciclare sticla "
            "trebuie purificata si curatata de contaminari, prin apa si apoi prin topire. Sticla zdrobita pentru "
            "topire poarta numele de calcit si este impartit in calcit intern(curat) si extern(cu impuritati) "
            "<br><br>Stiati ca sticla "
            "isi pastreaza culoarea si dupa topire? Majoritatea obiectelor de arta din sticla multicolora provin din "
            "reciclarea sticlei intr-o sigura categorie.",
            "B4mXMWIWQ94", "zJ0zqAfsQfM"],
    "cardboard":
        [
            "carton",
            "Cartonul curat, uscat si necontaminat este reciclat prin maruntirea si dizolvarea intr-un amestec de apa "
            "si alte substante chimice. Apoi, mixtura realizata din 1% carton si 99% apa, prin decantare si apoi "
            "uscare se realizeaza un sul de carton, care se refoloseste de catre fabricile care produc ambalaje din "
            "carton, Pentru o rezistenta sporita in compozitie se adauga si celuloza virgina in proportie de cel "
            "putin 5%. Cartonul se poate recicla de 4-5 ori, iar apoi se poate reutiliza la confectia de mobilier si "
            "jucarii ecologice sau hartie igienica. Pentru reciclare cartonul nu poate contine urme de alimente, apa, "
            "plastic sau alte substante <br><br>Stiati ca de cele mai multe ori capacul cutiei de pizza se poate "
            "recicla?",
            "jFYALKk7CIA", "HBGHa6xGwrY"],
    "clothes":
        [
            "imbracaminte",
            "Hainele utilizate se recicleaza in 3 moduri: reciclare prin curatare si donare catre organizatii "
            "caritabile, tranformarea in fibra textila sau incinerare pentru productia de ciment. Pentru realizarea de "
            "fibre, se extrag separat particulele de poliester, celuloza, bumbac si se dizolva chimic pentru realizarea "
            "de noi fire textile, la fel de rezistente, pentru producerea de noi produse. Companiile care "
            "comercializeaza haine din bumbac sunt obligate sa comercializeze haine din bumbac reciclat in proportie "
            "de minim 10%. Din fibra mai putin calitativa se produc covoare, lavete sau izolatii. <br><br> Stiati ca "
            "peste 50% din tapiteriile automobilelelor sunt produse din textile reciclate?",
            "Drw-LL3sQys", "pv_OP0B4RJo"],
    "e-waste":
        [
            "electronic",
            "Deseurile electronice sunt in cea mai mare masura electrocasnicele uzate si sunt destinate dezmembrarii, "
            "sortarii pe categorii de elemente, topire, returnare si reutilizare in crearea de noi electrocasnice. "
            "Expansiunea rapida a tehnologiei duce la o cantitate foarte mare de deseuri electronice, "
            "iar unele materiale precum bromul, bariliul sunt extrem de toxice. Astfel reciclarea electrocasnicelor "
            "face ca materialele scumpe si finite se pot reutiliza, iar natura nu este afectata. <br><br> Stiati ca "
            "din procesorul unui telefon vechi se pot realiza 4 noi procesoare de ultima generatie? ",
            "7aoanreD-J8", "pv_OP0B4RJo"],
    "green-glass":
        [
            "sticla verde",
            "Reciclarea sticlei este un proces foarte simplu, mai usor decat crearea de sticla noua. Prin zdrobirea "
            "in particule mici a deseului din sticla si retopirea ei, clarificarea si re-turnarea, sticla a terminat "
            "procesul de reciclare. Desigur pentru a produce sticla de o culoare anume aceasta trebuie selectata "
            "separat, uzual in 3 categorii: translarenta si alba, verde, maro si neagra. Inainte de reciclare sticla "
            "trebuie purificata si curatata de contaminari, prin apa si apoi prin topire. Sticla zdrobita pentru "
            "topire poarta numele de calcit si este impartit in calcit intern(curat) si extern(cu impuritati) "
            "<br><br>Stiati ca sticla "
            "isi pastreaza culoarea si dupa topire? Majoritatea obiectelor de arta din sticla multicolora provin din "
            "reciclarea sticlei intr-o sigura categorie.",
            "B4mXMWIWQ94", "zJ0zqAfsQfM"],
    "light-bulbs":
        [
            "bec",
            "Mercurul extrem de toxic din componenta becurilor dauneaza atat oamenilor si animalelor cat si solului. "
            "Exista becuri HID care contin inclusiv materiale radioactive. De obicei stocarea becurilor duce la "
            "spargerea acestora , si astfel, la incapacitatea de reciclare, prin reciclarea becurilor sticla se poate "
            "reutiliza, metalul se poate transforma in alte electronice care necesita conductibilitate a curentului "
            "electric, iar conectorii se pot refolosi la fabricarea altor becuri. Practic tot becul se poate recicla, "
            "astfel ca nimic nu se pierde, iar metalul din filamentul becului este extrem de scump, din cauza "
            "cantitatilor reduse. <br><br> Stiati ca becurile LED nu contin mercur, si au o durata de viata mult mai "
            "lunga in comparatie cu becurile clasice incandescente? Un alt avantaj este economia de curent electric.",
            "iYi8hfbIcxo", "IMt4klELO0E"],
    "metal":
        [
            "metal",
            "In procesele industriale se utilizeaza zilnic sute de tone de metal. Cele mai utilizate metale sunt fierul,"
            " aluminiul, cuprul, zincul, plumbul si nichelul, iar cele mai pretioase sunt aurul, platina, "
            "argintul. Multe din aceste metale devin toxice prin oxidare, iar pretul lor este foarte ridicat. "
            "Epuizarea metalelor ar putea duce rapid la o criza mondiala, iar pentru atenuarea oricaror eventuale "
            "crize economice, sau de materiale, reciclarea poate insemna salvare. De altfel reciclarea metalelor se "
            "realizeaza destul de usor si ieftin, si este practicata din cele mai vechi timpuri.<br><br> Stiati ca "
            "primul material reciclat constient de om a fost fierul? Fabricarea unei unelte noi dintr-o unealta uzata "
            "este considerata prima forma de reciclare.",
            "2Fou9c3ZB-w", "jYAZEPNxdl0"],
    "paper":
        [
            "hartie",
            "Reciclarea hartiei este procesul prin care deseurile de hartie sunt transformate in noi produse din "
            "hartie. Beneficiile aduse de aceste produse sunt: reducerea defrisarilor de paduri, reducerea de deseuri "
            "de hartie din depozite si din casele oamenilor, reducerea emisiilor de metan. Pentru un viitor "
            "sustenabil este recomandata reutilizarea a minim doua treimi din hartia pe care o folosim. Deseurile de "
            "hartie sunt obținute în mare parte din hartie utilizată o singura data, spre exemplu ambalajele care o "
            "data desfacute sunt aruncate cu prima ocazie. După utilizari repetate hartia isi pierde din calitati "
            "insa devine reutilizabila, daca se adauga celule de celuloza proaspete <br><br> Stiati ca cele mai "
            "reciclate produse din hartie sunt ziarele si reviste vechi?",
            "9HH5FlIGOXE", "VoMeE_PGVm8"],
    "plastic":
        [
            "plastic",
            "Reciclarea plasticului este procesul de recuperare a deseurilor produse din plastic si reprocesare a "
            "materialului in produse noi utile. Din cauza simbolurilor gresite intentionat de pe ambalaje si a "
            "numeroaselor obstacole mai putin de 10% din plastic a fost vreodata reciclat. Cea mai mare incercare a "
            "reciclarii plasticului este pretul. Inca din 1970 era cunoscut faptul ca reciclarea produselor din "
            "plastic este o provocare din cauza elementelor tehnice necesare, foarte scumpe, pentru un produs foarte "
            "ieftin realizat din plastic virgin. Abia din 2019 exista reglementari mondiale privind obligativitatea "
            "reciclarii plasticului pentru companiile care il utilizeaza, cu toate acestea s-au gasit solutii pentru "
            "cresterea cantitati de plastic virgin utilizat, in contra reglementarilor. <br><br>Stiati ca peste 40% "
            "din produsele din plastic sunt utilizate o singura data? ",
            "_E4QJViBcY0", "aJdYYt3Xh0w"],
    "shoes":
        [
            "incaltaminte",
            "Incaltaintea incepe ciclul de reciclare prin impartirea in functie de tipul de materiale folosite(piele, "
            "textil, plastic, cauciuc) iar apoi se separa talpa de restul incaltarii. Dupa clasificare, materialele "
            "precum plasticul, textilele se macina pentru reutilizare, iar pielea se stocheaza separat deoarece nu se "
            "poate recicla, astfel ca se incinereaza. Inainte de reciclarea propriu zisa incaltamintea in stare buna "
            "este curatata si preluata de organizatii sociale in scopul donarii. O parte din piele este reutilizata "
            "de catre artisti pentru producerea de elemente de arta sau chiar imbracaminte<br><br> Stiati ca "
            "papucii de casa eco sunt realizati din plastic provenit de la talpile incaltamintelor reciclate",
            "fMHPMycjqGQ", "KCn8Z3fghLA"],
    "trash":
        [
            "deseu nereciclabil",
            "Desurile nereciclabile sunt deseurile care nu se mai pot transforma in ceva util pentru omenire. De cele "
            "mai mule ori aceste ajung in stoucri imense in depozite unde urmeaza sa ramana pana la descompunere sau "
            "incinerare pentru productia de ciment. De "
            "cele mai multe ori in gunoiul nereciclabil ajung foarte multe deseuri cu potential de reciclare, "
            "care nu a ajuns sa fie sortate. De cele mai multe ori se cauta solutii pentru micsorarea cantitatii de "
            "deseu nereciclabil, iar o noua tehnologie propune o solutie de distrugere a acestora, care genereaza "
            "inclusiv energie. Din nefericire inca nu se pune accentul pe distrugerea deseurilor nereciclabile, "
            "date fiind problemele generate de desurile reciclabile.<br><br> Stiati ca o punga de plastic cu folie de "
            "aluminiu asteapta 1000 de ani cel putin pentru descompunere?",
            "I_1mJUyMSzY", "N9R1mMiSlM8"],
    "white-glass":
        [
            "sticla transparenta",
            "Reciclarea sticlei este un proces foarte simplu, mai usor decat crearea de sticla noua. Prin zdrobirea "
            "in particule mici a deseului din sticla si retopirea ei, clarificarea si re-turnarea, sticla a terminat "
            "procesul de reciclare. Desigur pentru a produce sticla de o culoare anume aceasta trebuie selectata "
            "separat, uzual in 3 categorii: translarenta si alba, verde, maro si neagra. Inainte de reciclare sticla "
            "trebuie purificata si curatata de contaminari, prin apa si apoi prin topire. Sticla zdrobita pentru "
            "topire poarta numele de calcit si este impartit in calcit intern(curat) si extern(cu impuritati) "
            "<br><br>Stiati ca sticla "
            "isi pastreaza culoarea si dupa topire? Majoritatea obiectelor de arta din sticla multicolora provin din "
            "reciclarea sticlei intr-o sigura categorie.",
            "B4mXMWIWQ94", "zJ0zqAfsQfM"],
    "unrated":  # neclasificat
        [
            "neclasificat",
            "Deseurile neclasificate sunt cele respinse de sistem, care nu a reusit clasificarea lor. Nu reprezinta "
            "gunoi nereciclabil, ci reprezinta deseu care trebuie clasificat de o persoana. In cazul in care imaginea "
            "cu deseul nu satisface cerintele sistemului este mai recomandata o a doua clasificare de un muncitor "
            "uman, pentru a evita contaminarea unui intreg lot de deseuri reciclabile sau clasificarea ca deseu "
            "nereciclabil, pentru a evita stocarea unui deseu care se poate recicla.",
            "rItgc45AmdU", "XlB277xDxzw"]
}


output_class = ['battery', 'biological', 'brown-glass', 'cardboard', 'clothes', 'e-waste', 'green-glass', 'light-bulbs',
                'metal', 'paper', 'plastic', 'shoes', 'trash', 'white-glass', 'unrated']

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def load_artifacts():
    global model1, model2, model3

    global models

    model1 = tf.keras.models.load_model("./model/model_xception8744.h5")
    model2 = tf.keras.models.load_model("./model/model_xception8851.h5")
    model3 = tf.keras.models.load_model("./model/model_VGG19.h5")

    models = [model1, model2, model3]


def classify_waste(image_path):
    test_image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    test_image = tf.keras.preprocessing.image.img_to_array(test_image) / 255
    test_image = np.expand_dims(test_image, axis=0)
    for model in models:
        result = model.predict(test_image)
        result = list(result[0])
        img_index = result.index(max(result))
    probability = round(result[img_index] * 100, 2)

    if probability >= 60:
        predicted_value = output_class[img_index]
        print(predicted_value)
        logging.warning("Predicted class is " + predicted_value + " for uploaded image with path " + image_path +
                        " probability :" + str(probability) + "%")
        return predicted_value, data[predicted_value][0], data[predicted_value][1], data[predicted_value][2], \
               data[predicted_value][3], probability
    else:
        logging.warning(
            "Predicted class is " + output_class[img_index] + " for uploaded image with path " + image_path +
            " !!! But is classified as unrated due to probability :" + str(probability) + "% ")
        predicted_value = output_class[14]
        print(predicted_value)
        logging.warning("Unable to predict classification for uploaded image with path " + image_path +
                        " because the probability was only:" + str(probability) + "% for class:" + output_class[
                            img_index])

        return predicted_value, data[predicted_value][0], data[predicted_value][1], data[predicted_value][2], \
               data[predicted_value][3], probability
