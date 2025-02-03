from get_anonymized_initials import gen_random_initial

def main():
        initials = ("A", "T", "B")
        for initial in initials:
            anonymized_initial = gen_random_initial(initial)
            print(initial + ": " + anonymized_initial) # The output will also be a valid YAML

if __name__ == "__main__":
    main()

