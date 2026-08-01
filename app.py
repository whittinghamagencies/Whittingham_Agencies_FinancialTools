"""
Internal Financial Tools — The Whittingham Agencies
Streamlit wrapper around the self-contained HTML calculators in this repo.

Each tool (Agent Pay Calculator, MRO Worksheet, Team Submit Pay Calculator)
is a standalone, client-side HTML page. Rather than reimplement the pay logic,
this app embeds each page as-is so all existing calculations stay identical,
and replaces the tools' cross-page links with a Streamlit sidebar for navigation.

Run with:
    pip install -r requirements.txt
    streamlit run app.py
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

APP_DIR = Path(__file__).parent

# Tool label -> HTML file. Order defines the sidebar order.
TOOLS = {
    "Home": "index.html",
    "Agent Pay Calculator": "agent-pay.html",
    "MRO Worksheet": "mro-worksheet.html",
    "Team Submit Pay Calculator": "team-submit.html",
}

# The HTML tools render their own tall, scrolling layouts; give the embedded
# iframe generous height so the full page is usable inside Streamlit.
EMBED_HEIGHT = 2600

st.set_page_config(
    page_title="Internal Financial Tools | The Whittingham Agencies",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data(show_spinner=False)
def load_html(filename: str) -> str:
    """Read a tool's HTML file from disk. Cached so re-renders are cheap."""
    return (APP_DIR / filename).read_text(encoding="utf-8")


def main() -> None:
    st.sidebar.title("Whittingham Agencies")
    st.sidebar.caption("Internal Financial Tools")

    choice = st.sidebar.radio("Select a tool", list(TOOLS.keys()), index=0)

    st.sidebar.markdown("---")
    st.sidebar.caption(
        "Each tool runs entirely in your browser — nothing is sent to a server. "
        "Use the selector above to switch tools instead of the in-page links."
    )

    filename = TOOLS[choice]
    html_path = APP_DIR / filename

    if not html_path.exists():
        st.error(f"Could not find `{filename}` next to app.py.")
        st.stop()

    components.html(load_html(filename), height=EMBED_HEIGHT, scrolling=True)


if __name__ == "__main__":
    main()
