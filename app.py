from flask import Flask, render_template, request,redirect,url_for
import json

app = Flask(__name__)


@app.route('/', methods=['get'])
def index():  
    return render_template('index.html')

@app.route('/cadastro', methods=['post'])
def cadastro():
    codItem = request.form.get('codItem')
    desc = request.form.get('desc')
    medida = request.form.get('medida')
    fabricante = request.form.get('fabricante')
    quantidade = request.form.get('quantidade')
    precunit = request.form.get('precunit')

    #DICIONARIO DO ITEM ATUAL
    dici = {
        'codItem':codItem,
        'desc':desc,
        'medida':medida,
        'fabricante':fabricante,
        'quantidade':quantidade,
        'precunit':precunit,
    }
    arq = open('estoque.json', mode='r')
    dados = json.load(arq)
    dados = [d for d in dados]
    dados.append(dici)
    arq.close()
    arq = open('estoque.json', mode='w')
    arq.write(json.dumps(dados))
    return redirect(url_for('index'))

@app.route('/relatorio', methods=['get'])
def relatorio():
    with open('estoque.json', 'r') as arq:
        valorEstoque = json.loads(arq.readline()) 
    return render_template('cadastro.html', dados=valorEstoque)

@app.route('/tabela', methods=['get'])
def tabela():
    with open('estoque.json', 'r') as arq:
        valorEstoque = json.loads(arq.readline()) 
    return render_template("tabela.html", dados=valorEstoque)


if __name__ == '__main__':
    app.run(debug=True)
