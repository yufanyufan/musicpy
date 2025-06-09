# music_composer

This library provides a Pythonic way to generate MusicXML files with declarative syntax. 

Basic Usage Example:

```python
from musicxml_schema import *
from musicxml import _

with ScorePartwise() as score:
  Work(WorkTitle="Sample Work")
  MovementTitle("Sample Movement")
  with Identification():
      Creator("John Doe")
      Rights("Copyright 2023 John Doe")
  with Defaults():
    Scaling(Millimeters=7.23, Tenths=40)
    with PageLayout(PageHeight=1250, PageWidth=950):
      PageMargins(
          type="both",
          LeftMargin=75,
          RightMargin=75,
          TopMargin=80,
          BottomMargin=80,
      )
    with SystemLayout(  # pytype: disable=wrong-arg-types
        SystemDistance=120, TopSystemDistance=70, SystemMargins=_(LeftMargin=1, RightMargin=2)
    ):
      pass  # SystemLayout is a context manager; SystemMargins is now an argument.
    StaffLayout(StaffDistance=80)
    with Appearance():
      pass  # LineWidth, NoteSize, etc. could be added here
    MusicFont(font_family="Maestro", font_size="20.5")
    WordFont(font_family="Times New Roman", font_size="10")
    LyricFont(number="1", font_family="Arial", font_size="9")
    LyricLanguage(number="1", lang="en")
  Credit(CreditWords=_("Sample Credit", font_size="10", justify="center"))
  with PartList():
    ScorePart(id="P1", PartName="Violin")
    ScorePart(id="P2", PartName="Cello")
  with Part(id="P1"):
    with Measure(number=1):
      Attributes(
          Divisions=1,
      )
      slur_1_number = "1"  # Explicitly manage slur numbers for pairing
      with Note(Pitch=_(Step="C", Octave="4"), Duration=4) as note1:
        with Notations():
          Slur(type="start", placement="above", number=slur_1_number)
        Lyric(number=1, Text="Hell", Syllabic="begin")
      with Note(
          Pitch=_(Step="D", Octave="4", Alter="1"),
          Duration=4,
      ) as note2:
        with Notations():
          Slur(type="stop", number=slur_1_number)
        Lyric(number=1, Text="-lo", Syllabic="end")
      Note(Rest=(), Duration=2)  # A half rest
      Note(Pitch=_(Step="E", Octave="4"), Duration=2)

      with Direction(placement="below"):
        with DirectionType():
          Pedal(type="start", line="yes")

  with Part(id="P2"):
    with Measure(1):
      Attributes(
          Divisions=1,
      )
      with Note(Pitch=_(Step="E", Octave="3"), Duration=4):
        Lyric(number=1, Text="World", Syllabic="single")
      Note(Pitch=_(Step="F", Octave="3"), Duration=4)
      with Direction(placement="below"):
        with DirectionType():
          Pedal(type="stop", line="yes")

print(score)

```
