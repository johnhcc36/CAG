inventory = []

# function to insert or update an item
def insert_or_update_item(name, category, price):
    # check if an item with the same name already exists
    for item in inventory:
        if item['name'] == name:
            # update the item with the new price and last updated date
            item['price'] = price
            item['last_updated_dt'] = datetime.now()
            return {'id': item['id']}

    # if the item does not exist, create a new one
    item = {
        'id': len(inventory) + 1,
        'name': name,
        'category': category,
        'price': price,
        'last_updated_dt': datetime.now()
    }
    inventory.append(item)
    return {'id': item['id']}

# function to retrieve items within a date range
def get_items_by_date_range(dt_from, dt_to):
    total_price = 0
    items = []
    for item in inventory:
        if dt_from <= item['last_updated_dt'] <= dt_to:
            items.append(item)
            total_price += item['price']
    return {'items': items, 'total_price': total_price}

# function to aggregate items by category
def get_items_by_category(category):
    categories = set(item['category'] for item in inventory)
    if category != 'all':
        categories = [category]

    results = []
    for category in categories:
        category_items = [item for item in inventory if item['category'] == category]
        total_price = sum(item['price'] for item in category_items)
        count = len(category_items)
        results.append({'category': category, 'total_price': total_price, 'count': count})
    return {'items': results}
