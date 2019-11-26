import json

class ETL:

    def __init__(self,infilename = "outputfile2.json" , outfilename="joined.json"):

        self.infile = infilename
        self.outfile = outfilename
        self.js = json.load(open(infilename , "r"))

    def Join(self):
        base = [obj  for obj in self.js if obj["infoType"] == "base"]
        additional = [obj  for obj in self.js if obj["infoType"] == "additional"]
        for b in base:
            b["link"] = b["link"].split("?")[0]
            b["additional"]  = {}
            for a in additional:
                if a["url"].find(b["link"]) >= 0:
                    b["additional"] = a
        return base

    def Transform(self,merged):
        for obj in merged:
            obj = self.Clean(obj)
        return merged

    def Clean(self, obj):
        #print(obj)
        obj["additional"]["weight"] = [ w.strip(" ") for w in obj.get("additional" ,{}).get("weight" , [])]
        obj["additional"]["description"] = obj.get("additional" ,{}).get("description" , "").strip("\t\n")
        return obj

    def Load(self,complete):
        json.dump(complete , open(self.outfile , "w"))

    def Do(self):
        base = self.Join()
        base = self.Transform(base)
        self.Load(base)

if __name__ == "__main__":
    ETL("outputfile_21_10_21_41.json" , "joined_outputfile_21_10_21_41.json").Do()
