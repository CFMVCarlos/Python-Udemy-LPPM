import sqlite3
import tkinter
from typing import Optional


class Scrollbox(tkinter.Listbox):

    def __init__(self, window: tkinter.Tk, **kwargs) -> None:
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(
            window, orient=tkinter.VERTICAL, command=self.yview
        )

    def grid(
        self,
        row: int,
        column: int,
        sticky: str = "nsw",
        rowspan: int = 1,
        columnspan: int = 1,
        **kwargs,
    ) -> None:
        super().grid(
            row=row,
            column=column,
            sticky=sticky,
            rowspan=rowspan,
            columnspan=columnspan,
            **kwargs,
        )
        self.scrollbar.grid(row=row, column=column, sticky="nse", rowspan=rowspan)
        self["yscrollcommand"] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(
        self,
        window: tkinter.Tk,
        connection: sqlite3.Connection,
        table: str,
        field: str,
        sort_order: tuple[str, ...] = (),
        **kwargs,
    ) -> None:
        super().__init__(window, **kwargs)

        self.linked_box: DataListBox | None = None
        self.link_field: str | None = None
        self.link_value: Optional[int] = None

        self.cursor: sqlite3.Cursor = connection.cursor()
        self.table: str = table
        self.field: str = field

        self.bind("<<ListboxSelect>>", self.on_select)

        self.sql_select: str = f"SELECT {self.field}, _id FROM {self.table}"
        self.sql_sort: str = f" ORDER BY {",".join(sort_order)}" if sort_order else f" ORDER BY {self.field}"

    def clear(self) -> None:
        self.delete(0, tkinter.END)

    def link(self, widget: "DataListBox", link_field: str) -> None:
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value: Optional[int] = None) -> None:
        self.link_value = link_value # store the id, so we know the "master" record we're populated from
        if link_value is not None and self.link_field is not None:
            sql: str = f"{self.sql_select} WHERE {self.link_field} = ?{self.sql_sort}"
            self.cursor.execute(sql, (link_value,))
            # print(sql, link_value)  # TODO remove
        else:
            self.cursor.execute(self.sql_select + self.sql_sort)
            # print(self.sql_select + self.sql_sort) # TODO remove

        # Clear the listbox contents before re-loading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event: tkinter.Event) -> None:
        if not self.linked_box or not self.curselection():
            return

        # print(self is event.widget) # TODO remove
        index: int = self.curselection()[0]
        value: tuple[str] | tuple[int, str] = (self.get(index),)

        # Get the ID from the database row
        if self.link_value is not None:
            value = (self.link_value, value[0])
            sql_where: str = f" WHERE {self.link_field} = ? AND {self.field} = ?"
        else:
            sql_where = f" WHERE {self.field} = ?"

        # Get the artist ID from the database row
        # link_id: int = self.cursor.execute(
        #     f"{self.sql_select} WHERE {self.field} = ?", value
        # ).fetchone()[
        #     1
        # ]  # _id is always the second column
        # print(f"{self.sql_select}{sql_where}", value) # TODO remove
        link_id: int = self.cursor.execute(
            f"{self.sql_select}{sql_where}", value
        ).fetchone()[1]
        self.linked_box.requery(link_id)

        # artist_id: str = conn.execute(
        #     "SELECT artists._id FROM artists WHERE artists.name = ?", artist_name
        # ).fetchone()
        # artist_list: list[str] = []
        # for row in conn.execute(
        #     "SELECT albums.name FROM albums WHERE albums.artist = ? ORDER BY albums.name",
        #     artist_id,
        # ):
        #     artist_list.append(row[0])
        # albumLV.set(tuple(artist_list))
        # songLV.set(("Choose an album",))


# def get_songs(event: tkinter.Event) -> None:
#     list_box: tkinter.Listbox = event.widget
#     if not list_box.curselection():
#         return
#     index: int = list_box.curselection()[0]
#     album_name: tuple[str] = (list_box.get(index),)

#     # Get the artist ID from the database row
#     album_id: str = conn.execute(
#         "SELECT albums._id FROM albums WHERE albums.name = ?", album_name
#     ).fetchone()
#     album_list: list[str] = []
#     for x in conn.execute(
#         "SELECT songs.title FROM songs WHERE songs.album = ? ORDER BY songs.track",
#         album_id,
#     ):
#         album_list.append(x[0])
#     songLV.set(tuple(album_list))

def main():
    conn: sqlite3.Connection = sqlite3.connect("Section11/music.db")

    mainWindow: tkinter.Tk = tkinter.Tk()
    mainWindow.title("Music DB Browser")
    mainWindow.geometry("1024x768")

    mainWindow.columnconfigure((0, 1, 2), weight=2)
    mainWindow.columnconfigure(3, weight=1)  # spacer column on right

    mainWindow.rowconfigure((0, 3), weight=1)
    mainWindow.rowconfigure((1, 2), weight=5)

    # ===== labels =====
    tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    # ===== Artists Listbox =====
    artistList: DataListBox = DataListBox(mainWindow, conn, "artists", "name")
    artistList.grid(row=1, column=0, sticky="nsew", rowspan=2, padx=(30, 0))
    artistList.config(border=2, relief="sunken")

    artistList.requery()
    # query: str = "SELECT name FROM artists ORDER BY name"
    # for artist in conn.execute(query):
    #     artistList.insert(tkinter.END, artist[0])

    # artistList.bind("<<ListboxSelect>>", get_albums)

    # ===== Albums Listbox =====
    albumLV: tkinter.Variable = tkinter.Variable(mainWindow)
    albumLV.set(("Choose an artist",))
    albumList: DataListBox = DataListBox(
        mainWindow, conn, "albums", "name", sort_order=("name",)
    )
    albumList.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
    albumList.config(border=2, relief="sunken")

    # albumList.bind("<<ListboxSelect>>", get_songs)
    artistList.link(albumList, "artist")

    # ===== Songs Listbox =====
    songLV: tkinter.Variable = tkinter.Variable(mainWindow)
    songLV.set(("Choose an album",))
    songList: DataListBox = DataListBox(
        mainWindow, conn, "songs", "title", sort_order=("track", "title")
    )
    songList.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
    songList.config(border=2, relief="sunken")

    albumList.link(songList, "album")
    # ===== Main loop =====
    # testList = range(0, 100)
    # albumLV.set(tuple(testList))
    mainWindow.mainloop()

    print("Closing database connection")
    conn.close()


if __name__ == '__main__':
    main()
