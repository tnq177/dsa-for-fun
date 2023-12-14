"""
ID: toannq12
LANG: PYTHON3
TASK: rockers
"""


def main():
    with open("rockers.in", "r") as f:
        N, T, M = [int(x) for x in f.readline().strip().split()]
        songs = [int(x) for x in f.readline().strip().split()]

    cache = {}

    def dp(disk_left, minutes_left, song_idx):
        if song_idx >= N:
            return 0

        if disk_left < 0:
            return 0

        if (disk_left, minutes_left, song_idx) in cache:
            return cache[(disk_left, minutes_left, song_idx)]

        res = []
        # don't add song_idx
        res.append(dp(disk_left, minutes_left, song_idx + 1))
        # add song_idx to current minutes_left
        if minutes_left >= songs[song_idx]:
            res.append(1 + dp(disk_left, minutes_left - songs[song_idx], song_idx + 1))
        # ignore current minutes_left, use a new disk
        res.append(dp(disk_left - 1, T, song_idx))
        # ignore current minutes_left, use a new disk and also ignore song_idx
        res.append(dp(disk_left - 1, T, song_idx + 1))
        res = max(res)
        cache[(disk_left, minutes_left, song_idx)] = res
        return res

    max_song = dp(M - 1, T, 0)
    with open("rockers.out", "w") as f:
        f.write(f"{max_song}\n")


if __name__ == "__main__":
    main()
