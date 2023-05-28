import pytest as pytest
from pydantic import ValidationError

from scribber.core.document import Title, Paragraph, CodeBlock, Table, SimpleDocument

LEVELS = [1, 2, 3, 4, 5, 6]
WRONG_LEVELS = [-2, 0, 7, 9]


@pytest.mark.parametrize("level", LEVELS)
def test_title_ok(level: int):
    title = Title(title="Title", level=level)
    assert title.title == "Title"
    assert title.level == level


@pytest.mark.parametrize("level", LEVELS)
def test_no_title(level: int):
    with pytest.raises(ValidationError):
        Title(level=level)


@pytest.mark.parametrize("level", LEVELS)
def test_title_empty(level: int):
    with pytest.raises(ValidationError):
        Title(title="", level=level)


@pytest.mark.parametrize("level", WRONG_LEVELS)
def test_title_low_level(level: int):
    with pytest.raises(ValidationError):
        Title(title="Title", level=level)


def test_paragraph():
    p = Paragraph(text="text text")
    assert p.text == "text text"


def test_paragraph_empty():
    with pytest.raises(ValidationError):
        Paragraph()


def test_paragraph_no_text():
    with pytest.raises(ValidationError):
        Paragraph(text="")


def test_code_block():
    b = CodeBlock(code="print('Hello')", style="python")
    assert b.code == "print('Hello')"
    assert b.style == "python"


def test_code_block_wo_style():
    b = CodeBlock(code="print('Hello')")
    assert b.code == "print('Hello')"
    assert b.style == ""


def test_code_block_empty():
    with pytest.raises(ValidationError):
        CodeBlock()


def test_code_block_no_code():
    with pytest.raises(ValidationError):
        CodeBlock(code="")


def test_table():
    t = Table(
        headers=["one", "two", "three", "four"],
        content=[
            (1, 2, 3, 4),
            ("234", 345, 986, ""),
            (89, 35, 587643, 8675),
        ],
    )
    assert t.headers == ["one", "two", "three", "four"]
    assert t.content == [
        (1, 2, 3, 4),
        ("234", 345, 986, ""),
        (89, 35, 587643, 8675),
    ]


def test_table_empty():
    with pytest.raises(ValidationError):
        Table()


def test_table_no_content():
    with pytest.raises(ValidationError):
        Table(headers=["one", "two", "three", "four"])


def test_table_no_header():
    with pytest.raises(ValidationError):
        Table(
            content=[
                (1, 2, 3, 4),
                ("234", 345, 986, ""),
                (89, 35, 587643, 8675),
            ]
        )

def test_simple_document():
    sd = SimpleDocument()
    p1 = Paragraph(text="text text")
    p2 = Paragraph(text="another text")
    sd.extend([p1, p2])

    assert sd.get_result() == [p1, p2]
