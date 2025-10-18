"""Helpers"""
from typing import Any
from utils.future import Future


def create(future: Future | None = None) -> Any:
    """Initialize and activate the future"""
    print("🔧 CREATE: Starting future creation process...")
    print(f"🔍 CREATE: Input future object: {future}")

    if future is None:
        print("⚠️ CREATE: No future provided, creating default future...")
        future = Future(value=5, delay=0.1)
        print(f"✨ CREATE: Created new Future with value={future.value}, delay={future.delay}s")
    else:
        print(f"📋 CREATE: Using provided future - value={future.value}, delay={future.delay}s")

    print("⏳ CREATE: Resolving future value...")
    result = future.get()
    print(f"🎯 CREATE: Future resolved! Final value: {result}")
    print("✅ CREATE: Future creation process complete!")

    return result
