def plot_data(constellation_id):
    import matplotlib.pyplot as plt
    from get_datas import get_constellation_name_by_id, get_constellation_polyline

    # Plot another constellation in same image
    constellation_lines=get_constellation_polyline(constellation_id)
    for line in constellation_lines:
        x = [point[0] for point in line] # RA values
        y = [point[1] for point in line] # Dec values
        plt.plot(x, y, color="cyan", linewidth=1) # Plot each segment
        plt.scatter(x, y, color="white", s=10) # Plot endpoints as dots
    return True
