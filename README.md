# Snow Access Suite

A Streamlit app shell that aggregates three dashboards — User Dashboard, Role Dashboard, and Role Metrics — into a single, tabbed interface.

## Quick Start

1. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`.

## Project Structure (Relevant Parts)

```
Projects/
  rbac_view/
    app.py                 # Streamlit entrypoint (shell)
    requirements.txt       # Dependencies for shell and modules
    docs/
      snow_access_suite/
        README.md
        requirements.md
        architecture.md
```

## How It Works
- `app.py` sets the page config, defines three tabs, and calls the imported dashboard functions:
  - `show_user_dashboard()` from `snow_user_dashboard`
  - `show_role_dashboard()` from `snow_role_dashboard`
  - `show_role_metrics_dashboard()` from `snow_role_metrics`
- Simple CSS is injected to style the tabs.

## Requirements
See `docs/snow_access_suite/requirements.md`.

## Architecture
See `docs/snow_access_suite/architecture.md`.

## Troubleshooting
- ImportError: Ensure the dashboard modules (`snow_user_dashboard`, `snow_role_dashboard`, `snow_role_metrics`) are installed or available on `PYTHONPATH`.
- Missing packages: Verify `pip install -r requirements.txt` ran successfully.
- Port in use: Run with `streamlit run app.py --server.port 8502` or free the port 8501.
- Browser not opening: Manually navigate to `http://localhost:8501`.

## License
Internal / proprietary. Add your organization’s license policy here. 