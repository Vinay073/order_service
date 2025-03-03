import queue
import time
from models import db, Order

# In-memory queue for order processing
order_queue = queue.Queue()

def process_orders():
    while True:
        try:
            # Get the next order ID from the queue
            order_id = order_queue.get(timeout=5)  # Wait for up to 5 seconds for an order
            order = Order.query.get(order_id)

            if order:
                print(f"Processing order {order_id}")
                order.status = 'Processing'
                db.session.commit()

                # Simulate order processing delay
                time.sleep(5)

                order.status = 'Completed'
                db.session.commit()
                print(f"Completed order {order_id}")

            order_queue.task_done()
        except queue.Empty:
            # No orders in the queue, continue waiting
            continue