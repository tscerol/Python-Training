# Python-Training
This is a repo to help track my Python progressing using an AI assisted syllabus

**Setup (week 0):** install Python 3.13 or newer from python.org, VS Code with the Python extension, Git, and create a GitHub account.

| Phase | Weeks | Focus | Portfolio project |
| --- | --- | --- | --- |
| 1. Foundations | 1–6 | Syntax, control flow, functions | Text adventure game + CLI tools |
| 2. Core Python | 7–12 | Data structures, files, errors, modules | Personal finance tracker (CSV/JSON) |
| 3. OOP and idiomatic Python | 13–18 | Classes, dunder methods, iterators, decorators | Library management system |
| 4. Professional tooling | 19–24 | Git, venvs, testing, typing, packaging | Publish a CLI package to PyPI |
| 5. The outside world | 25–32 | HTTP, APIs, SQL, async, scraping | Weather/price-alert service with a database |
| 6. Specialization | 33–44 | Web, data, automation, or ML track | One deployed track project |
| 7. Advanced Python | 45–50 | Internals, performance, concurrency | Rate limiter or task-queue library |
| 8. Capstone and career | 51–60 | Full production app, job search | Deployed full-stack capstone |

## Phase 1 – Foundations (weeks 1–6)

Goal: write small programs from scratch and read error messages without panic.

| Week | Topics | Practice |
| --- | --- | --- |
| 1 | How Python runs, the REPL, `print`, variables, `int`/`float`/`str`/`bool`, arithmetic, `input()` | Tip calculator, temperature converter |
| 2 | String methods, f-strings, slicing, type conversion, comments | Mad Libs generator, name formatter |
| 3 | Comparisons, `if`/`elif`/`else`, boolean logic, `match` statements | Grade calculator, rock-paper-scissors |
| 4 | `while` and `for` loops, `range`, `break`/`continue`, nested loops | Number-guessing game, multiplication table |
| 5 | Functions, parameters, return values, default and keyword args, scope | Refactor weeks 1–4 into functions |
| 6 | Lists and dicts (intro), the `random` and `math` modules, reading tracebacks | Phase project |

**Checkpoint:** you can solve FizzBuzz, reverse a string, count vowels and find the largest number in a list without looking anything up.

### Project 1: Text adventure game

A terminal game with at least 5 rooms, an inventory, and win/lose conditions.

- Rooms stored as a dictionary; movement with commands like `go north`
- Input validation: unknown commands get a helpful message, never a crash
- Every action handled by its own function
- Stretch: a save/load feature, a random event system

**Demonstrates:** control flow, functions, dictionaries, user input handling, program structure.

## Phase 2 – Core Python (weeks 7–12)

Goal: choose the right data structure, work with files, and handle failure gracefully.

| Week | Topics | Practice |
| --- | --- | --- |
| 7 | Lists in depth, tuples, sets, mutability, copying vs referencing | Remove duplicates, set operations on two guest lists |
| 8 | Dictionaries in depth, nested structures, `collections` (`Counter`, `defaultdict`, `namedtuple`) | Word-frequency counter on a book from Project Gutenberg |
| 9 | List/dict/set comprehensions, `enumerate`, `zip`, `sorted` with `key`, `lambda` | Rewrite earlier loops as comprehensions |
| 10 | File I/O, `with` statements, `pathlib`, CSV and JSON | Contact book saved to JSON |
| 11 | Exceptions: `try`/`except`/`else`/`finally`, raising, custom exceptions | Make the contact book crash-proof |
| 12 | Modules and packages, `import` mechanics, `if __name__ == "__main__"`, the standard library tour (`datetime`, `os`, `sys`, `argparse`) | Phase project |

**Checkpoint:** you can explain when to use a list vs a tuple vs a set vs a dict, and why `def f(x=[])` is a bug.

### Project 2: Personal finance tracker (CLI)

A command-line app that records income and expenses and reports on them.

- Commands via `argparse`: `add`, `list`, `report --month 2026-11`, `delete`
- Data persisted to CSV or JSON; imports a bank-export CSV
- Reports: totals by category, monthly balance, top 5 expenses
- Bad input (wrong dates, negative amounts, missing file) handled with clear messages
- Code split across at least 3 modules

**Demonstrates:** data structures, file I/O, error handling, modular design, a real CLI interface.

## Phase 3 – Object-oriented and idiomatic Python (weeks 13–18)

Goal: model real problems with classes and write code that reads like Python, not translated Java.

| Week | Topics | Practice |
| --- | --- | --- |
| 13 | Classes, `__init__`, instance vs class attributes, methods, `self` | Bank account class with deposit/withdraw |
| 14 | Inheritance, `super()`, composition over inheritance, abstract base classes | Shape hierarchy with area/perimeter |
| 15 | Dunder methods (`__repr__`, `__eq__`, `__lt__`, `__len__`, `__iter__`), `@property`, `@classmethod`, `@staticmethod` | A `Vector` class that supports `+`, `==`, `len()` |
| 16 | `dataclasses`, `enum`, iterators and generators, `yield` | Generator that streams a large log file line by line |
| 17 | Decorators, closures, first-class functions, `functools` | `@timer` and `@retry` decorators |
| 18 | Context managers, PEP 8, the Zen of Python, EAFP vs LBYL | Phase project |

**Checkpoint:** you can write a decorator from memory and explain the difference between an iterable, an iterator and a generator.

### Project 3: Library management system

A CLI (or simple Tkinter GUI) system for a small library.

- Classes: `Book`, `Member`, `Loan`, `Library` with clear responsibilities
- Borrow, return, reserve, overdue fines, search by title/author/ISBN
- Uses dataclasses, enums for status, at least one custom exception and one decorator
- State saved to JSON, with a generator to page through large catalogs
- A short design note in the README with a class diagram

**Demonstrates:** OOP design, encapsulation, idiomatic Python, separating logic from interface.

## Phase 4 – Professional tooling (weeks 19–24)

Goal: work the way professional Python teams work. This phase separates hobbyists from hireable developers.

| Week | Topics | Practice |
| --- | --- | --- |
| 19 | Git in depth: branches, merges, rebasing, pull requests, `.gitignore`, good commit messages | Work on Projects 1–3 via feature branches and PRs |
| 20 | Virtual environments, `pip`, `uv`, `pyproject.toml`, dependency pinning | Convert Project 2 to a `uv`-managed project |
| 21 | Testing with `pytest`: fixtures, parametrize, mocking, coverage | Reach 80%+ test coverage on Project 2 |
| 22 | Type hints, `mypy`/`pyright`, generics, `Protocol`, `TypedDict` | Fully type-check Project 3 |
| 23 | Linting and formatting with `ruff`, pre-commit hooks, `logging` instead of `print`, debugging with `pdb` and the VS Code debugger | Add pre-commit to every repo |
| 24 | GitHub Actions CI, packaging, semantic versioning, docs (docstrings, MkDocs) | Phase project |

**Checkpoint:** every push to your repos runs linting, type checks and tests automatically.

### Project 4: Publish a CLI tool to PyPI

Build and publish a useful command-line utility, e.g. a bulk file renamer, a Markdown-to-HTML converter, or a dotfiles manager.

- Installable with `pip install your-tool`
- CLI built with `typer` or `click`, with `--help` text for every command
- Full type hints, 90%+ test coverage, `ruff` clean
- GitHub Actions: test on Python 3.11–3.13 across Linux, macOS and Windows; auto-publish on tagged release
- README with badges, install instructions, usage GIF, and a CHANGELOG

**Demonstrates:** packaging, testing, CI/CD, typing, documentation — the full professional workflow.

## Phase 5 – Working with the outside world (weeks 25–32)

Goal: connect Python to the internet, databases and other programs.

| Week | Topics | Practice |
| --- | --- | --- |
| 25 | HTTP basics, REST, status codes, `requests`/`httpx`, authentication (API keys, OAuth) | Pull data from a public API (GitHub, OpenWeather) |
| 26 | Web scraping with `BeautifulSoup`, `robots.txt`, rate limiting, Playwright for JS pages | Scrape book prices from books.toscrape.com |
| 27 | SQL fundamentals: SELECT, JOIN, GROUP BY, indexes; `sqlite3` | Move Project 2's data into SQLite |
| 28 | ORMs with SQLAlchemy 2.0, migrations with Alembic, PostgreSQL | Rebuild the Project 3 storage layer on SQLAlchemy |
| 29 | Data validation with Pydantic, environment variables and secrets, config management | Validate all API responses with Pydantic models |
| 30 | Concurrency: threads vs processes vs async, `asyncio`, `httpx.AsyncClient` | Fetch 100 URLs sync vs async and time both |
| 31 | Scheduling (`APScheduler`, cron), sending email/Slack/Discord notifications | Daily summary sent to yourself |
| 32 | Docker basics: Dockerfile, images, `docker compose` | Phase project |

**Checkpoint:** you can explain when async helps (I/O-bound) and when it doesn't (CPU-bound).

### Project 5: Price or weather alert service

A background service that watches data sources and notifies you when something changes.

- Tracks product prices (scraped) or weather/stock data (API) on a schedule
- Stores history in PostgreSQL via SQLAlchemy, with Alembic migrations
- Fetches concurrently with `asyncio`; retries with backoff on failures
- Sends alerts by email or Discord when a threshold is crossed
- Configured via `.env`; runs with one `docker compose up`

**Demonstrates:** APIs, scraping, SQL, async, configuration, containerization.

## Phase 6 – Specialization (weeks 33–44)

Goal: go deep in one area employers hire for. Pick ONE track based on the jobs you want; read 20 job postings first and note the tools they repeat.

### Track A: Backend web development

- Weeks 33–36: FastAPI (routing, dependency injection, Pydantic schemas), REST design, OpenAPI docs
- Weeks 37–39: Django (models, admin, ORM, auth, Django REST Framework)
- Weeks 40–42: JWT auth, password hashing, CORS, caching with Redis, background jobs with Celery
- Weeks 43–44: Deployment (Render, Fly.io or AWS), Nginx, HTTPS, monitoring

**Project 6A – Task management API:** a multi-user FastAPI service with JWT auth, teams, projects, tasks and comments; PostgreSQL, Redis caching, Celery email reminders, full test suite, deployed with a public OpenAPI docs page.

### Track B: Data analysis and engineering

- Weeks 33–36: NumPy, pandas (cleaning, grouping, merging, time series), Jupyter
- Weeks 37–39: Visualization with Matplotlib, Seaborn, Plotly; statistics basics
- Weeks 40–42: Polars, DuckDB, ETL pipelines, Airflow or Prefect
- Weeks 43–44: Dashboards with Streamlit, communicating findings

**Project 6B – End-to-end data pipeline:** ingest a public dataset daily (e.g. city 311 calls, transit data), clean and load it into DuckDB/PostgreSQL with Prefect, and publish a Streamlit dashboard with a written analysis of three findings.

### Track C: Automation and DevOps

- Weeks 33–36: `subprocess`, `shutil`, Paramiko/Fabric for SSH, system scripting
- Weeks 37–39: Cloud SDKs (`boto3` for AWS), infrastructure as code (Pulumi in Python)
- Weeks 40–42: Kubernetes basics, writing CLI tooling for ops teams
- Weeks 43–44: Observability: structured logging, Prometheus metrics

**Project 6C – Infrastructure toolkit:** a CLI that provisions an AWS environment with Pulumi, deploys your Project 5 container, backs up its database to S3 on a schedule, and reports cost and health to Slack.

### Track D: Machine learning and AI

- Weeks 33–36: NumPy, pandas, linear algebra and statistics refresh, scikit-learn
- Weeks 37–39: Model evaluation, feature engineering, cross-validation
- Weeks 40–42: PyTorch fundamentals, neural networks, Hugging Face
- Weeks 43–44: LLM apps: calling model APIs, embeddings, retrieval-augmented generation, evaluation

**Project 6D – Document Q&A app:** a RAG app that answers questions about a document collection, with an embedding index, an evaluation set measuring answer accuracy, a FastAPI backend and a simple web UI.

**Demonstrates:** depth in a hireable specialty, plus deployment of a real system.

## Phase 7 – Advanced Python (weeks 45–50)

Goal: understand how Python works under the hood, so you can debug the hard problems and make code fast.

| Week | Topics | Practice |
| --- | --- | --- |
| 45 | The data model in depth, descriptors, `__slots__`, metaclasses and `__init_subclass__` | Build a tiny ORM-style field validator with descriptors |
| 46 | CPython internals: bytecode (`dis`), reference counting, garbage collection, the GIL and free-threaded builds | Disassemble and compare two implementations |
| 47 | Profiling (`cProfile`, `py-spy`, `line_profiler`), memory profiling, algorithmic complexity | Profile and speed up your slowest project by 5x |
| 48 | Advanced concurrency: `asyncio` internals, task groups, `concurrent.futures`, multiprocessing, queues | Async web crawler with a concurrency limit |
| 49 | Speeding up Python: vectorization, Cython, Numba, Rust extensions via PyO3 (overview) | Rewrite one hot loop with Numba or Cython |
| 50 | Design patterns in Python, clean architecture, SOLID, reading CPython/stdlib source | Phase project |

**Checkpoint:** you can explain what happens, step by step, when Python looks up `obj.attr`.

### Project 7: Open-source library

Build a small, well-engineered library that other developers can use, e.g. a rate limiter, an async task queue, or a caching decorator with TTL and eviction policies.

- Thread-safe and async-compatible APIs
- Benchmarks comparing it with an existing library, with results in the README
- Full docs site on GitHub Pages, typed public API, 95%+ coverage
- Also: make at least two merged contributions to an existing open-source Python project

**Demonstrates:** deep language knowledge, performance engineering, API design, open-source collaboration.

## Phase 8 – Capstone and going professional (weeks 51–60)

Goal: ship one production-quality application and turn your work into job offers.

### Capstone project (weeks 51–57)

Build an original application that solves a real problem for real users (yourself, a club, a small business). Example: a booking system for a local gym, a habit tracker with analytics, or an inventory tool for a shop. Whatever you pick, it must include:

- [ ] A written spec: problem, users, features, out-of-scope list
- [ ] Backend in FastAPI or Django with PostgreSQL and authentication
- [ ] A frontend (HTMX, Django templates, or a simple React/Vue app)
- [ ] Your Phase 6 specialty as a core feature (e.g. analytics dashboard, ML feature, automation)
- [ ] Unit, integration and end-to-end tests; CI/CD pipeline
- [ ] Dockerized and deployed on a public URL with HTTPS
- [ ] Logging, error tracking (e.g. Sentry) and basic monitoring
- [ ] At least 3 real users and one iteration based on their feedback
- [ ] README with architecture diagram, screenshots and a 2-minute demo video

**Demonstrates:** everything — that you can take an idea from spec to production and maintain it.
