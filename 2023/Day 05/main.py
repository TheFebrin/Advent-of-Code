from collections import defaultdict

from tqdm import tqdm


def get_location(s, maps):
    for k, v in maps.items():
        for destination_range, source_range, range_length in v:
            # print(f"{source_range} <= {s} <= {source_range + range_length}")
            if source_range <= s <= source_range + range_length:
                s = destination_range + (s - source_range)
                # print("new s: ", s)
                break
    return s

def solve(data):
    last_map = None
    seeds = None
    maps = defaultdict(list)
    for row in data:
        if "seeds:" in row:
            seeds = row.split(": ")[1].split(" ")
            continue

        if "-to-" in row:
            last_map = row.split(" ")[0]
            continue

        if len(row.strip()) > 0:
            maps[last_map].append([int(x) for x in row.split(" ")])

    seeds = [int(x) for x in seeds]
    locations = [get_location(s=s, maps=maps) for s in seeds]
    print(min(locations))


def get_location2(s, maps):
    arrays = [
        maps[x] for x in (
            "seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location",
        )
    ]
    for v in reversed(arrays):
        for source_range, destination_range, range_length in v:
            if source_range <= s < source_range + range_length:
                s = destination_range + (s - source_range)
                break
    return s

def solve2(data):
    last_map = None
    seeds = None
    maps = defaultdict(list)
    for row in data:
        if "seeds:" in row:
            seeds = row.split(": ")[1].split(" ")
            continue

        if "-to-" in row:
            last_map = row.split(" ")[0]
            continue

        if len(row.strip()) > 0:
            maps[last_map].append([int(x) for x in row.split(" ")])

    seeds = [int(x) for x in seeds]
    print("seeds: ", seeds)
    ans = None
    for i in tqdm(range(0, 10834441)):
        location = get_location2(s=i, maps=maps)
        for j in range(0, len(seeds), 2):
            if seeds[j] <= location < seeds[j] + seeds[j + 1]:
                print("GIIT: ", i, " <= ", location)
                ans = location
                break
        if ans:
            break

    check = get_location(s=ans, maps=maps)
    print("check: ", ans, " => ", check)


def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
        solve2(data)

if __name__ == "__main__":
    main()