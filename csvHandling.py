import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import transformers

np.set_printoptions(precision=3, suppress=True)

dataFrame1 = pd.read_csv(
    "dataSet.csv",
    delimiter='\t',
    names=["ID", "GrossMonthlyIncome", "CreditCardPayment", "CarPayment", "StudentLoanPayments",
           "AppraisedValue", "DownPayment", "LoanAmount", "MonthlyMortgagePayment", "CreditScore"]
)

dataFrame1.head()

dataFrame1_features = dataFrame1.copy()
# dataFrame1_labels = dataFrame1_features.pop('CreditScore')

dataFrame1_features = np.array(dataFrame1_features)
dataFrame1_features

dataFrame1_model = tf.keras.Sequential([
    layers.Dense(64),
    layers.Dense(1)
])

dataFrame1_model.compile(loss=tf.keras.losses.MeanSquaredError(),
                         optimizer=tf.keras.optimizers.Adam())

print(dataFrame1)

