import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print('Use 2 command-line arguments')
        sys.exit(1)

    # TODO: Read database file into a variable
    rows = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        sequence = file.read()
    # TODO: Find longest match of each STR in DNA sequence
    # Store each STR name in a list called STR
    STR = []
    Lmatches = []

    # loop to get the names of STR
    for key in rows[0].keys():
        # append the names to the list STR
        STR.append(key)

    for i in range(1, len(STR)):
        Lmatches.append(longest_match(sequence, STR[i]))

    # TODO: Check database for matching profiles
    match_1 = []
    for i in range(1, len(STR)):

        if match_1:
            k = 0
            for row in match_1:
                j = int(i)
                Check = False
                while Check == False:
                    if j > len(Lmatches):
                        Check = True
                    elif int(Lmatches[j-1]) != int(row[STR[j]]):
                        match_1.remove(match_1[k])
                        if not match_1:
                            print("No match")
                            return
                        else:
                            Check = True
                    else:
                        j += 1
                        continue
                k += 1

        elif not match_1:
            for row in rows:
                if int(Lmatches[i-1]) == int(row[STR[i]]):
                    match_1.append(row)

    print(match_1[0]["name"])

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
