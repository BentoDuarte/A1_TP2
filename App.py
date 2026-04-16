from flask import Flask, request, render_template
from werkzeug.utils import redirect

app = Flask(__name__)

produtos = []

@app.route("/")
def home():
    return render_template("index.html", produtos = produtos)

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/produtos/adicionar", methods=["POST"])
def adicionarProduto():
    id = request.form.get("id")
    nome = request.form.get("nome")
    preco = request.form.get("preco")
    quantidade = request.form.get("quantidade")

    if id is None:
        return "id vázio"
    elif nome is None:
        return "nome vázio"
    elif preco is None:
        return "preco vázio"
    elif quantidade is None:
        return "quantidade vázia"

    produto = {"id": id,"nome": nome, "preco": preco, "quantidade":quantidade}
    produtos.append(produto)

    print(produtos)

    if produtos:
        return redirect("/")
    return"Falha ao adicionar produto"

if __name__ == "__main__":
    app.run(debug=True)
