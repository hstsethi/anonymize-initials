import random


def genRandomInitial(input_initial: str) -> str:
    while True:
        rand_initial = chr(random.randint(65, 90))
        if rand_initial not in (input_initial, "I"):
            return rand_initial


def main() -> None:
    original_initials = ("H", "S")
    for initial in original_initials:
        anonymized_initial = genRandomInitial(initial)
        print(
            f"{initial}: {anonymized_initial}"
        )  # The output will also be a valid YAML


if __name__ == "__main__":
    main()
