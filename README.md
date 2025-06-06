# music_composer

This library provides a Pythonic way to generate MusicXML files with declarative syntax. 

Basic Usage Example:

```python
from music_composer import *

with ScorePartwise() as score:
    Work(work_title="My First Song")
    with PartList():
        with Defaults():
            Scaling(millimeters=7.2, tenths=40)
            with PageLayout(page_height=1200, page_width=900):
                PageMargins(type="both", left_margin=70, right_margin=70,
                top_margin=70, bottom_margin=70)
            MusicFont(font_family="Arial", font_size="20.5")
        ScorePart(id="P1", part_name="Piano")
    with Part(id="P1"):
        with Measure(number=1):
            Attributes(key_fifths=0, time_beats=4, time_beat_type=4,
            clef_sign="G", clef_line=2)
            with Note(pitch=("C", 4), duration=4):
                Lyric(number=1, text="Hel-", syllabic="begin")
            with Note(pitch=("D", 4), duration=4):
                Lyric(number=1, text="lo", syllabic="end")
print(score)
```
