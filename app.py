from flask import Flask, request, jsonify
from models import db, Order
from queue_processor import process_orders
import threading
from metrics import get_metrics

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Start the queue processor in a separate thread
queue_thread = threading.Thread(target=process_orders, daemon=True)
queue_thread.start()

@app.route('/order', methods=['POST'])
def create_order():
    data = request.json
    if not all(key in data for key in ['user_id', 'order_id', 'item_ids', 'total_amount']):
        return jsonify({"error": "Missing required fields"}), 400

    new_order = Order(
        order_id=data['order_id'],
        user_id=data['user_id'],
        item_ids=",".join(map(str, data['item_ids'])),
        total_amount=data['total_amount']
    )
    db.session.add(new_order)
    db.session.commit()

    # Add order to the processing queue (in-memory queue)
    from queue_processor import order_queue
    order_queue.put(new_order.order_id)

    return jsonify({"message": "Order created", "order_id": new_order.order_id}), 201


@app.route('/order/<order_id>', methods=['GET'])
def get_order_status(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order.to_dict()), 200


@app.route('/metrics', methods=['GET'])
def get_system_metrics():
    metrics = get_metrics()
    return jsonify(metrics), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)