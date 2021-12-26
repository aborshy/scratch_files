def sort_by_name(arr):
    output = []
    num_words = {
        "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight",
        "9": "nine",
    }
    the_weird_ones = {
        "10": "ten", "11": "eleven", "12": "twelve",
    }
    tens = {
        "2": "twen", "3": "thir", "4": "for", "5": "fif",
        "6": "six", "7": "seven", "8": "eigh", "9": "nine",
    }

    def double_digits(word: str):
        """
        takes in a double-digit string
        :return: word version of a number
        """
        if int(word) == 0:
            return "zero"
        if 0 < int(word) < 10:
            return num_words[word[-1]]
        if 9 < int(word) < 13:
            return the_weird_ones[word]
        if 12 < int(word) < 20:
            if int(word) == 14:
                return "fourteen"
            return tens[word[-1]] + "teen"
        if 19 < int(word) and word[-1] == '0':
            return tens[word[0]] + "ty "
        if 19 < int(word):
            return tens[word[0]] + "ty " + num_words[word[-1]]

    for n in arr:
        if len(str(n)) == 3:
            hundreds = num_words[str(n)[0]] + " hundred "
            if str(n)[-2:] != '00':
                word_output = hundreds + double_digits(str(n)[1:])
                output.append((n, word_output.strip()))
            else:
                output.append((n, hundreds.strip()))
        else:
            output.append((n, double_digits(str(n)).strip()))

    output.sort(key=lambda x: x[1])
    return [a for a, b in output]