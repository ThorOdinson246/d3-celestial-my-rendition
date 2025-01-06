import matplotlib.pyplot as plt
from get_datas import get_constellation_name_by_id, get_constellation_polyline
from plot_data import plot_data
def save_constellation_to_image(constellation_id):
    constellation_lines=get_constellation_polyline(constellation_id)
    plt.figure(figsize=(15, 10))
    my_star_map=plt.gca()
    my_star_map.set_facecolor("black")

    plot_data(constellation_id)
    plot_data("Tau")
    plot_data("Cet")
    plot_data("Tri")
    plot_data("Gem")
    plot_data("CMi")
    plot_data("CMa")


    # Add labels and title
    plt.title(get_constellation_name_by_id(constellation_id), color="white", fontsize=16)
    plt.xlabel("Right Ascension (RA)", color="white", fontsize=14)
    plt.ylabel("Declination (Dec)", color="white", fontsize=14)

    # Set tick parameters
    my_star_map.tick_params(axis='x', colors='white', labelsize=12)
    my_star_map.tick_params(axis='y', colors='white', labelsize=12)

    # Manually reverse the x-axis limits
    xlim = my_star_map.get_xlim()
    my_star_map.set_xlim(xlim[::-1])

    # Save the plot as an image
    plt.savefig(f"saved/{get_constellation_name_by_id(constellation_id)}.png", facecolor='black')
    plt.show()
    return True

if __name__ == "__main__":
    save_constellation_to_image("Ori")
    print("Image saved successfully")

