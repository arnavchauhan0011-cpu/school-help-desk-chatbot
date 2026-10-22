# School Help Desk Chatbot (Bilingual Streamlit Starter)

This is a beginner-friendly Streamlit starter for an English/Hindi school help desk chatbot.

## Files
- `app.py` — chatbot interface and FAQ matching
- `requirements.txt` — Python dependency for deployment

## Run locally
1. Install Python 3.10 or newer.
2. In this folder, run:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

## Deploy using GitHub + Streamlit Community Cloud
1. Create a GitHub account and a new repository.
2. Upload `app.py`, `requirements.txt`, and this README.
3. Open https://share.streamlit.io/ and connect GitHub.
4. Choose your repository and set the main file path to `app.py`.
5. Click Deploy.

## Important notes
- This is a keyword-based FAQ demo, not a generative AI chatbot.
- The current-year exam datesheet/planner has intentionally not been hard-coded because the complete verified source was not available in this file package. Add the official school planner only after checking the dates and class/section.
- Verify school policies, timings, fees and transport information with the school.
- Do not collect student IDs, passwords, personal contact details or other sensitive information.
