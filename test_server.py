# -*- coding: utf-8 -*-
import engine
import server
import unittest
import multiprocessing
import time

class TestServer(unittest.TestCase):

    def test_run(self):
        """" Testing if server can open the socket and query the engine for a list """
        try:
            run = multiprocessing.Process(target=server.run, args=(9002, ))
            run.start()
            # Wait a reasonable time for the server to boot.
            time.sleep(3)
            x = engine.query('test query')
            self.assertEqual(type(x), list)
        finally:
            run.terminate()


if __name__ == "__main__":
    unittest.main()
