# python script
import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series
from pandas import concat

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

from keras.models import model_from_json

from keras.callbacks import CSVLogger


 
def fit_lstm(train, batch_size, nb_epochs, neurons):
	X, y = train[:, 0:-1], train[:, -1]
	X = X.reshape(X.shape[0], 1, X.shape[1])
	model = Sequential()
	model.add(LSTM(neurons, batch_input_shape=(batch_size, X.shape[1], X.shape[2]), stateful=True))
	model.add(Dense(1))
	model.compile(loss='mean_squared_error', optimizer='adam')
	#for i in range(nb_epoch):
	hist = model.fit(X, y,validation_split=0.2, nb_epoch=nb_epochs, batch_size=batch_size, verbose=0, shuffle=False)
	#	model.reset_states()
	return model, hist


supervised_values = df.values

model, hist = fit_lstm(supervised_values, 1, 1000, 4)


df1= pd.DataFrame(np.array(hist.history['loss']), columns = ['loss'])

# serialize model to JSON
model_json = model.to_json()
with open("F:\Pentaho\pentaholab\London Air Quality\Predictive\Demo\model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("F:\Pentaho\pentaholab\London Air Quality\Predictive\Demo\model.h5")



