import argparse
import sys

def calc(args):
    if args.z == 'add':
        return args.x + args.y

    elif args.z == 'nul':
        return args.x * args.y

    elif args.z == 'sub':
        return args.x - args.y

    elif args.z == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,
                        help="Enter first num."
                             "This is utility for calculation")

    parser.add_argument('--y', type=float, default=2.0,
                        help="Enter second num."
                             "This is utility for calculation ")

    parser.add_argument('--z', type=str, default="add",
                        help="This is utility for calculation ")


    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))