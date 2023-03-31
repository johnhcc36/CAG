from datetime import datetime
from typing import List, Dict
import json

inventory = {}  # dictionary to store item records

def insert_or_update_item(name: str, category: str, price: float) -> Dict[str, int]:


    if name in inventory:
        inventory[name]['price'] = price
        inventory[name]['last_updated_dt'] = datetime.now()
        return {'id': inventory[name]['id']}
    else:
        new_id = len(inventory) + 1  # generate new ID
        inventory[name] = {
            'id': new_id,
            'name': name,
            'category': category,
            'price': price,
            'last_updated_dt': datetime.now()
        }
        return {'id': new_id}

def get_items_within_date_range(dt_from: str, dt_to: str) -> Dict[str, any]:

    items_within_date_range = []
    total_price = 0
    dt_from_obj = datetime.strptime(dt_from, '%Y-%m-%d %H:%M:%S')
    dt_to_obj = datetime.strptime(dt_to, '%Y-%m-%d %H:%M:%S')
    for item in inventory.values():
        if dt_from_obj <= item['last_updated_dt'] <= dt_to_obj:
            items_within_date_range.append(item)
            total_price += item['price']
    return {'items': items_within_date_range, 'total_price': total_price}
