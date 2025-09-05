import argparse
import requests

def download_file(url,localpath):
    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        with open(localpath,'wb') as  f :
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        return localpath

parser = argparse.ArgumentParser()

parser.add_argument("url",help="give the url to download the file")
parser.add_argument("output",help="give the name to save in the local disk")

args = parser.parse_args()

download_file(args.url,args.output)