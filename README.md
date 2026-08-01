# Whittingham Agencies — Internal Financial Tools

A small [Streamlit](https://streamlit.io) app that bundles the agency's
internal financial calculators behind a single navigable interface.

## Tools

| Tool | File | Purpose |
|------|------|---------|
| Home | `index.html` | Landing page / directory |
| Agent Pay Calculator | `agent-pay.html` | Calculate individual agent pay |
| MRO Worksheet | `mro-worksheet.html` | MRO worksheet + PDF export |
| Team Submit Pay Calculator | `team-submit.html` | Team submission pay calculations |

Each tool is a self-contained, client-side HTML page (all logic runs in the
browser, nothing is sent to a server). `app.py` embeds each page unchanged, so
the pay calculations are identical to the standalone files — the Streamlit layer
only adds a sidebar for switching between tools.

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the Local URL Streamlit prints (default http://localhost:8501) and
pick a tool from the sidebar.

## Notes

- The original HTML files remain fully usable on their own — open any of them
  directly in a browser.
- If you add or rename a tool, update the `TOOLS` mapping at the top of `app.py`.
