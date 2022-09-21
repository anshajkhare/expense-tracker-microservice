# Copyright (c) 2022. All rights reserved.

import json

import tornado.testing

from expense_service.tornado.app import (
    EXPENSE_TRACK_ENTRY_URI_FORMAT_STR
)

from tests.unit.tornado_app_handlers_test import (
    ExpenseServiceTornadoAppTestSetup
)


class TestAddressServiceApp(ExpenseServiceTornadoAppTestSetup):
    def test_address_book_endpoints(self):
        # Get all expenses in the expense tracker, must be ZERO
        r = self.fetch(
            EXPENSE_TRACK_ENTRY_URI_FORMAT_STR.format(id=''),
            method='GET',
            headers=None,
        )
        all_exps = json.loads(r.body.decode('utf-8'))
        self.assertEqual(r.code, 200, all_exps)
        self.assertEqual(len(all_exps), 0, all_exps)

        # Add an expense
        r = self.fetch(
            EXPENSE_TRACK_ENTRY_URI_FORMAT_STR.format(id=''),
            method='POST',
            headers=self.headers,
            body=json.dumps(self.exps0),
        )
        self.assertEqual(r.code, 201)
        exps_uri = r.headers['Expense']

        # POST: error cases
        r = self.fetch(
            EXPENSE_TRACK_ENTRY_URI_FORMAT_STR.format(id=''),
            method='POST',
            headers=self.headers,
            body='it is not json',
        )
        self.assertEqual(r.code, 400)
        self.assertEqual(r.reason, 'Invalid JSON body')
        
        # Get the added expense
        r = self.fetch(
            exps_uri,
            method='GET',
            headers=None,
        )
        self.assertEqual(r.code, 200)
        self.assertEqual(self.exps0, json.loads(r.body.decode('utf-8')))

        # GET: error cases
        r = self.fetch(
            EXPENSE_TRACK_ENTRY_URI_FORMAT_STR.format(id='no-such-id'),
            method='GET',
            headers=None,
        )
        self.assertEqual(r.code, 404)

        # Update that expense
        r = self.fetch(
            exps_uri,
            method='PUT',
            headers=self.headers,
            body=json.dumps(self.exps1),
        )
        self.assertEqual(r.code, 204)
        r = self.fetch(
            exps_uri,
            method='GET',
            headers=None,
        )
        self.assertEqual(r.code, 200)
        self.assertEqual(self.exps1, json.loads(r.body.decode('utf-8')))

        # PUT: error cases
        r = self.fetch(
            exps_uri,
            method='PUT',
            headers=self.headers,
            body='it is not json',
        )
        self.assertEqual(r.code, 400)
        self.assertEqual(r.reason, 'Invalid JSON body')
        r = self.fetch(
            EXPENSE_TRACK_ENTRY_URI_FORMAT_STR.format(id='1234'),
            method='PUT',
            headers=self.headers,
            body=json.dumps(self.exps1),
        )
        self.assertEqual(r.code, 404)

        # Delete that expense
        r = self.fetch(
            exps_uri,
            method='DELETE',
            headers=None,
        )
        self.assertEqual(r.code, 204)
        r = self.fetch(
            exps_uri,
            method='GET',
            headers=None,
        )
        self.assertEqual(r.code, 404)

        # DELETE: error cases
        r = self.fetch(
            exps_uri,
            method='DELETE',
            headers=None,
        )
        self.assertEqual(r.code, 404)

        # Get all expenses in the expense tracker, must be ZERO
        r = self.fetch(
            EXPENSE_TRACK_ENTRY_URI_FORMAT_STR.format(id=''),
            method='GET',
            headers=None,
        )
        all_exps = json.loads(r.body.decode('utf-8'))
        self.assertEqual(r.code, 200, all_exps)
        self.assertEqual(len(all_exps), 0, all_exps)


if __name__ == '__main__':
    tornado.testing.main()
