from flask import Flask

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False # Sensitive

@app.route("/")
def pagina_inicial():
    return "Continuous Integration and Continuous Delivery"