from typing import Literal

class Notification:
    def __init__(self, category: Literal['success', 'error'], message: str) -> None:
        self.category = category
        self.message = message
