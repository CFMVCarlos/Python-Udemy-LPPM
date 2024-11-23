import fnmatch
import os
from typing import Generator


def find_albums(root: str, artist_name: str) -> Generator[tuple[str, str], None, None]:
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            subdir: str = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(
    albums: Generator[tuple[str, str], None, None]
) -> Generator[str, None, None]:
    for album in albums:
        for song in os.listdir(album[0]):  # We want the path, not the name of the album
            yield song


def complete_filename(root: str, extension: str) -> Generator[str, None, None]:
    for path, _, files in os.walk(root):
        for file in fnmatch.filter(files, f"*.{extension}"):
            absolute_path: str = os.path.abspath(path)
            yield os.path.join(absolute_path, file)
            # yield os.path.join(path, file)


def main() -> None:
    album_list: Generator[tuple[str, str], None, None] = find_albums(
        "Section12\\music", "Aerosmith"
    )
    song_list: Generator[str, None, None] = find_songs(album_list)
    # for a in album_list:
    #     print(a)
    # for s in song_list:
    #     print(s)

    all_filenames: Generator[str, None, None] = complete_filename("Section12", "emp3")
    print(next(all_filenames))
    print(next(all_filenames))
    print(next(all_filenames))
    print(next(all_filenames))


if __name__ == "__main__":
    main()
