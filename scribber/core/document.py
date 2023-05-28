from abc import abstractmethod
from typing import Any, List, Protocol, Iterable, Optional
from pydantic import BaseModel, validator


class Title(BaseModel):
    title: str
    level: int = 1

    @validator("title",)
    def title_not_empty(cls, v):
        assert len(v) > 0, "must be one or more symbols"
        return v

    @validator("level")
    def level_in_range(cls, v):
        assert 0 < v <= 6, "must be in 1..6 range"
        return v


class Paragraph(BaseModel):
    text: str

    @validator("text")
    def field_not_empty(cls, v):
        assert len(v) > 0, "must be one or more symbols"
        return v


class CodeBlock(BaseModel):
    code: str
    style: Optional[str] = ""

    @validator("code")
    def field_not_empty(cls, v):
        assert len(v) > 0, "must be one or more symbols"
        return v


class Table(BaseModel):
    headers: List[str]
    content: List[Any]

    @validator("headers", "content")
    def not_empty(cls, v):
        assert len(v) > 0, "must not be empty"
        return v


class EmptyLine(BaseModel):
    pass


class AbstractDocument(Protocol):
    def add(self, part: Any) -> None:
        ...

    def get_result(self) -> Any:
        ...

    def extend(self, parts: Iterable[Any]) -> None:
        ...


class SimpleDocument:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def get_result(self) -> List[Any]:
        return self.parts

    def extend(self, parts: Iterable[Any]) -> None:
        for item in parts:
            self.add(item)


class Builder(Protocol):
    @property
    @abstractmethod
    def parts(self) -> List:
        ...

    def add_title(self, title: Title) -> None:
        ...

    def add_table(self, table: Table) -> None:
        ...

    def add_paragraph(self, paragraph: Paragraph) -> None:
        ...

    def add_code_block(self, code_block: CodeBlock) -> None:
        ...

    def add_brake(self):
        ...


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_report_from_doc(self, doc: SimpleDocument):
        for item in doc.get_result():
            if isinstance(item, Title):
                self.builder.add_title(item)
            elif isinstance(item, Paragraph):
                self.builder.add_paragraph(item)
            elif isinstance(item, EmptyLine):
                self.builder.add_brake()
            elif isinstance(item, Table):
                self.builder.add_table(item)
            elif isinstance(item, CodeBlock):
                self.builder.add_code_block(item)


class DocumentBuilder(Builder):
    def __init__(self, doc: AbstractDocument) -> None:
        self._report = None
        self.__doc = doc
        self.reset()

    def reset(self) -> None:
        self._report = self.__doc

    @property
    def parts(self) -> List:
        parts = self._report
        self.reset()
        return parts

    def add_title(self, title: Title) -> None:
        self._report.add(title)

    def add_table(self, table: Table) -> None:
        self._report.add(table)

    def add_paragraph(self, paragraph: Paragraph) -> None:
        self._report.add(paragraph)

    def add_brake(self) -> None:
        self._report.add(EmptyLine())

    def add_code_block(self, code_block: CodeBlock) -> None:
        self._report.add(code_block)
