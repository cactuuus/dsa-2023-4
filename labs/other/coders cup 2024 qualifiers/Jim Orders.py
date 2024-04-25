
def jimOrders(orders):
    serve_time = []
    for customer, order in enumerate(orders, 1):
        time_tot = order[0] + order[1]
        serve_time.append((time_tot, customer))
    serve_time.sort()
    return [y for x, y in serve_time]

print(jimOrders([[8, 1], [4, 2], [5, 6], [3, 1], [4, 3]]))