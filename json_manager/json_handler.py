import json


def read_json():
    """
    Retrieves the blog posts data from the JSON storage.
    """
    try:
        with open('json_storage/posts.json', 'r', encoding="utf8") as json_file:
            # a file can be empty but containing a formatting signs, spaces -> strip()
            raw_data = json_file.read().strip()
            if not raw_data:
                print('Warning: empty JSON storage!')
                return []
            json_data = json.loads(raw_data)
        return json_data
    except Exception as error:
        print(f"Error reading blog post data: {error}")
        return None


def write_json(data):
    """
    Writes the blog posts data into the JSON storage.
    """
    try:
        with open('json_storage/posts.json', 'w', encoding="utf8") as json_file:
            json.dump(data, json_file, indent=4)
            return True
    except Exception as error:
        print(f"Error writing blog post data: {error}")
        return None
