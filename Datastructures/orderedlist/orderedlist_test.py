import unittest

from orderedlist import LinkedList

class LinkedListTests(unittest.TestCase):
    #def setUp(self):
    #    self.list = LinkedList()

    def test_asc_ordered_list(self):
        Lst=LinkedList()
        Lst.asc_ordered_list(10)
        Lst.asc_ordered_list(20)

    # def test_asc_ordered_list_search_item_delete_item(self):
    #     Lst=LinkedList()
    #     Lst.asc_ordered_list(10)
    #     Lst.asc_ordered_list(20)
    #     Lst.asc_ordered_list(30)
    #     Lst.search_item(10)
    #     self.assertEqual(Lst.delete_item(1),10)
    def test_asc_ordered_list_search_item(self):
        Lst=LinkedList()
        Lst.asc_ordered_list(10)
        self.assertEqual(Lst.delete_item(122),Lst)
