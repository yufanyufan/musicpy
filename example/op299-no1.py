from musicxml_schema import *
from musicxml import _


with ScorePartwise(version="4.0"):
    with Defaults():
        with Scaling():
            Millimeters("5.7")
            Tenths("40")
        with PageLayout():
            PageHeight("2084.21")
            PageWidth("1473.68")
            with PageMargins(type="even"):
                LeftMargin("70.1755")
                RightMargin("70.1755")
                TopMargin("70.1755")
                BottomMargin("140.351")
            with PageMargins(type="odd"):
                LeftMargin("70.1755")
                RightMargin("70.1755")
                TopMargin("70.1755")
                BottomMargin("140.351")
        with Appearance():
            LineWidth("1.8", type="light barline")
            LineWidth("5.5", type="heavy barline")
            LineWidth("5", type="beam")
            LineWidth("4.4", type="bracket")
            LineWidth("1.5", type="dashes")
            LineWidth("1", type="enclosure")
            LineWidth("1.1", type="ending")
            LineWidth("1", type="extend")
            LineWidth("1.6", type="leger")
            LineWidth("1.1", type="pedal")
            LineWidth("1.1", type="octave shift")
            LineWidth("2.1", type="slur middle")
            LineWidth("0.7", type="slur tip")
            LineWidth("1.1", type="staff")
            LineWidth("1", type="stem")
            LineWidth("2.1", type="tie middle")
            LineWidth("0.7", type="tie tip")
            LineWidth("1", type="tuplet bracket")
            LineWidth("1.2", type="wedge")
            NoteSize("70", type="cue")
            NoteSize("70", type="grace")
            NoteSize("49", type="grace-cue")
        MusicFont(font_family="Leland")
        WordFont(font_family="FreeSerif", font_size="10")
        LyricFont(font_family="FreeSerif", font_size="11")
    with Credit(page="1"):
        CreditType("title")
        CreditWords("The School Of Velocity", default_x="736.842414", default_y="2014.032664", justify="center", valign="top", font_size="24")
    with Credit(page="1"):
        CreditType("composer")
        CreditWords("Carl Czerny", default_x="1403.509352", default_y="1914.032664", justify="right", valign="bottom", font_size="12")
        CreditWords("(1791-1857)")
    with Credit(page="1"):
        CreditType("subtitle")
        CreditWords("Op. 299, No. 1", default_x="736.842414", default_y="1943.857225", justify="center", valign="top", font_size="14")
    with PartList():
        with ScorePart(id="P1"):
            PartName("Piano", print_object="no")
            with ScoreInstrument(id="P1-I1"):
                InstrumentName("Piano")
                InstrumentSound("keyboard.piano")
            MidiDevice("", id="P1-I1", port="1")
            with MidiInstrument(id="P1-I1"):
                MidiChannel("1")
                MidiProgram("1")
                Volume("78.7402")
                Pan("0")
    with Part(id="P1"):
        with Measure(number="1", width="461.65"):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin("72.28")
                        RightMargin("0")
                    TopSystemDistance("230")
                with StaffLayout(number="2"):
                    StaffDistance("65")
                with MeasureLayout():
                    MeasureDistance("72.28")
            with Attributes():
                Divisions("4")
                with Key():
                    Fifths("0")
                with Time(symbol="cut"):
                    Beats("4")
                    BeatType("4")
                Staves("2")
                with Clef(number="1"):
                    Sign("G")
                    Line("2")
                with Clef(number="2"):
                    Sign("F")
                    Line("4")
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("C")
                Kind("major")
            with Direction(placement="above"):
                with DirectionType():
                    Words("1.", enclosure="rectangle", default_y="33.34", relative_y="20")
                Staff("1")
            with Direction(placement="above"):
                with DirectionType():
                    Words("Updated Sep 15, 2014", default_y="63.66", relative_y="20")
                Staff("1")
            with Note(default_x="81.88", default_y="-20"):
                Rest()
                Duration("1")
                Voice("1")
                Type("16th")
                Staff("1")
            with Note(default_x="105.5", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="129.12", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="152.75", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="176.37", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="199.99", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="223.62", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="247.24", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="270.86", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="43.14")
            with Note(default_x="294.49", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="45.18")
            with Note(default_x="318.11", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="341.74", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="365.36", default_y="-35"):
                with Pitch():
                    Step("F")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="48.18")
            with Note(default_x="388.98", default_y="-40"):
                with Pitch():
                    Step("E")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="51.86")
            with Note(default_x="412.61", default_y="-45"):
                with Pitch():
                    Step("D")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="436.23", default_y="-50"):
                with Pitch():
                    Step("C")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="80.91", default_y="-130"):
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("5", placement="below", default_x="7.46", default_y="-52.55")
            with Note(default_x="80.91", default_y="-120"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("4", placement="below", default_x="7.46", default_y="-49.19")
            with Note(default_x="80.91", default_y="-110"):
                Chord()
                with Pitch():
                    Step("G")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("1", placement="below", default_x="7.46", default_y="-45.69")
        with Measure(number="2", width="406.66"):
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("G")
                Kind("dominant", text="7")
            with Note(default_x="26.88", default_y="-20"):
                Rest()
                Duration("1")
                Voice("1")
                Type("16th")
                Staff("1")
            with Note(default_x="50.5", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="74.13", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="97.75", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="121.38", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="145", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="168.62", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="192.25", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="215.87", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="20.69")
            with Note(default_x="239.49", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="25.2")
            with Note(default_x="263.12", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="286.74", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="310.36", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="43.18")
            with Note(default_x="333.99", default_y="-35"):
                with Pitch():
                    Step("F")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="46.86")
            with Note(default_x="357.61", default_y="-40"):
                with Pitch():
                    Step("E")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="381.24", default_y="-45"):
                with Pitch():
                    Step("D")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="25.92", default_y="-135"):
                with Pitch():
                    Step("B")
                    Octave("2")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("5", placement="below", default_x="7.46", default_y="-47.55")
            with Note(default_x="12", default_y="-115"):
                Chord()
                with Pitch():
                    Step("F")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("2", placement="below", default_x="21.38", default_y="-54.19")
            with Note(default_x="25.92", default_y="-110"):
                Chord()
                with Pitch():
                    Step("G")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("1", placement="below", default_x="7.46", default_y="-45.69")
        with Measure(number="3", width="392.74"):
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("C")
                Kind("major")
            with Note(default_x="12.96", default_y="-20"):
                Rest()
                Duration("1")
                Voice("1")
                Type("16th")
                Staff("1")
            with Note(default_x="36.59", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="60.21", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="83.83", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="107.46", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="131.08", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="154.7", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="178.33", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="201.95", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="225.58", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="20.2")
            with Note(default_x="249.2", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="272.82", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="296.45", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="45.68")
            with Note(default_x="320.07", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="49.36")
            with Note(default_x="343.69", default_y="-35"):
                with Pitch():
                    Step("F")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="367.32", default_y="-40"):
                with Pitch():
                    Step("E")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="12", default_y="-130"):
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
            with Note(default_x="12", default_y="-120"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
            with Note(default_x="12", default_y="-110"):
                Chord()
                with Pitch():
                    Step("G")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
        with Measure(number="4", width="479.63"):
            with Print(new_system="yes"):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin("0")
                        RightMargin("0")
                    SystemDistance("150")
                with StaffLayout(number="2"):
                    StaffDistance("65")
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("G")
                Kind("major")
                with Bass():
                    BassStep("D")
            with Note(default_x="65.74", default_y="-20"):
                Rest()
                Duration("1")
                Voice("1")
                Type("16th")
                Staff("1")
            with Note(default_x="91.49", default_y="35"):
                with Pitch():
                    Step("F")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="117.25", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="143", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="168.76", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="194.52", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="220.27", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="246.03", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="271.78", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="297.54", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="323.29", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="349.05", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="374.81", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="43.16")
            with Note(default_x="400.56", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="46.02")
            with Note(default_x="426.32", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="452.07", default_y="-35"):
                with Pitch():
                    Step("F")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="64.77", default_y="-125"):
                with Pitch():
                    Step("D")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("5", placement="below", default_x="7.46", default_y="-70.55")
            with Note(default_x="50.86", default_y="-115"):
                Chord()
                with Pitch():
                    Step("F")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("3", placement="below", default_x="21.38", default_y="-67.18")
            with Note(default_x="64.77", default_y="-110"):
                Chord()
                with Pitch():
                    Step("G")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("2", placement="below", default_x="7.46", default_y="-59.19")
            with Note(default_x="64.77", default_y="-100"):
                Chord()
                with Pitch():
                    Step("B")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("1", placement="below", default_x="7.46", default_y="-55.69")
        with Measure(number="5", width="426.85"):
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("C")
                Kind("major")
                with Bass():
                    BassStep("E")
            with Note(default_x="12.96", default_y="-20"):
                Rest()
                Duration("1")
                Voice("1")
                Type("16th")
                Staff("1")
            with Note(default_x="38.72", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="48.24")
            with Note(default_x="64.47", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="90.23", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="42.65")
            with Note(default_x="115.99", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="25.69")
            with Note(default_x="141.74", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="167.5", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="193.25", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Direction(placement="above"):
                with DirectionType():
                    OctaveShift(type="down", size="8", number="1", default_y="37.25")
                Staff("1")
            with Note(default_x="219.01", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="40.69")
            with Note(default_x="244.76", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="270.52", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="30.2")
            with Note(default_x="296.27", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="25.69")
            with Note(default_x="322.03", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="347.79", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="373.54", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="399.3", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Direction(placement="above"):
                with DirectionType():
                    OctaveShift(type="stop", size="8", number="1")
                Staff("1")
            with Backup():
                Duration("16")
            with Note(default_x="12", default_y="-120"):
                with Pitch():
                    Step("E")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("4", placement="below", default_x="7.46", default_y="-35.2")
            with Note(default_x="12", default_y="-110"):
                Chord()
                with Pitch():
                    Step("G")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
            with Note(default_x="12", default_y="-95"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("4")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
        with Measure(number="6", width="426.85"):
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("F")
                Kind("major")
            with Note(default_x="12.96", default_y="-20"):
                Rest()
                Duration("1")
                Voice("1")
                Type("16th")
                Staff("1")
            with Note(default_x="38.72", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="35.69")
            with Note(default_x="64.47", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="90.23", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="25.2")
            with Note(default_x="115.99", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="20.69")
            with Note(default_x="141.74", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="167.5", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="193.25", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Direction(placement="above"):
                with DirectionType():
                    OctaveShift(type="down", size="8", number="1", default_y="37.25")
                Staff("1")
            with Note(default_x="219.01", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="35.69")
            with Note(default_x="244.76", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="270.52", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="25.2")
            with Note(default_x="296.27", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="20.69")
            with Note(default_x="322.03", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="347.79", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="373.54", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="399.3", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Direction(placement="above"):
                with DirectionType():
                    OctaveShift(type="stop", size="8", number="1")
                Staff("1")
            with Backup():
                Duration("16")
            with Note(default_x="12", default_y="-115"):
                with Pitch():
                    Step("F")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("3", placement="below", default_x="7.46", default_y="-40.2")
            with Note(default_x="12", default_y="-105"):
                Chord()
                with Pitch():
                    Step("A")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
            with Note(default_x="12", default_y="-95"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("4")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
        with Measure(number="7", width="472.65"):
            with Print(new_system="yes"):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin("0")
                        RightMargin("0")
                    SystemDistance("150")
                with StaffLayout(number="2"):
                    StaffDistance("106.13")
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("G")
                Kind("dominant", text="7")
            with Note(default_x="58.36", default_y="-20"):
                Rest()
                Duration("1")
                Voice("1")
                Type("16th")
                Staff("1")
            with Note(default_x="84.14", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="30.69")
            with Note(default_x="109.92", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="135.7", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="161.48", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="187.26", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="213.04", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="238.82", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Direction(placement="above"):
                with DirectionType():
                    OctaveShift(type="down", size="8", number="1", default_y="37.25")
                Staff("1")
            with Note(default_x="264.6", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="30.69")
            with Note(default_x="290.38", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="316.17", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="341.95", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="367.73", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="393.51", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="419.29", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="445.07", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Direction(placement="above"):
                with DirectionType():
                    OctaveShift(type="stop", size="8", number="1")
                Staff("1")
            with Backup():
                Duration("16")
            with Note(default_x="57.39", default_y="-151.13"):
                with Pitch():
                    Step("G")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("5", placement="below", default_x="7.46", default_y="-72.55")
            with Note(default_x="57.39", default_y="-131.13"):
                Chord()
                with Pitch():
                    Step("D")
                    Octave("4")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("2", placement="below", default_x="7.46", default_y="-79.19")
            with Note(default_x="57.39", default_y="-121.13"):
                Chord()
                with Pitch():
                    Step("F")
                    Octave("4")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("1", placement="below", default_x="7.46", default_y="-75.69")
        with Measure(number="8", width="427.26"):
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("A")
                Kind("minor", text="m")
            with Note(default_x="12.96", default_y="-20"):
                Rest()
                Duration("1")
                Voice("1")
                Type("16th")
                Staff("1")
            with Note(default_x="38.74", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="25.69")
            with Note(default_x="64.52", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="90.31", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="116.09", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="141.87", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="167.65", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="193.43", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Direction(placement="above"):
                with DirectionType():
                    OctaveShift(type="down", size="8", number="1", default_y="64.59")
                Staff("1")
            with Note(default_x="219.21", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="25.69")
            with Note(default_x="244.99", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="270.77", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="296.55", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="322.33", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="348.11", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="373.9", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="399.68", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="12", default_y="-146.13"):
                with Pitch():
                    Step("A")
                    Octave("3")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("4", placement="below", default_x="7.46", default_y="-50.2")
            with Note(default_x="12", default_y="-136.13"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("4")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
            with Note(default_x="12", default_y="-126.13"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("4")
                Duration("16")
                Voice("5")
                Type("whole")
                Staff("2")
        with Measure(number="9", width="433.43"):
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("D")
                Kind("minor", text="m")
                with Bass():
                    BassStep("F")
            with Note(default_x="12.96", default_y="-20"):
                Rest()
                Duration("1")
                Voice("1")
                Type("16th")
                Staff("1")
            with Note(default_x="38.74", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="20.69")
            with Note(default_x="64.52", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="90.31", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="116.09", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="141.87", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="167.65", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="199.6", default_y="20"):
                with Pitch():
                    Step("C")
                    Alter("1")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Accidental("sharp")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="225.38", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="251.16", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="276.94", default_y="35"):
                with Pitch():
                    Step("F")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="302.72", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="328.5", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="354.28", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="380.06", default_y="35"):
                with Pitch():
                    Step("F")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="405.85", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="12", default_y="-156.13"):
                with Pitch():
                    Step("F")
                    Octave("3")
                Duration("16")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="start")
                    with Technical():
                        Fingering("5", placement="below", default_x="7.46", default_y="-67.55")
            with Note(default_x="12", default_y="-146.13"):
                Chord()
                with Pitch():
                    Step("A")
                    Octave("3")
                Duration("16")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="start")
                    with Technical():
                        Fingering("3", placement="below", default_x="7.46", default_y="-64.19")
            with Note(default_x="12", default_y="-131.13"):
                Chord()
                with Pitch():
                    Step("D")
                    Octave("4")
                Duration("16")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="start")
                    with Technical():
                        Fingering("1", placement="below", default_x="7.46", default_y="-65.69")
        with Measure(number="10", width="475.64"):
            with Print(new_system="yes"):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin("0")
                        RightMargin("0")
                    SystemDistance("150")
                with StaffLayout(number="2"):
                    StaffDistance("104.27")
            with Note(default_x="61.32", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="87.1", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="112.88", default_y="35"):
                with Pitch():
                    Step("F")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="138.67", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="164.45", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="190.23", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="216.01", default_y="35"):
                with Pitch():
                    Step("F")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="241.8", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="267.58", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="293.36", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="319.15", default_y="35"):
                with Pitch():
                    Step("F")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="344.93", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="370.71", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="396.49", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="422.28", default_y="35"):
                with Pitch():
                    Step("F")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="448.06", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="60.36", default_y="-154.27"):
                with Pitch():
                    Step("F")
                    Octave("3")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
            with Note(default_x="60.36", default_y="-144.27"):
                Chord()
                with Pitch():
                    Step("A")
                    Octave("3")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
            with Note(default_x="60.36", default_y="-129.27"):
                Chord()
                with Pitch():
                    Step("D")
                    Octave("4")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
        with Measure(number="11", width="431.37"):
            with Note(default_x="12", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="37.78", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="63.57", default_y="35"):
                with Pitch():
                    Step("F")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="89.35", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="115.13", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="145.96", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Accidental("natural", cautionary="yes", parentheses="no")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="171.74", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="197.53", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="223.31", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="249.09", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="274.88", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="300.66", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="326.44", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="352.22", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="30.69")
            with Note(default_x="378.01", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="35.2")
            with Note(default_x="403.79", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Direction(placement="above"):
                with DirectionType():
                    OctaveShift(type="stop", size="8", number="1")
                Staff("1")
            with Backup():
                Duration("16")
            with Note(default_x="12", default_y="-154.27"):
                with Pitch():
                    Step("F")
                    Octave("3")
                Duration("4")
                Tie(type="stop")
                Voice("5")
                Type("quarter")
                Stem("down")
                Staff("2")
                with Notations():
                    Tied(type="stop")
            with Note(default_x="12", default_y="-144.27"):
                Chord()
                with Pitch():
                    Step("A")
                    Octave("3")
                Duration("4")
                Tie(type="stop")
                Voice("5")
                Type("quarter")
                Stem("down")
                Staff("2")
                with Notations():
                    Tied(type="stop")
            with Note(default_x="12", default_y="-129.27"):
                Chord()
                with Pitch():
                    Step("D")
                    Octave("4")
                Duration("4")
                Tie(type="stop")
                Voice("5")
                Type("quarter")
                Stem("down")
                Staff("2")
                with Notations():
                    Tied(type="stop")
            with Note(default_x="115.13", default_y="-164.27"):
                Rest()
                Duration("4")
                Voice("5")
                Type("quarter")
                Staff("2")
            with Note(default_x="223.31", default_y="-164.27"):
                Rest()
                Duration("8")
                Voice("5")
                Type("half")
                Staff("2")
        with Measure(number="12", width="426.32"):
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("D")
                    RootAlter("1")
                Kind("diminished", text="dim")
            with Note(default_x="12", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="37.78", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="63.57", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="89.35", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="115.13", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="43.16")
            with Note(default_x="140.91", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="46.02")
            with Note(default_x="166.7", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="192.48", default_y="-35"):
                with Pitch():
                    Step("F")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="218.26", default_y="-40"):
                with Pitch():
                    Step("E")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="48.35")
            with Note(default_x="244.04", default_y="-45"):
                with Pitch():
                    Step("D")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="269.83", default_y="-50"):
                with Pitch():
                    Step("C")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="295.61", default_y="-55"):
                with Pitch():
                    Step("B")
                    Octave("3")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="321.39", default_y="-45"):
                with Pitch():
                    Step("D")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="53.72")
            with Note(default_x="347.17", default_y="-50"):
                with Pitch():
                    Step("C")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="372.96", default_y="-55"):
                with Pitch():
                    Step("B")
                    Octave("3")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="398.74", default_y="-60"):
                with Pitch():
                    Step("A")
                    Octave("3")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="12", default_y="-164.27"):
                Rest()
                Duration("4")
                Voice("5")
                Type("quarter")
                Staff("2")
            with Note(default_x="115.13", default_y="-164.27"):
                Rest()
                Duration("8")
                Voice("5")
                Type("half")
                Staff("2")
            with Note(default_x="321.39", default_y="-189.27"):
                with Pitch():
                    Step("F")
                    Alter("1")
                    Octave("2")
                Duration("4")
                Voice("5")
                Type("quarter")
                Accidental("sharp")
                Stem("up")
                Staff("2")
            with Note(default_x="321.39", default_y="-169.27"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("4")
                Voice("5")
                Type("quarter")
                Stem("up")
                Staff("2")
            with Note(default_x="321.39", default_y="-159.27"):
                Chord()
                with Pitch():
                    Step("E")
                    Alter("-1")
                    Octave("3")
                Duration("4")
                Voice("5")
                Type("quarter")
                Accidental("flat")
                Stem("up")
                Staff("2")
        with Measure(number="13", width="474.68"):
            with Print(new_system="yes"):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin("0")
                        RightMargin("0")
                    SystemDistance("150")
                with StaffLayout(number="2"):
                    StaffDistance("102.41")
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("C")
                Kind("major")
                with Bass():
                    BassStep("G")
            with Note(default_x="58.36", default_y="-65"):
                with Pitch():
                    Step("G")
                    Octave("3")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="74.09")
            with Note(default_x="84.26", default_y="-60"):
                with Pitch():
                    Step("A")
                    Octave("3")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="110.17", default_y="-55"):
                with Pitch():
                    Step("B")
                    Octave("3")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="63.35")
            with Note(default_x="136.08", default_y="-50"):
                with Pitch():
                    Step("C")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="59.09")
            with Note(default_x="161.99", default_y="-45"):
                with Pitch():
                    Step("D")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="187.9", default_y="-40"):
                with Pitch():
                    Step("E")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="213.8", default_y="-35"):
                with Pitch():
                    Step("F")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="239.71", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="42.93")
            with Note(default_x="265.62", default_y="-40"):
                with Pitch():
                    Step("E")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="48.35")
            with Note(default_x="291.53", default_y="-50"):
                with Pitch():
                    Step("C")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="59.09")
            with Note(default_x="317.43", default_y="-45"):
                with Pitch():
                    Step("D")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="343.34", default_y="-40"):
                with Pitch():
                    Step("E")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="369.25", default_y="-35"):
                with Pitch():
                    Step("F")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="53.23")
            with Note(default_x="395.16", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="421.07", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="446.97", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="57.39", default_y="-182.41"):
                with Pitch():
                    Step("G")
                    Octave("2")
                Duration("16")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="start")
                    with Technical():
                        Fingering("5", placement="below", default_x="7.46", default_y="-42.95")
            with Note(default_x="57.39", default_y="-167.41"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("16")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="start")
                    with Technical():
                        Fingering("2", placement="below", default_x="7.46", default_y="-44.59")
            with Note(default_x="57.39", default_y="-157.41"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("3")
                Duration("16")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Accidental("natural", cautionary="yes", parentheses="no")
                Staff("2")
                with Notations():
                    Tied(type="start")
                    with Technical():
                        Fingering("1", placement="below", default_x="7.46", default_y="-41.09")
        with Measure(number="14", width="429.33"):
            with Note(default_x="13", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="42.9")
            with Note(default_x="38.91", default_y="-40"):
                with Pitch():
                    Step("E")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="65.68")
            with Note(default_x="64.82", default_y="-35"):
                with Pitch():
                    Step("F")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="90.72", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="116.63", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="35.69")
            with Note(default_x="142.54", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="168.45", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="194.36", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="220.26", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="246.17", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="40.69")
            with Note(default_x="272.08", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="297.99", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="323.89", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="25.69")
            with Note(default_x="349.8", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="375.71", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="401.62", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="12.04", default_y="-182.41"):
                with Pitch():
                    Step("G")
                    Octave("2")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
            with Note(default_x="12.04", default_y="-167.41"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
            with Note(default_x="12.04", default_y="-157.41"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("3")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Accidental("natural", cautionary="yes", parentheses="no")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
        with Measure(number="15", width="429.33"):
            with Note(default_x="13", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="38.91", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="25.69")
            with Note(default_x="64.82", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="90.72", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="116.63", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="142.54", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="168.45", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="194.36", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="220.26", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="246.17", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="272.08", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="297.99", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="323.89", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="349.8", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="375.71", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="401.62", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Backup():
                Duration("16")
            with Note(default_x="12.04", default_y="-182.41"):
                with Pitch():
                    Step("G")
                    Octave("2")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
            with Note(default_x="12.04", default_y="-167.41"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
            with Note(default_x="12.04", default_y="-157.41"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("3")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Accidental("natural", cautionary="yes", parentheses="no")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
        with Measure(number="16", width="479.35"):
            with Print(new_page="yes"):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin("0")
                        RightMargin("0")
                    TopSystemDistance("70")
                with StaffLayout(number="2"):
                    StaffDistance("91.27")
            with Note(default_x="65.36", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="91.12", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="116.88", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="142.64", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="168.4", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="194.17", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="219.93", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="245.69", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="271.45", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="297.21", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="322.98", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="348.74", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="374.5", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="400.26", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="426.02", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="451.79", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Backup():
                Duration("16")
            with Note(default_x="64.39", default_y="-171.27"):
                with Pitch():
                    Step("G")
                    Octave("2")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
            with Note(default_x="64.39", default_y="-156.27"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
            with Note(default_x="64.39", default_y="-146.27"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("3")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Accidental("natural", cautionary="yes", parentheses="no")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
        with Measure(number="17", width="426.99"):
            with Note(default_x="13", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="38.76", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="64.52", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="90.29", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("2", default_x="6.5", default_y="15.39")
            with Note(default_x="116.05", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="141.81", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("2", default_x="6.5", default_y="15.39")
            with Note(default_x="167.57", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="193.33", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="219.1", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="244.86", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="270.62", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="296.38", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("2", default_x="6.5", default_y="15.39")
            with Note(default_x="322.14", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="347.91", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="373.67", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="399.43", default_y="35"):
                with Pitch():
                    Step("F")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="12.04", default_y="-171.27"):
                with Pitch():
                    Step("G")
                    Octave("2")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
            with Note(default_x="12.04", default_y="-156.27"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
            with Note(default_x="12.04", default_y="-146.27"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("3")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Accidental("natural", cautionary="yes", parentheses="no")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
        with Measure(number="18", width="426.99"):
            with Direction(placement="above"):
                with DirectionType():
                    OctaveShift(type="down", size="8", number="1", default_y="51.95")
                Staff("1")
            with Note(default_x="13", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="38.76", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="64.52", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="90.29", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("2", default_x="6.5", default_y="15.39")
            with Note(default_x="116.05", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="141.81", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="167.57", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="193.33", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="219.1", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="244.86", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="270.62", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="296.38", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
                with Notations():
                    with Technical():
                        Fingering("2", default_x="6.5", default_y="15.39")
            with Note(default_x="322.14", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="347.91", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="373.67", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="399.43", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="12.04", default_y="-171.27"):
                with Pitch():
                    Step("G")
                    Octave("2")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
            with Note(default_x="12.04", default_y="-156.27"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
            with Note(default_x="12.04", default_y="-146.27"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("3")
                Duration("16")
                Tie(type="stop")
                Tie(type="start")
                Voice("5")
                Type("whole")
                Accidental("natural", cautionary="yes", parentheses="no")
                Staff("2")
                with Notations():
                    Tied(type="stop")
                    Tied(type="start")
        with Measure(number="19", width="451.27"):
            with Print(new_system="yes"):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin("0")
                        RightMargin("0")
                    SystemDistance("164.3")
                with StaffLayout(number="2"):
                    StaffDistance("100.56")
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("C")
                Kind("major")
                with Bass():
                    BassStep("G")
            with Note(default_x="64.39", default_y="25"):
                with Pitch():
                    Step("D")
                    Alter("1")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Accidental("sharp")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="88.01", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="118.84", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Accidental("natural")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="142.46", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("7")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="166.07", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="189.69", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="213.31", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="236.92", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Direction(placement="above"):
                with DirectionType():
                    OctaveShift(type="stop", size="8", number="1")
                Staff("1")
            with Note(default_x="260.54", default_y="30"):
                with Pitch():
                    Step("E")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="284.15", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="307.77", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="331.39", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="355", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="378.62", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="15.39")
            with Note(default_x="402.23", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="425.85", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="64.39", default_y="-180.56"):
                with Pitch():
                    Step("G")
                    Octave("2")
                Duration("4")
                Tie(type="stop")
                Voice("5")
                Type("quarter")
                Stem("up")
                Staff("2")
                with Notations():
                    Tied(type="stop")
            with Note(default_x="64.39", default_y="-165.56"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("4")
                Tie(type="stop")
                Voice("5")
                Type("quarter")
                Stem("up")
                Staff("2")
                with Notations():
                    Tied(type="stop")
            with Note(default_x="64.39", default_y="-155.56"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("3")
                Duration("4")
                Tie(type="stop")
                Voice("5")
                Type("quarter")
                Accidental("natural", cautionary="yes", parentheses="no")
                Stem("up")
                Staff("2")
                with Notations():
                    Tied(type="stop")
            with Note(default_x="166.07", default_y="-160.56"):
                Rest()
                Duration("4")
                Voice("5")
                Type("quarter")
                Staff("2")
            with Note(default_x="260.54", default_y="-145.56"):
                with Pitch():
                    Step("G")
                    Octave("3")
                Duration("4")
                Voice("5")
                Type("quarter")
                Stem("down")
                Staff("2")
            with Note(default_x="260.54", default_y="-130.56"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("4")
                Duration("4")
                Voice("5")
                Type("quarter")
                Stem("down")
                Staff("2")
            with Note(default_x="260.54", default_y="-120.56"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("4")
                Duration("4")
                Voice("5")
                Type("quarter")
                Stem("down")
                Staff("2")
            with Note(default_x="355", default_y="-160.56"):
                Rest()
                Duration("4")
                Voice("5")
                Type("quarter")
                Staff("2")
        with Measure(number="20", width="391.66"):
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("G")
                Kind("dominant", text="7")
            with Note(default_x="12", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="20.69")
            with Note(default_x="35.62", default_y="25"):
                with Pitch():
                    Step("D")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("5", default_x="6.5", default_y="15.64")
            with Note(default_x="59.23", default_y="20"):
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="82.85", default_y="15"):
                with Pitch():
                    Step("B")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="106.46", default_y="10"):
                with Pitch():
                    Step("A")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="130.08", default_y="5"):
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("1", default_x="6.5", default_y="15.89")
            with Note(default_x="153.7", default_y="0"):
                with Pitch():
                    Step("F")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("3", default_x="6.5", default_y="15.39")
            with Note(default_x="177.31", default_y="-5"):
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="200.93", default_y="-10"):
                with Pitch():
                    Step("D")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="224.54", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="25.2")
            with Note(default_x="248.16", default_y="-20"):
                with Pitch():
                    Step("B")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="271.78", default_y="-25"):
                with Pitch():
                    Step("A")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Note(default_x="295.39", default_y="-30"):
                with Pitch():
                    Step("G")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("begin", number="1")
                Beam("begin", number="2")
            with Note(default_x="319.01", default_y="-35"):
                with Pitch():
                    Step("F")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
                with Notations():
                    with Technical():
                        Fingering("4", default_x="6.5", default_y="46.86")
            with Note(default_x="342.63", default_y="-40"):
                with Pitch():
                    Step("E")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("continue", number="1")
                Beam("continue", number="2")
            with Note(default_x="366.24", default_y="-45"):
                with Pitch():
                    Step("D")
                    Octave("4")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("up")
                Staff("1")
                Beam("end", number="1")
                Beam("end", number="2")
            with Backup():
                Duration("16")
            with Note(default_x="12", default_y="-145.56"):
                with Pitch():
                    Step("G")
                    Octave("3")
                Duration("4")
                Voice("5")
                Type("quarter")
                Stem("down")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("5", placement="below", default_x="6.5", default_y="-72.55")
            with Note(default_x="12", default_y="-135.56"):
                Chord()
                with Pitch():
                    Step("B")
                    Octave("3")
                Duration("4")
                Voice("5")
                Type("quarter")
                Stem("down")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("3", placement="below", default_x="6.5", default_y="-69.19")
            with Note(default_x="12", default_y="-115.56"):
                Chord()
                with Pitch():
                    Step("F")
                    Octave("4")
                Duration("4")
                Voice("5")
                Type("quarter")
                Stem("down")
                Staff("2")
                with Notations():
                    with Technical():
                        Fingering("1", placement="below", default_x="6.5", default_y="-75.69")
            with Note(default_x="106.46", default_y="-160.56"):
                Rest()
                Duration("4")
                Voice("5")
                Type("quarter")
                Staff("2")
            with Note(default_x="200.93", default_y="-180.56"):
                with Pitch():
                    Step("G")
                    Octave("2")
                Duration("4")
                Voice("5")
                Type("quarter")
                Stem("up")
                Staff("2")
            with Note(default_x="200.93", default_y="-170.56"):
                Chord()
                with Pitch():
                    Step("B")
                    Octave("2")
                Duration("4")
                Voice("5")
                Type("quarter")
                Stem("up")
                Staff("2")
            with Note(default_x="200.93", default_y="-150.56"):
                Chord()
                with Pitch():
                    Step("F")
                    Octave("3")
                Duration("4")
                Voice("5")
                Type("quarter")
                Stem("up")
                Staff("2")
            with Note(default_x="295.39", default_y="-160.56"):
                Rest()
                Duration("4")
                Voice("5")
                Type("quarter")
                Staff("2")
        with Measure(number="21", width="273.58"):
            with Harmony(print_frame="no"):
                with Root():
                    RootStep("C")
                Kind("major")
            with Note(default_x="12", default_y="-50"):
                with Pitch():
                    Step("C")
                    Octave("4")
                Duration("2")
                Voice("1")
                Type("eighth")
                Stem("up")
                Staff("1")
            with Note(default_x="47.42", default_y="-20"):
                Rest()
                Duration("2")
                Voice("1")
                Type("eighth")
                Staff("1")
            with Note(default_x="82.85", default_y="-20"):
                Rest()
                Duration("4")
                Voice("1")
                Type("quarter")
                Staff("1")
            with Note(default_x="135.98", default_y="-15"):
                with Pitch():
                    Step("C")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
            with Note(default_x="135.98", default_y="-5"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
            with Note(default_x="135.98", default_y="5"):
                Chord()
                with Pitch():
                    Step("G")
                    Octave("5")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
            with Note(default_x="135.98", default_y="20"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("6")
                Duration("1")
                Voice("1")
                Type("16th")
                Stem("down")
                Staff("1")
            with Note(default_x="159.6", default_y="-20"):
                Rest()
                Duration("1")
                Voice("1")
                Type("16th")
                Staff("1")
            with Note(default_x="183.22", default_y="-20"):
                Rest()
                Duration("2")
                Voice("1")
                Type("eighth")
                Staff("1")
            with Note(default_x="218.64", default_y="-20"):
                Rest()
                Duration("4")
                Voice("1")
                Type("quarter")
                Staff("1")
            with Backup():
                Duration("16")
            with Note(default_x="12", default_y="-165.56"):
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("2")
                Voice("5")
                Type("eighth")
                Stem("down")
                Staff("2")
            with Note(default_x="12", default_y="-155.56"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("3")
                Duration("2")
                Voice("5")
                Type("eighth")
                Stem("down")
                Staff("2")
            with Note(default_x="47.42", default_y="-160.56"):
                Rest()
                Duration("2")
                Voice("5")
                Type("eighth")
                Staff("2")
            with Note(default_x="82.85", default_y="-160.56"):
                Rest()
                Duration("4")
                Voice("5")
                Type("quarter")
                Staff("2")
            with Note(default_x="135.98", default_y="-165.56"):
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("1")
                Voice("5")
                Type("16th")
                Stem("down")
                Staff("2")
            with Note(default_x="135.98", default_y="-155.56"):
                Chord()
                with Pitch():
                    Step("E")
                    Octave("3")
                Duration("1")
                Voice("5")
                Type("16th")
                Stem("down")
                Staff("2")
            with Note(default_x="135.98", default_y="-145.56"):
                Chord()
                with Pitch():
                    Step("G")
                    Octave("3")
                Duration("1")
                Voice("5")
                Type("16th")
                Stem("down")
                Staff("2")
            with Note(default_x="135.98", default_y="-130.56"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("4")
                Duration("1")
                Voice("5")
                Type("16th")
                Stem("down")
                Staff("2")
            with Note(default_x="159.6", default_y="-160.56"):
                Rest()
                Duration("1")
                Voice("5")
                Type("16th")
                Staff("2")
            with Note(default_x="183.22", default_y="-160.56"):
                Rest()
                Duration("2")
                Voice("5")
                Type("eighth")
                Staff("2")
            with Note(default_x="218.64", default_y="-160.56"):
                Rest()
                Duration("4")
                Voice("5")
                Type("quarter")
                Staff("2")
        with Measure(number="22", width="216.83"):
            with Note(default_x="12", default_y="-50"):
                with Pitch():
                    Step("C")
                    Octave("4")
                Duration("4")
                Voice("1")
                Type("quarter")
                Stem("up")
                Staff("1")
            with Note(default_x="65.14", default_y="-20"):
                Rest()
                Duration("4")
                Voice("1")
                Type("quarter")
                Staff("1")
            with Note(default_x="118.27", default_y="-20"):
                Rest()
                Duration("8")
                Voice("1")
                Type("half")
                Staff("1")
            with Backup():
                Duration("16")
            with Note(default_x="12", default_y="-200.56"):
                with Pitch():
                    Step("C")
                    Octave("2")
                Duration("4")
                Voice("5")
                Type("quarter")
                Stem("up")
                Staff("2")
            with Note(default_x="12", default_y="-165.56"):
                Chord()
                with Pitch():
                    Step("C")
                    Octave("3")
                Duration("4")
                Voice("5")
                Type("quarter")
                Stem("up")
                Staff("2")
            with Note(default_x="65.14", default_y="-160.56"):
                Rest()
                Duration("4")
                Voice("5")
                Type("quarter")
                Staff("2")
            with Note(default_x="118.27", default_y="-160.56"):
                Rest()
                Duration("8")
                Voice("5")
                Type("half")
                Staff("2")
            with Barline(location="right"):
                BarStyle("light-heavy")
                Repeat(direction="backward")
