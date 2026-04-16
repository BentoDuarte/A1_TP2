from flask import Flask, request, render_template

app = Flask(__name__)

produtos = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/produtos/adicionar", method="POST")
def adicionarProduto():
    id = request.form.get("id")
    nome = request.form.get("nome")
    preco = request.form.get("preco")
    quantidade = request.form.get("quantidade")

    produto = {"id": id,"nome": nome, "preco": preco, "quantidade":quantidade}

    produtos.append(produto)

    if produtos:
        return "Produto Acionado"
    return"Falha ao adicionar produto"

@app.route("/produtos/listar", method="GET")
def listarProdutos():
    if produtos:
        return render_template("lista.html", produtos = produtos)

    return"Nenhum produto encontrado"

if __name__ == "__main__":
    app.run(debug=True)
