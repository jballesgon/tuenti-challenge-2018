import os

def main():
    os.chdir(os.path.dirname(__file__))

    input_file = open('submitInput.txt', 'r')
    input_file.readline()
    output_file = open('submitOutput.txt', 'w')

    for index, line in enumerate(input_file):
        (horizontal, vertical) = (int(x) for x in line.split())
        output_file.write('Case #{}: {}\n'.format(
            index + 1,
            (horizontal - 1) * (vertical - 1)
        ))

    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main()
