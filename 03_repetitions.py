if __name__ == "__main__":
    dna_sequence = input()

    previous_char = dna_sequence[0]
    current_count = 1
    max_char = 1
    for dna_char in dna_sequence[1:]:
        if dna_char == previous_char:
            current_count += 1
        else:
            current_count = 1
        max_char = max(max_char, current_count)
        previous_char = dna_char

    print(max_char)
