from flask import Flask, render_template
import random

app = Flask(__name__)

# おみくじの結果をランダムに選ぶ関数
def get_fortune():
    fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
    return random.choice(fortunes)

# ホームページのルート
@app.route('/')
def home():
    return render_template('index.html')

# おみくじの結果を表示するページ
@app.route('/omikuji')
def omikuji():
    fortune = get_fortune()
    return render_template('omikuji.html', fortune=fortune)

if __name__ == '__main__':
    app.run(debug=True)
