from __future__ import annotations
from typing import Type as TYPE
from musicpy import MusicElementBase, _


class AboveBelow(MusicElementBase):
  """The above-below type is used to indicate whether one element appears above or below another element."""

  ABOVE = _
  BELOW = _

  def __init__(self, plain_text: str):
    self.init()


class AccidentalValue(MusicElementBase):
  """The accidental-value type represents notated accidentals supported by MusicXML.

  In the MusicXML 2.0 DTD this was a string with values that could be included.
  The XSD strengthens the data typing to an enumerated list. The quarter- and
  three-quarters- accidentals are Tartini-style quarter-tone accidentals. The
  -down and -up accidentals are quarter-tone accidentals that include arrows
  pointing down or up. The slash- accidentals are used in Turkish classical
  music. The numbered sharp and flat accidentals are superscripted versions of
  the accidental signs, used in Turkish folk music. The sori and koron
  accidentals are microtonal sharp and flat accidentals used in Iranian and
  Persian music. The other accidental covers accidentals other than those listed
  here. It is usually used in combination with the smufl attribute to specify a
  particular SMuFL accidental. The smufl attribute may be used with any
  accidental value to help specify the appearance of symbols that share the same
  MusicXML semantics.
  """

  ARROW_DOWN = _
  ARROW_UP = _
  DOUBLE_SHARP = _
  DOUBLE_SHARP_DOWN = _
  DOUBLE_SHARP_UP = _
  DOUBLE_SLASH_FLAT = _
  FLAT = _
  FLAT_1 = _
  FLAT_2 = _
  FLAT_3 = _
  FLAT_4 = _
  FLAT_DOWN = _
  FLAT_FLAT = _
  FLAT_FLAT_DOWN = _
  FLAT_FLAT_UP = _
  FLAT_UP = _
  KORON = _
  NATURAL = _
  NATURAL_DOWN = _
  NATURAL_FLAT = _
  NATURAL_SHARP = _
  NATURAL_UP = _
  OTHER = _
  QUARTER_FLAT = _
  QUARTER_SHARP = _
  SHARP = _
  SHARP_1 = _
  SHARP_2 = _
  SHARP_3 = _
  SHARP_5 = _
  SHARP_DOWN = _
  SHARP_SHARP = _
  SHARP_UP = _
  SLASH_FLAT = _
  SLASH_QUARTER_SHARP = _
  SLASH_SHARP = _
  SORI = _
  THREE_QUARTERS_FLAT = _
  THREE_QUARTERS_SHARP = _
  TRIPLE_FLAT = _
  TRIPLE_SHARP = _

  def __init__(self, plain_text: str):
    self.init()


class AccordionMiddle(MusicElementBase):
  """The accordion-middle type may have values of 1, 2, or 3, corresponding to having 1 to 3 dots in the middle section of the accordion registration symbol.

  This type is not used if no dots are present.
  """

  def __init__(self, plain_text: int):
    self.init()


class ArrowDirection(MusicElementBase):
  """The arrow-direction type represents the direction in which an arrow points, using Unicode arrow terminology."""

  DOWN = _
  LEFT = _
  LEFT_RIGHT = 'left right'
  NORTHEAST = _
  NORTHEAST_SOUTHWEST = 'northeast southwest'
  NORTHWEST = _
  NORTHWEST_SOUTHEAST = 'northwest southeast'
  OTHER = _
  RIGHT = _
  SOUTHEAST = _
  SOUTHWEST = _
  UP = _
  UP_DOWN = 'up down'

  def __init__(self, plain_text: str):
    self.init()


class ArrowStyle(MusicElementBase):
  """The arrow-style type represents the style of an arrow, using Unicode arrow terminology.

  Filled and hollow arrows indicate polygonal single arrows. Paired arrows are
  duplicate single arrows in the same direction. Combined arrows apply to double
  direction arrows like left right, indicating that an arrow in one direction
  should be combined with an arrow in the other direction.
  """

  COMBINED = _
  DOUBLE = _
  FILLED = _
  HOLLOW = _
  OTHER = _
  PAIRED = _
  SINGLE = _

  def __init__(self, plain_text: str):
    self.init()


class BackwardForward(MusicElementBase):
  """The backward-forward type is used to specify repeat directions.

  The start of the repeat has a forward direction while the end of the repeat
  has a backward direction.
  """

  BACKWARD = _
  FORWARD = _

  def __init__(self, plain_text: str):
    self.init()


class BarStyle(MusicElementBase):
  """The bar-style type represents barline style information.

  Choices are regular, dotted, dashed, heavy, light-light, light-heavy,
  heavy-light, heavy-heavy, tick (a short stroke through the top line), short (a
  partial barline between the 2nd and 4th lines), and none.
  """

  DASHED = _
  DOTTED = _
  HEAVY = _
  HEAVY_HEAVY = _
  HEAVY_LIGHT = _
  LIGHT_HEAVY = _
  LIGHT_LIGHT = _
  NONE = _
  REGULAR = _
  SHORT = _
  TICK = _

  def __init__(self, plain_text: str):
    self.init()


class BeamLevel(MusicElementBase):
  """The MusicXML format supports six levels of beaming, up to 1024th notes.

  Unlike the number-level type, the beam-level type identifies concurrent beams
  in a beam group. It does not distinguish overlapping beams such as grace notes
  within regular notes, or beams used in different voices.
  """

  def __init__(self, plain_text: int):
    self.init()


class BeamValue(MusicElementBase):
  """The beam-value type represents the type of beam associated with each of 8 beam levels (up to 1024th notes) available for each note."""

  BACKWARD_HOOK = 'backward hook'
  BEGIN = _
  CONTINUE = _
  END = _
  FORWARD_HOOK = 'forward hook'

  def __init__(self, plain_text: str):
    self.init()


class BeaterValue(MusicElementBase):
  """The beater-value type represents pictograms for beaters, mallets, and sticks that do not have different materials represented in the pictogram.

  The finger and hammer values are in addition to Stone's list.
  """

  BOW = _
  CHIME_HAMMER = 'chime hammer'
  COIN = _
  DRUM_STICK = 'drum stick'
  FINGER = _
  FINGERNAIL = _
  FIST = _
  GUIRO_SCRAPER = 'guiro scraper'
  HAMMER = _
  HAND = _
  JAZZ_STICK = 'jazz stick'
  KNITTING_NEEDLE = 'knitting needle'
  METAL_HAMMER = 'metal hammer'
  SLIDE_BRUSH_ON_GONG = 'slide brush on gong'
  SNARE_STICK = 'snare stick'
  SPOON_MALLET = 'spoon mallet'
  SUPERBALL = _
  TRIANGLE_BEATER = 'triangle beater'
  TRIANGLE_BEATER_PLAIN = 'triangle beater plain'
  WIRE_BRUSH = 'wire brush'

  def __init__(self, plain_text: str):
    self.init()


class BendShape(MusicElementBase):
  """The bend-shape type distinguishes between the angled bend symbols commonly used in standard notation and the curved bend symbols commonly used in both tablature and standard notation."""

  ANGLED = _
  CURVED = _

  def __init__(self, plain_text: str):
    self.init()


class BreathMarkValue(MusicElementBase):
  """The breath-mark-value type represents the symbol used for a breath mark."""

  COMMA = _
  SALZEDO = _
  TICK = _
  UPBOW = _

  def __init__(self, plain_text: str):
    self.init()


class CaesuraValue(MusicElementBase):
  """The caesura-value type represents the shape of the caesura sign."""

  CURVED = _
  NORMAL = _
  SHORT = _
  SINGLE = _
  THICK = _

  def __init__(self, plain_text: str):
    self.init()


class CancelLocation(MusicElementBase):
  """The cancel-location type is used to indicate where a key signature cancellation appears relative to a new key signature: to the left, to the right, or before the barline and to the left.

  It is left by default. For mid-measure key elements, a cancel-location of
  before-barline should be treated like a cancel-location of left.
  """

  BEFORE_BARLINE = _
  LEFT = _
  RIGHT = _

  def __init__(self, plain_text: str):
    self.init()


class CircularArrow(MusicElementBase):
  """The circular-arrow type represents the direction in which a circular arrow points, using Unicode arrow terminology."""

  ANTICLOCKWISE = _
  CLOCKWISE = _

  def __init__(self, plain_text: str):
    self.init()


class ClefSign(MusicElementBase):
  """The clef-sign type represents the different clef symbols.

  The jianpu sign indicates that the music that follows should be in jianpu
  numbered notation, just as the TAB sign indicates that the music that follows
  should be in tablature notation. Unlike TAB, a jianpu sign does not correspond
  to a visual clef notation.

  The none sign is deprecated as of MusicXML 4.0. Use the clef element's
  print-object attribute instead. When the none sign is used, notes should be
  displayed as if in treble clef.
  """

  C = _
  F = _
  G = _
  JIANPU = _
  NONE = _
  PERCUSSION = _
  TAB = _

  def __init__(self, plain_text: str):
    self.init()


class Color(MusicElementBase):
  """The color type indicates the color of an element.

  Color may be represented as hexadecimal RGB triples, as in HTML, or as
  hexadecimal ARGB tuples, with the A indicating alpha of transparency. An alpha
  value of 00 is totally transparent; FF is totally opaque. If RGB is used, the
  A value is assumed to be FF.

  For instance, the RGB value "#800080" represents purple. An ARGB value of
  "#40800080" would be a transparent purple.

  As in SVG 1.1, colors are defined in terms of the sRGB color space (IEC
  61966).
  """

  def __init__(self, plain_text: str):
    self.init()


class CommaSeparatedText(MusicElementBase):
  """The comma-separated-text type is used to specify a comma-separated list of text elements, as is used by the font-family attribute."""

  def __init__(self, plain_text: str):
    self.init()


class CssFontSize(MusicElementBase):
  """The css-font-size type includes the CSS font sizes used as an alternative to a numeric point size."""

  LARGE = _
  MEDIUM = _
  SMALL = _
  XX_LARGE = _
  XX_SMALL = _
  X_LARGE = _
  X_SMALL = _

  def __init__(self, plain_text: str):
    self.init()


class DegreeSymbolValue(MusicElementBase):
  """The degree-symbol-value type indicates which symbol should be used in specifying a degree."""

  AUGMENTED = _
  DIMINISHED = _
  HALF_DIMINISHED = _
  MAJOR = _
  MINOR = _

  def __init__(self, plain_text: str):
    self.init()


class DegreeTypeValue(MusicElementBase):
  """The degree-type-value type indicates whether the current degree element is an addition, alteration, or subtraction to the kind of the current chord in the harmony element."""

  ADD = _
  ALTER = _
  SUBTRACT = _

  def __init__(self, plain_text: str):
    self.init()


class DistanceType(MusicElementBase):
  """The distance-type defines what type of distance is being defined in a distance element.

  Values include beam and hyphen. This is left as a string so that other
  application-specific types can be defined, but it is made a separate type so
  that it can be redefined more strictly.
  """

  def __init__(self, plain_text: str):
    self.init()


class Divisions(MusicElementBase):
  """The divisions type is used to express values in terms of the musical divisions defined by the divisions element.

  It is preferred that these be integer values both for MIDI interoperability
  and to avoid roundoff errors.
  """

  def __init__(self, plain_text: float):
    self.init()


class EffectValue(MusicElementBase):
  """The effect-value type represents pictograms for sound effect percussion instruments.

  The cannon, lotus flute, and megaphone values are in addition to Stone's list.
  """

  ANVIL = _
  AUTO_HORN = 'auto horn'
  BIRD_WHISTLE = 'bird whistle'
  CANNON = _
  DUCK_CALL = 'duck call'
  GUN_SHOT = 'gun shot'
  KLAXON_HORN = 'klaxon horn'
  LIONS_ROAR = 'lions roar'
  LOTUS_FLUTE = 'lotus flute'
  MEGAPHONE = _
  POLICE_WHISTLE = 'police whistle'
  SIREN = _
  SLIDE_WHISTLE = 'slide whistle'
  THUNDER_SHEET = 'thunder sheet'
  WIND_MACHINE = 'wind machine'
  WIND_WHISTLE = 'wind whistle'

  def __init__(self, plain_text: str):
    self.init()


class EnclosureShape(MusicElementBase):
  """The enclosure-shape type describes the shape and presence / absence of an enclosure around text or symbols.

  A bracket enclosure is similar to a rectangle with the bottom line missing, as
  is common in jazz notation. An inverted-bracket enclosure is similar to a
  rectangle with the top line missing.
  """

  BRACKET = _
  CIRCLE = _
  DECAGON = _
  DIAMOND = _
  HEPTAGON = _
  HEXAGON = _
  INVERTED_BRACKET = _
  NONAGON = _
  NONE = _
  OCTAGON = _
  OVAL = _
  PENTAGON = _
  RECTANGLE = _
  SQUARE = _
  TRIANGLE = _

  def __init__(self, plain_text: str):
    self.init()


class EndingNumber(MusicElementBase):
  """The ending-number type is used to specify either a comma-separated list of positive integers without leading zeros, or a string of zero or more spaces.

  It is used for the number attribute of the ending element. The zero or more
  spaces version is used when software knows that an ending is present, but
  cannot determine the type of the ending.
  """

  def __init__(self, plain_text: str):
    self.init()


class Fan(MusicElementBase):
  """The fan type represents the type of beam fanning present on a note, used to represent accelerandos and ritardandos."""

  ACCEL = _
  NONE = _
  RIT = _

  def __init__(self, plain_text: str):
    self.init()


class FermataShape(MusicElementBase):
  """The fermata-shape type represents the shape of the fermata sign.

  The empty value is equivalent to the normal value.
  """

  ANGLED = _
  CURLEW = _
  DOUBLE_ANGLED = _
  DOUBLE_DOT = _
  DOUBLE_SQUARE = _
  HALF_CURVE = _
  NORMAL = _
  SQUARE = _

  def __init__(self, plain_text: str):
    self.init()


class Fifths(MusicElementBase):
  """The fifths type represents the number of flats or sharps in a traditional key signature.

  Negative numbers are used for flats and positive numbers for sharps,
  reflecting the key's placement within the circle of fifths (hence the type
  name).
  """

  def __init__(self, plain_text: int):
    self.init()


class FontFamily(MusicElementBase):
  """The font-family is a comma-separated list of font names.

  These can be specific font styles such as Maestro or Opus, or one of several
  generic font styles: music, engraved, handwritten, text, serif, sans-serif,
  handwritten, cursive, fantasy, and monospace. The music, engraved, and
  handwritten values refer to music fonts; the rest refer to text fonts. The
  fantasy style refers to decorative text such as found in older German-style
  printing.
  """

  def __init__(self, plain_text: str):
    self.init()


class FontSize(MusicElementBase):
  """The font-size can be one of the CSS font sizes (xx-small, x-small, small, medium, large, x-large, xx-large) or a numeric point size."""

  def __init__(self, plain_text: str):
    self.init()


class FontStyle(MusicElementBase):
  """The font-style type represents a simplified version of the CSS font-style property."""

  ITALIC = _
  NORMAL = _

  def __init__(self, plain_text: str):
    self.init()


class FontWeight(MusicElementBase):
  """The font-weight type represents a simplified version of the CSS font-weight property."""

  BOLD = _
  NORMAL = _

  def __init__(self, plain_text: str):
    self.init()


class GlassValue(MusicElementBase):
  """The glass-value type represents pictograms for glass percussion instruments."""

  GLASS_HARMONICA = 'glass harmonica'
  GLASS_HARP = 'glass harp'
  WIND_CHIMES = 'wind chimes'

  def __init__(self, plain_text: str):
    self.init()


class GlyphType(MusicElementBase):
  """The glyph-type defines what type of glyph is being defined in a glyph element.

  Values include quarter-rest, g-clef-ottava-bassa, c-clef, f-clef,
  percussion-clef, octave-shift-up-8, octave-shift-down-8,
  octave-shift-continue-8, octave-shift-down-15, octave-shift-up-15,
  octave-shift-continue-15, octave-shift-down-22, octave-shift-up-22, and
  octave-shift-continue-22. This is left as a string so that other
  application-specific types can be defined, but it is made a separate type so
  that it can be redefined more strictly.

  A quarter-rest type specifies the glyph to use when a note has a rest element
  and a type value of quarter. The c-clef, f-clef, and percussion-clef types
  specify the glyph to use when a clef sign element value is C, F, or percussion
  respectively. The g-clef-ottava-bassa type specifies the glyph to use when a
  clef sign element value is G and the clef-octave-change element value is -1.
  The octave-shift types specify the glyph to use when an octave-shift type
  attribute value is up, down, or continue and the octave-shift size attribute
  value is 8, 15, or 22.
  """

  def __init__(self, plain_text: str):
    self.init()


class GroupBarlineValue(MusicElementBase):
  """The group-barline-value type indicates if the group should have common barlines."""

  MENSURSTRICH = _
  NO = _
  YES = _

  def __init__(self, plain_text: str):
    self.init()


class GroupSymbolValue(MusicElementBase):
  """The group-symbol-value type indicates how the symbol for a group or multi-staff part is indicated in the score."""

  BRACE = _
  BRACKET = _
  LINE = _
  NONE = _
  SQUARE = _

  def __init__(self, plain_text: str):
    self.init()


class HandbellValue(MusicElementBase):
  """The handbell-value type represents the type of handbell technique being notated."""

  BELLTREE = _
  DAMP = _
  ECHO = _
  GYRO = _
  HAND_MARTELLATO = 'hand martellato'
  MALLET_LIFT = 'mallet lift'
  MALLET_TABLE = 'mallet table'
  MARTELLATO = _
  MARTELLATO_LIFT = 'martellato lift'
  MUTED_MARTELLATO = 'muted martellato'
  PLUCK_LIFT = 'pluck lift'
  SWING = _

  def __init__(self, plain_text: str):
    self.init()


class HarmonClosedLocation(MusicElementBase):
  """The harmon-closed-location type indicates which portion of the symbol is filled in when the corresponding harmon-closed-value is half."""

  BOTTOM = _
  LEFT = _
  RIGHT = _
  TOP = _

  def __init__(self, plain_text: str):
    self.init()


class HarmonClosedValue(MusicElementBase):
  """The harmon-closed-value type represents whether the harmon mute is closed, open, or half-open."""

  HALF = _
  NO = _
  YES = _

  def __init__(self, plain_text: str):
    self.init()


class HarmonyArrangement(MusicElementBase):
  """The harmony-arrangement type indicates how stacked chords and bass notes are displayed within a harmony element.

  The vertical value specifies that the second element appears below the first.
  The horizontal value specifies that the second element appears to the right of
  the first. The diagonal value specifies that the second element appears both
  below and to the right of the first.
  """

  DIAGONAL = _
  HORIZONTAL = _
  VERTICAL = _

  def __init__(self, plain_text: str):
    self.init()


class HarmonyType(MusicElementBase):
  """The harmony-type type differentiates different types of harmonies when alternate harmonies are possible.

  Explicit harmonies have all note present in the music; implied have some notes
  missing but implied; alternate represents alternate analyses.
  """

  ALTERNATE = _
  EXPLICIT = _
  IMPLIED = _

  def __init__(self, plain_text: str):
    self.init()


class HoleClosedLocation(MusicElementBase):
  """The hole-closed-location type indicates which portion of the hole is filled in when the corresponding hole-closed-value is half."""

  BOTTOM = _
  LEFT = _
  RIGHT = _
  TOP = _

  def __init__(self, plain_text: str):
    self.init()


class HoleClosedValue(MusicElementBase):
  """The hole-closed-value type represents whether the hole is closed, open, or half-open."""

  HALF = _
  NO = _
  YES = _

  def __init__(self, plain_text: str):
    self.init()


class KindValue(MusicElementBase):
  """A kind-value indicates the type of chord.

  Degree elements can then add, subtract, or alter from these starting points.
  Values include:

  Triads:
          major (major third, perfect fifth)
          minor (minor third, perfect fifth)
          augmented (major third, augmented fifth)
          diminished (minor third, diminished fifth)
  Sevenths:
          dominant (major triad, minor seventh)
          major-seventh (major triad, major seventh)
          minor-seventh (minor triad, minor seventh)
          diminished-seventh (diminished triad, diminished seventh)
          augmented-seventh (augmented triad, minor seventh)
          half-diminished (diminished triad, minor seventh)
          major-minor (minor triad, major seventh)
  Sixths:
          major-sixth (major triad, added sixth)
          minor-sixth (minor triad, added sixth)
  Ninths:
          dominant-ninth (dominant-seventh, major ninth)
          major-ninth (major-seventh, major ninth)
          minor-ninth (minor-seventh, major ninth)
  11ths (usually as the basis for alteration):
          dominant-11th (dominant-ninth, perfect 11th)
          major-11th (major-ninth, perfect 11th)
          minor-11th (minor-ninth, perfect 11th)
  13ths (usually as the basis for alteration):
          dominant-13th (dominant-11th, major 13th)
          major-13th (major-11th, major 13th)
          minor-13th (minor-11th, major 13th)
  Suspended:
          suspended-second (major second, perfect fifth)
          suspended-fourth (perfect fourth, perfect fifth)
  Functional sixths:
          Neapolitan
          Italian
          French
          German
  Other:
          pedal (pedal-point bass)
          power (perfect fifth)
          Tristan

  The "other" kind is used when the harmony is entirely composed of add
  elements.

  The "none" kind is used to explicitly encode absence of chords or functional
  harmony. In this case, the root, numeral, or function element has no meaning.
  When using the root or numeral element, the root-step or numeral-step text
  attribute should be set to the empty string to keep the root or numeral from
  being displayed.
  """

  AUGMENTED = _
  AUGMENTED_SEVENTH = _
  DIMINISHED = _
  DIMINISHED_SEVENTH = _
  DOMINANT = _
  DOMINANT_11TH = _
  DOMINANT_13TH = _
  DOMINANT_NINTH = _
  FRENCH = _
  GERMAN = _
  HALF_DIMINISHED = _
  ITALIAN = _
  MAJOR = _
  MAJOR_11TH = _
  MAJOR_13TH = _
  MAJOR_MINOR = _
  MAJOR_NINTH = _
  MAJOR_SEVENTH = _
  MAJOR_SIXTH = _
  MINOR = _
  MINOR_11TH = _
  MINOR_13TH = _
  MINOR_NINTH = _
  MINOR_SEVENTH = _
  MINOR_SIXTH = _
  NEAPOLITAN = _
  NONE = _
  OTHER = _
  PEDAL = _
  POWER = _
  SUSPENDED_FOURTH = _
  SUSPENDED_SECOND = _
  TRISTAN = _

  def __init__(self, plain_text: str):
    self.init()


class LeftCenterRight(MusicElementBase):
  """The left-center-right type is used to define horizontal alignment and text justification."""

  CENTER = _
  LEFT = _
  RIGHT = _

  def __init__(self, plain_text: str):
    self.init()


class LeftRight(MusicElementBase):
  """The left-right type is used to indicate whether one element appears to the left or the right of another element."""

  LEFT = _
  RIGHT = _

  def __init__(self, plain_text: str):
    self.init()


class LineEnd(MusicElementBase):
  """The line-end type specifies if there is a jog up or down (or both), an arrow, or nothing at the start or end of a bracket."""

  ARROW = _
  BOTH = _
  DOWN = _
  NONE = _
  UP = _

  def __init__(self, plain_text: str):
    self.init()


class LineLength(MusicElementBase):
  """The line-length type distinguishes between different line lengths for doit, falloff, plop, and scoop articulations."""

  LONG = _
  MEDIUM = _
  SHORT = _

  def __init__(self, plain_text: str):
    self.init()


class LineShape(MusicElementBase):
  """The line-shape type distinguishes between straight and curved lines."""

  CURVED = _
  STRAIGHT = _

  def __init__(self, plain_text: str):
    self.init()


class LineType(MusicElementBase):
  """The line-type type distinguishes between solid, dashed, dotted, and wavy lines."""

  DASHED = _
  DOTTED = _
  SOLID = _
  WAVY = _

  def __init__(self, plain_text: str):
    self.init()


class LineWidthType(MusicElementBase):
  """The line-width-type defines what type of line is being defined in a line-width element.

  Values include beam, bracket, dashes, enclosure, ending, extend, heavy
  barline, leger, light barline, octave shift, pedal, slur middle, slur tip,
  staff, stem, tie middle, tie tip, tuplet bracket, and wedge. This is left as a
  string so that other application-specific types can be defined, but it is made
  a separate type so that it can be redefined more strictly.
  """

  def __init__(self, plain_text: str):
    self.init()


class MarginType(MusicElementBase):
  """The margin-type type specifies whether margins apply to even page, odd pages, or both."""

  BOTH = _
  EVEN = _
  ODD = _

  def __init__(self, plain_text: str):
    self.init()


class MeasureNumberingValue(MusicElementBase):
  """The measure-numbering-value type describes how measure numbers are displayed on this part: no numbers, numbers every measure, or numbers every system."""

  MEASURE = _
  NONE = _
  SYSTEM = _

  def __init__(self, plain_text: str):
    self.init()


class MeasureText(MusicElementBase):
  """The measure-text type is used for the text attribute of measure elements.

  It has at least one character. The implicit attribute of the measure element
  should be set to "yes" rather than setting the text attribute to an empty
  string.
  """

  def __init__(self, plain_text: str):
    self.init()


class MembraneValue(MusicElementBase):
  """The membrane-value type represents pictograms for membrane percussion instruments."""

  BASS_DRUM = 'bass drum'
  BASS_DRUM_ON_SIDE = 'bass drum on side'
  BONGOS = _
  CHINESE_TOMTOM = 'Chinese tomtom'
  CONGA_DRUM = 'conga drum'
  CUICA = _
  GOBLET_DRUM = 'goblet drum'
  INDO_AMERICAN_TOMTOM = 'Indo-American tomtom'
  JAPANESE_TOMTOM = 'Japanese tomtom'
  MILITARY_DRUM = 'military drum'
  SNARE_DRUM = 'snare drum'
  SNARE_DRUM_SNARES_OFF = 'snare drum snares off'
  TABLA = _
  TAMBOURINE = _
  TENOR_DRUM = 'tenor drum'
  TIMBALES = _
  TOMTOM = _

  def __init__(self, plain_text: str):
    self.init()


class MetalValue(MusicElementBase):
  """The metal-value type represents pictograms for metal percussion instruments.

  The hi-hat value refers to a pictogram like Stone's high-hat cymbals but
  without the long vertical line at the bottom.
  """

  AGOGO = _
  ALMGLOCKEN = _
  BELL = _
  BELL_PLATE = 'bell plate'
  BELL_TREE = 'bell tree'
  BRAKE_DRUM = 'brake drum'
  CENCERRO = _
  CHAIN_RATTLE = 'chain rattle'
  CHINESE_CYMBAL = 'Chinese cymbal'
  COWBELL = _
  CRASH_CYMBALS = 'crash cymbals'
  CROTALE = _
  CYMBAL_TONGS = 'cymbal tongs'
  DOMED_GONG = 'domed gong'
  FINGER_CYMBALS = 'finger cymbals'
  FLEXATONE = _
  GONG = _
  HANDBELL = _
  HIGH_HAT_CYMBALS = 'high-hat cymbals'
  HI_HAT = _
  JAW_HARP = 'jaw harp'
  JINGLE_BELLS = 'jingle bells'
  MUSICAL_SAW = 'musical saw'
  SHELL_BELLS = 'shell bells'
  SISTRUM = _
  SIZZLE_CYMBAL = 'sizzle cymbal'
  SLEIGH_BELLS = 'sleigh bells'
  SUSPENDED_CYMBAL = 'suspended cymbal'
  TAM_TAM = 'tam tam'
  TAM_TAM_WITH_BEATER = 'tam tam with beater'
  TRIANGLE = _
  VIETNAMESE_HAT = 'Vietnamese hat'

  def __init__(self, plain_text: str):
    self.init()


class Midi128(MusicElementBase):
  """The midi-128 type is used to express MIDI 1.0 values that range from 1 to 128."""

  def __init__(self, plain_text: int):
    self.init()


class Midi16(MusicElementBase):
  """The midi-16 type is used to express MIDI 1.0 values that range from 1 to 16."""

  def __init__(self, plain_text: int):
    self.init()


class Midi16384(MusicElementBase):
  """The midi-16384 type is used to express MIDI 1.0 values that range from 1 to 16,384."""

  def __init__(self, plain_text: int):
    self.init()


class Millimeters(MusicElementBase):
  """The millimeters type is a number representing millimeters.

  This is used in the scaling element to provide a default scaling from tenths
  to physical units.
  """

  def __init__(self, plain_text: float):
    self.init()


class Milliseconds(MusicElementBase):
  """The milliseconds type represents an integral number of milliseconds."""

  def __init__(self, plain_text: int):
    self.init()


class Mode(MusicElementBase):
  """The mode type is used to specify major/minor and other mode distinctions.

  Valid mode values include major, minor, dorian, phrygian, lydian, mixolydian,
  aeolian, ionian, locrian, and none.
  """

  def __init__(self, plain_text: str):
    self.init()


class Mute(MusicElementBase):
  """The mute type represents muting for different instruments, including brass, winds, and strings.

  The on and off values are used for undifferentiated mutes. The remaining
  values represent specific mutes.
  """

  BUCKET = _
  CUP = _
  ECHO = _
  HARMON_NO_STEM = _
  HARMON_STEM = _
  HAT = _
  OFF = _
  ON = _
  PALM = _
  PLUNGER = _
  PRACTICE = _
  SOLOTONE = _
  STOP_HAND = _
  STOP_MUTE = _
  STRAIGHT = _

  def __init__(self, plain_text: str):
    self.init()


class NonNegativeDecimal(MusicElementBase):
  """The non-negative-decimal type specifies a non-negative decimal value."""

  def __init__(self, plain_text: float):
    self.init()


class NoteSizeType(MusicElementBase):
  """The note-size-type type indicates the type of note being defined by a note-size element.

  The grace-cue type is used for notes of grace-cue size. The grace type is used
  for notes of cue size that include a grace element. The cue type is used for
  all other notes with cue size, whether defined explicitly or implicitly via a
  cue element. The large type is used for notes of large size.
  """

  CUE = _
  GRACE = _
  GRACE_CUE = _
  LARGE = _

  def __init__(self, plain_text: str):
    self.init()


class NoteTypeValue(MusicElementBase):
  """The note-type-value type is used for the MusicXML type element and represents the graphic note type, from 1024th (shortest) to maxima (longest)."""

  BREVE = _
  EIGHTH = _
  HALF = _
  LONG = _
  MAXIMA = _
  QUARTER = _
  WHOLE = _
  _1024TH = _
  _128TH = _
  _16TH = _
  _256TH = _
  _32ND = _
  _512TH = _
  _64TH = _

  def __init__(self, plain_text: str):
    self.init()


class NoteheadValue(MusicElementBase):
  """The notehead-value type indicates shapes other than the open and closed ovals associated with note durations.

  The values do, re, mi, fa, fa up, so, la, and ti correspond to Aikin's 7-shape
  system.  The fa up shape is typically used with upstems; the fa shape is
  typically used with downstems or no stems.

  The arrow shapes differ from triangle and inverted triangle by being centered
  on the stem. Slashed and back slashed notes include both the normal notehead
  and a slash. The triangle shape has the tip of the triangle pointing up; the
  inverted triangle shape has the tip of the triangle pointing down. The left
  triangle shape is a right triangle with the hypotenuse facing up and to the
  left.

  The other notehead covers noteheads other than those listed here. It is
  usually used in combination with the smufl attribute to specify a particular
  SMuFL notehead. The smufl attribute may be used with any notehead value to
  help specify the appearance of symbols that share the same MusicXML semantics.
  Noteheads in the SMuFL Note name noteheads and Note name noteheads supplement
  ranges (U+E150–U+E1AF and U+EEE0–U+EEFF) should not use the smufl attribute or
  the "other" value, but instead use the notehead-text element.
  """

  ARROW_DOWN = 'arrow down'
  ARROW_UP = 'arrow up'
  BACK_SLASHED = 'back slashed'
  CIRCLED = _
  CIRCLE_DOT = 'circle dot'
  CIRCLE_X = _
  CLUSTER = _
  CROSS = _
  DIAMOND = _
  DO = _
  FA = _
  FA_UP = 'fa up'
  INVERTED_TRIANGLE = 'inverted triangle'
  LA = _
  LEFT_TRIANGLE = 'left triangle'
  MI = _
  NONE = _
  NORMAL = _
  OTHER = _
  RE = _
  RECTANGLE = _
  SLASH = _
  SLASHED = _
  SO = _
  SQUARE = _
  TI = _
  TRIANGLE = _
  X = _

  def __init__(self, plain_text: str):
    self.init()


class NumberLevel(MusicElementBase):
  """Slurs, tuplets, and many other features can be concurrent and overlap within a single musical part.

  The number-level entity distinguishes up to 16 concurrent objects of the same
  type when the objects overlap in MusicXML document order. Values greater than
  6 are usually only needed for music with a large number of divisi staves in a
  single part, or if there are more than 6 cross-staff arpeggios in a single
  measure. When a number-level value is implied, the value is 1 by default.

  When polyphonic parts are involved, the ordering within a MusicXML document
  can differ from musical score order. As an example, say we have a piano part
  in 4/4 where within a single measure, all the notes on the top staff are
  followed by all the notes on the bottom staff. In this example, each staff has
  a slur that starts on beat 2 and stops on beat 3, and there is a third slur
  that goes from beat 1 of one staff to beat 4 of the other staff.

  In this situation, the two mid-measure slurs can use the same number because
  they do not overlap in MusicXML document order, even though they do overlap in
  musical score order. Within the MusicXML document, the top staff slur will
  both start and stop before the bottom staff slur starts and stops.

  If the cross-staff slur starts in the top staff and stops in the bottom staff,
  it will need a separate number from the mid-measure slurs because it overlaps
  those slurs in MusicXML document order. However, if the cross-staff slur
  starts in the bottom staff and stops in the top staff, all three slurs can use
  the same number. None of them overlap within the MusicXML document, even
  though they all overlap each other in the musical score order. Within the
  MusicXML document, the start and stop of the top-staff slur will be followed
  by the stop and start of the cross-staff slur, followed by the start and stop
  of the bottom-staff slur.

  As this example demonstrates, a reading program should be prepared to handle
  cases where the number-levels start and stop in an arbitrary order. Because
  the start and stop values refer to musical score order, a program may find the
  stopping point of an object earlier in the MusicXML document than it will find
  its starting point.
  """

  def __init__(self, plain_text: int):
    self.init()


class NumberOfLines(MusicElementBase):
  """The number-of-lines type is used to specify the number of lines in text decoration attributes."""

  def __init__(self, plain_text: int):
    self.init()


class NumberOrNormal(MusicElementBase):
  """The number-or-normal values can be either a decimal number or the string "normal".

  This is used by the line-height and letter-spacing attributes.
  """

  def __init__(self, plain_text: str):
    self.init()


class NumeralMode(MusicElementBase):
  """The numeral-mode type specifies the mode similar to the mode type, but with a restricted set of values.

  The different minor values are used to interpret numeral-root values of 6 and
  7 when present in a minor key. The harmonic minor value sharpens the 7 and the
  melodic minor value sharpens both 6 and 7. If a minor mode is used without
  qualification, either in the mode or numeral-mode elements, natural minor is
  used.
  """

  HARMONIC_MINOR = 'harmonic minor'
  MAJOR = _
  MELODIC_MINOR = 'melodic minor'
  MINOR = _
  NATURAL_MINOR = 'natural minor'

  def __init__(self, plain_text: str):
    self.init()


class NumeralValue(MusicElementBase):
  """The numeral-value type represents a Roman numeral or Nashville number value as a positive integer from 1 to 7."""

  def __init__(self, plain_text: int):
    self.init()


class Octave(MusicElementBase):
  """Octaves are represented by the numbers 0 to 9, where 4 indicates the octave started by middle C."""

  def __init__(self, plain_text: int):
    self.init()


class OnOff(MusicElementBase):
  """The on-off type is used for notation elements such as string mutes."""

  OFF = _
  ON = _

  def __init__(self, plain_text: str):
    self.init()


class OverUnder(MusicElementBase):
  """The over-under type is used to indicate whether the tips of curved lines such as slurs and ties are overhand (tips down) or underhand (tips up)."""

  OVER = _
  UNDER = _

  def __init__(self, plain_text: str):
    self.init()


class PedalType(MusicElementBase):
  """The pedal-type simple type is used to distinguish types of pedal directions.

  The start value indicates the start of a damper pedal, while the sostenuto
  value indicates the start of a sostenuto pedal. The other values can be used
  with either the damper or sostenuto pedal. The soft pedal is not included here
  because there is no special symbol or graphic used for it beyond what can be
  specified with words and bracket elements.

  The change, continue, discontinue, and resume types are used when the line
  attribute is yes. The change type indicates a pedal lift and retake indicated
  with an inverted V marking. The continue type allows more precise formatting
  across system breaks and for more complex pedaling lines. The discontinue type
  indicates the end of a pedal line that does not include the explicit lift
  represented by the stop type. The resume type indicates the start of a pedal
  line that does not include the downstroke represented by the start type. It
  can be used when a line resumes after being discontinued, or to start a pedal
  line that is preceded by a text or symbol representation of the pedal.
  """

  CHANGE = _
  CONTINUE = _
  DISCONTINUE = _
  RESUME = _
  SOSTENUTO = _
  START = _
  STOP = _

  def __init__(self, plain_text: str):
    self.init()


class Percent(MusicElementBase):
  """The percent type specifies a percentage from 0 to 100."""

  def __init__(self, plain_text: float):
    self.init()


class PitchedValue(MusicElementBase):
  """The pitched-value type represents pictograms for pitched percussion instruments.

  The chimes and tubular chimes values distinguish the single-line and
  double-line versions of the pictogram.
  """

  CELESTA = _
  CHIMES = _
  GLOCKENSPIEL = _
  LITHOPHONE = _
  MALLET = _
  MARIMBA = _
  STEEL_DRUMS = 'steel drums'
  TUBAPHONE = _
  TUBULAR_CHIMES = 'tubular chimes'
  VIBRAPHONE = _
  XYLOPHONE = _

  def __init__(self, plain_text: str):
    self.init()


class PositiveDecimal(MusicElementBase):
  """The positive-decimal type specifies a positive decimal value."""

  def __init__(self, plain_text: float):
    self.init()


class PositiveDivisions(MusicElementBase):
  """The positive-divisions type restricts divisions values to positive numbers."""

  def __init__(self, plain_text: float):
    self.init()


class PositiveIntegerOrEmpty(MusicElementBase):
  """The positive-integer-or-empty values can be either a positive integer or an empty string."""

  def __init__(self, plain_text: str):
    self.init()


class PrincipalVoiceSymbol(MusicElementBase):
  """The principal-voice-symbol type represents the type of symbol used to indicate a principal or secondary voice.

  The "plain" value represents a plain square bracket. The value of "none" is
  used for analysis markup when the principal-voice element does not have a
  corresponding appearance in the score.
  """

  HAUPTSTIMME = _
  NEBENSTIMME = _
  NONE = _
  PLAIN = _

  def __init__(self, plain_text: str):
    self.init()


class RightLeftMiddle(MusicElementBase):
  """The right-left-middle type is used to specify barline location."""

  LEFT = _
  MIDDLE = _
  RIGHT = _

  def __init__(self, plain_text: str):
    self.init()


class RotationDegrees(MusicElementBase):
  """The rotation-degrees type specifies rotation, pan, and elevation values in degrees.

  Values range from -180 to 180.
  """

  def __init__(self, plain_text: float):
    self.init()


class SemiPitched(MusicElementBase):
  """The semi-pitched type represents categories of indefinite pitch for percussion instruments."""

  HIGH = _
  LOW = _
  MEDIUM = _
  MEDIUM_HIGH = _
  MEDIUM_LOW = _
  VERY_LOW = _

  def __init__(self, plain_text: str):
    self.init()


class Semitones(MusicElementBase):
  """The semitones type is a number representing semitones, used for chromatic alteration.

  A value of -1 corresponds to a flat and a value of 1 to a sharp. Decimal
  values like 0.5 (quarter tone sharp) are used for microtones.
  """

  def __init__(self, plain_text: float):
    self.init()


class ShowFrets(MusicElementBase):
  """The show-frets type indicates whether to show tablature frets as numbers (0, 1, 2) or letters (a, b, c).

  The default choice is numbers.
  """

  LETTERS = _
  NUMBERS = _

  def __init__(self, plain_text: str):
    self.init()


class ShowTuplet(MusicElementBase):
  """The show-tuplet type indicates whether to show a part of a tuplet relating to the tuplet-actual element, both the tuplet-actual and tuplet-normal elements, or neither."""

  ACTUAL = _
  BOTH = _
  NONE = _

  def __init__(self, plain_text: str):
    self.init()


class SmuflAccidentalGlyphName(MusicElementBase):
  """The smufl-accidental-glyph-name type is used to reference a specific Standard Music Font Layout (SMuFL) accidental character.

  The value is a SMuFL canonical glyph name that starts with one of the strings
  used at the start of glyph names for SMuFL accidentals.
  """

  def __init__(self, plain_text: str):
    self.init()


class SmuflCodaGlyphName(MusicElementBase):
  """The smufl-coda-glyph-name type is used to reference a specific Standard Music Font Layout (SMuFL) coda character.

  The value is a SMuFL canonical glyph name that starts with coda.
  """

  def __init__(self, plain_text: str):
    self.init()


class SmuflGlyphName(MusicElementBase):
  """The smufl-glyph-name type is used for attributes that reference a specific Standard Music Font Layout (SMuFL) character.

  The value is a SMuFL canonical glyph name, not a code point. For instance, the
  value for a standard piano pedal mark would be keyboardPedalPed, not U+E650.
  """

  def __init__(self, plain_text: str):
    self.init()


class SmuflLyricsGlyphName(MusicElementBase):
  """The smufl-lyrics-glyph-name type is used to reference a specific Standard Music Font Layout (SMuFL) lyrics elision character.

  The value is a SMuFL canonical glyph name that starts with lyrics.
  """

  def __init__(self, plain_text: str):
    self.init()


class SmuflPictogramGlyphName(MusicElementBase):
  """The smufl-pictogram-glyph-name type is used to reference a specific Standard Music Font Layout (SMuFL) percussion pictogram character.

  The value is a SMuFL canonical glyph name that starts with pict.
  """

  def __init__(self, plain_text: str):
    self.init()


class SmuflSegnoGlyphName(MusicElementBase):
  """The smufl-segno-glyph-name type is used to reference a specific Standard Music Font Layout (SMuFL) segno character.

  The value is a SMuFL canonical glyph name that starts with segno.
  """

  def __init__(self, plain_text: str):
    self.init()


class SmuflWavyLineGlyphName(MusicElementBase):
  """The smufl-wavy-line-glyph-name type is used to reference a specific Standard Music Font Layout (SMuFL) wavy line character.

  The value is a SMuFL canonical glyph name that either starts with wiggle, or
  begins with guitar and ends with VibratoStroke. This includes all the glyphs
  in the Multi-segment lines range, excluding the beam glyphs.
  """

  def __init__(self, plain_text: str):
    self.init()


class StaffDivideSymbol(MusicElementBase):
  """The staff-divide-symbol type is used for staff division symbols.

  The down, up, and up-down values correspond to SMuFL code points U+E00B,
  U+E00C, and U+E00D respectively.
  """

  DOWN = _
  UP = _
  UP_DOWN = _

  def __init__(self, plain_text: str):
    self.init()


class StaffLine(MusicElementBase):
  """The staff-line type indicates the line on a given staff.

  Staff lines are numbered from bottom to top, with 1 being the bottom line on a
  staff.
  """

  def __init__(self, plain_text: int):
    self.init()


class StaffLinePosition(MusicElementBase):
  """The staff-line-position type indicates the line position on a given staff.

  Staff lines are numbered from bottom to top, with 1 being the bottom line on a
  staff. A staff-line-position value can extend beyond the range of the lines on
  the current staff.
  """

  def __init__(self, plain_text: int):
    self.init()


class StaffNumber(MusicElementBase):
  """The staff-number type indicates staff numbers within a multi-staff part.

  Staves are numbered from top to bottom, with 1 being the top staff on a part.
  """

  def __init__(self, plain_text: int):
    self.init()


class StaffType(MusicElementBase):
  """The staff-type value can be ossia, editorial, cue, alternate, or regular.

  An ossia staff represents music that can be played instead of what appears on
  the regular staff. An editorial staff also represents musical alternatives,
  but is created by an editor rather than the composer. It can be used for
  suggested interpretations or alternatives from other sources. A cue staff
  represents music from another part. An alternate staff shares the same music
  as the prior staff, but displayed differently (e.g., treble and bass clef,
  standard notation and tablature). It is not included in playback. An alternate
  staff provides more information to an application reading a file than encoding
  the same music in separate parts, so its use is preferred in this situation if
  feasible. A regular staff is the standard default staff-type.
  """

  ALTERNATE = _
  CUE = _
  EDITORIAL = _
  OSSIA = _
  REGULAR = _

  def __init__(self, plain_text: str):
    self.init()


class StartNote(MusicElementBase):
  """The start-note type describes the starting note of trills and mordents for playback, relative to the current note."""

  BELOW = _
  MAIN = _
  UPPER = _

  def __init__(self, plain_text: str):
    self.init()


class StartStop(MusicElementBase):
  """The start-stop type is used for an attribute of musical elements that can either start or stop, such as tuplets.

  The values of start and stop refer to how an element appears in musical score
  order, not in MusicXML document order. An element with a stop attribute may
  precede the corresponding element with a start attribute within a MusicXML
  document. This is particularly common in multi-staff music. For example, the
  stopping point for a tuplet may appear in staff 1 before the starting point
  for the tuplet appears in staff 2 later in the document.

  When multiple elements with the same tag are used within the same note, their
  order within the MusicXML document should match the musical score order.
  """

  START = _
  STOP = _

  def __init__(self, plain_text: str):
    self.init()


class StartStopChangeContinue(MusicElementBase):
  """The start-stop-change-continue type is used to distinguish types of pedal directions."""

  CHANGE = _
  CONTINUE = _
  START = _
  STOP = _

  def __init__(self, plain_text: str):
    self.init()


class StartStopContinue(MusicElementBase):
  """The start-stop-continue type is used for an attribute of musical elements that can either start or stop, but also need to refer to an intermediate point in the symbol, as for complex slurs or for formatting of symbols across system breaks.

  The values of start, stop, and continue refer to how an element appears in
  musical score order, not in MusicXML document order. An element with a stop
  attribute may precede the corresponding element with a start attribute within
  a MusicXML document. This is particularly common in multi-staff music. For
  example, the stopping point for a slur may appear in staff 1 before the
  starting point for the slur appears in staff 2 later in the document.

  When multiple elements with the same tag are used within the same note, their
  order within the MusicXML document should match the musical score order. For
  example, a note that marks both the end of one slur and the start of a new
  slur should have the incoming slur element with a type of stop precede the
  outgoing slur element with a type of start.
  """

  CONTINUE = _
  START = _
  STOP = _

  def __init__(self, plain_text: str):
    self.init()


class StartStopDiscontinue(MusicElementBase):
  """The start-stop-discontinue type is used to specify ending types.

  Typically, the start type is associated with the left barline of the first
  measure in an ending. The stop and discontinue types are associated with the
  right barline of the last measure in an ending. Stop is used when the ending
  mark concludes with a downward jog, as is typical for first endings.
  Discontinue is used when there is no downward jog, as is typical for second
  endings that do not conclude a piece.
  """

  DISCONTINUE = _
  START = _
  STOP = _

  def __init__(self, plain_text: str):
    self.init()


class StartStopSingle(MusicElementBase):
  """The start-stop-single type is used for an attribute of musical elements that can be used for either multi-note or single-note musical elements, as for groupings.

  When multiple elements with the same tag are used within the same note, their
  order within the MusicXML document should match the musical score order.
  """

  SINGLE = _
  START = _
  STOP = _

  def __init__(self, plain_text: str):
    self.init()


class StemValue(MusicElementBase):
  """The stem-value type represents the notated stem direction."""

  DOUBLE = _
  DOWN = _
  NONE = _
  UP = _

  def __init__(self, plain_text: str):
    self.init()


class Step(MusicElementBase):
  """The step type represents a step of the diatonic scale, represented using the English letters A through G."""

  A = _
  B = _
  C = _
  D = _
  E = _
  F = _
  G = _

  def __init__(self, plain_text: str):
    self.init()


class StickLocation(MusicElementBase):
  """The stick-location type represents pictograms for the location of sticks, beaters, or mallets on cymbals, gongs, drums, and other instruments."""

  CENTER = _
  CYMBAL_BELL = 'cymbal bell'
  CYMBAL_EDGE = 'cymbal edge'
  RIM = _

  def __init__(self, plain_text: str):
    self.init()


class StickMaterial(MusicElementBase):
  """The stick-material type represents the material being displayed in a stick pictogram."""

  HARD = _
  MEDIUM = _
  SHADED = _
  SOFT = _
  X = _

  def __init__(self, plain_text: str):
    self.init()


class StickType(MusicElementBase):
  """The stick-type type represents the shape of pictograms where the material in the stick, mallet, or beater is represented in the pictogram."""

  BASS_DRUM = 'bass drum'
  DOUBLE_BASS_DRUM = 'double bass drum'
  GLOCKENSPIEL = _
  GUM = _
  HAMMER = _
  SUPERBALL = _
  TIMPANI = _
  WOUND = _
  XYLOPHONE = _
  YARN = _

  def __init__(self, plain_text: str):
    self.init()


class StringNumber(MusicElementBase):
  """The string-number type indicates a string number.

  Strings are numbered from high to low, with 1 being the highest pitched
  full-length string.
  """

  def __init__(self, plain_text: int):
    self.init()


class SwingTypeValue(MusicElementBase):
  """The swing-type-value type specifies the note type, either eighth or 16th, to which the ratio defined in the swing element is applied."""

  EIGHTH = _
  _16TH = _

  def __init__(self, plain_text: str):
    self.init()


class Syllabic(MusicElementBase):
  """Lyric hyphenation is indicated by the syllabic type.

  The single, begin, end, and middle values represent single-syllable words,
  word-beginning syllables, word-ending syllables, and mid-word syllables,
  respectively.
  """

  BEGIN = _
  END = _
  MIDDLE = _
  SINGLE = _

  def __init__(self, plain_text: str):
    self.init()


class SymbolSize(MusicElementBase):
  """The symbol-size type is used to distinguish between full, cue sized, grace cue sized, and oversized symbols."""

  CUE = _
  FULL = _
  GRACE_CUE = _
  LARGE = _

  def __init__(self, plain_text: str):
    self.init()


class SyncType(MusicElementBase):
  """The sync-type type specifies the style that a score following application should use to synchronize an accompaniment with a performer.

  The none type indicates no synchronization to the performer. The tempo type
  indicates synchronization based on the performer tempo rather than individual
  events in the score. The event type indicates synchronization by following the
  performance of individual events in the score rather than the performer tempo.
  The mostly-tempo and mostly-event types combine these two approaches, with
  mostly-tempo giving more weight to tempo and mostly-event giving more weight
  to performed events. The always-event type provides the strictest
  synchronization by not being forgiving of missing performed events.
  """

  ALWAYS_EVENT = _
  EVENT = _
  MOSTLY_EVENT = _
  MOSTLY_TEMPO = _
  NONE = _
  TEMPO = _

  def __init__(self, plain_text: str):
    self.init()


class SystemRelation(MusicElementBase):
  """The system-relation type distinguishes elements that are associated with a system rather than the particular part where the element appears.

  A value of only-top indicates that the element should appear only on the top
  part of the current system. A value of also-top indicates that the element
  should appear on both the current part and the top part of the current system.
  If this value appears in a score, when parts are created the element should
  only appear once in this part, not twice. A value of none indicates that the
  element is associated only with the current part, not with the system.
  """

  ALSO_TOP = _
  NONE = _
  ONLY_TOP = _

  def __init__(self, plain_text: str):
    self.init()


class SystemRelationNumber(MusicElementBase):
  """The system-relation-number type distinguishes measure numbers that are associated with a system rather than the particular part where the element appears.

  A value of only-top or only-bottom indicates that the number should appear
  only on the top or bottom part of the current system, respectively. A value of
  also-top or also-bottom indicates that the number should appear on both the
  current part and the top or bottom part of the current system, respectively.
  If these values appear in a score, when parts are created the number should
  only appear once in this part, not twice. A value of none indicates that the
  number is associated only with the current part, not with the system.
  """

  ALSO_BOTTOM = _
  ALSO_TOP = _
  NONE = _
  ONLY_BOTTOM = _
  ONLY_TOP = _

  def __init__(self, plain_text: str):
    self.init()


class TapHand(MusicElementBase):
  """The tap-hand type represents the symbol to use for a tap element.

  The left and right values refer to the SMuFL guitarLeftHandTapping and
  guitarRightHandTapping glyphs respectively.
  """

  LEFT = _
  RIGHT = _

  def __init__(self, plain_text: str):
    self.init()


class Tenths(MusicElementBase):
  """The tenths type is a number representing tenths of interline staff space (positive or negative).

  Both integer and decimal values are allowed, such as 5 for a half space and
  2.5 for a quarter space. Interline space is measured from the middle of a
  staff line.

  Distances in a MusicXML file are measured in tenths of staff space. Tenths are
  then scaled to millimeters within the scaling element, used in the defaults
  element at the start of a score. Individual staves can apply a scaling factor
  to adjust staff size. When a MusicXML element or attribute refers to tenths,
  it means the global tenths defined by the scaling element, not the local
  tenths as adjusted by the staff-size element.
  """

  def __init__(self, plain_text: float):
    self.init()


class TextDirection(MusicElementBase):
  """The text-direction type is used to adjust and override the Unicode bidirectional text algorithm, similar to the Directionality data category in the W3C Internationalization Tag Set recommendation.

  Values are ltr (left-to-right embed), rtl (right-to-left embed), lro
  (left-to-right bidi-override), and rlo (right-to-left bidi-override). The
  default value is ltr. This type is typically used by applications that store
  text in left-to-right visual order rather than logical order. Such
  applications can use the lro value to better communicate with other
  applications that more fully support bidirectional text.
  """

  LRO = _
  LTR = _
  RLO = _
  RTL = _

  def __init__(self, plain_text: str):
    self.init()


class TiedType(MusicElementBase):
  """The tied-type type is used as an attribute of the tied element to specify where the visual representation of a tie begins and ends.

  A tied element which joins two notes of the same pitch can be specified with
  tied-type start on the first note and tied-type stop on the second note. To
  indicate a note should be undamped, use a single tied element with tied-type
  let-ring. For other ties that are visually attached to a single note, such as
  a tie leading into or out of a repeated section or coda, use two tied elements
  on the same note, one start and one stop.

  In start-stop cases, ties can add more elements using a continue type. This is
  typically used to specify the formatting of cross-system ties.

  When multiple elements with the same tag are used within the same note, their
  order within the MusicXML document should match the musical score order. For
  example, a note with a tie at the end of a first ending should have the tied
  element with a type of start precede the tied element with a type of stop.
  """

  CONTINUE = _
  LET_RING = _
  START = _
  STOP = _

  def __init__(self, plain_text: str):
    self.init()


class TimeOnly(MusicElementBase):
  """The time-only type is used to indicate that a particular playback- or listening-related element only applies particular times through a repeated section.

  The value is a comma-separated list of positive integers arranged in ascending
  order, indicating which times through the repeated section that the element
  applies.
  """

  def __init__(self, plain_text: str):
    self.init()


class TimeRelation(MusicElementBase):
  """The time-relation type indicates the symbol used to represent the interchangeable aspect of dual time signatures."""

  BRACKET = _
  EQUALS = _
  HYPHEN = _
  PARENTHESES = _
  SLASH = _
  SPACE = _

  def __init__(self, plain_text: str):
    self.init()


class TimeSeparator(MusicElementBase):
  """The time-separator type indicates how to display the arrangement between the beats and beat-type values in a time signature.

  The default value is none. The horizontal, diagonal, and vertical values
  represent horizontal, diagonal lower-left to upper-right, and vertical lines
  respectively. For these values, the beats and beat-type values are arranged on
  either side of the separator line. The none value represents no separator with
  the beats and beat-type arranged vertically. The adjacent value represents no
  separator with the beats and beat-type arranged horizontally.
  """

  ADJACENT = _
  DIAGONAL = _
  HORIZONTAL = _
  NONE = _
  VERTICAL = _

  def __init__(self, plain_text: str):
    self.init()


class TimeSymbol(MusicElementBase):
  """The time-symbol type indicates how to display a time signature.

  The normal value is the usual fractional display, and is the implied symbol
  type if none is specified. Other options are the common and cut time symbols,
  as well as a single number with an implied denominator. The note symbol
  indicates that the beat-type should be represented with the corresponding
  downstem note rather than a number. The dotted-note symbol indicates that the
  beat-type should be represented with a dotted downstem note that corresponds
  to three times the beat-type value, and a numerator that is one third the
  beats value.
  """

  COMMON = _
  CUT = _
  DOTTED_NOTE = _
  NORMAL = _
  NOTE = _
  SINGLE_NUMBER = _

  def __init__(self, plain_text: str):
    self.init()


class TipDirection(MusicElementBase):
  """The tip-direction type represents the direction in which the tip of a stick or beater points, using Unicode arrow terminology."""

  DOWN = _
  LEFT = _
  NORTHEAST = _
  NORTHWEST = _
  RIGHT = _
  SOUTHEAST = _
  SOUTHWEST = _
  UP = _

  def __init__(self, plain_text: str):
    self.init()


class TopBottom(MusicElementBase):
  """The top-bottom type is used to indicate the top or bottom part of a vertical shape like non-arpeggiate."""

  BOTTOM = _
  TOP = _

  def __init__(self, plain_text: str):
    self.init()


class TremoloMarks(MusicElementBase):
  """The number of tremolo marks is represented by a number from 0 to 8: the same as beam-level with 0 added."""

  def __init__(self, plain_text: int):
    self.init()


class TremoloType(MusicElementBase):
  """The tremolo-type is used to distinguish double-note, single-note, and unmeasured tremolos."""

  SINGLE = _
  START = _
  STOP = _
  UNMEASURED = _

  def __init__(self, plain_text: str):
    self.init()


class TrillBeats(MusicElementBase):
  """The trill-beats type specifies the beats used in a trill-sound or bend-sound attribute group.

  It is a decimal value with a minimum value of 2.
  """

  def __init__(self, plain_text: float):
    self.init()


class TrillStep(MusicElementBase):
  """The trill-step type describes the alternating note of trills and mordents for playback, relative to the current note."""

  HALF = _
  UNISON = _
  WHOLE = _

  def __init__(self, plain_text: str):
    self.init()


class TwoNoteTurn(MusicElementBase):
  """The two-note-turn type describes the ending notes of trills and mordents for playback, relative to the current note."""

  HALF = _
  NONE = _
  WHOLE = _

  def __init__(self, plain_text: str):
    self.init()


class UpDown(MusicElementBase):
  """The up-down type is used for the direction of arrows and other pointed symbols like vertical accents, indicating which way the tip is pointing."""

  DOWN = _
  UP = _

  def __init__(self, plain_text: str):
    self.init()


class UpDownStopContinue(MusicElementBase):
  """The up-down-stop-continue type is used for octave-shift elements, indicating the direction of the shift from their true pitched values because of printing difficulty."""

  CONTINUE = _
  DOWN = _
  STOP = _
  UP = _

  def __init__(self, plain_text: str):
    self.init()


class UprightInverted(MusicElementBase):
  """The upright-inverted type describes the appearance of a fermata element.

  The value is upright if not specified.
  """

  INVERTED = _
  UPRIGHT = _

  def __init__(self, plain_text: str):
    self.init()


class Valign(MusicElementBase):
  """The valign type is used to indicate vertical alignment to the top, middle, bottom, or baseline of the text.

  If the text is on multiple lines, baseline alignment refers to the baseline of
  the lowest line of text. Defaults are implementation-dependent.
  """

  BASELINE = _
  BOTTOM = _
  MIDDLE = _
  TOP = _

  def __init__(self, plain_text: str):
    self.init()


class ValignImage(MusicElementBase):
  """The valign-image type is used to indicate vertical alignment for images and graphics, so it does not include a baseline value.

  Defaults are implementation-dependent.
  """

  BOTTOM = _
  MIDDLE = _
  TOP = _

  def __init__(self, plain_text: str):
    self.init()


class WedgeType(MusicElementBase):
  """The wedge type is crescendo for the start of a wedge that is closed at the left side, diminuendo for the start of a wedge that is closed on the right side, and stop for the end of a wedge.

  The continue type is used for formatting wedges over a system break, or for
  other situations where a single wedge is divided into multiple segments.
  """

  CONTINUE = _
  CRESCENDO = _
  DIMINUENDO = _
  STOP = _

  def __init__(self, plain_text: str):
    self.init()


class Winged(MusicElementBase):
  """The winged attribute indicates whether the repeat has winged extensions that appear above and below the barline.

  The straight and curved values represent single wings, while the
  double-straight and double-curved values represent double wings. The none
  value indicates no wings and is the default.
  """

  CURVED = _
  DOUBLE_CURVED = _
  DOUBLE_STRAIGHT = _
  NONE = _
  STRAIGHT = _

  def __init__(self, plain_text: str):
    self.init()


class WoodValue(MusicElementBase):
  """The wood-value type represents pictograms for wood percussion instruments.

  The maraca and maracas values distinguish the one- and two-maraca versions of
  the pictogram.
  """

  BAMBOO_SCRAPER = 'bamboo scraper'
  BOARD_CLAPPER = 'board clapper'
  CABASA = _
  CASTANETS = _
  CASTANETS_WITH_HANDLE = 'castanets with handle'
  CLAVES = _
  FOOTBALL_RATTLE = 'football rattle'
  GUIRO = _
  LOG_DRUM = 'log drum'
  MARACA = _
  MARACAS = _
  QUIJADA = _
  RAINSTICK = _
  RATCHET = _
  RECO_RECO = _
  SANDPAPER_BLOCKS = 'sandpaper blocks'
  SLIT_DRUM = 'slit drum'
  TEMPLE_BLOCK = 'temple block'
  VIBRASLAP = _
  WHIP = _
  WOOD_BLOCK = 'wood block'

  def __init__(self, plain_text: str):
    self.init()


class YesNo(MusicElementBase):
  """The yes-no type is used for boolean-like attributes.

  We cannot use W3C XML Schema booleans due to their restrictions on expression
  of boolean values.
  """

  NO = _
  YES = _

  def __init__(self, plain_text: str):
    self.init()


class YesNoNumber(MusicElementBase):
  """The yes-no-number type is used for attributes that can be either boolean or numeric values."""

  def __init__(self, plain_text: str):
    self.init()


class YyyyMmDd(MusicElementBase):
  """Calendar dates are represented yyyy-mm-dd format, following ISO 8601.

  This is a W3C XML Schema date type, but without the optional timezone data.
  """

  def __init__(self, plain_text: str):
    self.init()


class Accidental(AccidentalValue):
  """The accidental type represents actual notated accidentals.

  Editorial and cautionary indications are indicated by attributes. Values for
  these attributes are "no" if not present. Specific graphic display such as
  parentheses, brackets, and size are controlled by the level-display attribute
  group.
  """

  def __init__(
      self,
      plain_text: str,
      bracket: str | YesNo = None,
      cautionary: str | YesNo = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      editorial: str | YesNo = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      parentheses: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      size: str | SymbolSize = None,
      smufl: str | SmuflAccidentalGlyphName = None,
  ):
    self.init()


class AccidentalMark(AccidentalValue):
  """An accidental-mark can be used as a separate notation or as part of an ornament.

  When used in an ornament, position and placement are relative to the ornament,
  not relative to the note.
  """

  def __init__(
      self,
      plain_text: str,
      bracket: str | YesNo = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      id: str = None,
      parentheses: str | YesNo = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      size: str | SymbolSize = None,
      smufl: str | SmuflAccidentalGlyphName = None,
  ):
    self.init()


class AccidentalText(AccidentalValue):
  """The accidental-text type represents an element with an accidental value and text-formatting attributes."""

  lang = 'xml'
  space = 'xml'

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      dir: str | TextDirection = None,
      enclosure: str | EnclosureShape = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      justify: str | LeftCenterRight = None,
      lang: str = None,
      letter_spacing: str | NumberOrNormal = None,
      line_height: str | NumberOrNormal = None,
      line_through: int | NumberOfLines = None,
      overline: int | NumberOfLines = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      rotation: float | RotationDegrees = None,
      smufl: str | SmuflAccidentalGlyphName = None,
      space: str = None,
      underline: int | NumberOfLines = None,
      valign: str | Valign = None,
  ):
    self.init()


class Arpeggiate(MusicElementBase):
  """The arpeggiate type indicates that this note is part of an arpeggiated chord.

  The number attribute can be used to distinguish between two simultaneous
  chords arpeggiated separately (different numbers) or together (same number).
  The direction attribute is used if there is an arrow on the arpeggio sign. By
  default, arpeggios go from the lowest to highest note.  The length of the sign
  can be determined from the position attributes for the arpeggiate elements
  used with the top and bottom notes of the arpeggiated chord. If the unbroken
  attribute is set to yes, it indicates that the arpeggio continues onto another
  staff within the part. This serves as a hint to applications and is not
  required for cross-staff arpeggios.
  """

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      direction: str | UpDown = None,
      id: str = None,
      number: int | NumberLevel = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      unbroken: str | YesNo = None,
  ):
    self.init()


class Assess(MusicElementBase):
  """By default, an assessment application should assess all notes without a cue child element, and not assess any note with a cue child element.

  The assess type allows this default assessment to be overridden for individual
  notes. The optional player and time-only attributes restrict the type to apply
  to a single player or set of times through a repeated section, respectively.
  If missing, the type applies to all players or all times through the repeated
  section, respectively. The player attribute references the id attribute of a
  player element defined within the matching score-part.
  """

  def __init__(
      self,
      type: str | YesNo,
      player: str = None,
      time_only: str | TimeOnly = None,
  ):
    self.init()


class BarStyleColor(BarStyle):
  """The bar-style-color type contains barline style and color information."""

  def __init__(self, plain_text: str, color: str | Color = None):
    self.init()


class Barre(MusicElementBase):
  """The barre element indicates placing a finger over multiple strings on a single fret.

  The type is "start" for the lowest pitched string (e.g., the string with the
  highest MusicXML number) and is "stop" for the highest pitched string.
  """

  def __init__(self, type: str | StartStop, color: str | Color = None):
    self.init()


class BassStep(Step):
  """The bass-step type represents the pitch step of the bass of the current chord within the harmony element.

  The text attribute indicates how the bass should appear in a score if not
  using the element contents.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      text: str = None,
  ):
    self.init()


class Beam(BeamValue):
  """Beam values include begin, continue, end, forward hook, and backward hook.

  Up to eight concurrent beams are available to cover up to 1024th notes. Each
  beam in a note is represented with a separate beam element, starting with the
  eighth note beam using a number attribute of 1.

  Note that the beam number does not distinguish sets of beams that overlap, as
  it does for slur and other elements. Beaming groups are distinguished by being
  in different voices and/or the presence or absence of grace and cue elements.

  Beams that have a begin value can also have a fan attribute to indicate
  accelerandos and ritardandos using fanned beams. The fan attribute may also be
  used with a continue value if the fanning direction changes on that note. The
  value is "none" if not specified.

  The repeater attribute has been deprecated in MusicXML 3.0. Formerly used for
  tremolos, it needs to be specified with a "yes" value for each beam using it.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      fan: str | Fan = None,
      id: str = None,
      number: int | BeamLevel = None,
      repeater: str | YesNo = None,
  ):
    self.init()


class Beater(BeaterValue):
  """The beater type represents pictograms for beaters, mallets, and sticks that do not have different materials represented in the pictogram."""

  def __init__(self, plain_text: str, tip: str | TipDirection = None):
    self.init()


class Bookmark(MusicElementBase):
  """The bookmark type serves as a well-defined target for an incoming simple XLink."""

  def __init__(
      self, id: str, element: str = None, name: str = None, position: int = None
  ):
    self.init()


class Bracket(MusicElementBase):
  """Brackets are combined with words in a variety of modern directions.

  The line-end attribute specifies if there is a jog up or down (or both), an
  arrow, or nothing at the start or end of the bracket. If the line-end is up or
  down, the length of the jog can be specified using the end-length attribute.
  The line-type is solid if not specified.
  """

  def __init__(
      self,
      line_end: str | LineEnd,
      type: str | StartStopContinue,
      color: str | Color = None,
      dash_length: float | Tenths = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      end_length: float | Tenths = None,
      id: str = None,
      line_type: str | LineType = None,
      number: int | NumberLevel = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      space_length: float | Tenths = None,
  ):
    self.init()


class BreathMark(BreathMarkValue):
  """The breath-mark element indicates a place to take a breath."""

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class Caesura(CaesuraValue):
  """The caesura element indicates a slight pause.

  It is notated using a "railroad tracks" symbol or other variations specified
  in the element content.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class Cancel(Fifths):
  """A cancel element indicates that the old key signature should be cancelled before the new one appears.

  This will always happen when changing to C major or A minor and need not be
  specified then. The cancel value matches the fifths value of the cancelled key
  signature (e.g., a cancel of -2 will provide an explicit cancellation for
  changing from B flat major to F major). The optional location attribute
  indicates where the cancellation appears relative to the new key signature.
  """

  def __init__(self, plain_text: int, location: str | CancelLocation = None):
    self.init()


class Coda(MusicElementBase):
  """The coda type is the visual indicator of a coda sign.

  The exact glyph can be specified with the smufl attribute. A sound element is
  also needed to guide playback applications reliably.
  """

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      smufl: str | SmuflCodaGlyphName = None,
      valign: str | Valign = None,
  ):
    self.init()


class Dashes(MusicElementBase):
  """The dashes type represents dashes, used for instance with cresc.

  and dim. marks.
  """

  def __init__(
      self,
      type: str | StartStopContinue,
      color: str | Color = None,
      dash_length: float | Tenths = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      id: str = None,
      number: int | NumberLevel = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      space_length: float | Tenths = None,
  ):
    self.init()


class DegreeAlter(Semitones):
  """The degree-alter type represents the chromatic alteration for the current degree.

  If the degree-type value is alter or subtract, the degree-alter value is
  relative to the degree already in the chord based on its kind element. If the
  degree-type value is add, the degree-alter is relative to a dominant chord
  (major and perfect intervals except for a minor seventh). The plus-minus
  attribute is used to indicate if plus and minus symbols should be used instead
  of sharp and flat symbols to display the degree alteration. It is no if not
  specified.
  """

  def __init__(
      self,
      plain_text: float,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      plus_minus: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class DegreeType(DegreeTypeValue):
  """The degree-type type indicates if this degree is an addition, alteration, or subtraction relative to the kind of the current chord.

  The value of the degree-type element affects the interpretation of the value
  of the degree-alter element. The text attribute specifies how the type of the
  degree should be displayed.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      text: str = None,
  ):
    self.init()


class DegreeValue(MusicElementBase):
  """The content of the degree-value type is a number indicating the degree of the chord (1 for the root, 3 for third, etc).

  The text attribute specifies how the value of the degree should be displayed.
  The symbol attribute indicates that a symbol should be used in specifying the
  degree. If the symbol attribute is present, the value of the text attribute
  follows the symbol.
  """

  def __init__(
      self,
      plain_text: int,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      symbol: str | DegreeSymbolValue = None,
      text: str = None,
  ):
    self.init()


class Distance(Tenths):
  """The distance element represents standard distances between notation elements in tenths.

  The type attribute defines what type of distance is being defined. Valid
  values include hyphen (for hyphens in lyrics) and beam.
  """

  def __init__(self, plain_text: float, type: str | DistanceType):
    self.init()


class Double(MusicElementBase):
  """The double type indicates that the music is doubled one octave from what is currently written.

  If the above attribute is set to yes, the doubling is one octave above what is
  written, as for mixed flute / piccolo parts in band literature. Otherwise the
  doubling is one octave below what is written, as for mixed cello / bass parts
  in orchestral literature.
  """

  def __init__(self, above: str | YesNo = None):
    self.init()


class Effect(EffectValue):
  """The effect type represents pictograms for sound effect percussion instruments.

  The smufl attribute is used to distinguish different SMuFL stylistic
  alternates.
  """

  def __init__(
      self, plain_text: str, smufl: str | SmuflPictogramGlyphName = None
  ):
    self.init()


class Elision(MusicElementBase):
  """The elision type represents an elision between lyric syllables.

  The text content specifies the symbol used to display the elision. Common
  values are a no-break space (Unicode 00A0), an underscore (Unicode 005F), or
  an undertie (Unicode 203F). If the text content is empty, the smufl attribute
  is used to specify the symbol to use. Its value is a SMuFL canonical glyph
  name that starts with lyrics. The SMuFL attribute is ignored if the elision
  glyph is already specified by the text content. If neither text content nor a
  smufl attribute are present, the elision glyph is application-specific.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      smufl: str | SmuflLyricsGlyphName = None,
  ):
    self.init()


class Empty(MusicElementBase):
  """The empty type represents an empty element with no attributes."""

  def __init__(self):
    self.init()


class EmptyFont(MusicElementBase):
  """The empty-font type represents an empty element with font attributes."""

  def __init__(
      self,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
  ):
    self.init()


class EmptyLine(MusicElementBase):
  """The empty-line type represents an empty element with line-shape, line-type, line-length, dashed-formatting, print-style and placement attributes."""

  def __init__(
      self,
      color: str | Color = None,
      dash_length: float | Tenths = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      line_length: str | LineLength = None,
      line_shape: str | LineShape = None,
      line_type: str | LineType = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      space_length: float | Tenths = None,
  ):
    self.init()


class EmptyPlacement(MusicElementBase):
  """The empty-placement type represents an empty element with print-style and placement attributes."""

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class EmptyPlacementSmufl(MusicElementBase):
  """The empty-placement-smufl type represents an empty element with print-style, placement, and smufl attributes."""

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      smufl: str | SmuflGlyphName = None,
  ):
    self.init()


class EmptyPrintObjectStyleAlign(MusicElementBase):
  """The empty-print-style-align-object type represents an empty element with print-object and print-style-align attribute groups."""

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      valign: str | Valign = None,
  ):
    self.init()


class EmptyPrintStyle(MusicElementBase):
  """The empty-print-style type represents an empty element with print-style attribute group."""

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class EmptyPrintStyleAlign(MusicElementBase):
  """The empty-print-style-align type represents an empty element with print-style-align attribute group."""

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      valign: str | Valign = None,
  ):
    self.init()


class EmptyPrintStyleAlignId(MusicElementBase):
  """The empty-print-style-align-id type represents an empty element with print-style-align and optional-unique-id attribute groups."""

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      valign: str | Valign = None,
  ):
    self.init()


class EmptyTrillSound(MusicElementBase):
  """The empty-trill-sound type represents an empty element with print-style, placement, and trill-sound attributes."""

  def __init__(
      self,
      accelerate: str | YesNo = None,
      beats: float | TrillBeats = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      last_beat: float | Percent = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      second_beat: float | Percent = None,
      start_note: str | StartNote = None,
      trill_step: str | TrillStep = None,
      two_note_turn: str | TwoNoteTurn = None,
  ):
    self.init()


class Ending(MusicElementBase):
  """The ending type represents multiple (e.g. first and second) endings.

  Typically, the start type is associated with the left barline of the first
  measure in an ending. The stop and discontinue types are associated with the
  right barline of the last measure in an ending. Stop is used when the ending
  mark concludes with a downward jog, as is typical for first endings.
  Discontinue is used when there is no downward jog, as is typical for second
  endings that do not conclude a piece. The length of the jog can be specified
  using the end-length attribute. The text-x and text-y attributes are offsets
  that specify where the baseline of the start of the ending text appears,
  relative to the start of the ending line.

  The number attribute indicates which times the ending is played, similar to
  the time-only attribute used by other elements. While this often represents
  the numeric values for what is under the ending line, it can also indicate
  whether an ending is played during a larger dal segno or da capo repeat.
  Single endings such as "1" or comma-separated multiple endings such as "1,2"
  may be used. The ending element text is used when the text displayed in the
  ending is different than what appears in the number attribute. The
  print-object attribute is used to indicate when an ending is present but not
  printed, as is often the case for many parts in a full score.
  """

  def __init__(
      self,
      plain_text: str,
      number: str | EndingNumber,
      type: str | StartStopDiscontinue,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      end_length: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      system: str | SystemRelation = None,
      text_x: float | Tenths = None,
      text_y: float | Tenths = None,
  ):
    self.init()


class Extend(MusicElementBase):
  """The extend type represents lyric word extension / melisma lines as well as figured bass extensions.

  The optional type and position attributes are added in Version 3.0 to provide
  better formatting control.
  """

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      type: str | StartStopContinue = None,
  ):
    self.init()


class Feature(MusicElementBase):
  """The feature type is a part of the grouping element used for musical analysis.

  The type attribute represents the type of the feature and the element content
  represents its value. This type is flexible to allow for different analyses.
  """

  def __init__(self, plain_text: str, type: str = None):
    self.init()


class Fermata(FermataShape):
  """The fermata text content represents the shape of the fermata sign.

  An empty fermata element represents a normal fermata. The fermata type is
  upright if not specified.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      id: str = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      type: str | UprightInverted = None,
  ):
    self.init()


class Fingering(MusicElementBase):
  """Fingering is typically indicated 1,2,3,4,5.

  Multiple fingerings may be given, typically to substitute fingerings in the
  middle of a note. The substitution and alternate values are "no" if the
  attribute is not present. For guitar and other fretted instruments, the
  fingering element represents the fretting finger; the pluck element represents
  the plucking finger.
  """

  def __init__(
      self,
      plain_text: str,
      alternate: str | YesNo = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      substitution: str | YesNo = None,
  ):
    self.init()


class FirstFret(MusicElementBase):
  """The first-fret type indicates which fret is shown in the top space of the frame; it is fret 1 if the element is not present.

  The optional text attribute indicates how this is represented in the fret
  diagram, while the location attribute indicates whether the text appears to
  the left or right of the frame.
  """

  def __init__(
      self, plain_text: int, location: str | LeftRight = None, text: str = None
  ):
    self.init()


class FormattedSymbol(SmuflGlyphName):
  """The formatted-symbol type represents a SMuFL musical symbol element with formatting attributes."""

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      dir: str | TextDirection = None,
      enclosure: str | EnclosureShape = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      justify: str | LeftCenterRight = None,
      letter_spacing: str | NumberOrNormal = None,
      line_height: str | NumberOrNormal = None,
      line_through: int | NumberOfLines = None,
      overline: int | NumberOfLines = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      rotation: float | RotationDegrees = None,
      underline: int | NumberOfLines = None,
      valign: str | Valign = None,
  ):
    self.init()


class FormattedSymbolId(SmuflGlyphName):
  """The formatted-symbol-id type represents a SMuFL musical symbol element with formatting and id attributes."""

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      dir: str | TextDirection = None,
      enclosure: str | EnclosureShape = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      justify: str | LeftCenterRight = None,
      letter_spacing: str | NumberOrNormal = None,
      line_height: str | NumberOrNormal = None,
      line_through: int | NumberOfLines = None,
      overline: int | NumberOfLines = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      rotation: float | RotationDegrees = None,
      underline: int | NumberOfLines = None,
      valign: str | Valign = None,
  ):
    self.init()


class FormattedText(MusicElementBase):
  """The formatted-text type represents a text element with text-formatting attributes."""

  lang = 'xml'
  space = 'xml'

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      dir: str | TextDirection = None,
      enclosure: str | EnclosureShape = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      justify: str | LeftCenterRight = None,
      lang: str = None,
      letter_spacing: str | NumberOrNormal = None,
      line_height: str | NumberOrNormal = None,
      line_through: int | NumberOfLines = None,
      overline: int | NumberOfLines = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      rotation: float | RotationDegrees = None,
      space: str = None,
      underline: int | NumberOfLines = None,
      valign: str | Valign = None,
  ):
    self.init()


class FormattedTextId(MusicElementBase):
  """The formatted-text-id type represents a text element with text-formatting and id attributes."""

  lang = 'xml'
  space = 'xml'

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      dir: str | TextDirection = None,
      enclosure: str | EnclosureShape = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      justify: str | LeftCenterRight = None,
      lang: str = None,
      letter_spacing: str | NumberOrNormal = None,
      line_height: str | NumberOrNormal = None,
      line_through: int | NumberOfLines = None,
      overline: int | NumberOfLines = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      rotation: float | RotationDegrees = None,
      space: str = None,
      underline: int | NumberOfLines = None,
      valign: str | Valign = None,
  ):
    self.init()


class Fret(MusicElementBase):
  """The fret element is used with tablature notation and chord diagrams.

  Fret numbers start with 0 for an open string and 1 for the first fret.
  """

  def __init__(
      self,
      plain_text: int,
      color: str | Color = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
  ):
    self.init()


class Glass(GlassValue):
  """The glass type represents pictograms for glass percussion instruments.

  The smufl attribute is used to distinguish different SMuFL glyphs for wind
  chimes in the Chimes pictograms range, including those made of materials other
  than glass.
  """

  def __init__(
      self, plain_text: str, smufl: str | SmuflPictogramGlyphName = None
  ):
    self.init()


class Glissando(MusicElementBase):
  """Glissando and slide types both indicate rapidly moving from one pitch to the other so that individual notes are not discerned.

  A glissando sounds the distinct notes in between the two pitches and defaults
  to a wavy line. The optional text is printed alongside the line.
  """

  def __init__(
      self,
      plain_text: str,
      type: str | StartStop,
      color: str | Color = None,
      dash_length: float | Tenths = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      id: str = None,
      line_type: str | LineType = None,
      number: int | NumberLevel = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      space_length: float | Tenths = None,
  ):
    self.init()


class Glyph(SmuflGlyphName):
  """The glyph element represents what SMuFL glyph should be used for different variations of symbols that are semantically identical.

  The type attribute specifies what type of glyph is being defined. The element
  value specifies what SMuFL glyph to use, including recommended stylistic
  alternates. The SMuFL glyph name should match the type. For instance, a type
  of quarter-rest would use values restQuarter, restQuarterOld, or restQuarterZ.
  A type of g-clef-ottava-bassa would use values gClef8vb, gClef8vbOld, or
  gClef8vbCClef. A type of octave-shift-up-8 would use values ottava,
  ottavaBassa, ottavaBassaBa, ottavaBassaVb, or octaveBassa.
  """

  def __init__(self, plain_text: str, type: str | GlyphType):
    self.init()


class Grace(MusicElementBase):
  """The grace type indicates the presence of a grace note.

  The slash attribute for a grace note is yes for slashed grace notes. The
  steal-time-previous attribute indicates the percentage of time to steal from
  the previous note for the grace note. The steal-time-following attribute
  indicates the percentage of time to steal from the following note for the
  grace note, as for appoggiaturas. The make-time attribute indicates to make
  time, not steal time; the units are in real-time divisions for the grace note.
  """

  def __init__(
      self,
      make_time: float | Divisions = None,
      slash: str | YesNo = None,
      steal_time_following: float | Percent = None,
      steal_time_previous: float | Percent = None,
  ):
    self.init()


class GroupBarline(GroupBarlineValue):
  """The group-barline type indicates if the group should have common barlines."""

  def __init__(self, plain_text: str, color: str | Color = None):
    self.init()


class GroupName(MusicElementBase):
  """The group-name type describes the name or abbreviation of a part-group element.

  Formatting attributes in the group-name type are deprecated in Version 2.0 in
  favor of the new group-name-display and group-abbreviation-display elements.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      justify: str | LeftCenterRight = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class GroupSymbol(GroupSymbolValue):
  """The group-symbol type indicates how the symbol for a group is indicated in the score.

  It is none if not specified.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class HammerOnPullOff(MusicElementBase):
  """The hammer-on and pull-off elements are used in guitar and fretted instrument notation.

  Since a single slur can be marked over many notes, the hammer-on and pull-off
  elements are separate so the individual pair of notes can be specified. The
  element content can be used to specify how the hammer-on or pull-off should be
  notated. An empty element leaves this choice up to the application.
  """

  def __init__(
      self,
      plain_text: str,
      type: str | StartStop,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      number: int | NumberLevel = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class Handbell(HandbellValue):
  """The handbell element represents notation for various techniques used in handbell and handchime music."""

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class HarmonClosed(HarmonClosedValue):
  """The harmon-closed type represents whether the harmon mute is closed, open, or half-open.

  The optional location attribute indicates which portion of the symbol is
  filled in when the element value is half.
  """

  def __init__(
      self, plain_text: str, location: str | HarmonClosedLocation = None
  ):
    self.init()


class HarmonyAlter(Semitones):
  """The harmony-alter type represents the chromatic alteration of the root, numeral, or bass of the current harmony-chord group within the harmony element.

  In some chord styles, the text of the preceding element may include alteration
  information. In that case, the print-object attribute of this type can be set
  to no. The location attribute indicates whether the alteration should appear
  to the left or the right of the preceding element. Its default value varies by
  element.
  """

  def __init__(
      self,
      plain_text: float,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      location: str | LeftRight = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class HeelToe(EmptyPlacement):
  """The heel and toe elements are used with organ pedals.

  The substitution value is "no" if the attribute is not present.
  """

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      substitution: str | YesNo = None,
  ):
    self.init()


class HoleClosed(HoleClosedValue):
  """The hole-closed type represents whether the hole is closed, open, or half-open.

  The optional location attribute indicates which portion of the hole is filled
  in when the element value is half.
  """

  def __init__(
      self, plain_text: str, location: str | HoleClosedLocation = None
  ):
    self.init()


class HorizontalTurn(MusicElementBase):
  """The horizontal-turn type represents turn elements that are horizontal rather than vertical.

  These are empty elements with print-style, placement, trill-sound, and slash
  attributes. If the slash attribute is yes, then a vertical line is used to
  slash the turn. It is no if not specified.
  """

  def __init__(
      self,
      accelerate: str | YesNo = None,
      beats: float | TrillBeats = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      last_beat: float | Percent = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      second_beat: float | Percent = None,
      slash: str | YesNo = None,
      start_note: str | StartNote = None,
      trill_step: str | TrillStep = None,
      two_note_turn: str | TwoNoteTurn = None,
  ):
    self.init()


class Image(MusicElementBase):
  """The image type is used to include graphical images in a score."""

  def __init__(
      self,
      source: str,
      type: str,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      halign: str | LeftCenterRight = None,
      height: float | Tenths = None,
      id: str = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      valign: str | ValignImage = None,
      width: float | Tenths = None,
  ):
    self.init()


class Instrument(MusicElementBase):
  """The instrument type distinguishes between score-instrument elements in a score-part.

  The id attribute is an IDREF back to the score-instrument ID. If multiple
  score-instruments are specified in a score-part, there should be an instrument
  element for each note in the part. Notes that are shared between multiple
  score-instruments can have more than one instrument element.
  """

  def __init__(self, id: str):
    self.init()


class InstrumentLink(MusicElementBase):
  """Multiple part-link elements can link a condensed part within a score file to multiple MusicXML parts files.

  For example, a "Clarinet 1 and 2" part in a score file could link to separate
  "Clarinet 1" and "Clarinet 2" part files. The instrument-link type distinguish
  which of the score-instruments within a score-part are in which part file. The
  instrument-link id attribute refers to a score-instrument id attribute.
  """

  def __init__(self, id: str):
    self.init()


class Inversion(MusicElementBase):
  """The inversion type represents harmony inversions.

  The value is a number indicating which inversion is used: 0 for root position,
  1 for first inversion, etc.  The text attribute indicates how the inversion
  should be displayed in a score.
  """

  def __init__(
      self,
      plain_text: int,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      text: str = None,
  ):
    self.init()


class KeyAccidental(AccidentalValue):
  """The key-accidental type indicates the accidental to be displayed in a non-traditional key signature, represented in the same manner as the accidental type without the formatting attributes."""

  def __init__(
      self, plain_text: str, smufl: str | SmuflAccidentalGlyphName = None
  ):
    self.init()


class KeyOctave(Octave):
  """The key-octave type specifies in which octave an element of a key signature appears.

  The content specifies the octave value using the same values as the
  display-octave element. The number attribute is a positive integer that refers
  to the key signature element in left-to-right order. If the cancel attribute
  is set to yes, then this number refers to the canceling key signature
  specified by the cancel element in the parent key element. The cancel
  attribute cannot be set to yes if there is no corresponding cancel element
  within the parent key element. It is no by default.
  """

  def __init__(self, plain_text: int, number: int, cancel: str | YesNo = None):
    self.init()


class Kind(KindValue):
  """Kind indicates the type of chord.

  Degree elements can then add, subtract, or alter from these starting points

  The attributes are used to indicate the formatting of the symbol. Since the
  kind element is the constant in all the harmony-chord groups that can make up
  a polychord, many formatting attributes are here.

  The use-symbols attribute is yes if the kind should be represented when
  possible with harmony symbols rather than letters and numbers. These symbols
  include:

          major: a triangle, like Unicode 25B3
          minor: -, like Unicode 002D
          augmented: +, like Unicode 002B
          diminished: °, like Unicode 00B0
          half-diminished: ø, like Unicode 00F8

  For the major-minor kind, only the minor symbol is used when use-symbols is
  yes. The major symbol is set using the symbol attribute in the degree-value
  element. The corresponding degree-alter value will usually be 0 in this case.

  The text attribute describes how the kind should be spelled in a score. If
  use-symbols is yes, the value of the text attribute follows the symbol. The
  stack-degrees attribute is yes if the degree elements should be stacked above
  each other. The parentheses-degrees attribute is yes if all the degrees should
  be in parentheses. The bracket-degrees attribute is yes if all the degrees
  should be in a bracket. If not specified, these values are
  implementation-specific. The alignment attributes are for the entire
  harmony-chord group of which this kind element is a part.

  The text attribute may use strings such as "13sus" that refer to both the kind
  and one or more degree elements. In this case, the corresponding degree
  elements should have the print-object attribute set to "no" to keep redundant
  alterations from being displayed.
  """

  def __init__(
      self,
      plain_text: str,
      bracket_degrees: str | YesNo = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      parentheses_degrees: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      stack_degrees: str | YesNo = None,
      text: str = None,
      use_symbols: str | YesNo = None,
      valign: str | Valign = None,
  ):
    self.init()


class Level(MusicElementBase):
  """The level type is used to specify editorial information for different MusicXML elements.

  The content contains identifying and/or descriptive text about the editorial
  status of the parent element.

  If the reference attribute is yes, this indicates editorial information that
  is for display only and should not affect playback. For instance, a modern
  edition of older music may set reference="yes" on the attributes containing
  the music's original clef, key, and time signature. It is no if not specified.

  The type attribute indicates whether the editorial information applies to the
  start of a series of symbols, the end of a series of symbols, or a single
  symbol. It is single if not specified for compatibility with earlier MusicXML
  versions.
  """

  def __init__(
      self,
      plain_text: str,
      bracket: str | YesNo = None,
      parentheses: str | YesNo = None,
      reference: str | YesNo = None,
      size: str | SymbolSize = None,
      type: str | StartStopSingle = None,
  ):
    self.init()


class LineDetail(MusicElementBase):
  """If the staff-lines element is present, the appearance of each line may be individually specified with a line-detail type.

  Staff lines are numbered from bottom to top. The print-object attribute allows
  lines to be hidden within a staff. This is used in special situations such as
  a widely-spaced percussion staff where a note placed below the higher line is
  distinct from a note placed above the lower line. Hidden staff lines are
  included when specifying clef lines and determining display-step /
  display-octave values, but are not counted as lines for the purposes of the
  system-layout and staff-layout elements.
  """

  def __init__(
      self,
      line: int | StaffLine,
      color: str | Color = None,
      line_type: str | LineType = None,
      print_object: str | YesNo = None,
      width: float | Tenths = None,
  ):
    self.init()


class LineWidth(Tenths):
  """The line-width type indicates the width of a line type in tenths.

  The type attribute defines what type of line is being defined. Values include
  beam, bracket, dashes, enclosure, ending, extend, heavy barline, leger, light
  barline, octave shift, pedal, slur middle, slur tip, staff, stem, tie middle,
  tie tip, tuplet bracket, and wedge. The text content is expressed in tenths.
  """

  def __init__(self, plain_text: float, type: str | LineWidthType):
    self.init()


class Link(MusicElementBase):
  """The link type serves as an outgoing simple XLink.

  If a relative link is used within a document that is part of a compressed
  MusicXML file, the link is relative to the root folder of the zip file.
  """

  actuate = 'xlink'
  href = 'xlink'
  role = 'xlink'
  show = 'xlink'
  title = 'xlink'
  type = 'xlink'

  def __init__(
      self,
      actuate: str = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      element: str = None,
      href: str = None,
      name: str = None,
      position: int = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      role: str = None,
      show: str = None,
      title: str = None,
      type: str = None,
  ):
    self.init()


class LyricFont(MusicElementBase):
  """The lyric-font type specifies the default font for a particular name and number of lyric."""

  def __init__(
      self,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      name: str = None,
      number: str = None,
  ):
    self.init()


class LyricLanguage(MusicElementBase):
  """The lyric-language type specifies the default language for a particular name and number of lyric."""

  lang = 'xml'

  def __init__(self, lang: str = None, name: str = None, number: str = None):
    self.init()


class MeasureNumbering(MeasureNumberingValue):
  """The measure-numbering type describes how frequently measure numbers are displayed on this part.

  The text attribute from the measure element is used for display, or the number
  attribute if the text attribute is not present. Measures with an implicit
  attribute set to "yes" never display a measure number, regardless of the
  measure-numbering setting.

  The optional staff attribute refers to staff numbers within the part, from top
  to bottom on the system. It indicates which staff is used as the reference
  point for vertical positioning. A value of 1 is assumed if not present.

  The optional multiple-rest-always and multiple-rest-range attributes describe
  how measure numbers are shown on multiple rests when the measure-numbering
  value is not set to none. The multiple-rest-always attribute is set to yes
  when the measure number should always be shown, even if the multiple rest
  starts midway through a system when measure numbering is set to system level.
  The multiple-rest-range attribute is set to yes when measure numbers on
  multiple rests display the range of numbers for the first and last measure,
  rather than just the number of the first measure.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      multiple_rest_always: str | YesNo = None,
      multiple_rest_range: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      staff: int | StaffNumber = None,
      system: str | SystemRelationNumber = None,
      valign: str | Valign = None,
  ):
    self.init()


class MeasureRepeat(PositiveIntegerOrEmpty):
  """The measure-repeat type is used for both single and multiple measure repeats.

  The text of the element indicates the number of measures to be repeated in a
  single pattern. The slashes attribute specifies the number of slashes to use
  in the repeat sign. It is 1 if not specified. The text of the element is
  ignored when the type is stop.

  The stop type indicates the first measure where the repeats are no longer
  displayed. Both the start and the stop of the measure-repeat should be
  specified unless the repeats are displayed through the end of the part.

  The measure-repeat element specifies a notation style for repetitions. The
  actual music being repeated needs to be repeated within each measure of the
  MusicXML file. This element specifies the notation that indicates the repeat.
  """

  def __init__(
      self, plain_text: str, type: str | StartStop, slashes: int = None
  ):
    self.init()


class Membrane(MembraneValue):
  """The membrane type represents pictograms for membrane percussion instruments.

  The smufl attribute is used to distinguish different SMuFL stylistic
  alternates.
  """

  def __init__(
      self, plain_text: str, smufl: str | SmuflPictogramGlyphName = None
  ):
    self.init()


class Metal(MetalValue):
  """The metal type represents pictograms for metal percussion instruments.

  The smufl attribute is used to distinguish different SMuFL stylistic
  alternates.
  """

  def __init__(
      self, plain_text: str, smufl: str | SmuflPictogramGlyphName = None
  ):
    self.init()


class MetronomeBeam(BeamValue):
  """The metronome-beam type works like the beam type in defining metric relationships, but does not include all the attributes available in the beam type."""

  def __init__(self, plain_text: str, number: int | BeamLevel = None):
    self.init()


class MetronomeTied(MusicElementBase):
  """The metronome-tied indicates the presence of a tie within a metric relationship mark.

  As with the tied element, both the start and stop of the tie should be
  specified, in this case within separate metronome-note elements.
  """

  def __init__(self, type: str | StartStop):
    self.init()


class MidiDevice(MusicElementBase):
  """The midi-device type corresponds to the DeviceName meta event in Standard MIDI Files.

  The optional port attribute is a number from 1 to 16 that can be used with the
  unofficial MIDI 1.0 port (or cable) meta event. Unlike the DeviceName meta
  event, there can be multiple midi-device elements per MusicXML part. The
  optional id attribute refers to the score-instrument assigned to this device.
  If missing, the device assignment affects all score-instrument elements in the
  score-part.
  """

  def __init__(
      self, plain_text: str, id: str = None, port: int | Midi16 = None
  ):
    self.init()


class MiscellaneousField(MusicElementBase):
  """If a program has other metadata not yet supported in the MusicXML format, each type of metadata can go in a miscellaneous-field element.

  The required name attribute indicates the type of metadata the element content
  represents.
  """

  def __init__(self, plain_text: str, name: str):
    self.init()


class Mordent(EmptyTrillSound):
  """The mordent type is used for both represents the mordent sign with the vertical line and the inverted-mordent sign without the line.

  The long attribute is "no" by default. The approach and departure attributes
  are used for compound ornaments, indicating how the beginning and ending of
  the ornament look relative to the main part of the mordent.
  """

  def __init__(
      self,
      accelerate: str | YesNo = None,
      approach: str | AboveBelow = None,
      beats: float | TrillBeats = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      departure: str | AboveBelow = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      last_beat: float | Percent = None,
      long: str | YesNo = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      second_beat: float | Percent = None,
      start_note: str | StartNote = None,
      trill_step: str | TrillStep = None,
      two_note_turn: str | TwoNoteTurn = None,
  ):
    self.init()


class MultipleRest(MusicElementBase):
  """The text of the multiple-rest type indicates the number of measures in the multiple rest.

  Multiple rests may use the 1-bar / 2-bar / 4-bar rest symbols, or a single
  shape. The use-symbols attribute indicates which to use; it is no if not
  specified.
  """

  def __init__(self, plain_text: int, use_symbols: str | YesNo = None):
    self.init()


class NonArpeggiate(MusicElementBase):
  """The non-arpeggiate type indicates that this note is at the top or bottom of a bracket indicating to not arpeggiate these notes.

  Since this does not involve playback, it is only used on the top or bottom
  notes, not on each note as for the arpeggiate type.
  """

  def __init__(
      self,
      type: str | TopBottom,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      id: str = None,
      number: int | NumberLevel = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class NoteSize(NonNegativeDecimal):
  """The note-size type indicates the percentage of the regular note size to use for notes with a cue and large size as defined in the type element.

  The grace type is used for notes of cue size that that include a grace
  element. The cue type is used for all other notes with cue size, whether
  defined explicitly or implicitly via a cue element. The large type is used for
  notes of large size. The text content represent the numeric percentage. A
  value of 100 would be identical to the size of a regular note as defined by
  the music font.
  """

  def __init__(self, plain_text: float, type: str | NoteSizeType):
    self.init()


class NoteType(NoteTypeValue):
  """The note-type type indicates the graphic note type.

  Values range from 1024th to maxima. The size attribute indicates full, cue,
  grace-cue, or large size. The default is full for regular notes, grace-cue for
  notes that contain both grace and cue elements, and cue for notes that contain
  either a cue or a grace element, but not both.
  """

  def __init__(self, plain_text: str, size: str | SymbolSize = None):
    self.init()


class Notehead(NoteheadValue):
  """The notehead type indicates shapes other than the open and closed ovals associated with note durations.

  The smufl attribute can be used to specify a particular notehead, allowing
  application interoperability without requiring every SMuFL glyph to have a
  MusicXML element equivalent. This attribute can be used either with the
  "other" value, or to refine a specific notehead value such as "cluster".
  Noteheads in the SMuFL Note name noteheads and Note name noteheads supplement
  ranges (U+E150–U+E1AF and U+EEE0–U+EEFF) should not use the smufl attribute or
  the "other" value, but instead use the notehead-text element.

  For the enclosed shapes, the default is to be hollow for half notes and
  longer, and filled otherwise. The filled attribute can be set to change this
  if needed.

  If the parentheses attribute is set to yes, the notehead is parenthesized. It
  is no by default.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      filled: str | YesNo = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      parentheses: str | YesNo = None,
      smufl: str | SmuflGlyphName = None,
  ):
    self.init()


class NumeralRoot(NumeralValue):
  """The numeral-root type represents the Roman numeral or Nashville number as a positive integer from 1 to 7.

  The text attribute indicates how the numeral should appear in the score. A
  numeral-root value of 5 with a kind of major would have a text attribute of
  "V" if displayed as a Roman numeral, and "5" if displayed as a Nashville
  number. If the text attribute is not specified, the display is
  application-dependent.
  """

  def __init__(
      self,
      plain_text: int,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      text: str = None,
  ):
    self.init()


class OctaveShift(MusicElementBase):
  """The octave shift type indicates where notes are shifted up or down from their true pitched values because of printing difficulty.

  Thus a treble clef line noted with 8va will be indicated with an octave-shift
  down from the pitch data indicated in the notes. A size of 8 indicates one
  octave; a size of 15 indicates two octaves.
  """

  def __init__(
      self,
      type: str | UpDownStopContinue,
      color: str | Color = None,
      dash_length: float | Tenths = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      id: str = None,
      number: int | NumberLevel = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      size: int = None,
      space_length: float | Tenths = None,
  ):
    self.init()


class Offset(Divisions):
  """An offset is represented in terms of divisions, and indicates where the direction will appear relative to the current musical location.

  The current musical location is always within the current measure, even at the
  end of a measure.

  The offset affects the visual appearance of the direction. If the sound
  attribute is "yes", then the offset affects playback and listening too. If the
  sound attribute is "no", then any sound or listening associated with the
  direction takes effect at the current location. The sound attribute is "no" by
  default for compatibility with earlier versions of the MusicXML format. If an
  element within a direction includes a default-x attribute, the offset value
  will be ignored when determining the appearance of that element.
  """

  def __init__(self, plain_text: float, sound: str | YesNo = None):
    self.init()


class Opus(MusicElementBase):
  """The opus type represents a link to a MusicXML opus document that composes multiple MusicXML scores into a collection."""

  actuate = 'xlink'
  href = 'xlink'
  role = 'xlink'
  show = 'xlink'
  title = 'xlink'
  type = 'xlink'

  def __init__(
      self,
      actuate: str = None,
      href: str = None,
      role: str = None,
      show: str = None,
      title: str = None,
      type: str = None,
  ):
    self.init()


class OtherAppearance(MusicElementBase):
  """The other-appearance type is used to define any graphical settings not yet in the current version of the MusicXML format.

  This allows extended representation, though without application
  interoperability.
  """

  def __init__(self, plain_text: str, type: str):
    self.init()


class OtherDirection(MusicElementBase):
  """The other-direction type is used to define any direction symbols not yet in the MusicXML format.

  The smufl attribute can be used to specify a particular direction symbol,
  allowing application interoperability without requiring every SMuFL glyph to
  have a MusicXML element equivalent. Using the other-direction type without the
  smufl attribute allows for extended representation, though without application
  interoperability.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      smufl: str | SmuflGlyphName = None,
      valign: str | Valign = None,
  ):
    self.init()


class OtherListening(MusicElementBase):
  """The other-listening type represents other types of listening control and interaction.

  The required type attribute indicates the type of listening to which the
  element content applies. The optional player and time-only attributes restrict
  the element to apply to a single player or set of times through a repeated
  section, respectively.
  """

  def __init__(
      self,
      plain_text: str,
      type: str,
      player: str = None,
      time_only: str | TimeOnly = None,
  ):
    self.init()


class OtherNotation(MusicElementBase):
  """The other-notation type is used to define any notations not yet in the MusicXML format.

  It handles notations where more specific extension elements such as
  other-dynamics and other-technical are not appropriate. The smufl attribute
  can be used to specify a particular notation, allowing application
  interoperability without requiring every SMuFL glyph to have a MusicXML
  element equivalent. Using the other-notation type without the smufl attribute
  allows for extended representation, though without application
  interoperability.
  """

  def __init__(
      self,
      plain_text: str,
      type: str | StartStopSingle,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      id: str = None,
      number: int | NumberLevel = None,
      placement: str | AboveBelow = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      smufl: str | SmuflGlyphName = None,
  ):
    self.init()


class OtherPlacementText(MusicElementBase):
  """The other-placement-text type represents a text element with print-style, placement, and smufl attribute groups.

  This type is used by MusicXML notation extension elements to allow
  specification of specific SMuFL glyphs without needed to add every glyph as a
  MusicXML element.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      smufl: str | SmuflGlyphName = None,
  ):
    self.init()


class OtherPlay(MusicElementBase):
  """The other-play element represents other types of playback.

  The required type attribute indicates the type of playback to which the
  element content applies.
  """

  def __init__(self, plain_text: str, type: str):
    self.init()


class OtherText(MusicElementBase):
  """The other-text type represents a text element with a smufl attribute group.

  This type is used by MusicXML direction extension elements to allow
  specification of specific SMuFL glyphs without needed to add every glyph as a
  MusicXML element.
  """

  def __init__(self, plain_text: str, smufl: str | SmuflGlyphName = None):
    self.init()


class PartName(MusicElementBase):
  """The part-name type describes the name or abbreviation of a score-part element.

  Formatting attributes for the part-name element are deprecated in Version 2.0
  in favor of the new part-name-display and part-abbreviation-display elements.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      justify: str | LeftCenterRight = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class PartSymbol(GroupSymbolValue):
  """The part-symbol type indicates how a symbol for a multi-staff part is indicated in the score; brace is the default value.

  The top-staff and bottom-staff attributes are used when the brace does not
  extend across the entire part. For example, in a 3-staff organ part, the
  top-staff will typically be 1 for the right hand, while the bottom-staff will
  typically be 2 for the left hand. Staff 3 for the pedals is usually outside
  the brace. By default, the presence of a part-symbol element that does not
  extend across the entire part also indicates a corresponding change in the
  common barlines within a part.
  """

  def __init__(
      self,
      plain_text: str,
      bottom_staff: int | StaffNumber = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      top_staff: int | StaffNumber = None,
  ):
    self.init()


class Pedal(MusicElementBase):
  """The pedal type represents piano pedal marks, including damper and sostenuto pedal marks.

  The line attribute is yes if pedal lines are used. The sign attribute is yes
  if Ped, Sost, and * signs are used. For compatibility with older versions, the
  sign attribute is yes by default if the line attribute is no, and is no by
  default if the line attribute is yes. If the sign attribute is set to yes and
  the type is start or sostenuto, the abbreviated attribute is yes if the short
  P and S signs are used, and no if the full Ped and Sost signs are used. It is
  no by default. Otherwise the abbreviated attribute is ignored. The alignment
  attributes are ignored if the sign attribute is no.
  """

  def __init__(
      self,
      type: str | PedalType,
      abbreviated: str | YesNo = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      line: str | YesNo = None,
      number: int | NumberLevel = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      sign: str | YesNo = None,
      valign: str | Valign = None,
  ):
    self.init()


class PerMinute(MusicElementBase):
  """The per-minute type can be a number, or a text description including numbers.

  If a font is specified, it overrides the font specified for the overall
  metronome element. This allows separate specification of a music font for the
  beat-unit and a text font for the numeric value, in cases where a single
  metronome font is not used.
  """

  def __init__(
      self,
      plain_text: str,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
  ):
    self.init()


class Pitched(PitchedValue):
  """The pitched-value type represents pictograms for pitched percussion instruments.

  The smufl attribute is used to distinguish different SMuFL glyphs for a
  particular pictogram within the Tuned mallet percussion pictograms range.
  """

  def __init__(
      self, plain_text: str, smufl: str | SmuflPictogramGlyphName = None
  ):
    self.init()


class PlacementText(MusicElementBase):
  """The placement-text type represents a text element with print-style and placement attribute groups."""

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class PrincipalVoice(MusicElementBase):
  """The principal-voice type represents principal and secondary voices in a score, either for analysis or for square bracket symbols that appear in a score.

  The element content is used for analysis and may be any text value. The symbol
  attribute indicates the type of symbol used. When used for analysis separate
  from any printed score markings, it should be set to none. Otherwise if the
  type is stop it should be set to plain.
  """

  def __init__(
      self,
      plain_text: str,
      symbol: str | PrincipalVoiceSymbol,
      type: str | StartStop,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      valign: str | Valign = None,
  ):
    self.init()


class Release(Empty):
  """The release type indicates that a bend is a release rather than a normal bend or pre-bend.

  The offset attribute specifies where the release starts in terms of divisions
  relative to the current note. The first-beat and last-beat attributes of the
  parent bend element are relative to the original note position, not this
  offset value.
  """

  def __init__(self, offset: float | Divisions = None):
    self.init()


class Repeat(MusicElementBase):
  """The repeat type represents repeat marks.

  The start of the repeat has a forward direction while the end of the repeat
  has a backward direction. The times and after-jump attributes are only used
  with backward repeats that are not part of an ending. The times attribute
  indicates the number of times the repeated section is played. The after-jump
  attribute indicates if the repeats are played after a jump due to a da capo or
  dal segno.
  """

  def __init__(
      self,
      direction: str | BackwardForward,
      after_jump: str | YesNo = None,
      times: int = None,
      winged: str | Winged = None,
  ):
    self.init()


class RootStep(Step):
  """The root-step type represents the pitch step of the root of the current chord within the harmony element.

  The text attribute indicates how the root should appear in a score if not
  using the element contents.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      text: str = None,
  ):
    self.init()


class Segno(MusicElementBase):
  """The segno type is the visual indicator of a segno sign.

  The exact glyph can be specified with the smufl attribute. A sound element is
  also needed to guide playback applications reliably.
  """

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      smufl: str | SmuflSegnoGlyphName = None,
      valign: str | Valign = None,
  ):
    self.init()


class Slide(MusicElementBase):
  """Glissando and slide types both indicate rapidly moving from one pitch to the other so that individual notes are not discerned.

  A slide is continuous between the two pitches and defaults to a solid line.
  The optional text for a is printed alongside the line.
  """

  def __init__(
      self,
      plain_text: str,
      type: str | StartStop,
      accelerate: str | YesNo = None,
      beats: float | TrillBeats = None,
      color: str | Color = None,
      dash_length: float | Tenths = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      first_beat: float | Percent = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      id: str = None,
      last_beat: float | Percent = None,
      line_type: str | LineType = None,
      number: int | NumberLevel = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      space_length: float | Tenths = None,
  ):
    self.init()


class Slur(MusicElementBase):
  """Slur types are empty.

  Most slurs are represented with two elements: one with a start type, and one
  with a stop type. Slurs can add more elements using a continue type. This is
  typically used to specify the formatting of cross-system slurs, or to specify
  the shape of very complex slurs.
  """

  def __init__(
      self,
      type: str | StartStopContinue,
      bezier_offset: float | Divisions = None,
      bezier_offset2: float | Divisions = None,
      bezier_x: float | Tenths = None,
      bezier_x2: float | Tenths = None,
      bezier_y: float | Tenths = None,
      bezier_y2: float | Tenths = None,
      color: str | Color = None,
      dash_length: float | Tenths = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      id: str = None,
      line_type: str | LineType = None,
      number: int | NumberLevel = None,
      orientation: str | OverUnder = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      space_length: float | Tenths = None,
  ):
    self.init()


class StaffDivide(MusicElementBase):
  """The staff-divide element represents the staff division arrow symbols found at SMuFL code points U+E00B, U+E00C, and U+E00D."""

  def __init__(
      self,
      type: str | StaffDivideSymbol,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      valign: str | Valign = None,
  ):
    self.init()


class StaffSize(NonNegativeDecimal):
  """The staff-size element indicates how large a staff space is on this staff, expressed as a percentage of the work's default scaling.

  Values less than 100 make the staff space smaller while values over 100 make
  the staff space larger. A staff-type of cue, ossia, or editorial implies a
  staff-size of less than 100, but the exact value is implementation-dependent
  unless specified here. Staff size affects staff height only, not the
  relationship of the staff to the left and right margins.

  In some cases, a staff-size different than 100 also scales the notation on the
  staff, such as with a cue staff. In other cases, such as percussion staves,
  the lines may be more widely spaced without scaling the notation on the staff.
  The scaling attribute allows these two cases to be distinguished. It specifies
  the percentage scaling that applies to the notation. Values less that 100 make
  the notation smaller while values over 100 make the notation larger. The
  staff-size content and scaling attribute are both non-negative decimal values.
  """

  def __init__(
      self, plain_text: float, scaling: float | NonNegativeDecimal = None
  ):
    self.init()


class Stem(StemValue):
  """Stems can be down, up, none, or double.

  For down and up stems, the position attributes can be used to specify stem
  length. The relative values specify the end of the stem relative to the
  program default. Default values specify an absolute end stem position.
  Negative values of relative-y that would flip a stem instead of shortening it
  are ignored. A stem element associated with a rest refers to a stemlet.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class String(StringNumber):
  """The string type is used with tablature notation, regular notation (where it is often circled), and chord diagrams.

  String numbers start with 1 for the highest pitched full-length string.
  """

  def __init__(
      self,
      plain_text: int,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class StringMute(MusicElementBase):
  """The string-mute type represents string mute on and mute off symbols."""

  def __init__(
      self,
      type: str | OnOff,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      valign: str | Valign = None,
  ):
    self.init()


class StrongAccent(EmptyPlacement):
  """The strong-accent type indicates a vertical accent mark.

  The type attribute indicates if the point of the accent is down or up.
  """

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      type: str | UpDown = None,
  ):
    self.init()


class StyleText(MusicElementBase):
  """The style-text type represents a text element with a print-style attribute group."""

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class Supports(MusicElementBase):
  """The supports type indicates if a MusicXML encoding supports a particular MusicXML element.

  This is recommended for elements like beam, stem, and accidental, where the
  absence of an element is ambiguous if you do not know if the encoding supports
  that element. For Version 2.0, the supports element is expanded to allow
  programs to indicate support for particular attributes or particular values.
  This lets applications communicate, for example, that all system and/or page
  breaks are contained in the MusicXML file.
  """

  def __init__(
      self,
      element: str,
      type: str | YesNo,
      attribute: str = None,
      value: str = None,
  ):
    self.init()


class Sync(MusicElementBase):
  """The sync type specifies the style that a score following application should use the synchronize an accompaniment with a performer.

  If this type is not included in a score, default synchronization depends on
  the application.

  The optional latency attribute specifies a time in milliseconds that the
  listening application should expect from the performer. The optional player
  and time-only attributes restrict the element to apply to a single player or
  set of times through a repeated section, respectively.
  """

  def __init__(
      self,
      type: str | SyncType,
      latency: int | Milliseconds = None,
      player: str = None,
      time_only: str | TimeOnly = None,
  ):
    self.init()


class Tap(MusicElementBase):
  """The tap type indicates a tap on the fretboard.

  The text content allows specification of the notation; + and T are common
  choices. If the element is empty, the hand attribute is used to specify the
  symbol to use. The hand attribute is ignored if the tap glyph is already
  specified by the text content. If neither text content nor the hand attribute
  are present, the display is application-specific.
  """

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      hand: str | TapHand = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
  ):
    self.init()


class TextElementData(MusicElementBase):
  """The text-element-data type represents a syllable or portion of a syllable for lyric text underlay.

  A hyphen in the string content should only be used for an actual hyphenated
  word. Language names for text elements come from ISO 639, with optional
  country subcodes from ISO 3166.
  """

  lang = 'xml'

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      dir: str | TextDirection = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      lang: str = None,
      letter_spacing: str | NumberOrNormal = None,
      line_through: int | NumberOfLines = None,
      overline: int | NumberOfLines = None,
      rotation: float | RotationDegrees = None,
      underline: int | NumberOfLines = None,
  ):
    self.init()


class Tie(MusicElementBase):
  """The tie element indicates that a tie begins or ends with this note.

  If the tie element applies only particular times through a repeat, the
  time-only attribute indicates which times to apply it. The tie element
  indicates sound; the tied element indicates notation.
  """

  def __init__(self, type: str | StartStop, time_only: str | TimeOnly = None):
    self.init()


class Tied(MusicElementBase):
  """The tied element represents the notated tie.

  The tie element represents the tie sound.

  The number attribute is rarely needed to disambiguate ties, since note pitches
  will usually suffice. The attribute is implied rather than defaulting to 1 as
  with most elements. It is available for use in more complex tied notation
  situations.

  Ties that join two notes of the same pitch together should be represented with
  a tied element on the first note with type="start" and a tied element on the
  second note with type="stop".  This can also be done if the two notes being
  tied are enharmonically equivalent, but have different step values. It is not
  recommended to use tied elements to join two notes with enharmonically
  inequivalent pitches.

  Ties that indicate that an instrument should be undamped are specified with a
  single tied element with type="let-ring".

  Ties that are visually attached to only one note, other than undamped ties,
  should be specified with two tied elements on the same note, first
  type="start" then type="stop". This can be used to represent ties into or out
  of repeated sections or codas.
  """

  def __init__(
      self,
      type: str | TiedType,
      bezier_offset: float | Divisions = None,
      bezier_offset2: float | Divisions = None,
      bezier_x: float | Tenths = None,
      bezier_x2: float | Tenths = None,
      bezier_y: float | Tenths = None,
      bezier_y2: float | Tenths = None,
      color: str | Color = None,
      dash_length: float | Tenths = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      id: str = None,
      line_type: str | LineType = None,
      number: int | NumberLevel = None,
      orientation: str | OverUnder = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      space_length: float | Tenths = None,
  ):
    self.init()


class Timpani(MusicElementBase):
  """The timpani type represents the timpani pictogram.

  The smufl attribute is used to distinguish different SMuFL stylistic
  alternates.
  """

  def __init__(self, smufl: str | SmuflPictogramGlyphName = None):
    self.init()


class Tremolo(TremoloMarks):
  """The tremolo ornament can be used to indicate single-note, double-note, or unmeasured tremolos.

  Single-note tremolos use the single type, double-note tremolos use the start
  and stop types, and unmeasured tremolos use the unmeasured type. The default
  is "single" for compatibility with Version 1.1. The text of the element
  indicates the number of tremolo marks and is an integer from 0 to 8. Note that
  the number of attached beams is not included in this value, but is represented
  separately using the beam element. The value should be 0 for unmeasured
  tremolos.

  When using double-note tremolos, the duration of each note in the tremolo
  should correspond to half of the notated type value. A time-modification
  element should also be added with an actual-notes value of 2 and a
  normal-notes value of 1. If used within a tuplet, this 2/1 ratio should be
  multiplied by the existing tuplet ratio.

  The smufl attribute specifies the glyph to use from the SMuFL Tremolos range
  for an unmeasured tremolo. It is ignored for other tremolo types. The SMuFL
  buzzRoll glyph is used by default if the attribute is missing.

  Using repeater beams for indicating tremolos is deprecated as of MusicXML 3.0.
  """

  def __init__(
      self,
      plain_text: int,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      smufl: str | SmuflGlyphName = None,
      type: str | TremoloType = None,
  ):
    self.init()


class TupletDot(MusicElementBase):
  """The tuplet-dot type is used to specify dotted tuplet types."""

  def __init__(
      self,
      color: str | Color = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
  ):
    self.init()


class TupletNumber(MusicElementBase):
  """The tuplet-number type indicates the number of notes for this portion of the tuplet."""

  def __init__(
      self,
      plain_text: int,
      color: str | Color = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
  ):
    self.init()


class TupletType(NoteTypeValue):
  """The tuplet-type type indicates the graphical note type of the notes for this portion of the tuplet."""

  def __init__(
      self,
      plain_text: str,
      color: str | Color = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
  ):
    self.init()


class TypedText(MusicElementBase):
  """The typed-text type represents a text element with a type attribute."""

  def __init__(self, plain_text: str, type: str = None):
    self.init()


class Wait(MusicElementBase):
  """The wait type specifies a point where the accompaniment should wait for a performer event before continuing.

  This typically happens at the start of new sections or after a held note or
  indeterminate music. These waiting points cannot always be inferred reliably
  from the contents of the displayed score. The optional player and time-only
  attributes restrict the type to apply to a single player or set of times
  through a repeated section, respectively.
  """

  def __init__(self, player: str = None, time_only: str | TimeOnly = None):
    self.init()


class WavyLine(MusicElementBase):
  """Wavy lines are one way to indicate trills and vibrato.

  When used with a barline element, they should always have type="continue" set.
  The smufl attribute specifies a particular wavy line glyph from the SMuFL
  Multi-segment lines range.
  """

  def __init__(
      self,
      type: str | StartStopContinue,
      accelerate: str | YesNo = None,
      beats: float | TrillBeats = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      last_beat: float | Percent = None,
      number: int | NumberLevel = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      second_beat: float | Percent = None,
      smufl: str | SmuflWavyLineGlyphName = None,
      start_note: str | StartNote = None,
      trill_step: str | TrillStep = None,
      two_note_turn: str | TwoNoteTurn = None,
  ):
    self.init()


class Wedge(MusicElementBase):
  """The wedge type represents crescendo and diminuendo wedge symbols.

  The type attribute is crescendo for the start of a wedge that is closed at the
  left side, and diminuendo for the start of a wedge that is closed on the right
  side. Spread values are measured in tenths; those at the start of a crescendo
  wedge or end of a diminuendo wedge are ignored. The niente attribute is yes if
  a circle appears at the point of the wedge, indicating a crescendo from
  nothing or diminuendo to nothing. It is no by default, and used only when the
  type is crescendo, or the type is stop for a wedge that began with a
  diminuendo type. The line-type is solid if not specified.
  """

  def __init__(
      self,
      type: str | WedgeType,
      color: str | Color = None,
      dash_length: float | Tenths = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      id: str = None,
      line_type: str | LineType = None,
      niente: str | YesNo = None,
      number: int | NumberLevel = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      space_length: float | Tenths = None,
      spread: float | Tenths = None,
  ):
    self.init()


class Wood(WoodValue):
  """The wood type represents pictograms for wood percussion instruments.

  The smufl attribute is used to distinguish different SMuFL stylistic
  alternates.
  """

  def __init__(
      self, plain_text: str, smufl: str | SmuflPictogramGlyphName = None
  ):
    self.init()


class Accord(MusicElementBase):
  """The accord type represents the tuning of a single string in the scordatura element.

  It uses the same group of elements as the staff-tuning element. Strings are
  numbered from high to low.
  """

  TuningAlter = Semitones
  TuningOctave = Octave
  TuningStep = Step

  def __init__(
      self,
      string: int | StringNumber = None,
      TuningStep: str | TuningStep = None,
      TuningAlter: float | TuningAlter = None,
      TuningOctave: int | TuningOctave = None,
  ):
    self.init()


class AccordionRegistration(MusicElementBase):
  """The accordion-registration type is used for accordion registration symbols.

  These are circular symbols divided horizontally into high, middle, and low
  sections that correspond to 4', 8', and 16' pipes. Each accordion-high,
  accordion-middle, and accordion-low element represents the presence of one or
  more dots in the registration diagram. An accordion-registration element needs
  to have at least one of the child elements present.
  """

  AccordionHigh = Empty
  AccordionLow = Empty

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      valign: str | Valign = None,
      AccordionHigh: AccordionHigh = None,
      AccordionMiddle: int | AccordionMiddle = None,
      AccordionLow: AccordionLow = None,
  ):
    self.init()


class Appearance(MusicElementBase):
  """The appearance type controls general graphical settings for the music's final form appearance on a printed page of display.

  This includes support for line widths, definitions for note sizes, and
  standard distances between notation elements, plus an extension element for
  other aspects of appearance.
  """

  def __init__(self):
    self.init()


class Arrow(MusicElementBase):
  """The arrow element represents an arrow used for a musical technical indication.

  It can represent both Unicode and SMuFL arrows. The presence of an arrowhead
  element indicates that only the arrowhead is displayed, not the arrow stem.
  The smufl attribute distinguishes different SMuFL glyphs that have an arrow
  appearance such as arrowBlackUp, guitarStrumUp, or handbellsSwingUp. The
  specified glyph should match the descriptive representation.
  """

  Arrowhead = Empty

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      smufl: str | SmuflGlyphName = None,
      ArrowDirection: str | ArrowDirection = None,
      ArrowStyle: str | ArrowStyle = None,
      Arrowhead: Arrowhead = None,
      CircularArrow: str | CircularArrow = None,
  ):
    self.init()


class Articulations(MusicElementBase):
  """Articulations and accents are grouped together here."""

  Accent = EmptyPlacement
  DetachedLegato = EmptyPlacement
  Doit = EmptyLine
  Falloff = EmptyLine
  OtherArticulation = OtherPlacementText
  Plop = EmptyLine
  Scoop = EmptyLine
  SoftAccent = EmptyPlacement
  Spiccato = EmptyPlacement
  Staccatissimo = EmptyPlacement
  Staccato = EmptyPlacement
  Stress = EmptyPlacement
  Tenuto = EmptyPlacement
  Unstress = EmptyPlacement

  def __init__(self, id: str = None):
    self.init()


class Attributes(MusicElementBase):
  """The attributes element contains musical information that typically changes on measure boundaries.

  This includes key and time signatures, clefs, transpositions, and staving.
  When attributes are changed mid-measure, it affects the music in score order,
  not in MusicXML document order.
  """

  Divisions = PositiveDivisions
  Footnote = FormattedText

  class Directive(MusicElementBase):
    lang = 'xml'

    def __init__(
        self,
        plain_text: str,
        color: str | Color = None,
        default_x: float | Tenths = None,
        default_y: float | Tenths = None,
        font_family: str | FontFamily = None,
        font_size: str | FontSize = None,
        font_style: str | FontStyle = None,
        font_weight: str | FontWeight = None,
        lang: str = None,
        relative_x: float | Tenths = None,
        relative_y: float | Tenths = None,
    ):
      self.init()

  class Instruments(MusicElementBase):
    """The instruments element is only used if more than one instrument is represented in the part (e.g., oboe I and II where they play together most of the time).

    If absent, a value of 1 is assumed.
    """

    def __init__(self, plain_text: int):
      self.init()

  class Staves(MusicElementBase):
    """The staves element is used if there is more than one staff represented in the given part (e.g., 2 staves for typical piano parts).

    If absent, a value of 1 is assumed. Staves are ordered from top to bottom in
    a part in numerical order, with staff 1 above staff 2.
    """

    def __init__(self, plain_text: int):
      self.init()

  def __init__(
      self,
      Footnote: Footnote = None,
      Level: Level = None,
      Divisions: float | Divisions = None,
      Staves: int | Staves = None,
      PartSymbol: PartSymbol = None,
      Instruments: int | Instruments = None,
  ):
    self.init()


class Backup(MusicElementBase):
  """The backup and forward elements are required to coordinate multiple voices in one part, including music on multiple staves.

  The backup type is generally used to move between voices and staves. Thus the
  backup element does not include voice or staff elements. Duration values
  should always be positive, and should not cross measure boundaries or
  mid-measure changes in the divisions value.
  """

  Duration = PositiveDivisions
  Footnote = FormattedText

  def __init__(
      self,
      Duration: float | Duration = None,
      Footnote: Footnote = None,
      Level: Level = None,
  ):
    self.init()


class Barline(MusicElementBase):
  """If a barline is other than a normal single barline, it should be represented by a barline type that describes it.

  This includes information about repeats and multiple endings, as well as line
  style. Barline data is on the same level as the other musical data in a score
  - a child of a measure in a partwise score, or a part in a timewise score.
  This allows for barlines within measures, as in dotted barlines that subdivide
  measures in complex meters. The two fermata elements allow for fermatas on
  both sides of the barline (the lower one inverted).

  Barlines have a location attribute to make it easier to process barlines
  independently of the other musical data in a score. It is often easier to set
  up measures separately from entering notes. The location attribute must match
  where the barline element occurs within the rest of the musical data in the
  score. If location is left, it should be the first element in the measure,
  aside from the print, bookmark, and link elements. If location is right, it
  should be the last element, again with the possible exception of the print,
  bookmark, and link elements. If no location is specified, the right barline is
  the default. The segno, coda, and divisions attributes work the same way as in
  the sound element. They are used for playback when barline elements contain
  segno or coda child elements.
  """

  BarStyle = BarStyleColor
  Footnote = FormattedText

  def __init__(
      self,
      coda: str = None,
      divisions: float | Divisions = None,
      id: str = None,
      location: str | RightLeftMiddle = None,
      segno: str = None,
      BarStyle: BarStyle = None,
      Footnote: Footnote = None,
      Level: Level = None,
      WavyLine: WavyLine = None,
      Segno: Segno = None,
      Coda: Coda = None,
      Ending: Ending = None,
      Repeat: Repeat = None,
  ):
    self.init()


class Bass(MusicElementBase):
  """The bass type is used to indicate a bass note in popular music chord symbols, e.g.

  G/C. It is generally not used in functional harmony, as inversion is generally
  not used in pop chord symbols. As with root, it is divided into step and alter
  elements, similar to pitches. The arrangement attribute specifies where the
  bass is displayed relative to what precedes it.
  """

  BassAlter = HarmonyAlter
  BassSeparator = StyleText

  def __init__(
      self,
      arrangement: str | HarmonyArrangement = None,
      BassSeparator: BassSeparator = None,
      BassStep: BassStep = None,
      BassAlter: BassAlter = None,
  ):
    self.init()


class BeatRepeat(MusicElementBase):
  """The beat-repeat type is used to indicate that a single beat (but possibly many notes) is repeated.

  The slashes attribute specifies the number of slashes to use in the symbol.
  The use-dots attribute indicates whether or not to use dots as well (for
  instance, with mixed rhythm patterns). The value for slashes is 1 and the
  value for use-dots is no if not specified.

  The stop type indicates the first beat where the repeats are no longer
  displayed. Both the start and stop of the beat being repeated should be
  specified unless the repeats are displayed through the end of the part.

  The beat-repeat element specifies a notation style for repetitions. The actual
  music being repeated needs to be repeated within the MusicXML file. This
  element specifies the notation that indicates the repeat.
  """

  SlashDot = Empty
  SlashType = NoteTypeValue

  class ExceptVoice(MusicElementBase):
    """The except-voice element is used to specify a combination of slash notation and regular notation.

    Any note elements that are in voices specified by the except-voice elements
    are displayed in normal notation, in addition to the slash notation that is
    always displayed.
    """

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      type: str | StartStop,
      slashes: int = None,
      use_dots: str | YesNo = None,
      SlashType: str | SlashType = None,
  ):
    self.init()


class BeatUnitTied(MusicElementBase):
  """The beat-unit-tied type indicates a beat-unit within a metronome mark that is tied to the preceding beat-unit.

  This allows two or more tied notes to be associated with a per-minute value in
  a metronome mark, whereas the metronome-tied element is restricted to metric
  relationship marks.
  """

  BeatUnit = NoteTypeValue
  BeatUnitDot = Empty

  def __init__(self, BeatUnit: str | BeatUnit = None):
    self.init()


class Bend(MusicElementBase):
  """The bend type is used in guitar notation and tablature.

  A single note with a bend and release will contain two bend elements: the
  first to represent the bend and the second to represent the release. The shape
  attribute distinguishes between the angled bend symbols commonly used in
  standard notation and the curved bend symbols commonly used in both tablature
  and standard notation.
  """

  BendAlter = Semitones
  PreBend = Empty
  WithBar = PlacementText

  def __init__(
      self,
      accelerate: str | YesNo = None,
      beats: float | TrillBeats = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      first_beat: float | Percent = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      last_beat: float | Percent = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      shape: str | BendShape = None,
      BendAlter: float | BendAlter = None,
      PreBend: PreBend = None,
      Release: Release = None,
      WithBar: WithBar = None,
  ):
    self.init()


class Clef(MusicElementBase):
  """Clefs are represented by a combination of sign, line, and clef-octave-change elements.

  The optional number attribute refers to staff numbers within the part. A value
  of 1 is assumed if not present.

  Sometimes clefs are added to the staff in non-standard line positions, either
  to indicate cue passages, or when there are multiple clefs present
  simultaneously on one staff. In this situation, the additional attribute is
  set to "yes" and the line value is ignored. The size attribute is used for
  clefs where the additional attribute is "yes". It is typically used to
  indicate cue clefs.

  Sometimes clefs at the start of a measure need to appear after the barline
  rather than before, as for cues or for use after a repeated section. The
  after-barline attribute is set to "yes" in this situation. The attribute is
  ignored for mid-measure clefs.

  Clefs appear at the start of each system unless the print-object attribute has
  been set to "no" or the additional attribute has been set to "yes".
  """

  Line = StaffLinePosition
  Sign = ClefSign

  class ClefOctaveChange(MusicElementBase):
    """The clef-octave-change element is used for transposing clefs.

    A treble clef for tenors would have a value of -1.
    """

    def __init__(self, plain_text: int):
      self.init()

  def __init__(
      self,
      additional: str | YesNo = None,
      after_barline: str | YesNo = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      id: str = None,
      number: int | StaffNumber = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      size: str | SymbolSize = None,
      Sign: str | Sign = None,
      Line: int | Line = None,
      ClefOctaveChange: int | ClefOctaveChange = None,
  ):
    self.init()


class Credit(MusicElementBase):
  """The credit type represents the appearance of the title, composer, arranger, lyricist, copyright, dedication, and other text, symbols, and graphics that commonly appear on the first page of a score.

  The credit-words, credit-symbol, and credit-image elements are similar to the
  words, symbol, and image elements for directions. However, since the credit is
  not part of a measure, the default-x and default-y attributes adjust the
  origin relative to the bottom left-hand corner of the page. The enclosure for
  credit-words and credit-symbol is none by default.

  By default, a series of credit-words and credit-symbol elements within a
  single credit element follow one another in sequence visually. Non-positional
  formatting attributes are carried over from the previous element by default.

  The page attribute for the credit element specifies the page number where the
  credit should appear. This is an integer value that starts with 1 for the
  first page. Its value is 1 by default. Since credits occur before the music,
  these page numbers do not refer to the page numbering specified by the print
  element's page-number attribute.

  The credit-type element indicates the purpose behind a credit. Multiple types
  of data may be combined in a single credit, so multiple elements may be used.
  Standard values include page number, title, subtitle, composer, arranger,
  lyricist, rights, and part name.
  """

  CreditImage = Image
  CreditSymbol = FormattedSymbolId
  CreditWords = FormattedTextId

  class CreditType(MusicElementBase):

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      id: str = None,
      page: int = None,
      CreditImage: CreditImage = None,
      CreditWords: CreditWords = None,
      CreditSymbol: CreditSymbol = None,
  ):
    self.init()


class Defaults(MusicElementBase):
  """The defaults type specifies score-wide defaults for scaling; whether or not the file is a concert score; layout; and default values for the music font, word font, lyric font, and lyric language.

  Except for the concert-score element, if any defaults are missing, the choice
  of what to use is determined by the application.
  """

  ConcertScore = Empty
  MusicFont = EmptyFont
  WordFont = EmptyFont

  def __init__(
      self,
      Scaling: Scaling = None,
      ConcertScore: ConcertScore = None,
      PageLayout: PageLayout = None,
      SystemLayout: SystemLayout = None,
      Appearance: Appearance = None,
      MusicFont: MusicFont = None,
      WordFont: WordFont = None,
  ):
    self.init()


class Degree(MusicElementBase):
  """The degree type is used to add, alter, or subtract individual notes in the chord.

  The print-object attribute can be used to keep the degree from printing
  separately when it has already taken into account in the text attribute of the
  kind element. The degree-value and degree-type text attributes specify how the
  value and type of the degree should be displayed.

  A harmony of kind "other" can be spelled explicitly by using a series of
  degree elements together with a root.
  """

  def __init__(
      self,
      print_object: str | YesNo = None,
      DegreeValue: DegreeValue = None,
      DegreeAlter: DegreeAlter = None,
      DegreeType: DegreeType = None,
  ):
    self.init()


class Direction(MusicElementBase):
  """A direction is a musical indication that is not necessarily attached to a specific note.

  Two or more may be combined to indicate words followed by the start of a
  dashed line, the end of a wedge followed by dynamics, etc. For applications
  where a specific direction is indeed attached to a specific note, the
  direction element can be associated with the first note element that follows
  it in score order that is not in a different voice.

  By default, a series of direction-type elements and a series of child elements
  of a direction-type within a single direction element follow one another in
  sequence visually. For a series of direction-type children, non-positional
  formatting attributes are carried over from the previous element by default.
  """

  Footnote = FormattedText

  class Staff(MusicElementBase):
    """Staff assignment is only needed for music notated on multiple staves.

    Used by both notes and directions. Staff values are numbers, with 1
    referring to the top-most staff in a part.
    """

    def __init__(self, plain_text: int):
      self.init()

  class Voice(MusicElementBase):

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      directive: str | YesNo = None,
      id: str = None,
      placement: str | AboveBelow = None,
      system: str | SystemRelation = None,
      Offset: Offset = None,
      Footnote: Footnote = None,
      Level: Level = None,
      Voice: str | Voice = None,
      Staff: int | Staff = None,
      Sound: Sound = None,
      Listening: Listening = None,
  ):
    self.init()


class DirectionType(MusicElementBase):
  """Textual direction types may have more than 1 component due to multiple fonts.

  The dynamics element may also be used in the notations element. Attribute
  groups related to print suggestions apply to the individual direction-type,
  not to the overall direction.
  """

  Damp = EmptyPrintStyleAlignId
  DampAll = EmptyPrintStyleAlignId
  Eyeglasses = EmptyPrintStyleAlignId
  Rehearsal = FormattedTextId
  Symbol = FormattedSymbolId
  Words = FormattedTextId

  def __init__(
      self,
      id: str = None,
      Wedge: Wedge = None,
      Dashes: Dashes = None,
      Bracket: Bracket = None,
      Pedal: Pedal = None,
      Metronome: Metronome = None,
      OctaveShift: OctaveShift = None,
      HarpPedals: HarpPedals = None,
      Damp: Damp = None,
      DampAll: DampAll = None,
      Eyeglasses: Eyeglasses = None,
      StringMute: StringMute = None,
      Scordatura: Scordatura = None,
      Image: Image = None,
      PrincipalVoice: PrincipalVoice = None,
      AccordionRegistration: AccordionRegistration = None,
      StaffDivide: StaffDivide = None,
      OtherDirection: OtherDirection = None,
  ):
    self.init()


class Dynamics(MusicElementBase):
  """Dynamics can be associated either with a note or a general musical direction.

  To avoid inconsistencies between and amongst the letter abbreviations for
  dynamics (what is sf vs. sfz, standing alone or with a trailing dynamic that
  is not always piano), we use the actual letters as the names of these dynamic
  elements. The other-dynamics element allows other dynamic marks that are not
  covered here. Dynamics elements may also be combined to create marks not
  covered by a single element, such as sfmp.

  These letter dynamic symbols are separated from crescendo, decrescendo, and
  wedge indications. Dynamic representation is inconsistent in scores. Many
  things are assumed by the composer and left out, such as returns to original
  dynamics. The MusicXML format captures what is in the score, but does not try
  to be optimal for analysis or synthesis of dynamics.

  The placement attribute is used when the dynamics are associated with a note.
  It is ignored when the dynamics are associated with a direction. In that case
  the direction element's placement attribute is used instead.
  """

  F = Empty
  Ff = Empty
  Fff = Empty
  Ffff = Empty
  Fffff = Empty
  Ffffff = Empty
  Fp = Empty
  Fz = Empty
  Mf = Empty
  Mp = Empty
  N = Empty
  OtherDynamics = OtherText
  P = Empty
  Pf = Empty
  Pp = Empty
  Ppp = Empty
  Pppp = Empty
  Ppppp = Empty
  Pppppp = Empty
  Rf = Empty
  Rfz = Empty
  Sf = Empty
  Sffz = Empty
  Sfp = Empty
  Sfpp = Empty
  Sfz = Empty
  Sfzp = Empty

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      enclosure: str | EnclosureShape = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      line_through: int | NumberOfLines = None,
      overline: int | NumberOfLines = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      underline: int | NumberOfLines = None,
      valign: str | Valign = None,
  ):
    self.init()


class Encoding(MusicElementBase):
  """The encoding element contains information about who did the digital encoding, when, with what software, and in what aspects.

  Standard type values for the encoder element are music, words, and
  arrangement, but other types may be used. The type attribute is only needed
  when there are multiple encoder elements.
  """

  Encoder = TypedText
  EncodingDate = YyyyMmDd

  class EncodingDescription(MusicElementBase):

    def __init__(self, plain_text: str):
      self.init()

  class Software(MusicElementBase):

    def __init__(self, plain_text: str):
      self.init()

  def __init__(self):
    self.init()


class Figure(MusicElementBase):
  """The figure type represents a single figure within a figured-bass element."""

  FigureNumber = StyleText
  Footnote = FormattedText
  Prefix = StyleText
  Suffix = StyleText

  def __init__(
      self,
      Prefix: Prefix = None,
      FigureNumber: FigureNumber = None,
      Suffix: Suffix = None,
      Extend: Extend = None,
      Footnote: Footnote = None,
      Level: Level = None,
  ):
    self.init()


class FiguredBass(MusicElementBase):
  """The figured-bass element represents figured bass notation.

  Figured bass elements take their position from the first regular note (not a
  grace note or chord note) that follows in score order. The optional duration
  element is used to indicate changes of figures under a note.

  Figures are ordered from top to bottom. The value of parentheses is "no" if
  not present.
  """

  Duration = PositiveDivisions
  Footnote = FormattedText

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      parentheses: str | YesNo = None,
      placement: str | AboveBelow = None,
      print_dot: str | YesNo = None,
      print_lyric: str | YesNo = None,
      print_object: str | YesNo = None,
      print_spacing: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      valign: str | Valign = None,
      Duration: float | Duration = None,
      Footnote: Footnote = None,
      Level: Level = None,
  ):
    self.init()


class ForPart(MusicElementBase):
  """The for-part type is used in a concert score to indicate the transposition for a transposed part created from that score.

  It is only used in score files that contain a concert-score element in the
  defaults. This allows concert scores with transposed parts to be represented
  in a single uncompressed MusicXML file.

  The optional number attribute refers to staff numbers, from top to bottom on
  the system. If absent, the child elements apply to all staves in the created
  part.
  """

  def __init__(
      self,
      id: str = None,
      number: int | StaffNumber = None,
      PartClef: PartClef = None,
      PartTranspose: PartTranspose = None,
  ):
    self.init()


class Forward(MusicElementBase):
  """The backup and forward elements are required to coordinate multiple voices in one part, including music on multiple staves.

  The forward element is generally used within voices and staves. Duration
  values should always be positive, and should not cross measure boundaries or
  mid-measure changes in the divisions value.
  """

  Duration = PositiveDivisions
  Footnote = FormattedText

  class Staff(MusicElementBase):
    """Staff assignment is only needed for music notated on multiple staves.

    Used by both notes and directions. Staff values are numbers, with 1
    referring to the top-most staff in a part.
    """

    def __init__(self, plain_text: int):
      self.init()

  class Voice(MusicElementBase):

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      Duration: float | Duration = None,
      Footnote: Footnote = None,
      Level: Level = None,
      Voice: str | Voice = None,
      Staff: int | Staff = None,
  ):
    self.init()


class Frame(MusicElementBase):
  """The frame type represents a frame or fretboard diagram used together with a chord symbol.

  The representation is based on the NIFF guitar grid with additional
  information. The frame type's unplayed attribute indicates what to display
  above a string that has no associated frame-note element. Typical values are x
  and the empty string. If the attribute is not present, the display of the
  unplayed string is application-defined.
  """

  class FrameFrets(MusicElementBase):
    """The frame-frets element gives the overall size of the frame in horizontal spaces (frets)."""

    def __init__(self, plain_text: int):
      self.init()

  class FrameStrings(MusicElementBase):
    """The frame-strings element gives the overall size of the frame in vertical lines (strings)."""

    def __init__(self, plain_text: int):
      self.init()

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      halign: str | LeftCenterRight = None,
      height: float | Tenths = None,
      id: str = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      unplayed: str = None,
      valign: str | ValignImage = None,
      width: float | Tenths = None,
      FrameStrings: int | FrameStrings = None,
      FrameFrets: int | FrameFrets = None,
      FirstFret: FirstFret = None,
  ):
    self.init()


class FrameNote(MusicElementBase):
  """The frame-note type represents each note included in the frame.

  An open string will have a fret value of 0, while a muted string will not be
  associated with a frame-note element.
  """

  def __init__(
      self,
      String: String = None,
      Fret: Fret = None,
      Fingering: Fingering = None,
      Barre: Barre = None,
  ):
    self.init()


class Grouping(MusicElementBase):
  """The grouping type is used for musical analysis.

  When the type attribute is "start" or "single", it usually contains one or
  more feature elements. The number attribute is used for distinguishing between
  overlapping and hierarchical groupings. The member-of attribute allows for
  easy distinguishing of what grouping elements are in what hierarchy. Feature
  elements contained within a "stop" type of grouping may be ignored.

  This element is flexible to allow for different types of analyses. Future
  versions of the MusicXML format may add elements that can represent more
  standardized categories of analysis data, allowing for easier data sharing.
  """

  def __init__(
      self,
      type: str | StartStopSingle,
      id: str = None,
      member_of: str = None,
      number: str = None,
  ):
    self.init()


class HarmonMute(MusicElementBase):
  """The harmon-mute type represents the symbols used for harmon mutes in brass notation."""

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      HarmonClosed: HarmonClosed = None,
  ):
    self.init()


class Harmonic(MusicElementBase):
  """The harmonic type indicates natural and artificial harmonics.

  Allowing the type of pitch to be specified, combined with controls for
  appearance/playback differences, allows both the notation and the sound to be
  represented. Artificial harmonics can add a notated touching pitch; artificial
  pinch harmonics will usually not notate a touching pitch. The attributes for
  the harmonic element refer to the use of the circular harmonic symbol,
  typically but not always used with natural harmonics.
  """

  Artificial = Empty
  BasePitch = Empty
  Natural = Empty
  SoundingPitch = Empty
  TouchingPitch = Empty

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      Natural: Natural = None,
      Artificial: Artificial = None,
      BasePitch: BasePitch = None,
      TouchingPitch: TouchingPitch = None,
      SoundingPitch: SoundingPitch = None,
  ):
    self.init()


class Harmony(MusicElementBase):
  """The harmony type represents harmony analysis, including chord symbols in popular music as well as functional harmony analysis in classical music.

  If there are alternate harmonies possible, this can be specified using
  multiple harmony elements differentiated by type. Explicit harmonies have all
  note present in the music; implied have some notes missing but implied;
  alternate represents alternate analyses.

  The print-object attribute controls whether or not anything is printed due to
  the harmony element. The print-frame attribute controls printing of a frame or
  fretboard diagram. The print-style attribute group sets the default for the
  harmony, but individual elements can override this with their own print-style
  values. The arrangement attribute specifies how multiple harmony-chord groups
  are arranged relative to each other. Harmony-chords with vertical arrangement
  are separated by horizontal lines. Harmony-chords with diagonal or horizontal
  arrangement are separated by diagonal lines or slashes.
  """

  Footnote = FormattedText
  Function = StyleText

  class Staff(MusicElementBase):
    """Staff assignment is only needed for music notated on multiple staves.

    Used by both notes and directions. Staff values are numbers, with 1
    referring to the top-most staff in a part.
    """

    def __init__(self, plain_text: int):
      self.init()

  def __init__(
      self,
      arrangement: str | HarmonyArrangement = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      id: str = None,
      placement: str | AboveBelow = None,
      print_frame: str | YesNo = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      system: str | SystemRelation = None,
      type: str | HarmonyType = None,
      Frame: Frame = None,
      Offset: Offset = None,
      Footnote: Footnote = None,
      Level: Level = None,
      Staff: int | Staff = None,
  ):
    self.init()


class HarpPedals(MusicElementBase):
  """The harp-pedals type is used to create harp pedal diagrams.

  The pedal-step and pedal-alter elements use the same values as the step and
  alter elements. For easiest reading, the pedal-tuning elements should follow
  standard harp pedal order, with pedal-step values of D, C, B, E, F, G, and A.
  """

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      valign: str | Valign = None,
  ):
    self.init()


class Hole(MusicElementBase):
  """The hole type represents the symbols used for woodwind and brass fingerings as well as other notations."""

  class HoleShape(MusicElementBase):
    """The optional hole-shape element indicates the shape of the hole symbol; the default is a circle."""

    def __init__(self, plain_text: str):
      self.init()

  class HoleType(MusicElementBase):
    """The content of the optional hole-type element indicates what the hole symbol represents in terms of instrument fingering or other techniques."""

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      HoleType: str | HoleType = None,
      HoleClosed: HoleClosed = None,
      HoleShape: str | HoleShape = None,
  ):
    self.init()


class Identification(MusicElementBase):
  """Identification contains basic metadata about the score.

  It includes information that may apply at a score-wide, movement-wide, or
  part-wide level. The creator, rights, source, and relation elements are based
  on Dublin Core.
  """

  Creator = TypedText
  Relation = TypedText
  Rights = TypedText

  class Source(MusicElementBase):
    """The source for the music that is encoded.

    This is similar to the Dublin Core source element.
    """

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      Encoding: Encoding = None,
      Source: str | Source = None,
      Miscellaneous: Miscellaneous = None,
  ):
    self.init()


class InstrumentChange(MusicElementBase):
  """The instrument-change element type represents a change to the virtual instrument sound for a given score-instrument.

  The id attribute refers to the score-instrument affected by the change. All
  instrument-change child elements can also be initially specified within the
  score-instrument element.
  """

  Ensemble = PositiveIntegerOrEmpty
  Solo = Empty

  class InstrumentSound(MusicElementBase):
    """The instrument-sound element describes the default timbre of the score-instrument.

    This description is independent of a particular virtual or MIDI instrument
    specification and allows playback to be shared more easily between
    applications and libraries.
    """

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      id: str,
      InstrumentSound: str | InstrumentSound = None,
      Solo: Solo = None,
      Ensemble: str | Ensemble = None,
      VirtualInstrument: VirtualInstrument = None,
  ):
    self.init()


class Interchangeable(MusicElementBase):
  """The interchangeable type is used to represent the second in a pair of interchangeable dual time signatures, such as the 6/8 in 3/4 (6/8).

  A separate symbol attribute value is available compared to the time element's
  symbol attribute, which applies to the first of the dual time signatures.
  """

  class BeatType(MusicElementBase):
    """The beat-type element indicates the beat unit, as found in the denominator of a time signature."""

    def __init__(self, plain_text: str):
      self.init()

  class Beats(MusicElementBase):
    """The beats element indicates the number of beats, as found in the numerator of a time signature."""

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      separator: str | TimeSeparator = None,
      symbol: str | TimeSymbol = None,
      TimeRelation: str | TimeRelation = None,
  ):
    self.init()


class Key(MusicElementBase):
  """The key type represents a key signature.

  Both traditional and non-traditional key signatures are supported. The
  optional number attribute refers to staff numbers. If absent, the key
  signature applies to all staves in the part. Key signatures appear at the
  start of each system unless the print-object attribute has been set to "no".
  """

  KeyAlter = Semitones
  KeyStep = Step

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      id: str = None,
      number: int | StaffNumber = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      Cancel: Cancel = None,
      Fifths: int | Fifths = None,
      Mode: str | Mode = None,
  ):
    self.init()


class Listen(MusicElementBase):
  """The listen and listening types, new in Version 4.0, specify different ways that a score following or machine listening application can interact with a performer.

  The listen type handles interactions that are specific to a note. If multiple
  child elements of the same type are present, they should have distinct player
  and/or time-only attributes.
  """

  OtherListen = OtherListening

  def __init__(self):
    self.init()


class Listening(MusicElementBase):
  """The listen and listening types, new in Version 4.0, specify different ways that a score following or machine listening application can interact with a performer.

  The listening type handles interactions that change the state of the listening
  application from the specified point in the performance onward. If multiple
  child elements of the same type are present, they should have distinct player
  and/or time-only attributes.

  The offset element is used to indicate that the listening change takes place
  offset from the current score position. If the listening element is a child of
  a direction element, the listening offset element overrides the direction
  offset element if both elements are present. Note that the offset reflects the
  intended musical position for the change in state. It should not be used to
  compensate for latency issues in particular hardware configurations.
  """

  def __init__(self, Offset: Offset = None):
    self.init()


class Lyric(MusicElementBase):
  """The lyric type represents text underlays for lyrics.

  Two text elements that are not separated by an elision element are part of the
  same syllable, but may have different text formatting. The MusicXML XSD is
  more strict than the DTD in enforcing this by disallowing a second syllabic
  element unless preceded by an elision element. The lyric number indicates
  multiple lines, though a name can be used as well. Common name examples are
  verse and chorus.

  Justification is center by default; placement is below by default. Vertical
  alignment is to the baseline of the text and horizontal alignment matches
  justification. The print-object attribute can override a note's print-lyric
  attribute in cases where only some lyrics on a note are printed, as when
  lyrics for later verses are printed in a block of text rather than with each
  note. The time-only attribute precisely specifies which lyrics are to be sung
  which time through a repeated section.
  """

  EndLine = Empty
  EndParagraph = Empty
  Footnote = FormattedText
  Humming = Empty
  Laughing = Empty
  Text = TextElementData

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      id: str = None,
      justify: str | LeftCenterRight = None,
      name: str = None,
      number: str = None,
      placement: str | AboveBelow = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      time_only: str | TimeOnly = None,
      Syllabic: str | Syllabic = None,
      Text: Text = None,
      Extend: Extend = None,
      Laughing: Laughing = None,
      Humming: Humming = None,
      EndLine: EndLine = None,
      EndParagraph: EndParagraph = None,
      Footnote: Footnote = None,
      Level: Level = None,
  ):
    self.init()


class MeasureLayout(MusicElementBase):
  """The measure-layout type includes the horizontal distance from the previous measure.

  It applies to the current measure only.
  """

  MeasureDistance = Tenths

  def __init__(self, MeasureDistance: float | MeasureDistance = None):
    self.init()


class MeasureStyle(MusicElementBase):
  """A measure-style indicates a special way to print partial to multiple measures within a part.

  This includes multiple rests over several measures, repeats of beats, single,
  or multiple measures, and use of slash notation.

  The multiple-rest and measure-repeat elements indicate the number of measures
  covered in the element content. The beat-repeat and slash elements can cover
  partial measures. All but the multiple-rest element use a type attribute to
  indicate starting and stopping the use of the style. The optional number
  attribute specifies the staff number from top to bottom on the system, as with
  clef.
  """

  def __init__(
      self,
      color: str | Color = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      id: str = None,
      number: int | StaffNumber = None,
      MultipleRest: MultipleRest = None,
      MeasureRepeat: MeasureRepeat = None,
      BeatRepeat: BeatRepeat = None,
      Slash: Slash = None,
  ):
    self.init()


class Metronome(MusicElementBase):
  """The metronome type represents metronome marks and other metric relationships.

  The beat-unit group and per-minute element specify regular metronome marks.
  The metronome-note and metronome-relation elements allow for the specification
  of metric modulations and other metric relationships, such as swing tempo
  marks where two eighths are equated to a quarter note / eighth note triplet.
  Tied notes can be represented in both types of metronome marks by using the
  beat-unit-tied and metronome-tied elements. The parentheses attribute
  indicates whether or not to put the metronome mark in parentheses; its value
  is no if not specified. The print-object attribute is set to no in cases where
  the metronome element represents a relationship or range that is not displayed
  in the music notation.
  """

  BeatUnit = NoteTypeValue
  BeatUnitDot = Empty
  MetronomeArrows = Empty

  class MetronomeRelation(MusicElementBase):
    """The metronome-relation element describes the relationship symbol that goes between the two sets of metronome-note elements.

    The currently allowed value is equals, but this may expand in future
    versions. If the element is empty, the equals value is used.
    """

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      justify: str | LeftCenterRight = None,
      parentheses: str | YesNo = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      valign: str | Valign = None,
      PerMinute: PerMinute = None,
      BeatUnit: str | BeatUnit = None,
      MetronomeArrows: MetronomeArrows = None,
      MetronomeRelation: str | MetronomeRelation = None,
  ):
    self.init()


class MetronomeNote(MusicElementBase):
  """The metronome-note type defines the appearance of a note within a metric relationship mark."""

  MetronomeDot = Empty
  MetronomeType = NoteTypeValue

  def __init__(
      self,
      MetronomeType: str | MetronomeType = None,
      MetronomeTied: MetronomeTied = None,
      MetronomeTuplet: MetronomeTuplet = None,
  ):
    self.init()


class MidiInstrument(MusicElementBase):
  """The midi-instrument type defines MIDI 1.0 instrument playback.

  The midi-instrument element can be a part of either the score-instrument
  element at the start of a part, or the sound element within a part. The id
  attribute refers to the score-instrument affected by the change.
  """

  Elevation = RotationDegrees
  MidiBank = Midi16384
  MidiChannel = Midi16
  MidiProgram = Midi128
  MidiUnpitched = Midi128
  Pan = RotationDegrees
  Volume = Percent

  class MidiName(MusicElementBase):
    """The midi-name element corresponds to a ProgramName meta-event within a Standard MIDI File."""

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      id: str,
      MidiChannel: int | MidiChannel = None,
      MidiName: str | MidiName = None,
      MidiBank: int | MidiBank = None,
      MidiProgram: int | MidiProgram = None,
      MidiUnpitched: int | MidiUnpitched = None,
      Volume: float | Volume = None,
      Pan: float | Pan = None,
      Elevation: float | Elevation = None,
  ):
    self.init()


class Miscellaneous(MusicElementBase):
  """If a program has other metadata not yet supported in the MusicXML format, it can go in the miscellaneous element.

  The miscellaneous type puts each separate part of metadata into its own
  miscellaneous-field type.
  """

  def __init__(self):
    self.init()


class NameDisplay(MusicElementBase):
  """The name-display type is used for exact formatting of multi-font text in part and group names to the left of the system.

  The print-object attribute can be used to determine what, if anything, is
  printed at the start of each system. Enclosure for the display-text element is
  none by default. Language for the display-text element is Italian ("it") by
  default.
  """

  DisplayText = FormattedText

  def __init__(self, print_object: str | YesNo = None):
    self.init()


class Notations(MusicElementBase):
  """Notations refer to musical notations, not XML notations.

  Multiple notations are allowed in order to represent multiple editorial
  levels. The print-object attribute, added in Version 3.0, allows notations to
  represent details of performance technique, such as fingerings, without having
  them appear in the score.
  """

  Footnote = FormattedText

  def __init__(
      self,
      id: str = None,
      print_object: str | YesNo = None,
      Footnote: Footnote = None,
      Level: Level = None,
  ):
    self.init()


class Note(MusicElementBase):
  """Notes are the most common type of MusicXML data.

  The MusicXML format distinguishes between elements used for sound information
  and elements used for notation information (e.g., tie is used for sound, tied
  for notation). Thus grace notes do not have a duration element. Cue notes have
  a duration element, as do forward elements, but no tie elements. Having these
  two types of information available can make interchange easier, as some
  programs handle one type of information more readily than the other.

  The print-leger attribute is used to indicate whether leger lines are printed.
  Notes without leger lines are used to indicate indeterminate high and low
  notes. By default, it is set to yes. If print-object is set to no, print-leger
  is interpreted to also be set to no if not present. This attribute is ignored
  for rests.

  The dynamics and end-dynamics attributes correspond to MIDI 1.0's Note On and
  Note Off velocities, respectively. They are expressed in terms of percentages
  of the default forte value (90 for MIDI 1.0).

  The attack and release attributes are used to alter the starting and stopping
  time of the note from when it would otherwise occur based on the flow of
  durations - information that is specific to a performance. They are expressed
  in terms of divisions, either positive or negative. A note that starts a tie
  should not have a release attribute, and a note that stops a tie should not
  have an attack attribute. The attack and release attributes are independent of
  each other. The attack attribute only changes the starting time of a note, and
  the release attribute only changes the stopping time of a note.

  If a note is played only particular times through a repeat, the time-only
  attribute shows which times to play the note.

  The pizzicato attribute is used when just this note is sounded pizzicato, vs.
  the pizzicato element which changes overall playback between pizzicato and
  arco.
  """

  Chord = Empty
  Cue = Empty
  Dot = EmptyPlacement
  Duration = PositiveDivisions
  Footnote = FormattedText
  Type = NoteType

  class Staff(MusicElementBase):
    """Staff assignment is only needed for music notated on multiple staves.

    Used by both notes and directions. Staff values are numbers, with 1
    referring to the top-most staff in a part.
    """

    def __init__(self, plain_text: int):
      self.init()

  class Voice(MusicElementBase):

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      attack: float | Divisions = None,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      dynamics: float | NonNegativeDecimal = None,
      end_dynamics: float | NonNegativeDecimal = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      id: str = None,
      pizzicato: str | YesNo = None,
      print_dot: str | YesNo = None,
      print_leger: str | YesNo = None,
      print_lyric: str | YesNo = None,
      print_object: str | YesNo = None,
      print_spacing: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      release: float | Divisions = None,
      time_only: str | TimeOnly = None,
      Grace: Grace = None,
      Cue: Cue = None,
      Chord: Chord = None,
      Pitch: Pitch = None,
      Unpitched: Unpitched = None,
      Rest: Rest = None,
      Duration: float | Duration = None,
      Footnote: Footnote = None,
      Level: Level = None,
      Voice: str | Voice = None,
      Type: Type = None,
      Accidental: Accidental = None,
      TimeModification: TimeModification = None,
      Stem: Stem = None,
      Notehead: Notehead = None,
      NoteheadText: NoteheadText = None,
      Staff: int | Staff = None,
      Play: Play = None,
      Listen: Listen = None,
  ):
    self.init()


class NoteheadText(MusicElementBase):
  """The notehead-text type represents text that is displayed inside a notehead, as is done in some educational music.

  It is not needed for the numbers used in tablature or jianpu notation. The
  presence of a TAB or jianpu clefs is sufficient to indicate that numbers are
  used. The display-text and accidental-text elements allow display of fully
  formatted text and accidentals.
  """

  DisplayText = FormattedText

  def __init__(self):
    self.init()


class Numeral(MusicElementBase):
  """The numeral type represents the Roman numeral or Nashville number part of a harmony.

  It requires that the key be specified in the encoding, either with a key or
  numeral-key element.
  """

  NumeralAlter = HarmonyAlter

  def __init__(
      self,
      NumeralRoot: NumeralRoot = None,
      NumeralAlter: NumeralAlter = None,
      NumeralKey: NumeralKey = None,
  ):
    self.init()


class NumeralKey(MusicElementBase):
  """The numeral-key type is used when the key for the numeral is different than the key specified by the key signature.

  The numeral-fifths element specifies the key in the same way as the fifths
  element. The numeral-mode element specifies the mode similar to the mode
  element, but with a restricted set of values
  """

  NumeralFifths = Fifths

  def __init__(
      self,
      print_object: str | YesNo = None,
      NumeralFifths: int | NumeralFifths = None,
      NumeralMode: str | NumeralMode = None,
  ):
    self.init()


class Ornaments(MusicElementBase):
  """Ornaments can be any of several types, followed optionally by accidentals.

  The accidental-mark element's content is represented the same as an accidental
  element, but with a different name to reflect the different musical meaning.
  """

  DelayedInvertedTurn = HorizontalTurn
  DelayedTurn = HorizontalTurn
  Haydn = EmptyTrillSound
  InvertedMordent = Mordent
  InvertedTurn = HorizontalTurn
  InvertedVerticalTurn = EmptyTrillSound
  OtherOrnament = OtherPlacementText
  Schleifer = EmptyPlacement
  Shake = EmptyTrillSound
  TrillMark = EmptyTrillSound
  Turn = HorizontalTurn
  VerticalTurn = EmptyTrillSound

  def __init__(
      self,
      id: str = None,
      TrillMark: TrillMark = None,
      Turn: Turn = None,
      DelayedTurn: DelayedTurn = None,
      InvertedTurn: InvertedTurn = None,
      DelayedInvertedTurn: DelayedInvertedTurn = None,
      VerticalTurn: VerticalTurn = None,
      InvertedVerticalTurn: InvertedVerticalTurn = None,
      Shake: Shake = None,
      WavyLine: WavyLine = None,
      Mordent: Mordent = None,
      InvertedMordent: InvertedMordent = None,
      Schleifer: Schleifer = None,
      Tremolo: Tremolo = None,
      Haydn: Haydn = None,
      OtherOrnament: OtherOrnament = None,
  ):
    self.init()


class PageLayout(MusicElementBase):
  """Page layout can be defined both in score-wide defaults and in the print element.

  Page margins are specified either for both even and odd pages, or via separate
  odd and even page number values. The type is not needed when used as part of a
  print element. If omitted when used in the defaults element, "both" is the
  default.

  If no page-layout element is present in the defaults element, default page
  layout values are chosen by the application.

  When used in the print element, the page-layout element affects the appearance
  of the current page only. All other pages use the default values as determined
  by the defaults element. If any child elements are missing from the
  page-layout element in a print element, the values determined by the defaults
  element are used there as well.
  """

  PageHeight = Tenths
  PageWidth = Tenths

  def __init__(
      self,
      PageHeight: float | PageHeight = None,
      PageWidth: float | PageWidth = None,
  ):
    self.init()


class PageMargins(MusicElementBase):
  """Page margins are specified either for both even and odd pages, or via separate odd and even page number values.

  The type attribute is not needed when used as part of a print element. If
  omitted when the page-margins type is used in the defaults element, "both" is
  the default value.
  """

  BottomMargin = Tenths
  LeftMargin = Tenths
  RightMargin = Tenths
  TopMargin = Tenths

  def __init__(
      self,
      type: str | MarginType = None,
      LeftMargin: float | LeftMargin = None,
      RightMargin: float | RightMargin = None,
      TopMargin: float | TopMargin = None,
      BottomMargin: float | BottomMargin = None,
  ):
    self.init()


class PartClef(MusicElementBase):
  """The child elements of the part-clef type have the same meaning as for the clef type.

  However that meaning applies to a transposed part created from the existing
  score file.
  """

  Line = StaffLinePosition
  Sign = ClefSign

  class ClefOctaveChange(MusicElementBase):
    """The clef-octave-change element is used for transposing clefs.

    A treble clef for tenors would have a value of -1.
    """

    def __init__(self, plain_text: int):
      self.init()

  def __init__(
      self,
      Sign: str | Sign = None,
      Line: int | Line = None,
      ClefOctaveChange: int | ClefOctaveChange = None,
  ):
    self.init()


class PartGroup(MusicElementBase):
  """The part-group element indicates groupings of parts in the score, usually indicated by braces and brackets.

  Braces that are used for multi-staff parts should be defined in the attributes
  element for that part. The part-group start element appears before the first
  score-part in the group. The part-group stop element appears after the last
  score-part in the group.

  The number attribute is used to distinguish overlapping and nested
  part-groups, not the sequence of groups. As with parts, groups can have a name
  and abbreviation. Values for the child elements are ignored at the stop of a
  group.

  A part-group element is not needed for a single multi-staff part. By default,
  multi-staff parts include a brace symbol and (if appropriate given the
  bar-style) common barlines. The symbol formatting for a multi-staff part can
  be more fully specified using the part-symbol element.
  """

  Footnote = FormattedText
  GroupAbbreviation = GroupName
  GroupAbbreviationDisplay: TYPE[NameDisplay] = None
  GroupNameDisplay: TYPE[NameDisplay] = None
  GroupTime = Empty

  def __init__(
      self,
      type: str | StartStop,
      number: str = None,
      GroupName: GroupName = None,
      GroupNameDisplay: GroupNameDisplay = None,
      GroupAbbreviation: GroupAbbreviation = None,
      GroupAbbreviationDisplay: GroupAbbreviationDisplay = None,
      GroupSymbol: GroupSymbol = None,
      GroupBarline: GroupBarline = None,
      GroupTime: GroupTime = None,
      Footnote: Footnote = None,
      Level: Level = None,
  ):
    self.init()


class PartLink(MusicElementBase):
  """The part-link type allows MusicXML data for both score and parts to be contained within a single compressed MusicXML file.

  It links a score-part from a score document to MusicXML documents that contain
  parts data. In the case of a single compressed MusicXML file, the link href
  values are paths that are relative to the root folder of the zip file.
  """

  actuate = 'xlink'
  href = 'xlink'
  role = 'xlink'
  show = 'xlink'
  title = 'xlink'
  type = 'xlink'

  class GroupLink(MusicElementBase):
    """Multiple part-link elements can reference different types of linked documents, such as parts and condensed score.

    The optional group-link elements identify the groups used in the linked
    document. The content of a group-link element should match the content of a
    group element in the linked document.
    """

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      actuate: str = None,
      href: str = None,
      role: str = None,
      show: str = None,
      title: str = None,
      type: str = None,
  ):
    self.init()


class PartList(MusicElementBase):
  """The part-list identifies the different musical parts in this document.

  Each part has an ID that is used later within the musical data. Since parts
  may be encoded separately and combined later, identification elements are
  present at both the score and score-part levels. There must be at least one
  score-part, combined as desired with part-group elements that indicate braces
  and brackets. Parts are ordered from top to bottom in a score based on the
  order in which they appear in the part-list.
  """

  def __init__(self, ScorePart: ScorePart = None):
    self.init()


class PartTranspose(MusicElementBase):
  """The child elements of the part-transpose type have the same meaning as for the transpose type.

  However that meaning applies to a transposed part created from the existing
  score file.
  """

  Chromatic = Semitones

  class Diatonic(MusicElementBase):
    """The diatonic element specifies the number of pitch steps needed to go from written to sounding pitch.

    This allows for correct spelling of enharmonic transpositions. This value
    does not include octave-change values; the values for both elements need to
    be added to the written pitch to get the correct sounding pitch.
    """

    def __init__(self, plain_text: int):
      self.init()

  class OctaveChange(MusicElementBase):
    """The octave-change element indicates how many octaves to add to get from written pitch to sounding pitch.

    The octave-change element should be included when using transposition
    intervals of an octave or more, and should not be present for intervals of
    less than an octave.
    """

    def __init__(self, plain_text: int):
      self.init()

  def __init__(
      self,
      Diatonic: int | Diatonic = None,
      Chromatic: float | Chromatic = None,
      OctaveChange: int | OctaveChange = None,
      Double: Double = None,
  ):
    self.init()


class PedalTuning(MusicElementBase):
  """The pedal-tuning type specifies the tuning of a single harp pedal."""

  PedalAlter = Semitones
  PedalStep = Step

  def __init__(
      self,
      PedalStep: str | PedalStep = None,
      PedalAlter: float | PedalAlter = None,
  ):
    self.init()


class Percussion(MusicElementBase):
  """The percussion element is used to define percussion pictogram symbols.

  Definitions for these symbols can be found in Kurt Stone's "Music Notation in
  the Twentieth Century" on pages 206-212 and 223. Some values are added to
  these based on how usage has evolved in the 30 years since Stone's book was
  published.
  """

  OtherPercussion = OtherText

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      enclosure: str | EnclosureShape = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      valign: str | Valign = None,
      Glass: Glass = None,
      Metal: Metal = None,
      Wood: Wood = None,
      Pitched: Pitched = None,
      Membrane: Membrane = None,
      Effect: Effect = None,
      Timpani: Timpani = None,
      Beater: Beater = None,
      Stick: Stick = None,
      StickLocation: str | StickLocation = None,
      OtherPercussion: OtherPercussion = None,
  ):
    self.init()


class Pitch(MusicElementBase):
  """Pitch is represented as a combination of the step of the diatonic scale, the chromatic alteration, and the octave."""

  Alter = Semitones

  def __init__(
      self,
      Step: str | Step = None,
      Alter: float | Alter = None,
      Octave: int | Octave = None,
  ):
    self.init()


class Play(MusicElementBase):
  """The play type specifies playback techniques to be used in conjunction with the instrument-sound element.

  When used as part of a sound element, it applies to all notes going forward in
  score order. In multi-instrument parts, the affected instrument should be
  specified using the id attribute. When used as part of a note element, it
  applies to the current note only.
  """

  class Ipa(MusicElementBase):
    """The ipa element represents International Phonetic Alphabet (IPA) sounds for vocal music.

    String content is limited to IPA 2015 symbols represented in Unicode 13.0.
    """

    def __init__(self, plain_text: str):
      self.init()

  def __init__(self, id: str = None):
    self.init()


class Player(MusicElementBase):
  """The player type allows for multiple players per score-part for use in listening applications.

  One player may play multiple instruments, while a single instrument may
  include multiple players in divisi sections.
  """

  class PlayerName(MusicElementBase):
    """The player-name element is typically used within a software application, rather than appearing on the printed page of a score."""

    def __init__(self, plain_text: str):
      self.init()

  def __init__(self, id: str, PlayerName: str | PlayerName = None):
    self.init()


class Print(MusicElementBase):
  """The print type contains general printing parameters, including layout elements.

  The part-name-display and part-abbreviation-display elements may also be used
  here to change how a part name or abbreviation is displayed over the course of
  a piece. They take effect when the current measure or a succeeding measure
  starts a new system.

  Layout group elements in a print element only apply to the current page,
  system, or staff. Music that follows continues to take the default values from
  the layout determined by the defaults element.
  """

  PartAbbreviationDisplay: TYPE[NameDisplay] = None
  PartNameDisplay: TYPE[NameDisplay] = None

  def __init__(
      self,
      blank_page: int = None,
      id: str = None,
      new_page: str | YesNo = None,
      new_system: str | YesNo = None,
      page_number: str = None,
      staff_spacing: float | Tenths = None,
      PageLayout: PageLayout = None,
      SystemLayout: SystemLayout = None,
      MeasureLayout: MeasureLayout = None,
      MeasureNumbering: MeasureNumbering = None,
      PartNameDisplay: PartNameDisplay = None,
      PartAbbreviationDisplay: PartAbbreviationDisplay = None,
  ):
    self.init()


class Rest(MusicElementBase):
  """The rest element indicates notated rests or silences.

  Rest elements are usually empty, but placement on the staff can be specified
  using display-step and display-octave elements. If the measure attribute is
  set to yes, this indicates this is a complete measure rest.
  """

  DisplayOctave = Octave
  DisplayStep = Step

  def __init__(
      self,
      measure: str | YesNo = None,
      DisplayStep: str | DisplayStep = None,
      DisplayOctave: int | DisplayOctave = None,
  ):
    self.init()


class Root(MusicElementBase):
  """The root type indicates a pitch like C, D, E vs.

  a scale degree like 1, 2, 3. It is used with chord symbols in popular music.
  The root element has a root-step and optional root-alter element similar to
  the step and alter elements, but renamed to distinguish the different musical
  meanings.
  """

  RootAlter = HarmonyAlter

  def __init__(self, RootStep: RootStep = None, RootAlter: RootAlter = None):
    self.init()


class Scaling(MusicElementBase):
  """Margins, page sizes, and distances are all measured in tenths to keep MusicXML data in a consistent coordinate system as much as possible.

  The translation to absolute units is done with the scaling type, which
  specifies how many millimeters are equal to how many tenths. For a staff
  height of 7 mm, millimeters would be set to 7 while tenths is set to 40. The
  ability to set a formula rather than a single scaling factor helps avoid
  roundoff errors.
  """

  def __init__(
      self,
      Millimeters: float | Millimeters = None,
      Tenths: float | Tenths = None,
  ):
    self.init()


class Scordatura(MusicElementBase):
  """Scordatura string tunings are represented by a series of accord elements, similar to the staff-tuning elements.

  Strings are numbered from high to low.
  """

  def __init__(self, id: str = None):
    self.init()


class ScoreInstrument(MusicElementBase):
  """The score-instrument type represents a single instrument within a score-part.

  As with the score-part type, each score-instrument has a required ID
  attribute, a name, and an optional abbreviation.

  A score-instrument type is also required if the score specifies MIDI 1.0
  channels, banks, or programs. An initial midi-instrument assignment can also
  be made here. MusicXML software should be able to automatically assign
  reasonable channels and instruments without these elements in simple cases,
  such as where part names match General MIDI instrument names.

  The score-instrument element can also distinguish multiple instruments of the
  same type that are on the same part, such as Clarinet 1 and Clarinet 2
  instruments within a Clarinets 1 and 2 part.
  """

  Ensemble = PositiveIntegerOrEmpty
  Solo = Empty

  class InstrumentAbbreviation(MusicElementBase):
    """The optional instrument-abbreviation element is typically used within a software application, rather than appearing on the printed page of a score."""

    def __init__(self, plain_text: str):
      self.init()

  class InstrumentName(MusicElementBase):
    """The instrument-name element is typically used within a software application, rather than appearing on the printed page of a score."""

    def __init__(self, plain_text: str):
      self.init()

  class InstrumentSound(MusicElementBase):
    """The instrument-sound element describes the default timbre of the score-instrument.

    This description is independent of a particular virtual or MIDI instrument
    specification and allows playback to be shared more easily between
    applications and libraries.
    """

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      id: str,
      InstrumentName: str | InstrumentName = None,
      InstrumentAbbreviation: str | InstrumentAbbreviation = None,
      InstrumentSound: str | InstrumentSound = None,
      Solo: Solo = None,
      Ensemble: str | Ensemble = None,
      VirtualInstrument: VirtualInstrument = None,
  ):
    self.init()


class ScorePart(MusicElementBase):
  """The score-part type collects part-wide information for each part in a score.

  Often, each MusicXML part corresponds to a track in a Standard MIDI Format 1
  file. In this case, the midi-device element is used to make a MIDI device or
  port assignment for the given track or specific MIDI instruments. Initial
  midi-instrument assignments may be made here as well. The score-instrument
  elements are used when there are multiple instruments per track.
  """

  PartAbbreviation = PartName
  PartAbbreviationDisplay: TYPE[NameDisplay] = None
  PartNameDisplay: TYPE[NameDisplay] = None

  class Group(MusicElementBase):
    """The group element allows the use of different versions of the part for different purposes.

    Typical values include score, parts, sound, and data. Ordering information
    can be derived from the ordering within a MusicXML score or opus.
    """

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      id: str,
      Identification: Identification = None,
      PartName: PartName = None,
      PartNameDisplay: PartNameDisplay = None,
      PartAbbreviation: PartAbbreviation = None,
      PartAbbreviationDisplay: PartAbbreviationDisplay = None,
  ):
    self.init()


class Slash(MusicElementBase):
  """The slash type is used to indicate that slash notation is to be used.

  If the slash is on every beat, use-stems is no (the default). To indicate
  rhythms but not pitches, use-stems is set to yes. The type attribute indicates
  whether this is the start or stop of a slash notation style. The use-dots
  attribute works as for the beat-repeat element, and only has effect if
  use-stems is no.
  """

  SlashDot = Empty
  SlashType = NoteTypeValue

  class ExceptVoice(MusicElementBase):
    """The except-voice element is used to specify a combination of slash notation and regular notation.

    Any note elements that are in voices specified by the except-voice elements
    are displayed in normal notation, in addition to the slash notation that is
    always displayed.
    """

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      type: str | StartStop,
      use_dots: str | YesNo = None,
      use_stems: str | YesNo = None,
      SlashType: str | SlashType = None,
  ):
    self.init()


class Sound(MusicElementBase):
  """The sound element contains general playback parameters.

  They can stand alone within a part/measure, or be a component element within a
  direction.

  Tempo is expressed in quarter notes per minute. If 0, the sound-generating
  program should prompt the user at the time of compiling a sound (MIDI) file.

  Dynamics (or MIDI velocity) are expressed as a percentage of the default forte
  value (90 for MIDI 1.0).

  Dacapo indicates to go back to the beginning of the movement. When used it
  always has the value "yes".

  Segno and dalsegno are used for backwards jumps to a segno sign; coda and
  tocoda are used for forward jumps to a coda sign. If there are multiple jumps,
  the value of these parameters can be used to name and distinguish them. If
  segno or coda is used, the divisions attribute can also be used to indicate
  the number of divisions per quarter note. Otherwise sound and MIDI generating
  programs may have to recompute this.

  By default, a dalsegno or dacapo attribute indicates that the jump should
  occur the first time through, while a tocoda attribute indicates the jump
  should occur the second time through. The time that jumps occur can be changed
  by using the time-only attribute.

  The forward-repeat attribute indicates that a forward repeat sign is implied
  but not displayed. It is used for example in two-part forms with repeats, such
  as a minuet and trio where no repeat is displayed at the start of the trio.
  This usually occurs after a barline. When used it always has the value of
  "yes".

  The fine attribute follows the final note or rest in a movement with a da capo
  or dal segno direction. If numeric, the value represents the actual duration
  of the final note or rest, which can be ambiguous in written notation and
  different among parts and voices. The value may also be "yes" to indicate no
  change to the final duration.

  If the sound element applies only particular times through a repeat, the
  time-only attribute indicates which times to apply the sound element.

  Pizzicato in a sound element effects all following notes. Yes indicates
  pizzicato, no indicates arco.

  The pan and elevation attributes are deprecated in Version 2.0. The pan and
  elevation elements in the midi-instrument element should be used instead. The
  meaning of the pan and elevation attributes is the same as for the pan and
  elevation elements. If both are present, the mid-instrument elements take
  priority.

  The damper-pedal, soft-pedal, and sostenuto-pedal attributes effect playback
  of the three common piano pedals and their MIDI controller equivalents. The
  yes value indicates the pedal is depressed; no indicates the pedal is
  released. A numeric value from 0 to 100 may also be used for half pedaling.
  This value is the percentage that the pedal is depressed. A value of 0 is
  equivalent to no, and a value of 100 is equivalent to yes.

  Instrument changes, MIDI devices, MIDI instruments, and playback techniques
  are changed using the instrument-change, midi-device, midi-instrument, and
  play elements. When there are multiple instances of these elements, they
  should be grouped together by instrument using the id attribute values.

  The offset element is used to indicate that the sound takes place offset from
  the current score position. If the sound element is a child of a direction
  element, the sound offset element overrides the direction offset element if
  both elements are present. Note that the offset reflects the intended musical
  position for the change in sound. It should not be used to compensate for
  latency issues in particular hardware configurations.
  """

  def __init__(
      self,
      coda: str = None,
      dacapo: str | YesNo = None,
      dalsegno: str = None,
      damper_pedal: str | YesNoNumber = None,
      divisions: float | Divisions = None,
      dynamics: float | NonNegativeDecimal = None,
      elevation: float | RotationDegrees = None,
      fine: str = None,
      forward_repeat: str | YesNo = None,
      id: str = None,
      pan: float | RotationDegrees = None,
      pizzicato: str | YesNo = None,
      segno: str = None,
      soft_pedal: str | YesNoNumber = None,
      sostenuto_pedal: str | YesNoNumber = None,
      tempo: float | NonNegativeDecimal = None,
      time_only: str | TimeOnly = None,
      tocoda: str = None,
      Swing: Swing = None,
      Offset: Offset = None,
  ):
    self.init()


class StaffDetails(MusicElementBase):
  """The staff-details element is used to indicate different types of staves.

  The optional number attribute specifies the staff number from top to bottom on
  the system, as with clef. The print-object attribute is used to indicate when
  a staff is not printed in a part, usually in large scores where empty parts
  are omitted. It is yes by default. If print-spacing is yes while print-object
  is no, the score is printed in cutaway format where vertical space is left for
  the empty part.
  """

  class Capo(MusicElementBase):
    """The capo element indicates at which fret a capo should be placed on a fretted instrument.

    This changes the open tuning of the strings specified by staff-tuning by the
    specified number of half-steps.
    """

    def __init__(self, plain_text: int):
      self.init()

  class StaffLines(MusicElementBase):
    """The staff-lines element specifies the number of lines and is usually used for a non 5-line staff.

    If the staff-lines element is present, the appearance of each line may be
    individually specified with a line-detail element.
    """

    def __init__(self, plain_text: int):
      self.init()

  def __init__(
      self,
      number: int | StaffNumber = None,
      print_object: str | YesNo = None,
      print_spacing: str | YesNo = None,
      show_frets: str | ShowFrets = None,
      StaffType: str | StaffType = None,
      StaffLines: int | StaffLines = None,
      Capo: int | Capo = None,
      StaffSize: StaffSize = None,
  ):
    self.init()


class StaffLayout(MusicElementBase):
  """Staff layout includes the vertical distance from the bottom line of the previous staff in this system to the top line of the staff specified by the number attribute.

  The optional number attribute refers to staff numbers within the part, from
  top to bottom on the system. A value of 1 is used if not present.

  When used in the defaults element, the values apply to all systems in all
  parts. When used in the print element, the values apply to the current system
  only. This value is ignored for the first staff in a system.
  """

  StaffDistance = Tenths

  def __init__(
      self,
      number: int | StaffNumber = None,
      StaffDistance: float | StaffDistance = None,
  ):
    self.init()


class StaffTuning(MusicElementBase):
  """The staff-tuning type specifies the open, non-capo tuning of the lines on a tablature staff."""

  TuningAlter = Semitones
  TuningOctave = Octave
  TuningStep = Step

  def __init__(
      self,
      line: int | StaffLine,
      TuningStep: str | TuningStep = None,
      TuningAlter: float | TuningAlter = None,
      TuningOctave: int | TuningOctave = None,
  ):
    self.init()


class Stick(MusicElementBase):
  """The stick type represents pictograms where the material of the stick, mallet, or beater is included.The parentheses and dashed-circle attributes indicate the presence of these marks around the round beater part of a pictogram.

  Values for these attributes are "no" if not present.
  """

  def __init__(
      self,
      dashed_circle: str | YesNo = None,
      parentheses: str | YesNo = None,
      tip: str | TipDirection = None,
      StickType: str | StickType = None,
      StickMaterial: str | StickMaterial = None,
  ):
    self.init()


class Swing(MusicElementBase):
  """The swing element specifies whether or not to use swing playback, where consecutive on-beat / off-beat eighth or 16th notes are played with unequal nominal durations.

  The straight element specifies that no swing is present, so consecutive notes
  have equal durations.

  The first and second elements are positive integers that specify the ratio
  between durations of consecutive notes. For example, a first element with a
  value of 2 and a second element with a value of 1 applied to eighth notes
  specifies a quarter note / eighth note tuplet playback, where the first note
  is twice as long as the second note. Ratios should be specified with the
  smallest integers possible. For example, a ratio of 6 to 4 should be specified
  as 3 to 2 instead.

  The optional swing-type element specifies the note type, either eighth or
  16th, to which the ratio is applied. The value is eighth if this element is
  not present.

  The optional swing-style element is a string describing the style of swing
  used.

  The swing element has no effect for playback of grace notes, notes where a
  type element is not present, and notes where the specified duration is
  different than the nominal value associated with the specified type. If a
  swung note has attack and release attributes, those values modify the swung
  playback.
  """

  Straight = Empty
  SwingType = SwingTypeValue

  class First(MusicElementBase):

    def __init__(self, plain_text: int):
      self.init()

  class Second(MusicElementBase):

    def __init__(self, plain_text: int):
      self.init()

  class SwingStyle(MusicElementBase):

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      Straight: Straight = None,
      First: int | First = None,
      Second: int | Second = None,
      SwingType: str | SwingType = None,
      SwingStyle: str | SwingStyle = None,
  ):
    self.init()


class SystemDividers(MusicElementBase):
  """The system-dividers element indicates the presence or absence of system dividers (also known as system separation marks) between systems displayed on the same page.

  Dividers on the left and right side of the page are controlled by the
  left-divider and right-divider elements respectively. The default vertical
  position is half the system-distance value from the top of the system that is
  below the divider. The default horizontal position is the left and right
  system margin, respectively.

  When used in the print element, the system-dividers element affects the
  dividers that would appear between the current system and the previous system.
  """

  LeftDivider = EmptyPrintObjectStyleAlign
  RightDivider = EmptyPrintObjectStyleAlign

  def __init__(
      self, LeftDivider: LeftDivider = None, RightDivider: RightDivider = None
  ):
    self.init()


class SystemLayout(MusicElementBase):
  """A system is a group of staves that are read and played simultaneously.

  System layout includes left and right margins and the vertical distance from
  the previous system. The system distance is measured from the bottom line of
  the previous system to the top line of the current system. It is ignored for
  the first system on a page. The top system distance is measured from the
  page's top margin to the top line of the first system. It is ignored for all
  but the first system on a page.

  Sometimes the sum of measure widths in a system may not equal the system width
  specified by the layout elements due to roundoff or other errors. The behavior
  when reading MusicXML files in these cases is application-dependent. For
  instance, applications may find that the system layout data is more reliable
  than the sum of the measure widths, and adjust the measure widths accordingly.

  When used in the defaults element, the system-layout element defines a default
  appearance for all systems in the score. If no system-layout element is
  present in the defaults element, default system layout values are chosen by
  the application.

  When used in the print element, the system-layout element affects the
  appearance of the current system only. All other systems use the default
  values as determined by the defaults element. If any child elements are
  missing from the system-layout element in a print element, the values
  determined by the defaults element are used there as well. This type of
  system-layout element need only be read from or written to the first visible
  part in the score.
  """

  SystemDistance = Tenths
  TopSystemDistance = Tenths

  def __init__(
      self,
      SystemMargins: SystemMargins = None,
      SystemDistance: float | SystemDistance = None,
      TopSystemDistance: float | TopSystemDistance = None,
      SystemDividers: SystemDividers = None,
  ):
    self.init()


class SystemMargins(MusicElementBase):
  """System margins are relative to the page margins.

  Positive values indent and negative values reduce the margin size.
  """

  LeftMargin = Tenths
  RightMargin = Tenths

  def __init__(
      self,
      LeftMargin: float | LeftMargin = None,
      RightMargin: float | RightMargin = None,
  ):
    self.init()


class Technical(MusicElementBase):
  """Technical indications give performance information for individual instruments."""

  BrassBend = EmptyPlacement
  DoubleTongue = EmptyPlacement
  DownBow = EmptyPlacement
  Fingernails = EmptyPlacement
  Flip = EmptyPlacement
  Golpe = EmptyPlacement
  HalfMuted = EmptyPlacementSmufl
  HammerOn = HammerOnPullOff
  Heel = HeelToe
  Open = EmptyPlacementSmufl
  OpenString = EmptyPlacement
  OtherTechnical = OtherPlacementText
  Pluck = PlacementText
  PullOff = HammerOnPullOff
  Smear = EmptyPlacement
  SnapPizzicato = EmptyPlacement
  Stopped = EmptyPlacementSmufl
  ThumbPosition = EmptyPlacement
  Toe = HeelToe
  TripleTongue = EmptyPlacement
  UpBow = EmptyPlacement

  def __init__(self, id: str = None):
    self.init()


class Time(MusicElementBase):
  """Time signatures are represented by the beats element for the numerator and the beat-type element for the denominator.

  The symbol attribute is used to indicate common and cut time symbols as well
  as a single number display. Multiple pairs of beat and beat-type elements are
  used for composite time signatures with multiple denominators, such as 2/4 +
  3/8. A composite such as 3+2/8 requires only one beat/beat-type pair.

  The print-object attribute allows a time signature to be specified but not
  printed, as is the case for excerpts from the middle of a score. The value is
  "yes" if not present. The optional number attribute refers to staff numbers
  within the part. If absent, the time signature applies to all staves in the
  part.
  """

  class BeatType(MusicElementBase):
    """The beat-type element indicates the beat unit, as found in the denominator of a time signature."""

    def __init__(self, plain_text: str):
      self.init()

  class Beats(MusicElementBase):
    """The beats element indicates the number of beats, as found in the numerator of a time signature."""

    def __init__(self, plain_text: str):
      self.init()

  class SenzaMisura(MusicElementBase):
    """A senza-misura element explicitly indicates that no time signature is present.

    The optional element content indicates the symbol to be used, if any, such
    as an X. The time element's symbol attribute is not used when a senza-misura
    element is present.
    """

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      color: str | Color = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      font_family: str | FontFamily = None,
      font_size: str | FontSize = None,
      font_style: str | FontStyle = None,
      font_weight: str | FontWeight = None,
      halign: str | LeftCenterRight = None,
      id: str = None,
      number: int | StaffNumber = None,
      print_object: str | YesNo = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      separator: str | TimeSeparator = None,
      symbol: str | TimeSymbol = None,
      valign: str | Valign = None,
      Interchangeable: Interchangeable = None,
      SenzaMisura: str | SenzaMisura = None,
  ):
    self.init()


class TimeModification(MusicElementBase):
  """Time modification indicates tuplets, double-note tremolos, and other durational changes.

  A time-modification element shows how the cumulative, sounding effect of
  tuplets and double-note tremolos compare to the written note type represented
  by the type and dot elements. Nested tuplets and other notations that use more
  detailed information need both the time-modification and tuplet elements to be
  represented accurately.
  """

  NormalDot = Empty
  NormalType = NoteTypeValue

  class ActualNotes(MusicElementBase):
    """The actual-notes element describes how many notes are played in the time usually occupied by the number in the normal-notes element."""

    def __init__(self, plain_text: int):
      self.init()

  class NormalNotes(MusicElementBase):
    """The normal-notes element describes how many notes are usually played in the time occupied by the number in the actual-notes element."""

    def __init__(self, plain_text: int):
      self.init()

  def __init__(
      self,
      ActualNotes: int | ActualNotes = None,
      NormalNotes: int | NormalNotes = None,
      NormalType: str | NormalType = None,
  ):
    self.init()


class Transpose(MusicElementBase):
  """The transpose type represents what must be added to a written pitch to get a correct sounding pitch.

  The optional number attribute refers to staff numbers, from top to bottom on
  the system. If absent, the transposition applies to all staves in the part.
  Per-staff transposition is most often used in parts that represent multiple
  instruments.
  """

  Chromatic = Semitones

  class Diatonic(MusicElementBase):
    """The diatonic element specifies the number of pitch steps needed to go from written to sounding pitch.

    This allows for correct spelling of enharmonic transpositions. This value
    does not include octave-change values; the values for both elements need to
    be added to the written pitch to get the correct sounding pitch.
    """

    def __init__(self, plain_text: int):
      self.init()

  class OctaveChange(MusicElementBase):
    """The octave-change element indicates how many octaves to add to get from written pitch to sounding pitch.

    The octave-change element should be included when using transposition
    intervals of an octave or more, and should not be present for intervals of
    less than an octave.
    """

    def __init__(self, plain_text: int):
      self.init()

  def __init__(
      self,
      id: str = None,
      number: int | StaffNumber = None,
      Diatonic: int | Diatonic = None,
      Chromatic: float | Chromatic = None,
      OctaveChange: int | OctaveChange = None,
      Double: Double = None,
  ):
    self.init()


class Tuplet(MusicElementBase):
  """A tuplet element is present when a tuplet is to be displayed graphically, in addition to the sound data provided by the time-modification elements.

  The number attribute is used to distinguish nested tuplets. The bracket
  attribute is used to indicate the presence of a bracket. If unspecified, the
  results are implementation-dependent. The line-shape attribute is used to
  specify whether the bracket is straight or in the older curved or slurred
  style. It is straight by default.

  Whereas a time-modification element shows how the cumulative, sounding effect
  of tuplets and double-note tremolos compare to the written note type, the
  tuplet element describes how this is displayed. The tuplet element also
  provides more detailed representation information than the time-modification
  element, and is needed to represent nested tuplets and other complex tuplets
  accurately.

  The show-number attribute is used to display either the number of actual
  notes, the number of both actual and normal notes, or neither. It is actual by
  default. The show-type attribute is used to display either the actual type,
  both the actual and normal types, or neither. It is none by default.
  """

  TupletActual: TYPE[TupletPortion] = None
  TupletNormal: TYPE[TupletPortion] = None

  def __init__(
      self,
      type: str | StartStop,
      bracket: str | YesNo = None,
      default_x: float | Tenths = None,
      default_y: float | Tenths = None,
      id: str = None,
      line_shape: str | LineShape = None,
      number: int | NumberLevel = None,
      placement: str | AboveBelow = None,
      relative_x: float | Tenths = None,
      relative_y: float | Tenths = None,
      show_number: str | ShowTuplet = None,
      show_type: str | ShowTuplet = None,
      TupletActual: TupletActual = None,
      TupletNormal: TupletNormal = None,
  ):
    self.init()


class TupletPortion(MusicElementBase):
  """The tuplet-portion type provides optional full control over tuplet specifications.

  It allows the number and note type (including dots) to be set for the actual
  and normal portions of a single tuplet. If any of these elements are absent,
  their values are based on the time-modification element.
  """

  def __init__(
      self, TupletNumber: TupletNumber = None, TupletType: TupletType = None
  ):
    self.init()


class Unpitched(MusicElementBase):
  """The unpitched type represents musical elements that are notated on the staff but lack definite pitch, such as unpitched percussion and speaking voice.

  If the child elements are not present, the note is placed on the middle line
  of the staff. This is generally used with a one-line staff. Notes in
  percussion clef should always use an unpitched element rather than a pitch
  element.
  """

  DisplayOctave = Octave
  DisplayStep = Step

  def __init__(
      self,
      DisplayStep: str | DisplayStep = None,
      DisplayOctave: int | DisplayOctave = None,
  ):
    self.init()


class VirtualInstrument(MusicElementBase):
  """The virtual-instrument element defines a specific virtual instrument used for an instrument sound."""

  class VirtualLibrary(MusicElementBase):
    """The virtual-library element indicates the virtual instrument library name."""

    def __init__(self, plain_text: str):
      self.init()

  class VirtualName(MusicElementBase):
    """The virtual-name element indicates the library-specific name for the virtual instrument."""

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      VirtualLibrary: str | VirtualLibrary = None,
      VirtualName: str | VirtualName = None,
  ):
    self.init()


class Work(MusicElementBase):
  """Works are optionally identified by number and title.

  The work type also may indicate a link to the opus document that composes
  multiple scores into a collection.
  """

  class WorkNumber(MusicElementBase):
    """The work-number element specifies the number of a work, such as its opus number."""

    def __init__(self, plain_text: str):
      self.init()

  class WorkTitle(MusicElementBase):
    """The work-title element specifies the title of a work, not including its opus or other work number."""

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      WorkNumber: str | WorkNumber = None,
      WorkTitle: str | WorkTitle = None,
      Opus: Opus = None,
  ):
    self.init()


class MetronomeTuplet(TimeModification):
  """The metronome-tuplet type uses the same element structure as the time-modification element along with some attributes from the tuplet element."""

  def __init__(
      self,
      type: str | StartStop,
      bracket: str | YesNo = None,
      show_number: str | ShowTuplet = None,
      ActualNotes: int | ActualNotes = None,
      NormalNotes: int | NormalNotes = None,
      NormalType: str | NormalType = None,
  ):
    self.init()


class ScorePartwise(MusicElementBase):
  """The score-partwise element is the root element for a partwise MusicXML score.

  It includes a score-header group followed by a series of parts with measures
  inside. The document-attributes attribute group includes the version
  attribute.
  """

  class MovementNumber(MusicElementBase):
    """The movement-number element specifies the number of a movement."""

    def __init__(self, plain_text: str):
      self.init()

  class MovementTitle(MusicElementBase):
    """The movement-title element specifies the title of a movement, not including its number."""

    def __init__(self, plain_text: str):
      self.init()

  class Part(MusicElementBase):

    class Measure(MusicElementBase):

      def __init__(
          self,
          number: str,
          id: str = None,
          implicit: str | YesNo = None,
          non_controlling: str | YesNo = None,
          text: str | MeasureText = None,
          width: float | Tenths = None,
      ):
        self.init()

    def __init__(self, id: str):
      self.init()

  def __init__(
      self,
      version: str = None,
      Work: Work = None,
      MovementNumber: str | MovementNumber = None,
      MovementTitle: str | MovementTitle = None,
      Identification: Identification = None,
      Defaults: Defaults = None,
      PartList: PartList = None,
  ):
    self.init()


class ScoreTimewise(MusicElementBase):
  """The score-timewise element is the root element for a timewise MusicXML score.

  It includes a score-header group followed by a series of measures with parts
  inside. The document-attributes attribute group includes the version
  attribute.
  """

  class Measure(MusicElementBase):

    class Part(MusicElementBase):

      def __init__(self, id: str):
        self.init()

    def __init__(
        self,
        number: str,
        id: str = None,
        implicit: str | YesNo = None,
        non_controlling: str | YesNo = None,
        text: str | MeasureText = None,
        width: float | Tenths = None,
    ):
      self.init()

  class MovementNumber(MusicElementBase):
    """The movement-number element specifies the number of a movement."""

    def __init__(self, plain_text: str):
      self.init()

  class MovementTitle(MusicElementBase):
    """The movement-title element specifies the title of a movement, not including its number."""

    def __init__(self, plain_text: str):
      self.init()

  def __init__(
      self,
      version: str = None,
      Work: Work = None,
      MovementNumber: str | MovementNumber = None,
      MovementTitle: str | MovementTitle = None,
      Identification: Identification = None,
      Defaults: Defaults = None,
      PartList: PartList = None,
  ):
    self.init()


PartGroup.GroupAbbreviationDisplay = NameDisplay
PartGroup.GroupNameDisplay = NameDisplay
Print.PartAbbreviationDisplay = NameDisplay
Print.PartNameDisplay = NameDisplay
ScorePart.PartAbbreviationDisplay = NameDisplay
ScorePart.PartNameDisplay = NameDisplay
Tuplet.TupletActual = TupletPortion
Tuplet.TupletNormal = TupletPortion

__all__ = [
    name
    for name in globals()
    if not name.startswith('_')
    and not name in ('TYPE', 'annotations', 'MusicElementBase')
]
__all__.append('_')