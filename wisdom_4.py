"""Wisdom 4: Small steps create lasting progress."""


def build_progress(goal: str, steps: list[str]) -> None:
    """Reach a goal by taking one manageable step at a time."""
    progress = 0

    print(f"Goal: {goal}")
    for step in steps:
        progress += 1
        print(f"  Step {progress}: {step}")

    print("Wisdom: Great journeys are built from small, steady steps.")


if __name__ == "__main__":
    build_progress(
        "learn something new",
        ["begin with curiosity", "practice patiently", "share what you learn"],
    )
