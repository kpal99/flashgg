import json
import sys

def jsonFileCheck(path):
    try:
        with open(path, 'r') as file:
            data = file.read()
            json_data = json.loads(data)
    except ValueError as e:
        print(f"Error: {e} in file: {path}")

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file.json>")

    for file in sys.argv[1:]:
        jsonFileCheck(file)

if __name__ == "__main__":
    main()
