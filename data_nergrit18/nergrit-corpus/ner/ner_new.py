# Anago new 1.0.8
# Irvan R. - Ashar "Aviezab" - Harits A.
# 2018 Sept 6, 7

import anago
from anago.utils import load_data_and_labels, load_glove
import keras
from keras import optimizers
import pprint
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
alamatsimpan = dir_path + "/data/"

x_train, y_train = load_data_and_labels(alamatsimpan + "train.txt")
x_test, y_test = load_data_and_labels(alamatsimpan + "test.txt")
x_valid, y_valid = load_data_and_labels(alamatsimpan + "valid.txt")

# Glove can't be uploaded to github since the size is more than 100MB
# embed = load_glove(alamatsimpan + "glove.txt")

# default using Keras Adam
# van = optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)

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
alamatsimpan1 = "model/"
model.save(weights_file= alamatsimpan1 + "nerweight.h5", 
            params_file= alamatsimpan1 + "nerparams.json", 
            preprocessor_file= alamatsimpan1 + "nerprepro.pkl")
