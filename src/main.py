from argparse import ArgumentParser
from fcm import Fcm
from generator import Generator


class Main:
    parser: ArgumentParser()

    def __init__(self) -> None:
        self.parser = ArgumentParser()

    def parse_args(self):
        parser = ArgumentParser()
        parser.add_argument(dest='smoothing', type=float,
                            help="A number between 0 and 1 for the smoothing parameter")
        parser.add_argument(dest='context_size', type=int,
                            help="A number greater than 0 for the context size")
        parser.add_argument(dest='file_paths', type=str, nargs="*",
                            help="Files' paths to build the model")
        parser.add_argument('--prior',  type=str, required=False,
                            help="A sequence of n chars to start generating the text, n must be same length as context_size")
        parser.add_argument('--length', type=int, required=False,
                            help="A number greater than 0 that represents the length of the generated text")
        return parser.parse_args()

    def main(self):
        args = self.parse_args()
        fcm = Fcm(args.smoothing, args.context_size)

        for file_path in args.file_paths:
            fcm.add_file(file_path)

        if args.prior and args.length:
            generator = Generator(fcm)
            print(generator.generate(args.prior, args.length))


if __name__ == "__main__":
    Main().main()
