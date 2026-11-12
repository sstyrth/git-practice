orders = [100, 200, 300]

total_orders_value = sum(orders)
average_order_value = total_orders_value / len(orders)

print(f"Total orders value: {total_orders_value}")
print(f"Average order value: {average_order_value}")
print(f"Number of orders: {len(orders)}")
print("Testing Git reset")

# Data quality validation

if all(order > 0 for order in orders):
    print("Data validation successful")
else:
    print("Invalid order values detected")