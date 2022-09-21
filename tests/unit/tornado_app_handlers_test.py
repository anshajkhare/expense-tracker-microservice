# Copyright (c) 2022. All rights reserved.

import atexit
from io import StringIO
import json
import yaml

from tornado.ioloop import IOLoop
import tornado.testing

from expense_service.tornado.app import make_expense_service_app

from data import expense_data_suite


IN_MEMORY_CFG_TXT = '''
service:
  name: Expense Track Test
'''

with StringIO(IN_MEMORY_CFG_TXT) as f:
    TEST_CONFIG = yaml.load(f.read(), Loader=yaml.SafeLoader)


class ExpenseServiceTornadoAppTestSetup(tornado.testing.AsyncHTTPTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.headers = {'Content-Type': 'application/json; charset=UTF-8'}
        expense_data = expense_data_suite()
        keys = list(expense_data.keys())
        self.assertGreaterEqual(len(keys), 2)
        self.exps0 = expense_data[keys[0]]
        self.exps1 = expense_data[keys[1]]

    def get_app(self) -> tornado.web.Application:
        addr_service, app = make_expense_service_app(
            config=TEST_CONFIG,
            debug=True
        )

        addr_service.start()
        atexit.register(lambda: addr_service.stop())

        return app

    def get_new_ioloop(self):
        return IOLoop.current()


class ExpenseServiceTornadoAppUnitTests(ExpenseServiceTornadoAppTestSetup):
    def test_default_handler(self):
        r = self.fetch(
            '/does-not-exist',
            method='GET',
            headers=None,
        )
        info = json.loads(r.body.decode('utf-8'))

        self.assertEqual(r.code, 404, info)
        self.assertEqual(info['code'], 404)
        self.assertEqual(info['message'], 'Unknown Endpoint')


if __name__ == '__main__':
    tornado.testing.main()
