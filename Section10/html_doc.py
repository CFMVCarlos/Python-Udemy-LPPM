from typing import Any, Optional, TextIO


class Tag:

    def __init__(self, name: str, contents: Any = "") -> None:
        self.name: str = name
        self.contents: Any = contents

    def __str__(self) -> str:
        return f"<{self.name}>{self.contents}</{self.name}>"

    def display(self, file: Optional[TextIO] = None) -> None:
        print(self, file=file)


class DocType(Tag):

    def __init__(self) -> None:
        super().__init__("!DOCTYPE", "")
        self.contents = ""  # DocType doesn't have end tag


class Head(Tag):

    def __init__(self, title: str = "") -> None:
        super().__init__("head", "")
        self._head_contents: list = []
        if title:
            self.add_tag("title", title)

    def add_tag(self, tag_name: str, contents: Any) -> None:
        new_tag: Tag = Tag(tag_name, contents)
        self._head_contents.append(new_tag)

    def __str__(self) -> str:
        head_contents = "".join(str(tag) for tag in self._head_contents)
        return f"<{self.name}>{head_contents}</{self.name}>"


class Body(Tag):

    def __init__(self) -> None:
        super().__init__("body", "")
        self._body_contents: list = []

    def add_tag(self, tag_name: str, contents: Any) -> None:
        new_tag: Tag = Tag(tag_name, contents)
        self._body_contents.append(new_tag)

    def __str__(self) -> str:
        body_contents: str = "".join(str(tag) for tag in self._body_contents)
        return f"<{self.name}>{body_contents}</{self.name}>"


class HtmlDoc:

    def __init__(self, doc_type: DocType, head: Head, body: Body) -> None:
        self._doc_type: DocType = doc_type
        self._head: Head = head
        self._body: Body = body

    def add_tag(self, name: str, contents: Any) -> None:
        self._body.add_tag(name, contents)

    def display(self, file: Optional[TextIO] = None) -> None:
        print(self._doc_type, file=file)
        print("<html>", file=file)
        print(self._head, file=file)
        print(self._body, file=file)
        print("</html>", file=file)


def main() -> None:
    # my_page: HtmlDoc = HtmlDoc(title="Document title")
    # my_page.add_tag("h1", "Main heading")
    # my_page.add_tag("h2", "Sub-heading")
    # my_page.add_tag("p", "This is a paragraph")
    # my_page.display()
    # with open("Section10/test.html", "w+") as test_doc:
    #     my_page.display(file=test_doc)

    ################################################################

    # my_page: HtmlDoc = HtmlDoc(title="Document title")

    # new_body: Body = Body()
    # new_body.add_tag("h1", "Aggregation")
    # new_body.add_tag(
    #     "p",
    #     "Unlike <strong>composition</strong>, aggregation uses existing instances of objects to build up another object.",
    # )
    # new_body.add_tag(
    #     "p",
    #     "The composed object doesn't actually own the objects that it's composed of. This is a 'has-a' relationship.",
    # )

    # # Give our document new content by switching the body
    # my_page._body = new_body
    # with open("Section10/test2.html", "w+") as test_doc:
    #     my_page.display(file=test_doc)

    ################################################################

    new_body: Body = Body()
    new_body.add_tag("h1", "Aggregation")
    new_body.add_tag(
        "p",
        "Unlike <strong>composition</strong>, aggregation uses existing instances of objects to build up another object.",
    )
    new_body.add_tag(
        "p",
        "The composed object doesn't actually own the objects that it's composed of. This is a 'has-a' relationship.",
    )
    new_doc_type: DocType = DocType()
    new_head: Head = Head("Aggregation document")
    my_page: HtmlDoc = HtmlDoc(new_doc_type, new_head, new_body)

    # Give our document new content by switching the body
    with open("Section10/test3.html", "w+") as test_doc:
        my_page.display(file=test_doc)


if __name__ == "__main__":
    main()
