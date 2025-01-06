from plot_data import plot_data
from get_datas import get_constellation_name_by_id, get_constellation_polyline
import matplotlib.pyplot as plt
import json

all_constellations = []
def byamboom_everything_everywhere_all_at_once():

    # getting all the constellations 
    with open ('constellation_data/constellations.json', encoding='utf-8') as f:
        data = json.load(f)
        for constellation in data["features"]:
            all_constellations.append(constellation["id"])

    # plotting everything everywhere all at once
    plt.figure(figsize=(210, 140))
    my_star_map=plt.gca()
    my_star_map.set_facecolor("black")


    for constellation in all_constellations:
        plot_data(constellation)

    plt.title(get_constellation_name_by_id("ByamBoom"), color="white", fontsize=16)
    plt.xlabel("Right Ascension (RA)", color="white", fontsize=14)
    plt.ylabel("Declination (Dec)", color="white", fontsize=14)

    # Set tick parameters
    my_star_map.tick_params(axis='x', colors='white', labelsize=12)
    my_star_map.tick_params(axis='y', colors='white', labelsize=12)

    # Manually reverse the x-axis limits
    xlim = my_star_map.get_xlim()
    my_star_map.set_xlim(xlim[::-1])

    # Save the plot as an image
    plt.savefig(f"saved/ByaamBoomEverythingEverywhere.png", facecolor='black')
    # plt.show()
    return True


byamboom_everything_everywhere_all_at_once()
print("Image saved successfully")
