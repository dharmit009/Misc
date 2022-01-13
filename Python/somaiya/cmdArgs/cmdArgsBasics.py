import sys

if __name__ == "__main__":
    print(f"Argument counts: ", {len(sys.argv)});
    for i , arg in enumerate(sys.argv):
        print(f'Argument {i>6}: {arg}')
