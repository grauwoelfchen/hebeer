#!/usr/bin/env python
# encoding: utf-8

import unittest
import hebeer

class HebeerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = hebeer.app.test_client()
        hebeer.app.config['USERNAME'] = 'Hebeer'
        hebeer.init()

    def tearDown(self):
        pass

    def test_index(self):
        rv = self.app.get('/')
        assert 'Hello, Hebeer!' in rv.data
        assert 'Index' in rv.data

    def test_show(self):
        rv = self.app.get('/9')
        assert 'Hello, Hebeer!' in rv.data
        assert 'Repo id is 9' in rv.data

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(HebeerTestCase))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
