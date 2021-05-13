from argparse import ArgumentParser


class Config:

    def __init__(self, input_path, delimiter):
        self.__input_path = input_path
        self.__delimiter = delimiter

    def get_input_path(self):
        return self.__input_path

    def get_delimiter(self):
        return self.__delimiter

    def __str__(self):
        return "Input: " + self.__input_path + " Delimiter: " + self.__delimiter


class ArgParser:

    @staticmethod
    def parse_argument():
        arg_parser = ArgParser.create_parser()
        args = arg_parser.parse_args()
        return Config(args.filepath, args.delimiter)

    @staticmethod
    def create_parser():
        parser = ArgumentParser(description='Wyszukiwanie wzorca w tekscie')
        parser.add_argument('filepath', help="Sciezka do pliku z szukanym wzorcem")
        parser.add_argument('-d', '--delimiter', help="Symbol rozdzielajacy wartosci", default=' ', required=True)
        return parser
