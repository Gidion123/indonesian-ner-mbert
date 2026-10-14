# Anago new 1.0.8
# Muhamad Jumadil Akbar
# 2019 June

import anago
from anago.utils import load_data_and_labels, load_glove
import keras
from keras import optimizers
import pprint
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
alamatsimpan = dir_path + "/data/"

x_train, y_train = load_data_and_labels(alamatsimpan + "train_data.txt")
x_test, y_test = load_data_and_labels(alamatsimpan + "test_data.txt")
x_valid, y_valid = load_data_and_labels(alamatsimpan + "valid_data.txt")

model = anago.Sequence(
                    word_embedding_dim=50,
                    char_embedding_dim=25,
                    word_lstm_size=100,
                    char_lstm_size=25,
                    use_crf=False,
                    # embeddings=embed,

)

model.fit(x_train, y_train, batch_size=32,x_valid=x_valid, y_valid=y_valid, epochs=30,
          callbacks=[keras.callbacks.TerminateOnNaN(),
                     keras.callbacks.CSVLogger(alamatsimpan + "log.csv"),
                     keras.callbacks.ReduceLROnPlateau(monitor='lr')])

print('model.score(x_test, y_test): ', model.score(x_test, y_test))

model.save(weights_file= "model/nerweight.h5", 
            params_file= "model/nerparams.json", 
            preprocessor_file= "model/nerprepro.pkl")
