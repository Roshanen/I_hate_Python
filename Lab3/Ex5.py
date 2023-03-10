record_collection = {
  2548: {
    'albumTitle': 'Slippery When Wet',
    'artist': 'Bon Jovi',
    'tracks': ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    'albumTitle': '1999',
    'artist': 'Prince',
    'tracks': ['1999', 'Little Red Corvette']
  },
  1245: {
    'artist': 'Robert Palmer',
    'tracks': []
  },
  5439: {
    'albumTitle': 'ABBA Gold'
  }
}

def update_records(record, id, property, value):
    if value == "":
        try:
            del record[id][property]
        except:
            pass
        return record
    if property not in record[id]:
        if property != "tracks":
            record[id][property] = {}
        else:
            record[id][property] = []
    if property != "tracks":
        record[id][property] = value
    elif property == "tracks":
        record[id][property].append(value)
    return record
