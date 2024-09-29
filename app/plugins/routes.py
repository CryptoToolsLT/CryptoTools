from flask import Flask, render_template
from flask import request, redirect
from ..controllers import register_user, RegisterForm
from ..controllers import login_user, LoginForm, logout_user
from ..controllers import login_required # type: ignore

def register_routes(app: Flask):
    @app.route('/login', methods=['GET', 'POST'])
    def login_page():
        if request.method == 'GET':
            return render_template("login.html")
        elif request.method == 'POST':
            return login_user(
                LoginForm(**request.form)
            )
        else:
            return redirect('/')
    
    @app.route('/register', methods=['GET', 'POST'])
    def register_page():
        if request.method == 'GET':
            return render_template("register.html")
        elif request.method == 'POST':
            return register_user(
                RegisterForm(**request.form)
            )
        else:
            return redirect('/')
    
    @app.route("/logout")
    @login_required
    def logout():
        return logout_user()

    @app.get('/')
    def index_page():
        return render_template("index.html")
    
    x: list[function] = [login_page, register_page, index_page, logout]
    return x
