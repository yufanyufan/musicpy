import os
import textwrap

import requests
import streamlit as st
import verovio
import logging
import musicpy_ast


st.set_page_config(page_title="Open Music Sheet", page_icon="🎼", layout="wide")

logging.basicConfig(
    level=logging.INFO,  # Set the desired default logging level
    format=(
        "%(levelname)s - [%(filename)s:%(lineno)d] - %(funcName)s() -"
        " %(message)s"
    ),
)

def rate_limit():
  url = "https://api.github.com/rate_limit"
  headers={"Authorization": "cdscc"}
  response = requests.get(
      url, headers
  )
  st.code(response.json())

@st.cache_data
def list_sheet(dir=""):
  url = (
      "https://api.github.com/repos/yufanyufan/open_music_sheet/contents" + dir
  )
  headers={"Authorization": st.secrets["github_key"]}
  response = requests.get(
      url, headers=headers
  )
  logging.info(response)
  response.raise_for_status()  # Raise an exception for bad status codes
  data = response.json()
  return [
      item["name"] + "/" if item["type"] == "dir" else item["name"]
      for item in data
      if item["name"].endswith(".py") or item["type"] == "dir"
  ]


st.markdown("Choose a file")

cols = iter(st.columns([1, 1, 1, 1, 1]))


def render_path_chooser(path: str) -> str:
  with next(cols):
    sheet_list = list_sheet(path)
    if sheet_list:
      choosen = st.selectbox(
          "Select a File",
          index=None,
          options=sheet_list,
          key=path,
          label_visibility="collapsed",
      )
      if choosen:
        if choosen.endswith("/"):
          return render_path_chooser(path + choosen)
        else:
          return path + choosen
      return path
    else:
      st.warning("Failed to load composer list.")


@st.cache_data
def get_music_sheet(path: str) -> str:
  url = (
      "https://raw.githubusercontent.com/yufanyufan/open_music_sheet/main/"
      + path
  )
  response = requests.get(url)
  response.raise_for_status()  # Raise an exception for bad status codes
  return response.text


def render_music_sheet(path: str) -> str:
  st.session_state.svg = []
  st.session_state.path = path
  music_sheet = get_music_sheet(path)
  try:
    xml = musicpy_ast.safe_exec_musicpy(music_sheet)
  except Exception as e:
    st.error(e)
    return
  toolkit = verovio.toolkit()
  toolkit.setResourcePath(
      os.path.join(os.path.dirname(verovio.__file__), "data")
  )
  toolkit.setInputFrom("musicxml")
  toolkit.loadData(xml)
  page_count = toolkit.getPageCount()
  for i in range(page_count):
    st.session_state.svg.append(toolkit.renderToSVG(i + 1))

path = render_path_chooser("/")
if path.endswith("/"):
  with next(cols):
    st.markdown(
        "[Add new on Github]"
        f"(https://github.com/yufanyufan/open_music_sheet/new/main/{path})"
    )

if path and path.endswith(".py"):
  with next(cols):
    st.markdown(
        "[Modify it on Github]"
        f"(https://github.com/yufanyufan/open_music_sheet/edit/main/{path})"
    )

if path and path.endswith(".py"):
  if "path" not in st.session_state:
    st.session_state.path = None
  if "svg" not in st.session_state:
    st.session_state.svg = None

  if st.session_state.path != path:
    render_music_sheet(path)

  if st.session_state.svg:
    if len(st.session_state.svg) > 1:
      tabs = st.tabs(
          [f"Page {i + 1}" for i in range(len(st.session_state.svg))]
      )
      for i, svg in enumerate(st.session_state.svg):
        with tabs[i]:
          st.image(svg)
    else:
      st.image(st.session_state.svg[0])
