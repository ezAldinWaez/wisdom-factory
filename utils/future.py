"""Future"""

from typing import Any
import time


class Future:
    """Represents a future state or value"""

    def __init__(self, value: Any = None, delay: float = 0.0):
        self.value: Any = value
        self.delay: float = delay
        self.created_at: float = time.time()
        self.resolved: bool = False

    def get(self) -> Any:
        """Get the future value, waiting if necessary"""
        if not self.resolved:
            time.sleep(self.delay)
            self.resolved = True
        return self.value

    def is_ready(self) -> bool:
        """Check if future is ready"""
        return time.time() - self.created_at >= self.delay


the_future: Future = None
