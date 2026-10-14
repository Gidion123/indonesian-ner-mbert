# Anago Tagging Engine using anago 1.0.8
# Irvan R. - Ashar "Aviezab" - Harits A.
# 2018 Sept 6

import anago
from anago.utils import load_data_and_labels, load_glove
import keras
from keras import optimizers
import pprint
from anagojsono import jsonkansaja
import json

#alamatsimpan = "./data/ner/"
alamatsimpan = "model/"
model = anago.Sequence().load(weights_file=alamatsimpan + "nerweight.h5", 
            params_file=alamatsimpan + "nerparams.json", 
            preprocessor_file=alamatsimpan + "nerprepro.pkl")
hasil = model.analyze("TANGERANG SELATAN - Saat memberi sambutan pada Festival11 HUT ke-4 Partai Solidaritas Indonesia (PSI), di ICE BSD, Pagedangan, Tangerang, Presiden Joko Widodo (Jokowi) kembali menyindir apa yang disebutnya gaya politik genderuwo. Menurut Jokowi, masih ada kelompok di dalam negeri yang selalu menebarkan ketakutan-ketakutan kepada generasi muda. Padahal kata dia, saat ini bangsa lain benar-benar khawatir disalip dengan kreatifitas anak-anak muda Indonesia dalam dunia bisnis. \"Anak-anak muda harus diberi harapan, bukan ditaburi ketakutan. Ada yang menakut-nakuti rakyat kita sendiri, bangsa lain saja takut pada anak-anak muda kita. Loh kok justru ada yang menakut-nakuti anak muda kita dari dalam negeri sendiri,\" ucapnya, Minggu (11/11/2018) malam.")


#print (hasil)
hasil2 = str(hasil['entities'])
hasil2 = hasil2.replace('[', '')
hasil2 = hasil2.replace(']', '')
hasil2 = json.dumps(hasil2)
#print (hasil2)
hasil = jsonkansaja(hasil2)
#print(hasil)
pprint.pprint(hasil)
