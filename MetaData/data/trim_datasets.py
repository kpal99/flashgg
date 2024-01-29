import json
import math
import sys
import os

def rename2orig(jsonFile):
    #make sure archive folder exists
    if not os.path.exists('archive'):
        os.makedirs('archive')

    #copy json file to archive
    os.system(f"cp {jsonFile} archive/")
    os.rename(jsonFile + ".trimmed", jsonFile)
    print(f"Renamed {jsonFile}.trimmed to {jsonFile}, original file moved to archive")
    print()


def reduce_files(dataset):
    reduce_ratio = 10
    lenVal = math.ceil(len(dataset['files']) / reduce_ratio)
    dataset['files'] = dataset['files'][:lenVal]

def trim_datasets(jsonFile):
    with open(jsonFile, 'r') as f:
        jsonData = json.load(f)
        for dataset in jsonData:
            reduce_files(jsonData[dataset])

    with open(jsonFile + '.trimmed', 'w') as f:
        json.dump(jsonData, indent=4, sort_keys=True, fp=f)
        # message of output file written
        print(f"Wrote trimmed file to {jsonFile}.trimmed")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python trim_datasets.py <jsonFile(s)>")

    for jsonFile in sys.argv[1:]:
        trim_datasets(jsonFile)
        rename2orig(jsonFile)
