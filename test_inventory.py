import unittest
from inventory_management import Inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()

    def test_add_item(self):
        self.inventory.add_item('1', 'Item 1', 10, 5.99)
        self.assertIn('1', self.inventory.items)

        self.inventory.add_item('1', 'Item 2', 20, 10.99)
        self.assertNotEqual(self.inventory.items['1']['name'], 'Item 2')

    def test_remove_item(self):
        self.inventory.add_item('2', 'Item 2', 20, 10.99)
        self.inventory.remove_item('2')
        self.assertNotIn('2', self.inventory.items)

        self.inventory.remove_item('3')

    def test_update_item(self):
        self.inventory.add_item('3', 'Item 3', 30, 15.99)
        self.inventory.update_item('3', name='Updated Item 3', quantity=40, price=20.99)
        self.assertEqual(self.inventory.items['3']['name'], 'Updated Item 3')
        self.assertEqual(self.inventory.items['3']['quantity'], 40)
        self.assertEqual(self.inventory.items['3']['price'], 20.99)

        self.inventory.update_item('4', name='New Item', quantity=50, price=25.99)

    def test_list_items(self):
        self.assertEqual(self.inventory.list_items(), None)

        self.inventory.add_item('4', 'Item 4', 40, 25.99)
        self.inventory.add_item('5', 'Item 5', 50, 30.99)
        self.assertIsNotNone(self.inventory.list_items())

    def test_search_by_name(self):
        self.inventory.add_item('6', 'Apple', 100, 0.5)
        self.inventory.add_item('7', 'Banana', 200, 0.3)
        self.inventory.add_item('8', 'Orange', 150, 0.4)
        self.assertEqual(self.inventory.search_by_name('apple'), None)
        self.assertEqual(self.inventory.search_by_name('Banana'), [('Banana', 200, 0.3)])

        self.assertEqual(self.inventory.search_by_name('Grapes'), [])

    def test_calculate_inventory_value(self):
        self.assertEqual(self.inventory.calculate_inventory_value(), None)

        self.inventory.add_item('9', 'Item 6', 60, 35.99)
        self.inventory.add_item('10', 'Item 7', 70, 40.99)
        self.assertIsNotNone(self.inventory.calculate_inventory_value())

if __name__ == '__main__':
    unittest.main()
