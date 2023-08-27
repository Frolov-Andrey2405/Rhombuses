class RhombusPrinter:
    def __init__(self):
        self.printer = self.displayOutlineDiamond
        self.diamond_sizes = range(6)

    def main(self):
        print('Rhombuses:')

        for diamond_size in self.diamond_sizes:
            self.printer(diamond_size)
            print()
            self.displayFilledDiamond(diamond_size)
            print()

    def displayOutlineDiamond(self, size):
        for i in range(size):
            print(' ' * (size - i - 1), end='')
            print('/', end='')
            print(' ' * (i * 2), end='')
            print('\\')

        for i in range(size):
            print(' ' * i, end='')
            print('\\', end='')
            print(' ' * ((size - i - 1) * 2), end='')
            print('/')

    def displayFilledDiamond(self, size):
        for i in range(size):
            print(' ' * (size - i - 1), end='')
            print('/' * (i + 1), end='')
            print('\\' * (i + 1))

        for i in range(size):
            print(' ' * i, end='')
            print('\\' * (size - i), end='')
            print('/' * (size - i))


if __name__ == '__main__':
    printer = RhombusPrinter()
    printer.main()
