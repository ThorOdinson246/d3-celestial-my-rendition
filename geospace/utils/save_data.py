import matplotlib.pyplot as plt
from get_datas import get_constellation_name_by_id, get_constellation_polyline
from plot_data import plot_data
def save_constellation_to_image(constellation_id):
    constellation_lines=get_constellation_polyline(constellation_id)
    plt.figure(figsize=(15, 15))
    my_star_map=plt.gca()
    my_star_map.set_facecolor("black")

    # Plot constellation lines and endpoints
    for line in constellation_lines:
        x = [point[0] for point in line] # RA values
        y = [point[1] for point in line] # Dec values
        plt.plot(x, y, color="cyan", linewidth=1) # Plot each segment
        plt.scatter(x, y, color="white", s=10) # Plot endpoints as dots

    # plot_data("Scl")
    # plot_data("CMa")
    # plot_data("Eri")
    # plot_data("Ori")
    # plot_data("Mon")
    # plot_data("Hya")
    

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

