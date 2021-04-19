import sys
from wbib.wbib import render_dashboard
import requests
from pybtex.database.input import bibtex
from tqdm import tqdm
import time

# Set functions 

def format_ids(ids):
    formatted_readings = "{"
    for i in ids:
        formatted_readings = formatted_readings + "wd:" + i + " "
    formatted_readings = formatted_readings + " }"
    return formatted_readings

def get_qid_for_title(title):
    """
    Gets the best Wikidata candidate from the title of the paper. 
    """
    api_call = f"https://www.wikidata.org/w/api.php?action=wbsearchentities&search={title}&language=en&format=json"
    api_result = requests.get(api_call).json()
    if api_result["success"] == 1:
        return(api_result["search"][0]["id"])


parser = bibtex.Parser()
bibtexFile= parser.parse_file(sys.argv[1])   

list_of_qids = []
print("===== Querying Wikidata to get IDs =====")
for i in tqdm(bibtexFile.entries):
    title = bibtexFile.entries[i].fields["title"]
    title = title.replace("{", "")
    title = title.replace("}", "")
    try:
        list_of_qids.append(get_qid_for_title(title))
    except:
        tqdm.write(f"Failed for {title}")
    time.sleep(0.3)

formatted_readings = format_ids(list_of_qids)
with open("index.html", "w") as f:
    html = render_dashboard(formatted_readings)
    f.write(html)

