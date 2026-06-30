import pandas as pd


def flatten_dict(row, data, main):
    for key, val in data.items():
        if isinstance(val, dict):
            next_main = f"{main}.{key}" if main else key
            row = flatten_dict(row, val, next_main)
        elif not key.startswith("@odata"):
            nk = f"{main}.{key}" if main else key
            row[nk] = val
    return row


def explode_lists(data):
    expanded = []
    for record in data:
        list_found = False
        for key, val in record.items():
            if isinstance(val, list):
                list_found = True
                for item in val:
                    new_record = {}
                    for parent_key, parent_val in record.items():
                        if parent_key == key or parent_key.startswith("@odata"):
                            continue
                        new_record[parent_key] = parent_val
                    if isinstance(item, dict):
                        new_record = flatten_dict(new_record, item, "")
                    else:
                        new_record[key] = item

                    expanded.append(new_record)
        if not list_found:
            expanded.append(record)
    return expanded


def data_processor(data):
    data = explode_lists(data)
    cleaned = []
    for record in data:
        new_row = {}
        for key, val in record.items():
            if isinstance(val, dict):
                new_row = flatten_dict(new_row, val, key)
            elif not key.startswith("@odata"):
                new_row[key] = val
        cleaned.append(new_row)
    return cleaned
def frame_data(data):
    return pd.DataFrame(data)

if __name__ == "__main__":
    pass
