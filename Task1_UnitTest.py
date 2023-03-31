import unittest

class TestInsertItem(unittest.TestCase):
    def test_insert_new_item(self):
        name = 'Notebook'
        category = 'Stationary'
        price = 5.5
        item_id = insert_item(name, category, price)
        self.assertTrue(isinstance(item_id, int))
        self.assertTrue(item_id > 0)

    def test_update_existing_item(self):
        name = 'Notebook'
        category = 'Stationary'
        price = 7.5
        item_id = insert_item(name, category, price)
        updated_price = 6.5
        updated_item_id = insert_item(name, category, updated_price)
        self.assertEqual(item_id, updated_item_id)