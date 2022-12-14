# Scribber

---

A simple document generator with not very rich functionality that can export a document to some formats such 
as text, docx, xlsx and markdown.

## Installation
```shell
pip install scribber
```

## Usage

```python
from core.document import SimpleDocument, Title, EmptyLine, Paragraph, Table, Director
from formats.excel.excel_document import ExcelDocumentBuilder
from formats.markdown.markdown_document import MarkdownDocumentBuilder
from formats.text.text_document import TextDocumentBuilder
from formats.word.word_document import WordDocumentBuilder

doc = SimpleDocument()
doc.add(Title(title="Funny report"))
doc.add(EmptyLine())
doc.add(Paragraph(text="Let me show you report"))
doc.add(
    Table(
        headers=['one', 'two', 'three', 'four'],
        content=[
            (1, 2, 3, 4),
            ('234', 345, 986, ''),
            (89, 35, 587643, 8675),
        ]
    )
)
doc.add(Title(title="Total", level=2))
doc.add(Paragraph(text="It's Ok!"))

director = Director()
text_report_builder = TextDocumentBuilder()
word_report_builder = WordDocumentBuilder()
excel_report_builder = ExcelDocumentBuilder()
marckdown_report_builder = MarkdownDocumentBuilder()

print("Make a Text Document")
director.builder = text_report_builder
director.build_report_from_doc(doc)
text_report_builder.parts.save('test.txt')

print("Make a Word Document")
director.builder = word_report_builder
director.build_report_from_doc(doc)
word_report_builder.parts.save('test.docx')

print("Make a Excel Document")
director.builder = excel_report_builder
director.build_report_from_doc(doc)
excel_report_builder.parts.save('test.xlsx')

print("Make a Marckdown Document")
director.builder = marckdown_report_builder
director.build_report_from_doc(doc)
marckdown_report_builder.parts.save('test.md')

print()
print('Build without Director')
text_report_builder.add_title(Title(title="Next report"))
text_report_builder.add_paragraph(Paragraph(text="That is all!"))
print(text_report_builder.parts.get_result())
```

The text file example
```text
Funny report
============

Let me show you report
---------------------------
 one | two | three  | four 
---------------------------
  1  |  2  |   3    |  4   
 234 | 345 |  986   |      
 89  | 35  | 587643 | 8675 
---------------------------
Total
=====
It's Ok!
```

## requirements

- lxml==4.9.1
- pydantic==1.10.2
- python-docx==0.8.11
- typing_extensions==4.4.0
- XlsxWriter==3.0.3