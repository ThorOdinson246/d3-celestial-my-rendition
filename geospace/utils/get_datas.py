import json

def get_constellation_polyline(constellation_id):
    constellation_lines = []
    try:
        with open('constellation_data/constellations.lines.json', encoding='utf-8') as f:
            data = json.load(f)
            # load the constellation lines of a particular constellation by id 
            for constellation in data["features"]:
                if constellation_id == constellation["id"] :
                    constellation_lines=constellation["geometry"]["coordinates"]
            print("Data returned successfully")
            return constellation_lines

    except FileNotFoundError:
        print("File not found: constellations.json")
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}")

def get_constellation_name_by_id(constellation_id):
    constellation_name = ""
    try:
        with open('constellation_data/constellations.json', encoding='utf-8') as f:
            data = json.load(f)
            # load the constellation lines of a particular constellation by id 
            for constellation in data["features"]:
                if constellation_id == constellation["id"] :
                    constellation_name=constellation["properties"]["name"]
            print("Data returned successfully")
            return constellation_name

    except FileNotFoundError:
        print("File not found: constellations.json")
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}")


if __name__ == "__main__":
    constellation_lines = get_constellation_polyline("Ori")
    print(constellation_lines)
    print(get_constellation_name_by_id("Ori"))

