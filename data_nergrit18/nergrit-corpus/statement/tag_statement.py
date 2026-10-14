# Anago new 1.0.8
# Muhamad Jumadil Akbar
# 2019 June
import anago
from anago.utils import load_data_and_labels, load_glove
import keras
from keras import optimizers
import pprint
# from anagojsono import jsonkansaja
import json

#alamatsimpan = "./data/ner/"
alamatsimpan = "model/"
model = anago.Sequence().load(weights_file=alamatsimpan + "nerweight.h5", 
            params_file=alamatsimpan + "nerparams.json", 
            preprocessor_file=alamatsimpan + "nerprepro.pkl")
hasil = model.analyze('Atas isu KLB yang berembus, Max Sopacua langsung memberikan klarifikasi. Max membantah mengusulkan ada KLB di partainya. GMPPD mengakui memang sempat menyinggung soal KLB Demokrat dalam siaran persnya, namun bukan hal itu poin dari pernyataan para senior partai. "Saya titik beratkan konpers (konferensi pers) kemarin adalah penyelamatan partai saja. kalau ada KLB itu alternatif. Mereka itu kan membaca, mereka membiarkan partai hancur. Baca dulu bagiannya. Wartawan juga bisa baca. KLB alternatif. Jangan itu yang jadi acuan. Yang jadi acuan adalah bagaimana selamatkan partai di 2024. itu titik tolaknya," tegas Max. "Konpers dibuat untuk selamatkan partai di 2024. KLB adalah alternatif, bukan konferensi pers itu buat KLB. Bego aja yang baca itu. Saya bicara dari awal sampai akhir bagaimana menyelamatkan partai," imbuhnya. Hal senada juga disampaikan senior Demokrat yang hadir dalam konferensi pers, Ahmad Mubarok. Ia menegaskan, tak ada yang menginginkan adanya KLB. Mubarok menjelaskan, konferensi pers beberapa hari lalu itu merupakan wujud keprihatinan senior partai akan kondisi Partai Demokrat. "Nggak ada KLB. Kalau toh ada KLB harus sesuai dengan anggaran dasar. Yang ada itu keprihatinan karena Demokrat sekarang menjadi urutan no 7. Mundur, mundur gitu," kata Mubarok. "Ada yang salah, menyimpang dari ftirahnya. Dulu partai Demokrat terbuka dengan ideologis nasional religius. Cirinya bersih, cerdas, dan santun. Kita ingin kembali ke prinsip pertama itu," imbuh dia.')
pprint.pprint(hasil)