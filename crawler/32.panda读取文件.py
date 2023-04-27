import pandas as pd
from flask import Flask, render_template

data = pd.read_csv('./movie.csv', header=None)

data = data.loc[:, [1, 3]]
data = data.rename(columns={1: 'title', 3: 'price'})
data = data.to_dict(orient="list")
app = Flask(__name__)


@app.route('/')
def get():
    return render_template('/index.html', data=data)


print(data)
if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port='8080')
