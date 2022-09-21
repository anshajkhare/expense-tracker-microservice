# Copyright (c) 2022. All rights reserved.

from typing import Dict
import uuid


class ExpenseTrackerService:
    def __init__(
        self,
        config: Dict
    ) -> None:
        # TODO FIXME full class is just dummy stubs
        self.exps: Dict[str, Dict] = {}

    def start(self):
        # TODO FIXME
        self.exps = {}

    def stop(self):
        # TODO FIXME
        pass

    async def create_expense(self, value: Dict) -> str:
        # TODO FIXME
        key = uuid.uuid4().hex
        self.exps[key] = value
        return key

    async def get_expense(self, key: str) -> Dict:
        # TODO FIXME
        return self.exps[key]

    async def update_expense(self, key: str, value: Dict) -> None:
        # TODO FIXME
        self.exps[key]  # will cause exception if key doesn't exist
        self.exps[key] = value

    async def delete_expense(self, key: str) -> None:
        self.exps[key]  # will cause exception if key doesn't exist
        del self.exps[key]

    async def get_all_expenses(self) -> Dict[str, Dict]:
        # TODO FIXME
        return self.exps
