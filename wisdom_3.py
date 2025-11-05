"""Wisdom 3"""

from utils import *


class Transformation:
    """A transformation that grows through challenges"""

    def __init__(self, seed: str = "potential"):
        self.seed = seed
        self.growth_stages = []
        self.current_form = seed
        print(f"🌱 TRANSFORM: Planted seed of {seed}")

    def evolve(self, challenge: str) -> str:
        """Evolve through facing a challenge"""
        print(f"⚡ TRANSFORM: Facing challenge: {challenge}")
        self.growth_stages.append(challenge)

        # Transform the current form by embracing the challenge
        self.current_form = f"{self.current_form} + {challenge}"

        stage_num = len(self.growth_stages)
        print(f"🦋 TRANSFORM: Evolution stage {stage_num} complete!")
        print(f"✨ TRANSFORM: Current form: {self.current_form}")

        return self.current_form

    def bloom(self) -> None:
        """Reveal the final transformation"""
        print(f"\n🌸 TRANSFORM: Final transformation achieved!")
        print(f"🌟 TRANSFORM: From '{self.seed}' through {len(self.growth_stages)} challenges:")
        for i, stage in enumerate(self.growth_stages, 1):
            print(f"   Stage {i}: Embraced '{stage}'")
        print(f"🎆 TRANSFORM: Emerged as: {self.current_form}")
        print(f"\n💎 WISDOM: Growth happens not despite challenges, but because of them.\n")


# The journey of transformation
transformation = Transformation("a spark of curiosity")

# Evolve through challenges
transformation.evolve("doubt")
transformation.evolve("failure")
transformation.evolve("persistence")
transformation.evolve("understanding")

# Reveal the transformation
transformation.bloom()
