from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

# text (plain)
# **Bold text** <b>                             <b>bold</b>
# _Italic text_ <i>                             <i>italic</i>
# `Code text`                                   <code>This is code</code>
# Links, in this format: [anchor text](url)     <a href="https://www.google.com">link</a>.
# Images, in this format: ![alt text](url)      <img src="url/of/image.jpg" alt="Description of image" />

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
