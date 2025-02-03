
from get_anonymized_initials import gen_random_initial

def anonymize_initials_text():
    ORIGINAL_FILE = "lessons.html"
    original_text = open(ORIGINAL_FILE, "r").read()
    ORIGINAL_INITIALS = ('T', 'B', 'A', 'U')
    for initial in ORIGINAL_INITIALS:
        random_initial = gen_random_initial(initial)
        original_text = original_text.replace(initial, random_initial)
    output_file = "anonymized-test.html"
    with open(output_file, "w") as f:
        f.write(original_text)
anonymize_initials_text()

