# Example of approximate solution using greedy technique

# find the minimum number of radio stations which covers all states
# REF: Grokking algorithm, loc: 1806

stations = {
    "one": {'id', 'nv', 'ut'},
    "two": {'wa', 'mt', 'id'},
    "three": {'or', 'ca', 'nv'},
    "four": {'nv', 'ut'},
    "five": {'ca', 'az'},
}

stations_needed = {'wa', 'mt', 'id', 'nv', 'ut', 'or', 'ca', 'az'}
final_stations = set()

while stations_needed:
    states_covered = set()
    station = None

    for station_name, station_states in stations.items():
        covered = station_states & stations_needed
        if len(covered) > len(states_covered):
            states_covered = covered
            station = station_name

    stations_needed -= states_covered
    final_stations.add(station)

if __name__ == "__main__":
    print(final_stations)
