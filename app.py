from wise_sentence import lines
from markov import Markov

wise = Markov()

def line_parser(lines):
    for line in lines:
        if not line:
            continue
        yield line[3:].split('-')[0][:-1]

def main():
    wise_maker = line_parser(lines.split('\n'))
    next(wise_maker)
    while True:
        try:
            wise_saying = next(wise_maker)
            wise.train(wise_saying)
        except StopIteration as e:
            break
    for i in range(10):
        print(i + 1, wise.make_sentence())

if __name__ == "__main__":
    main()