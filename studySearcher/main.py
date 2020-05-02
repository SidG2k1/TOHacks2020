"""
"""
def summarize(text):
    import requests
    r = requests.post(
    "https://api.deepai.org/api/summarization",
    data={
        'text': 'YOUR_TEXT_HERE',
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    return r.json()

def auto_summarize(text):
    # TODO: implement
    return text

def best_studies(text, n = 5):
    """
    Returns the top n studies for text.
    A 'study' is [Title, Summary, Journal, URL]
    """
    import csv
    from similarity import similarity_score
    studies_csv = open('./metadata.csv', mode = 'r')
    csv_reader = csv.reader(studies_csv, delimiter=',')
    rankings = []
    for row, vals in enumerate(csv_reader[1:]):
        rankings.append([similarity_score(text, vals[1]), row])
    rankings.sort(key = lambda data: data[0])
    tops = rankings[::-1][:5]
    ret = []
    for i in tops:
        to_add = csv_reader[1 + i[1]]
        ret.append([to_add[0], auto_summarize(to_add[1]), to_add[2], to_add[3]])
        # TODO: implement and integrate summarize function
    return ret

if __name__ == "__main__":
    read = 'testing here'  # replace with source file
    print(best_studies(read))
