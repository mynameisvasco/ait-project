from main import Main
from sys import argv

main = Main()
args = main.parse_args()

assert args.file_path == argv[1]
assert args.smoothing == float(argv[2])
assert args.context_size == int(argv[3])
assert args.prior == None or args.prior == argv[4].split("=")[1]
assert args.length == None or args.length == int(argv[5].split("=")[1])
