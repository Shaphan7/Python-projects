# Python-projects
Projects built while learning Python, progressing from fundamentals toward Data Science, Machine Learning, and AI.
## Roadmap Projects
Sequential projects following a structured curriculum, each introducing new concepts.
| # | Project | Concepts |
|---|---------|----------|
| 01 | [Stats Calculator](roadmap-projects/01-stats-calculator) | Functions, lists, loops |
| 02 | [CSV Parser & Sorter](roadmap-projects/02-csv-parser-sorter) | File I/O, dictionaries, sorting |
| 03 | [GradeBook Stats Calculator](roadmap-projects/03-gradebook-stats-calculator) | Data analysis |
| 04 | [CSV Parser & Analyzer](roadmap-projects/04-csv-parser-analyzer-class-based) | Classes, `zip()`, OOP basics |
| 05 | [Inventory Management System](roadmap-projects/05-inventory-management-system) | OOP practice |
| 06 | [Analyzer (Inheritance)](roadmap-projects/06-analyzer-inheritance) | Inheritance |
| 07 | [Bank Management System](roadmap-projects/07-bank-management-system) | Composition, JSON |
| 08 | [Movie Database](roadmap-projects/08-movie-database) | Multi-file OOP, `getattr`, filtering |
| 09 | [Task Manager CLI](roadmap-projects/09-task-manager-cli) | `datetime`, JSON persistence, CLI design |
| 10 | [Library Management System](roadmap-projects/10-library-management-system) | Multi-file OOP, object relationships, `hashlib`/`hmac`/`secrets`, `datetime` cooldowns, JSON persistence |
| 11 | [Quiz Engine](roadmap-projects/11-quiz-engine) | JSON-driven content, `random` (shuffling), custom exceptions with `raise`/`try`/`except` for control flow, dispatch dicts |
| 12 | [Store Management System](roadmap-projects/12-store-management-system) | Multi-file object isolation, data cross-referencing (Sales ↔ Inventory ↔ Salesmen), one-pass hashmap-style aggregation (daily/monthly revenue), real-time stock/revenue metrics, multi-database JSON serialization |
| 13 | [ByteBudget – Expense Tracker](roadmap-projects/13-bytebudget-expense-tracker) | Multi-file app/CLI separation, `datetime` arithmetic for recurring monthly resets (month/year rollover handling), unique ID generation (`uuid`) for safe record deletion, reusable single-category aggregation helper, JSON-based settings/limits persistence, date-filtered data export |
## Own Ideas
Self-directed bonus projects.
- [Collatz Conjecture](own-ideas/collatz-conjecture)
- [Data Encrypter](own-ideas/data-encrypter) — Fernet encryption, HMAC
- [File Organizer](own-ideas/file-organizer) — built into a `.exe` with PyInstaller
- [Mini CLI Tool](own-ideas/mini-cli-tool)
- [Password Generator](own-ideas/password-generator)
- [Weather App](own-ideas/weather-app) — OpenWeatherMap API
- [MP3 Player / Converter](own-ideas/mp3-player-converter) — `pygame` audio playback, `ffmpeg` MP4→MP3 conversion via `subprocess`
## Library Projects
Self-directed projects focused on NumPy, Pandas, Matplotlib, and other data-science tooling.
- **[Stock Market Simulator & Portfolio Analyzer](library-projects/stocks-market-simulator)** — *first NumPy project.* Vectorized synthetic price generation (random walk, per-stock volatility), `axis`-based statistics (mean/min/max/argmin/argmax), daily % returns via `np.diff`, volatility via `np.std`, buy/sell portfolio tracking, CLI with input validation and dispatch dict
- **[Student Grade Analyzer](library-projects/student-grade-analyzer)** — *first Pandas project.* DataFrame indexing (`loc`/`iloc`), boolean masking across multiple columns (`.any(axis=1)`), cross-column aggregation (`.sum()`, `.mean()`, `.describe()`), `idxmax`/`idxmin` for row-level lookups, real-world data cleaning (`.replace()`, `.dropna()`, `pd.to_numeric(errors="coerce")`, `.mask()`, `.str` accessor chains, `.duplicated()`), CSV I/O (`read_csv`/`to_csv`)
## Algorithms
Algorithm practice, built from scratch without reference code.
- [Merge Sort](algorithms/merge-sort) — `merge()` written and debugged independently
## Practice
- [Syntax Improvement Practice](syntax-improvement-practice) — intermediate Python syntax drills
## Disclaimer
- AI (ChatGPT / Claude / Gemini) was used for guided debugging, concept explanations, and structuring the project roadmap.
- All code in the roadmap projects was written by me — AI did not write code directly, only explained concepts and pointed out bugs for me to fix myself.
- The "Own Ideas" and "Algorithms" projects were inspired by concepts I came across online (YouTube, Discord, etc.).
- In some cases I saw existing code at the time, but I never had it open or referenced it while building — by the time I wrote each project, it was entirely from memory and my own understanding, not a copy or adaptation.
- (and yes, AI did write this disclaimer)
