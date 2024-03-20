import argparse
from newmath.add import add
from newmath.mul import mul

def main():
    parser = argparse.ArgumentParser(description="Add and multiply two integers using newmath package.")
    parser.add_argument('integer1', type=int, help='First integer to add')
    parser.add_argument('integer2', type=int, help='Second integer to add')
    args = parser.parse_args()

    result_add = add(args.integer1, args.integer2)
    print(f"The sum of {args.integer1} and {args.integer2} is: {result_add}")
    
    result_mul = mul(args.integer1, args.integer2)
    print(f"The mul of {args.integer1} and {args.integer2} is: {result_mul}")

if __name__ == "__main__":
    main()