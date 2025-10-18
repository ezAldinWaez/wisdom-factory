"""Dream"""

import random
import time
from typing import Optional


class Dream:
    """A dream that can be actualized"""

    def __init__(self, description: str = "A beautiful dream", difficulty: float = 0.3):
        self.description: str = description
        self.difficulty: float = max(0.0, min(1.0, difficulty))
        self.actualized: bool = False
        self.attempts: int = 0
        self.start_time: Optional[float] = None

    def __str__(self) -> str:
        return self.description

    def actualize(self) -> bool:
        """Actualize the dream with random success rate"""
        if self.actualized:
            print(f"Dream already actualized: {self.description}")
            return True

        if self.start_time is None:
            self.start_time = time.time()

        self.attempts += 1

        success_chance = 1.0 - self.difficulty

        if random.random() < success_chance:
            elapsed = time.time() - self.start_time
            print(f"✨ Dream actualized after {self.attempts} attempts ({elapsed:.1f}s): {self.description}")
            self.actualized = True
            return True
        else:
            print(f"💭 Attempt {self.attempts} failed for: {self.description} (trying again...)")
            time.sleep(random.uniform(0.4, 0.9))  # Random delay
            return False


the_dream = Dream(
    description="Become an informatic engineer",
    difficulty=.85,
)
