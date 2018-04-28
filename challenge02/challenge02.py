import os
import itertools

class NumberBase:

    base_digits = '0123456789abcdefghijklmnopqrstuvwxyz'

    @staticmethod
    def get_minimum_non_repeating_number(base):
        min_number_digits = ['1', '0'] + [NumberBase.base_digits[x] for x in range(2, base)]
        min_number = int(''.join(min_number_digits), base)

        return min_number

    @staticmethod
    def get_maximum_non_repeating_number(base):
        max_number_digits = [NumberBase.base_digits[x] for x in range(base - 1, -1, -1)]
        max_number = int(''.join(max_number_digits), base)

        return max_number


def main():
    os.chdir(os.path.dirname(__file__))

    input_file = open('submitInput.txt', 'r')
    input_file.readline()
    output_file = open('submitOutput.txt', 'w')

    for index, line in enumerate(input_file):
        base = len(line.rstrip())
        min_number = NumberBase.get_minimum_non_repeating_number(base)
        max_number = NumberBase.get_maximum_non_repeating_number(base)

        output_file.write('Case #{}: {}\n'.format(
            index + 1,
            max_number - min_number
        ))

    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main()
