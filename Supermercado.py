from flask import Flask, request, jsonify

app = Flask(__name__)

produtos = []
usuarios = []
setores = []
categorias = []

class Item:
    def __init__(self, _id, nome):
        self.id = _id
        self.nome = nome

# Endpoint para produtos
@app.route('/produtos', methods=['GET', 'POST'])
def handle_produtos():
    if request.method == 'GET':
        produto_id = request.args.get('id') # pegando id informado
        if produto_id: # se procurar por um id em especifico
            for produto in produtos:
                if produto.id == int(produto_id):
                    return jsonify(produto.__dict__), 200
            return f"Produto com ID {produto_id} não encontrado!", 404
        else: # exibindo a lista completa
            return jsonify([produto.__dict__ for produto in produtos]), 200
    elif request.method == 'POST': # criando e adicionando um novo item na lista
        data = request.json
        produto = Item(data['id'], data['nome'])
        produtos.append(produto)
        return jsonify(produto.__dict__), 201

# Endpoint para usuários
@app.route('/usuarios', methods=['GET', 'POST'])
def handle_usuarios():
    if request.method == 'GET':
        usuario_id = request.args.get('id') # pegando id informado
        if usuario_id: # se procurar por um id em especifico
            for usuario in usuarios:
                if usuario.id == int(usuario_id):
                    return jsonify(usuario.__dict__), 200
            return f"Usuário com ID {usuario_id} não encontrado!", 404
        else: # exibindo a lista completa
            return jsonify([usuario.__dict__ for usuario in usuarios]), 200
    elif request.method == 'POST': # criando e adicionando um novo item na lista
        data = request.json
        usuario = Item(data['id'], data['nome'])
        usuarios.append(usuario)
        return jsonify(usuario.__dict__), 201

# Endpoint para setores
@app.route('/setores', methods=['GET', 'POST'])
def handle_setores():
    if request.method == 'GET':
        setor_id = request.args.get('id') # pegando id informado
        if setor_id: # se procurar por um id em especifico
            for setor in setores:
                if setor.id == int(setor_id):
                    return jsonify(setor.__dict__), 200
            return f"Setor com ID {setor_id} não encontrado!", 404
        else: # exibindo a lista completa
            return jsonify([setor.__dict__ for setor in setores]), 200
    elif request.method == 'POST': # criando e adicionando um novo item na lista
        data = request.json
        setor = Item(data['id'], data['nome'])
        setores.append(setor)
        return jsonify(setor.__dict__), 201

# Endpoint para categorias
@app.route('/categorias', methods=['GET', 'POST'])
def handle_categorias():
    if request.method == 'GET':
        categoria_id = request.args.get('id') # pegando id informado
        if categoria_id: # se procurar por um id em especifico
            for categoria in categorias:
                if categoria.id == int(categoria_id):
                    return jsonify(categoria.__dict__), 200
            return f"Categoria com ID {categoria_id} não encontrada!", 404
        else: # exibindo a lista completa
            return jsonify([categoria.__dict__ for categoria in categorias]), 200
    elif request.method == 'POST': # criando e adicionando um novo item na lista
        data = request.json
        categoria = Item(data['id'], data['nome'])
        categorias.append(categoria)
        return jsonify(categoria.__dict__), 201