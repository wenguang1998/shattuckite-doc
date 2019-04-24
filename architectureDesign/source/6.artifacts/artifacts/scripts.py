import argparse
import json
import logging
from generateUMLClass import  generateUMLClass


logger=logging.getLogger("Root")
logger.setLevel(logging.NOTSET)


parser = argparse.ArgumentParser()

parser.add_argument(
    '--data', '-d', type=argparse.FileType('r', encoding="utf8"))

parser.add_argument(
    '--out', '-o', type=argparse.FileType('w',encoding='utf8'))









if __name__ == "__main__":
    args = parser.parse_args()
    jsobj = json.load(args.data)
    logger.debug("start parsing")
    generateUMLClass(jsobj,args.out)

    

    

