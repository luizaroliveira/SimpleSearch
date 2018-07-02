# -*- coding: utf-8 -*-
import engine
import unittest


class TestServer(unittest.TestCase):

    def test_load_index(self):
        """" Testing the creation of the index """
        engine.load_files('test_data')
        test_index = {
            'simple': set([1]),
            'test': set([1]),
            'file': set([1])
        }
        self.assertDictEqual(dict(engine.INDEX), test_index)

    def test_load_index_failure(self):
        """" Testing the creation of the index with an invalid data directory """
        with self.assertRaises(AttributeError):
            engine.load_files('not a valid path')


if __name__ == "__main__":
    unittest.main()
