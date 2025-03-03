from models import Order

def get_metrics():
    total_orders = Order.query.count()
    completed_orders = Order.query.filter_by(status='Completed').count()
    pending_orders = Order.query.filter_by(status='Pending').count()
    processing_orders = Order.query.filter_by(status='Processing').count()

    # Calculate average processing time for completed orders
    completed_orders_list = Order.query.filter_by(status='Completed').all()
    total_processing_time = sum(
        (order.updated_at - order.created_at).total_seconds()
        for order in completed_orders_list
    )
    avg_processing_time = total_processing_time / completed_orders if completed_orders > 0 else 0

    return {
        "total_orders_processed": total_orders,
        "average_processing_time_seconds": avg_processing_time,
        "order_counts_by_status": {
            "pending": pending_orders,
            "processing": processing_orders,
            "completed": completed_orders
        }
    }