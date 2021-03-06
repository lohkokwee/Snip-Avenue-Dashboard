import math
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from scipy.stats import percentileofscore

def get_bins(df, col, interval):
    col_max = math.ceil(df[col].max())
    bin_intervals = [i * interval for i in range(col_max//interval + (1 if col_max % interval > 0 else 0) + 1)]
    bin_labels = [f"<{bin_interval}" for bin_interval in bin_intervals[1:]]

    df[f"{col}_bins"] = pd.cut(df[col], bins = bin_intervals, labels = bin_labels)

    return df

def get_col_dict(cols):
    col_dict = {f"Average {' '.join(list(map(lambda x: x.capitalize(), col.split('_'))))}" : f"average_{col}" for col in cols}

    return col_dict


def get_prediction(variables):

    HERE = Path(__file__).parent
    
    pickle_in = open(HERE / 'logreg.sav', 'rb')
    model = pickle.load(pickle_in)
    x_test = pd.DataFrame(np.array([variables]))
    prediction = model.predict(x_test)
    confidence = model.predict_proba(x_test)

    return int(prediction[0]), list(confidence[0])[int(prediction[0])]

def get_percentile(variables, df):
    variable_names = ['wait_time', 'process_duration', 'queue_length', 'rating', 'price_paid']
    percentile_list = []

    for i in range(len(variable_names)):
        dataset = df[variable_names[i]]
        percentile = percentileofscore(dataset, variables[i])
        percentile_list.append(percentile)

    return percentile_list