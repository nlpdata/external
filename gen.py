import json

arc_corpus = []
with open("./data/ARC_Corpus.txt", encoding='utf-8', errors='ignore') as f:
    l = f.readline()
    while l:
        arc_corpus += [l.strip().lower()]
        l = f.readline()

def gen(fin, fout):
    with open(fin, "r") as f:
        data = json.load(f)
    for qid in data:
        for i in range(len(data[qid])):
            doc = []
            for j in range(len(data[qid][i])):
                if data[qid][i][j][1] == 2:
                    doc += [arc_corpus[data[qid][i][j][0]]]
                else:
                    doc += [data[qid][i][j][0]]
            data[qid][i] = '\n'.join(doc)
    with open(fout, "w") as f:
        json.dump(data, f, indent=1)
        
        
gen("./data/arc_challenge_pointer.json", "arc_challenge.json")
gen("./data/arc_easy_pointer.json", "arc_easy.json")
gen("./data/openbookqa_pointer.json", "openbookqa.json")
