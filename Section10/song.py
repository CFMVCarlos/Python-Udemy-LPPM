from os import name
from typing import Optional


class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist_name (str): The name of the artist responsible for the song
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title: str, artist_name: str, duration: int = 0) -> None:
        self.title: str = title
        self.artist: str = artist_name
        self.duration: int = duration

    def get_title(self) -> str:
        """Returns the title of the song"""
        return self.title

    name: property = property(get_title)


class Album:
    """Class to represent an Album, using its track list

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist_name (str): The artist name responsible for the album. If not specified, the artist will default to an artist with the name "Various Artists"
        tracks (List[Song]): A list of the songs on the album

    Methods:
        add_song: Used to add a new song to the album's track list
    """

    def __init__(self, name: str, year: int, artist_name: Optional[str] = None) -> None:
        self.name: str = name
        self.year: int = year
        if artist_name is None:
            self.artist_name: str = "Various Artists"
        else:
            self.artist_name: str = artist_name

        self.tracks: list[Song] = []

    def add_song(self, title: str, position: Optional[int] = None) -> None:
        """Adds a song to the track list

        Args:
            title (str): The title of the song to add
            position (Optional[int]): If specified, the song will be added to that position in the track list - inserting it between other songs if necessary. Otherwise, the song will be added to the end of the list
        """
        find_song: Artist | Album | Song | None = find_object(title, self.tracks)
        if find_song is None:
            song = Song(title, self.artist_name)
            if position is None:
                self.tracks.append(song)
            else:
                self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist
        albums (List[Album]): A list of the albums by this artist. The list includes only those albums in this collection, it is not an exhaustive list of the artist's discography

    Methods:
        add_album: Used to add a new album to the artist's discography
    """

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.albums: list[Album] = []

    def add_album(self, album: Album) -> None:
        """Adds a new album to the list

        Args:
            album (Album): Album object to add to the list. If the album is already present, it will not be added again
        """
        self.albums.append(album)

    def add_song(self, name: str, year: int, title: str) -> None:
        """Add a new song to the collection of albums

        This method will add the song to an album in the collection. A new album will be created in the collection if it does not already exist

        Args:
            name (str): The name of the album
            year (int): The year the album was released
            title (str): The title of the song
        """
        find_album: Artist | Album | Song | None = find_object(name, self.albums)
        if find_album is None:
            album = Album(name, year, self.name)
            self.add_album(album)
        elif isinstance(find_album, Album):
            album: Album = find_album
        else:
            return
        album.add_song(title)


def find_object(
    field: str, object_list: list[Artist] | list[Album] | list[Song]
) -> Artist | Album | Song | None:
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, returning it if so"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data() -> list[Artist]:
    # new_artist: Artist | None = None
    # new_album: Album | None = None
    artist_list: list[Artist] = []

    with open("Section10/albums.txt", "r") as albums:
        for line in albums:
            # Data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(
                line.strip("\n").split("\t")
            )
            year_field = int(year_field)

            new_artist: Artist | Album | Song | None = find_object(
                artist_field, artist_list
            )
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif isinstance(new_artist, Artist):
                new_artist.add_song(album_field, year_field, song_field)
    return artist_list

    #         if new_artist is None:
    #             new_artist = Artist(artist_field)
    #             artist_list.append(new_artist)
    #         elif new_artist.name != artist_field:
    #             # We've just read details for a new artist
    #             # retrieve the artist object if there is one, otherwise create a new artist
    #             find_artist: Artist | Album | Song | None = find_object(
    #                 artist_field, artist_list
    #             )
    #             if find_artist is None:
    #                 new_artist = Artist(artist_field)
    #                 artist_list.append(new_artist)
    #             elif isinstance(find_artist, Artist):
    #                 new_artist = find_artist
    #             new_album = None

    #         if new_album is None:
    #             new_album = Album(album_field, year_field, new_artist)
    #             new_artist.add_album(new_album)
    #         elif new_album.name != album_field:
    #             # We've just read a new album for the current artist
    #             # retrieve the album object if there is one, otherwise create a new album object
    #             # and store it in the artist's collection
    #             find_album: Artist | Album | Song | None = find_object(
    #                 album_field, new_artist.albums
    #             )
    #             if find_album is None:
    #                 new_album = Album(album_field, year_field, new_artist)
    #                 new_artist.add_album(new_album)
    #             elif isinstance(find_album, Album):
    #                 new_album = find_album

    #         # Create a new song object and add it to the current album's collection
    #         new_song = Song(song_field, new_artist)
    #         new_album.add_song(new_song)

    #     # After reading the last line, we will have an artist and album that haven't been stored
    #     if new_artist is not None:
    #         if new_album is not None:
    #             new_artist.add_album(new_album)
    #         artist_list.append(new_artist)

    # return artist_list


def create_check_file(artist_list: list[Artist]) -> None:
    with open("Section10/check_file.txt", "w") as check_file:
        for artist in artist_list:
            for album in artist.albums:
                for song in album.tracks:
                    check_file.write(
                        f"{artist.name}\t{album.name}\t{album.year}\t{song.title}\n"
                    )


def main() -> None:
    artist: list[Artist] = load_data()
    print(f"Loaded {len(artist)} artists")

    create_check_file(artist)


if __name__ == "__main__":
    main()
