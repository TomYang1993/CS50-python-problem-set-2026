# CS50P Problem Set Solutions

My solutions to [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/), psets 0–8 (the course has no pset 9; week 9 is the final project).

These are self-study solutions, not submitted for any course credential. Each problem lives in its own folder, matching the course's structure.

## Layout

```
pset0/   Functions, Variables       indoor, playback, faces, einstein, tip
pset1/   Conditionals                deep, bank, extensions, interpreter, meal
pset2/   Loops                       camel, coke, twttr, plates, nutrition
pset3/   Exceptions                  fuel, taqueria, grocery, outdated
pset4/   Libraries                   emojize, figlet, adieu, game, professor, bitcoin
pset5/   Unit Tests                  test_twttr, test_bank, test_plates, test_fuel
pset6/   File I/O                    lines, pizza, scourgify, shirt
pset7/   Regular Expressions         numb3rs, watch, working, um, response
pset8/   Object-Oriented Programming seasons, jar, shirtificate
```

## Running

Most problems are plain scripts with no dependencies:

```
python3 psetN/problem/problem.py
```

Some need third-party packages (emoji, pyfiglet, inflect, requests, tabulate, Pillow, validators, fpdf2) and pytest for the test files. Set up a virtual environment once at the repo root:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run a problem's tests, e.g.:

```
cd pset5/test_fuel
pytest -q
```

## Notes on specific problems

- **pset4/figlet**: requires `pyfiglet`.
- **pset4/bitcoin**: requires a CoinCap v3 API key; set it in the `API_KEY` constant in `bitcoin.py`.
- **pset6/shirt**: requires a `shirt.png` (transparent background) in the same folder; download it from the pset page.
- **pset6/scourgify**: requires a `before.csv` input file; download it from the pset page.
- **pset8/shirtificate**: requires a `shirtificate.png` in the same folder; download it from the pset page.

All problems were manually verified against the examples given on each pset's page.
