from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 바꿀 예정
users = {'bis04': '6230'}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # 로그인 성공
        if username == 'bis04':
            return render_template('flag_pageee.html', username=username)
        else:
            return f'로그인 성공, {username}님!'
    else:
        # 로그인 실패
        return '로그인 실패. 아이디 또는 비밀번호를 확인하세요.'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users[username] = password
        return f'회원가입이 완료되었습니다, {username}님!'

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run(debug=True)
    #app.run()