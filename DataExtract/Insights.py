import json
import pandas as pd
import re
import csv
import os

class Insights:

    def __init__(self , infilename="joined.json" , outfilename="processed.json"):
        self.json = json.load(open(infilename , "r"))
        self.outfilename = outfilename
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__) , "Data")))

    def Preprocess(self):
        for obj in self.json:
            obj["weight"] = next(iter(obj["additional"]["weight"]), None)
            obj["rank"] = next(iter(obj["additional"]["bestSelling"]["ranks"]), None)
            obj["description"] = obj["additional"]["description"]
            obj["stars"] = obj["stars"].split(" out")[0]
            obj["brand"] = obj["title"].split(" ")[0]
            obj["colors"] = [ " ".join(c.split(" ")[1:]) if len(c.split(" ")) > 1 else c for c in obj["additional"]["colors"]]
            del obj["additional"]

        with open("{}_complete.json".format(self.outfilename), "w" ) as f:
            json.dump(self.json , f)

        with open("{}_partial.csv".format(self.outfilename ), "w") as f:
            writer = csv.writer(f)
            writer.writerow([k for k,v in obj.items()])
            for obj in self.json:
                writer.writerow([v for k,v in obj.items()])


    def Color(self):
        self.Preprocess()
        with open("{}_color.csv".format(self.outfilename ), "w") as f:
            writer = csv.writer(f)
            cols = [k for k,v in self.json[0].items()] + ["Color" , "RGB"]
            writer.writerow(cols)
            for obj in self.json:
                for color in obj["colors"]:
                    writer.writerow([v for k,v in obj.items()] + [color , "NULL"])



if __name__ == "__main__":

    #Insights().Preprocess()
    Insights().Color()
