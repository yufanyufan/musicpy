import streamlit as st
from code_editor import code_editor

import verovio
import os
import textwrap

st.set_page_config(page_title="MusicPy", page_icon="💡", layout="wide")


preemple = """
from musicxml_schema import *
from musicxml import _, MusicXML
with MusicXML() as __score:
"""

musicpy = code_editor(
    "",
    lang="python",
    height=[20, 20],
    options={"wrap": True},
    focus=True,
    response_mode="blur",
)["text"]

if "svg" not in st.session_state:
  st.session_state.svg = None
if "xml" not in st.session_state:
  st.session_state.xml = None

if st.button("Render", icon=":material/save:", type="primary"):
  result = {}
  exec(preemple + textwrap.indent(musicpy, "  "), {}, result)
  print("exec result", result)
  st.session_state.xml = str(result["__score"].get_xml())
  toolkit = verovio.toolkit()
  toolkit.setResourcePath(os.path.join(os.path.dirname(verovio.__file__),"data"));
  toolkit.setInputFrom("musicxml")
  xml_data = toolkit.loadData(st.session_state.xml)
  page_count = toolkit.getPageCount()
  st.session_state.svg = []
  for i in range(page_count):
    st.session_state.svg.append(toolkit.renderToSVG(i + 1))
  st.rerun()

if st.session_state.xml:
  with st.expander("MusicXML"):
    st.code(st.session_state.xml)

if st.session_state.svg:
  if len(st.session_state.svg) > 1:
    tabs = st.tabs([ f"Page {i + 1}" for i in range(len(st.session_state.svg))])
    for i, svg in enumerate(st.session_state.svg):
      with tabs[i]:
        st.image(svg)
  else:
    st.image(st.session_state.svg[0])
