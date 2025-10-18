"""Past"""


class Past(dict):
    """A dictionary that announces when it's being deleted"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update({
            "memories": ["childhood dreams", "old mistakes", "forgotten lessons"],
            "regrets": ["missed opportunities", "words unsaid"],
            "achievements": ["small victories", "lessons learned"]
        })
        print(f"📖 PAST: Populated with {len(self)} categories of memories")

    def __del__(self):
        print("🔥 PAST: Past is being deleted...")
        print(f"🗑️ PAST: Releasing {len(self)} memory categories")
        for key, value in self.items():
            print(f"   💨 PAST: Letting go of {key}: {value}")
        print("✨ PAST: Past successfully released - making room for the future!")


the_past = Past()
