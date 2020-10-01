# acronym

A python3 command-line tool for generating English language acronyms from a list of words. The tool will check all combinations of initial letters and keep only those that can be combined to generate words in an English dictionary.

For example:
```sh
python acronym.py some acronyms please
```

will generate:

```
Loading words ...
Generating intial combinations ...
Filtering acronyms for valid words ...
Found 11 valid acronyms
SAP     some acronyms please
SOAP    some acronyms please
SAPLE   some acronyms please
SPA     some please acronyms
ASP     acronyms some please
ASOP    acronyms some please
PLASOME please acronyms some
PASO    please acronyms some
PLEAS   please acronyms some
PAS     please acronyms some
PACS    please acronyms some
```

To save results to file, pass the `--write` flag.
