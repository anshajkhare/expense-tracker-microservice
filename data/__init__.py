# Copyright (c) 2022. All rights reserved.

import glob
import json
import os
from typing import Dict, Sequence

EXPS_SERVICE_TEST_DATA_DIR = os.path.abspath(os.path.dirname(__file__))


EXPENSE_DATA_DIR = os.path.abspath(os.path.join(
    EXPS_SERVICE_TEST_DATA_DIR,
    'expenses'
))

EXPENSE_FILES = glob.glob(EXPENSE_DATA_DIR + '/*.json')


def expense_data_suite(
    json_files: Sequence[str] = EXPENSE_FILES
) -> Dict[str, Dict]:
    exps_data_suite = {}

    for fname in json_files:
        nickname = os.path.splitext(os.path.basename(fname))[0]
        with open(fname, mode='r', encoding='utf-8') as f:
            exps_json = json.load(f)
            exps_data_suite[nickname] = exps_json

    return exps_data_suite
