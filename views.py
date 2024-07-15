from config import app
from model import db, Order, orders_schema, order_schema
from flask import request, jsonify

# Creare un nuovo ordine
@app.route('/order', methods=['POST'])
def add_order():
    name = request.json['name']
    description = request.json.get('description', "")
    price = request.json['price']
    
    new_order = Order(name, description, price)
    
    db.session.add(new_order)
    db.session.commit()
    
    return order_schema.jsonify(new_order)

# Ottenere tutti gli ordini
@app.route('/order', methods=['GET'])
def get_orders():
    all_orders = Order.query.all()
    result = orders_schema.dump(all_orders)
    return jsonify(result)

# Ottenere un singolo ordine
@app.route('/order/<id>', methods=['GET'])
def get_order(id):
    order = Order.query.get(id)
    return order_schema.jsonify(order)

# Aggiornare un ordine
@app.route('/order/<id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get(id)
    
    name = request.json['name']
    description = request.json.get('description', "")
    price = request.json['price']
    
    order.name = name
    order.description = description
    order.price = price
    
    db.session.commit()
    
    return order_schema.jsonify(order)

# Eliminare un ordine
@app.route('/order/<id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()
    
    return order_schema.jsonify(order)

# Eseguire l'app Flask
if __name__ == '__main__':
    db.create_all()  # Crea tutte le tabelle
    app.run(debug=True)
