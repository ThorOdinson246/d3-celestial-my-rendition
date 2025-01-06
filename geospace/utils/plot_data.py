def plot_data(constellation_id):
    import matplotlib.pyplot as plt
    from get_datas import get_constellation_name_by_id, get_constellation_polyline

    # Plot another constellation in same image
    constellation_lines=get_constellation_polyline(constellation_id)
    for line in constellation_lines:
        x = [point[0] for point in line] # RA values
        y = [point[1] for point in line] # Dec values
        plt.plot(x, y, color="cyan", linewidth=2) # Plot each segment
        plt.scatter(x, y, color="white", s=10) # Plot endpoints as dots
        plt.scatter(return_name_plot_position(constellation_id)[0], return_name_plot_position(constellation_id)[1], color="red", s=20)
        plt.text(return_name_plot_position(constellation_id)[0], return_name_plot_position(constellation_id)[1], get_constellation_name_by_id(constellation_id), color="white", fontsize=15)
    return True


def return_name_plot_position(constellation_id):
    import matplotlib.pyplot as plt
    import json 

    with open('constellation_data/constellations.json',encoding='utf-8') as f:
        data = json.load(f)
        for constellation in data["features"]:
            position=constellation["geometry"]["coordinates"]
            if constellation_id == constellation["id"] :
                return position
            

