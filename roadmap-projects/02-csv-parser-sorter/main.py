headers = []
values = []

# Project: cvs-parser-sorter

with open("./data.csv", "r") as file:
    for index, line in enumerate(file):
        if index == 0:
            headers = line.strip().split(",")
        else:
            values.append(dict(zip(headers, line.strip().split(","))))

def clean(rows):
    cleaned = []
    for row in rows:
        try:
            if row["name"] == "":
                continue
            if row["score"] == "":
                continue
            if row["age"] == "":
                row["age"] = None
                row["score"] = int(row["score"])
            else:
                row["age"] = int(row["age"])
                row["score"] = int(row["score"])
            cleaned.append(row)
        except ValueError:
            continue
    return cleaned

def findMean(rows):
    scores = [row["score"] for row in rows]
    return round(sum(scores) / len(scores), 2)

print(findMean(clean(values)))
