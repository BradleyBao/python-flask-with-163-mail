from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message

app = Flask("EmailDemo", static_folder="static", template_folder="templates")

# Email
app.config['MAIL_SERVER'] = "smtp.163.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'noreplytranslate@163.com'
app.config['MAIL_PASSWORD'] = '自己的授权码'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# 错误信息
Exception_Info = ""

@app.route("/", methods=['GET', 'POST'])
def main():
    global Exception_Info
    if request.method == "GET":
        return render_template("main.html")

    else:
        try:
            Name = request.form.get('name')
            Email = request.form.get('email')
            Title = request.form.get('title')
            Content = request.form.get('content')

            msg = Message(Title, sender='noreplytranslate@163.com', recipients=[Email, 'admin@bradleyproject.site'])
            msg.body = f"你好 {Name}, \n\n我收到了你的信息: \n {Content} "
            mail.send(msg)

            return redirect(url_for('success'))

        except Exception as e:
            Exception_Info = e
            print(Exception_Info)

            return redirect(url_for('error'))

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/error")
def error():
    return render_template("error.html", error_info = Exception_Info)

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)