# Insert some items
insert_or_update_item('Notebook', 'Stationary', 5.5)
insert_or_update_item('Key Chain', 'Gift', 3)
insert_or_update_item('Baggage Cover', 'Gift', 15)

# Get items within a date range
date_range = {'dt_from': '2022-01-01 10:00:00', 'dt_to': '2022-01-25 10:00:00'}
result = get_items_within_date_range(date_range['dt_from'], date_range['dt_to'])
print(json.dumps(result, indent=4))