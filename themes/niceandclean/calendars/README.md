# How To Generate conky Calendars

The conky calendar widget requires three month files:
``month1``, ``month2``, and ``month3``.

```bash
python make_calendars.py
python make_calendars.py 2017 9
```

or

```bash
python -m calendar 2017  9 > month1
python -m calendar 2017 10 > month2
python -m calendar 2017 11 > month3
```
