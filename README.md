# Scribber

A Python library for generating documents in multiple formats from a single document model.

Build a document once and export it as **Markdown**, **Word**, **Excel**, or plain text without changing your application logic.

Scribber was originally created as an experiment in applying object-oriented design patterns, particularly the **Builder** pattern. Later it evolved into a reusable library and was used in a production monitoring system to generate scheduled reports in multiple output formats.

---

## Features

- Single document model
- Multiple output formats
- Builder pattern implementation
- Extensible rendering pipeline
- Python API
- Easy to add new exporters

Supported formats:

- Plain Text
- Markdown
- Microsoft Word (.docx)
- Microsoft Excel (.xlsx)

---

## Why Scribber?

Many applications need to produce the same report in several formats.

Instead of duplicating formatting logic for every export type, Scribber represents the document as an abstract model and delegates rendering to format-specific builders.

This approach separates document construction from presentation, making the system easier to extend and maintain.

---

## Design

The project intentionally applies the **Builder** design pattern.

```
SimpleDocument
        │
        ▼
DocumentBuilder
        │
        ├──────────────┐
        ▼              ▼
MarkdownDocument   WordDocument
        │              │
        ├──────────────┤
        ▼              ▼
TextDocument      ExcelDocument
```

A document is constructed only once and can then be rendered into different output formats without modifying business logic.

---

## Typical Use Cases

- Automated report generation
- Monitoring and infrastructure reports
- Scheduled background jobs
- Exporting business reports
- Multi-format document generation

---

## Installation

```bash
pip install scribber
```

---

## Quick Example

```python
from scribber import *

doc = SimpleDocument()

doc.add(Title("Monthly Report"))
doc.add(Paragraph("Everything works as expected."))

builder = DocumentBuilder(doc=MarkdownDocument())
Director(builder).build_report_from_doc(doc)

builder.parts.save("report.md")
```

The same document can be rendered as:

- Markdown
- Word (.docx)
- Excel (.xlsx)
- Plain Text

without changing the document itself.

---

## Documentation

Detailed documentation is available in the `docs` directory.

- Installation
- API Reference
- Builder Architecture
- Examples

---

## Project Background

Scribber started as an exercise in applying object-oriented design patterns to a practical problem.

During development it proved flexible enough to become part of a production monitoring system, where it was used to generate scheduled reports in multiple formats from a single document description.

The project is published as a reference implementation of a multi-format document rendering library built around the Builder pattern.

---

## License

MIT License
