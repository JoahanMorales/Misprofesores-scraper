# MisProfesores Scraper

This project allows you to extract teacher ratings from the IPN (UPIICSA, ESCOM, etc.) from [MisProfesores](https://www.misprofesores.com/), save the data in JSON files, and perform flexible searches by teacher name.

---

## Repository Structure

- `App.py` → Main code for general teacher searches.
- `Obtener_html.py` → Saves the full HTML of the school's page locally.
- `Obtener_todo.py` → Extracts the `dataSet` variable from the page and saves it as a JSON file.
- `RequestJson.py` → Reads the saved JSON and allows flexible teacher searches.
- `dataset_upiicsa.json` and `dataset_escom.json` → Example JSON files with teacher data.
- `pagina.html` → Example HTML file saved by `Obtener_html.py`.
- `requirements.txt` → Python dependencies.

---

## Requirements

- Python 3.12 or higher.
- Google Chrome (updated version).
- Python packages:
```bash
pip install selenium webdriver-manager beautifulsoup4
