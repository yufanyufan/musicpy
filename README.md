# Music Composer

Music Composer is a programming launguage for music. It provides a Pythonic way to generate [MusicXML](https://www.w3.org/2021/06/musicxml40/tutorial/introduction/) files with declarative syntax. 

API Reference:

* Element Naming: Child elements are represented by classes in PascalCase (e.g., `ScorePartwise`, `PartName`).
* Attribute Naming: Attributes of elements are passed as keyword arguments in lowercase with underscores if needed (e.g., `work_title`, `page_height`). These are automatically converted to kebab-case in the XML output (e.g., `work-title`, `page-height`).
* String Values: Many element text content and attribute values are passed as strings (e.g., `Millimeters="7.2", PartName="Piano"`).
* Complex Arguments with `_()`: For elements that have their own child elements or a complex structure not representable by a simple string (like `Pitch` which has `Step` and `Octave`, or `Key` which has `Fifths`), the `_()` helper function is used. This helper takes keyword arguments that correspond to the sub-elements or attributes of the complex argument. For example: `Pitch=_(Step="C", Octave="4") Key=_(Fifths="0") SystemMargins=_(LeftMargin=1, RightMargin=2)` The `_()` helper packages these into a `MusicElementArg` object, which is then processed by the parent element's constructor to create the appropriate nested XML structure.


This example creates a simple score with one part (Piano), one measure, and two notes with lyrics. The output will be a MusicXML string.

```python
from musicxml_schema import *
from musicxml import _

with ScorePartwise(version="4.0") as score:
    Work(WorkTitle="My First Song")
    with Defaults():
        Scaling(Millimeters=7.2, Tenths=40)
        with PageLayout(PageHeight=1200, PageWidth=900):
            PageMargins(type="both", LeftMargin=70, RightMargin=70, TopMargin=70, BottomMargin=70)
        MusicFont(font_family="Arial", font_size=20.5)
    with PartList():
        ScorePart(id="P1", PartName="Piano")
    with Part(id="P1"):
        with Measure(number=1):
            Attributes(
                Divisions=1,  # Specifies how many divisions per quarter note, affects Duration
                Key=_(Fifths=0),
                Time=_(Beats=4, BeatType=4),
                Clef=_(Sign="G", Line=2)
            )
            # Duration "4" with Divisions "1" would typically mean 4 quarter-note durations
            with Note(Pitch=_(Step="C", Octave=4), Duration=4):
                Lyric(number=1, Text="Hel-", Syllabic="begin")
            with Note(Pitch=_(Step="D", Octave="4"), Duration=4):
                Lyric(number=1, Text="lo", Syllabic="end")
```
