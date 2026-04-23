# Tweet Analysis GUI

A simple Python application to collect Indonesian tweets with Tweepy, store them in SQLite, run lexicon-based sentiment scoring, and view results through either a CLI or Tkinter GUI.

## Features

- Fetch tweets from Twitter/X using Tweepy (`twitter.py`)
- Save tweet data into a local SQLite database (`tweet.db`)
- Compute sentiment scores using positive/negative word lists
- View tweet records filtered by date range
- Visualize sentiment distribution with a bar chart
- Show summary statistics (mean, median, standard deviation)
- Two interfaces:
  - Command-line interface (CLI)
  - Desktop graphical interface (GUI via Tkinter)

## Project Structure

- `/home/runner/work/Tweet_AnalysisGUI/Tweet_AnalysisGUI/app.py` – application entry point (choose CLI or GUI)
- `/home/runner/work/Tweet_AnalysisGUI/Tweet_AnalysisGUI/cli.py` – CLI flow/menu
- `/home/runner/work/Tweet_AnalysisGUI/Tweet_AnalysisGUI/gui.py` – Tkinter GUI flow
- `/home/runner/work/Tweet_AnalysisGUI/Tweet_AnalysisGUI/twitter.py` – tweet retrieval and preprocessing
- `/home/runner/work/Tweet_AnalysisGUI/Tweet_AnalysisGUI/connection.py` – SQLite CRUD helpers
- `/home/runner/work/Tweet_AnalysisGUI/Tweet_AnalysisGUI/analysis.py` – lexicon-based sentiment logic
- `/home/runner/work/Tweet_AnalysisGUI/Tweet_AnalysisGUI/plot.py` – chart generation with Matplotlib
- `/home/runner/work/Tweet_AnalysisGUI/Tweet_AnalysisGUI/kata_positif.txt` – positive words lexicon
- `/home/runner/work/Tweet_AnalysisGUI/Tweet_AnalysisGUI/kata_negatif.txt` – negative words lexicon
- `/home/runner/work/Tweet_AnalysisGUI/Tweet_AnalysisGUI/tweet.db` – SQLite database

## Requirements

- Python 3.8+
- Internet access for tweet retrieval
- Python packages:
  - `tweepy`
  - `pandas`
  - `numpy`
  - `matplotlib`
- Tkinter (usually bundled with standard Python installations)

## Installation

1. Open terminal in the repository:
   ```bash
   cd /home/runner/work/Tweet_AnalysisGUI/Tweet_AnalysisGUI
   ```
2. (Recommended) create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install tweepy pandas numpy matplotlib
   ```

## Twitter API Configuration

Before running the app, add your credentials in:

- `/home/runner/work/Tweet_AnalysisGUI/Tweet_AnalysisGUI/twitter.py`

Set these variables in `getTweet()`:

- `key`
- `secretKey`
- `token`
- `tokenSecret`

Without valid credentials, tweet retrieval will fail.

## Running the Application

From repository root:

```bash
python app.py
```

You will be prompted:

- `cli` → run command-line mode
- `gui` → open Tkinter desktop app

## Usage Workflow

### 1) Update Data
Fetches recent tweets (query currently fixed to `vaksin covid`) and stores new records into `tweet.db`.

### 2) Update Nilai Sentiment
Calculates sentiment scores for tweets where `sentimen IS NULL`.

Scoring approach:

- `sentiment = (count of matched positive words) - (count of matched negative words)`

### 3) Lihat Data
Shows tweets between two dates (`yyyy-mm-dd`).

### 4) Visualisasi
Builds a sentiment-frequency bar chart and displays:

- Mean sentiment
- Median sentiment
- Standard deviation

## Database

The app uses SQLite with table `data`:

- `tweet_id` (PRIMARY KEY)
- `screen_name`
- `tweet_text`
- `tanggal`
- `sentimen` (nullable until analyzed)

## Text Preprocessing

Tweets are normalized by:

- removing mentions (`@user`)
- removing URLs
- removing non-alphanumeric symbols
- converting to lowercase

## Troubleshooting

- **`No module named tweepy` (or others):** install dependencies with `pip install ...`
- **No tweets fetched:** verify API credentials and network connectivity
- **GUI does not open:** ensure Tkinter is available in your Python installation
- **Sentiment values not changing:** run "Update Nilai Sentiment" after fetching new data
- **Database appears stale:** ensure you are running from repository root so `tweet.db` and lexicon files resolve correctly

## Known Limitations

- Sentiment analysis is simple lexicon matching (no context/negation handling)
- Search keyword and language are hardcoded in `twitter.py`
- Date filtering uses direct SQL string formatting
- Credentials are currently read from source code variables

## Notes for Improvement

- Move API credentials to environment variables
- Add configurable search query/date range
- Add automated tests and dependency file (`requirements.txt`)
- Improve sentiment model (stemming, negation, weighting)
- Parameterize database path and add migration/init scripts
