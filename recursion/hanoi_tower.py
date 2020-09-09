def hanoi_tower(height, init_pole, to_pole, with_pole):
    """Simulates solving a hanoi tower problem which obeys three restrictions:
    1. Move a tower of height-1 to an intermediate pole, using final pole.
    2. Move the remaining disk to the final pole.
    3. Move the tower of height-1 from the intermediate pole to the final
    pole using the original pole."""
    if height >= 1:
        hanoi_tower(height - 1, init_pole, with_pole, to_pole)
        move_disk(init_pole, to_pole)
        hanoi_tower(height - 1, with_pole, to_pole, init_pole)


def move_disk(from_pole, to_pole):
    print(f"Moving disk from {from_pole} to {to_pole}")
