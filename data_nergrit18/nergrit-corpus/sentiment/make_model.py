# Anago Tagging Engine using anago 0.0.5
# Muhamad Jumadil Akbar, Irfan Fakri,
# 2019 July 22
import anago
from anago.reader import load_data_and_labels,load_glove
import os
import numpy as np
import random as rn
 
namaDir = "data/"
 
namaFileTrain = namaDir + "train.txt"
namaFileValid = namaDir + "test.txt"
namaFileTest = namaDir + "valid.txt"

x_train, y_train = load_data_and_labels(namaFileTrain)
x_valid, y_valid = load_data_and_labels(namaFileValid)
x_test, y_test = load_data_and_labels(namaFileTest)
 
os.environ['PYTHONHASHSEED'] = '0'
np.random.seed(42)
rn.seed(12345)
import tensorflow as tf
from keras import backend as K
tf.set_random_seed(1234)
 
# atur parameternya disini
model = anago.Sequence(char_emb_size=25, word_emb_size=50, char_lstm_units=25,
              word_lstm_units=100, dropout=0.5, char_feature=True, crf=True,
              batch_size=36, optimizer='adam', learning_rate=0.001,lr_decay=0.9,
              clip_gradients=5.0, max_epoch=30, early_stopping=False, patience=3,
              train_embeddings=False,max_checkpoints_to_keep=5, log_dir=None)
 
model.train(x_train, y_train, x_valid, y_valid)
 
print("\n\nEvaluasi Test:")
model.eval(x_test, y_test)
dirOutput = "model/"
model.save(dirOutput)
 
words = 'Teroris berada di Mabes Polri'.split()
print(model.analyze(words))
 
words = 'Jakarta adalah ibu kota Indonesia'.split()
print(model.analyze(words))

words = 'Budi Martami kuliah di UPI yang berlokasi di Bandung'.split()
print(model.analyze(words))

words = 'PDIP yang dipimpin oleh Megawati menang dalam Pilkada DKI Jakarta'.split()
print(model.analyze(words))

