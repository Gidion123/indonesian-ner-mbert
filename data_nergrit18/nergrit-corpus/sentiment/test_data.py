import sys
import anago
import pprint
import os
import tensorflow as tf
import re
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

sumber = 'Kepolisian menyebutkan bahwa pelaku kasus pembunuhan terhadap Abdullah Fithri Setiawan alias Dufi (43) ternyata lebih dari dua orang. Polisi hingga kini baru menangkap dua orang yaitu Nurhadi dan Sari. Dua lainnya masih dalam perburuan."Total ada empat (tersangka)," ujar Kepala Biro Penerangan Masyarakat Divisi Humas Polri Brigjen Pol Dedi Prasetyo di kantornya, Jakarta Selatan, Kamis, 22 November 2018.Kedua pelaku juga berperan memasukkan jasad Dufi ke dalam mobil hingga ke drum. "Yang satu yang membantu mengangkat korban, yang satu yang menampung penjualan mobil korban," kata Dedi.Tak dijelaskan lebih detail identitas dari kedua pelaku tersebut karena masih dalam penyelidikan, tapi yang jelas kedua orang itu masih dalam kejaran kepolisian. "Nah, saat ini polisi sedang mengejar dua pelaku lain, satu pelaku yang membantu para tersangka untuk mengangkut korban ke dalam mobil, satu pelaku yang membeli Innova korban yang dijual tersangka," ujarnya.'
kata=re.findall(r"[\w']+|[.,(!?;)-/:]", sumber)
sb=" ".join(kata)
#dirOutput = "/anago/data/ner/model7"
dirOutput = "model/"
model = anago.Sequence().load(dirOutput)

words = sb.split()
hasil = model.analyze(words)
pprint.pprint(hasil)
