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
    with SystemLayout(
        SystemDistance=120, TopSystemDistance=70, SystemMargins=_(LeftMargin=1, RightMargin=2)
    ):
      pass
    StaffLayout(StaffDistance=80)
    with Appearance():
      pass
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
      slur_1_number = "1"
      with Note(Pitch=_(Step="C", Octave="4"), Duration=4):
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
      Note(Rest=(), Duration=2)
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

It generates:

```xml
<score-partwise>
  <work>
    <work-title>Sample Work</work-title>
  </work>
  <movement-title>Sample Movement</movement-title>
  <identification>
    <creator>John Doe</creator>
    <rights>Copyright 2023 John Doe</rights>
  </identification>
  <defaults>
    <scaling>
      <millimeters>7.23</millimeters>
      <tenths>40</tenths>
    </scaling>
    <page-layout>
      <page-height>1250</page-height>
      <page-width>950</page-width>
      <page-margins type="both">
        <left-margin>75</left-margin>
        <right-margin>75</right-margin>
        <top-margin>80</top-margin>
        <bottom-margin>80</bottom-margin>
      </page-margins>
    </page-layout>
    <system-layout>
      <system-margins>
        <left-margin>1</left-margin>
        <right-margin>2</right-margin>
      </system-margins>
      <system-distance>120</system-distance>
      <top-system-distance>70</top-system-distance>
    </system-layout>
    <staff-layout>
      <staff-distance>80</staff-distance>
    </staff-layout>
    <appearance />
    <music-font font-family="Maestro" font-size="20.5" />
    <word-font font-family="Times New Roman" font-size="10" />
    <lyric-font font-family="Arial" font-size="9" number="1" />
    <lyric-language xml:lang="en" number="1" />
  </defaults>
  <credit>
    <credit-words font-size="10" justify="center">Sample Credit</credit-words>
  </credit>
  <part-list>
    <score-part id="P1">
      <part-name>Violin</part-name>
    </score-part>
    <score-part id="P2">
      <part-name>Cello</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>1</divisions>
      </attributes>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>4</duration>
        <notations>
          <slur type="start" number="1" placement="above" />
        </notations>
        <lyric number="1">
          <syllabic>begin</syllabic>
          <text>Hell</text>
        </lyric>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <alter>1</alter>
          <octave>4</octave>
        </pitch>
        <duration>4</duration>
        <notations>
          <slur type="stop" number="1" />
        </notations>
        <lyric number="1">
          <syllabic>end</syllabic>
          <text>-lo</text>
        </lyric>
      </note>
      <note>
        <rest />
        <duration>2</duration>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <octave>4</octave>
        </pitch>
        <duration>2</duration>
      </note>
      <direction placement="below">
        <direction-type>
          <pedal type="start" line="yes" />
        </direction-type>
      </direction>
    </measure>
  </part>
  <part id="P2">
    <measure number="1">
      <attributes>
        <divisions>1</divisions>
      </attributes>
      <note>
        <pitch>
          <step>E</step>
          <octave>3</octave>
        </pitch>
        <duration>4</duration>
        <lyric number="1">
          <syllabic>single</syllabic>
          <text>World</text>
        </lyric>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>4</duration>
      </note>
      <direction placement="below">
        <direction-type>
          <pedal type="stop" line="yes" />
        </direction-type>
      </direction>
    </measure>
  </part>
</score-partwise>
```
