# 🏎 F1 Controller Mapping Converter

A desktop app that shows you exactly which buttons changed between any F1 game (2011–2024) and **F1 25**, so you know what to remap before jumping in.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square&logo=windows)
![Controller](https://img.shields.io/badge/Controller-Xbox%20%7C%20PlayStation-green?style=flat-square)

---

## Features

- Covers every F1 game from **F1 2011 to F1 24**
- Supports both **Xbox** and **PlayStation** controllers
- Highlights exactly which inputs changed in **amber**
- Filter to show all inputs, changed only, or unchanged only
- Era-based game sidebar (PS3/360 → PS4/One → PS5/Series)
- Color-coded button chips (A, B, X, Y, Cross, Circle, etc.)
- Notes for each game explaining key differences
- Dark themed native desktop window

---

## How to run

### Option 1 — Double click launcher (easiest)
1. Install Python from [python.org](https://python.org) — tick **"Add to PATH"** during install
2. Download both files: `F1-Mapping-Converter.py` and `Launch-F1-Mapping.bat`
3. Put them in the same folder
4. Double-click `Launch-F1-Mapping.bat` — it installs the dependency and opens the app

### Option 2 — Run manually
```bash
pip install customtkinter
python F1-Mapping-Converter.py
```

---

## Games supported

| Era | Games |
|-----|-------|
| PS3 / Xbox 360 | F1 2011, F1 2012, F1 2013, F1 2014, F1 2015 |
| PS4 / Xbox One | F1 2016, F1 2017, F1 2018, F1 2019, F1 2020, F1 2021 |
| PS5 / Xbox Series | F1 22, F1 23, F1 24 |

---

## How to remap in F1 25

1. Go to **Settings → Controls, Vibration & Force Feedback**
2. Create a new profile to avoid overwriting defaults
3. Click the input you want to change, then press the new button
4. Focus on the amber highlighted rows — those are the only ones that differ
5. Test in **Time Trial** before a race session
