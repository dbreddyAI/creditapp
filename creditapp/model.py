from creditapp import app
import pandas as pd
from flask import jsonify, request
import pickle

lr_model = pickle.load(open('model.pkl', 'rb'))


@app.route('/', methods=['POST', 'GET'])
def predict():
    data = request.get_json(force=True)
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)
    result = lr_model.predict(data_df)
    output = {
        'creditability': list(map(
            lambda x: 'Good' if int(x) == 1 else 'Bad', [result[0]]
        ))[0]
    }
    return jsonify(results=output)
