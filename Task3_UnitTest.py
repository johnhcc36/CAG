import unittest
from datetime import datetime
from inventory_management import *

class TestInventoryManagement(unittest.TestCase):

    def setUp(self):
        self.item1 = {"name": "Notebook", "category": "Stationary", "price": 5.5}
        self.item2 = {"name": "Key Chain", "category": "Gift", "price": 3}
        self.item3 = {"name": "Baggage Cover", "category": "Gift", "price": 15}
        self.dt1 = datetime(2022, 1, 1, 10, 0, 0)
        self.dt2 = datetime(2022, 1, 25, 10, 0, 0)
        
    def test_insert_item(self):
        # test inserting a new item
        item_id = insert_item(self.item1)
        self.assertIsNotNone(item_id)
        # test updating an existing item
        updated_item_id = insert_item(self.item1)
        self.assertEqual(updated_item_id, item_id)
        item = get_item_by_id(item_id)
        self.assertEqual(item["price"], self.item1["price"])
        
    def test_get_items_by_date_range(self):
        insert_item(self.item1)
        insert_item(self.item2)
        insert_item(self.item3)
        items, total_price = get_items_by_date_range(self.dt1, self.dt2)
        self.assertEqual(len(items), 3)
        self.assertEqual(total_price, 23.5)
        
    def test_get_items_by_category(self):
        insert_item(self.item1)
        insert_item(self.item2)
        insert_item(self.item3)
        result = get_items_by_category("Gift")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["category"], "Gift")
        self.assertEqual(result[0]["total_price"], 18)
        self.assertEqual(result[0]["count"], 2)
        
    def tearDown(self):
        clear_all_items()

if __name__ == '__main__':
    unittest.main()
