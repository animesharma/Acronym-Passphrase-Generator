# Acronym-Passphrase-Generator
A fast and efficient Python tool to generate a secure passphrase from a user desired acronym.

## Usage:
```
usage: Acronym Passphrase Generator [-h] --acronym ACRONYM [--min_word_len MIN_WORD_LEN] [--separators [SEPARATORS ...]] [--case CASE]

Python program to generate a secure passphrase from a user desired acronym.

options:
  -h, --help            show this help message and exit
  --acronym ACRONYM, -a ACRONYM
                        Acronym from which passphrase is generated.
  --min_word_len MIN_WORD_LEN, -m MIN_WORD_LEN
                        Minimum length of words used in the passphrase.
  --separators [SEPARATORS ...], -s [SEPARATORS ...]
                        List of separators to separate words in the passphrase. Defaults to hyphen (-)
  --case CASE, -c CASE  Specifies the case style to use for the generated passphrase. Supported options include: 
                        0. kebab-case (default) 
                        1. PascalCase 
                        2. Intermittent Capitalization 
                        3. StIcKy CaPs
  --num_passphrases NUM_PASSPHRASES, -n NUM_PASSPHRASES
                        The number of passphrases to be generated from the acronym
```

## Examples:
```
> python .\src\passgen.py -a "lmao"
lymphocystosis-mender-amassments-overburningly

> python .\src\passgen.py -a "PILL" -n 3 -c 1
Preconizer-Ivyflower-Latinizing-Linable
Purpurigenous-Indifulvin-Larches-Leally
Polyhalite-Immaterialization-Latinistic-Laundered

> python .\src\passgen.py -a "lmao" -m 8 -s "@", "&"
limpidly&microprograms@aquarist@overfrugality

> python .\src\passgen.py -a "fubar" -s "&_&" -n 4
filmgoing&_&unsandalled&_&bullskin&_&accidentary&_&reliquefying
ferulaceous&_&unobstruent&_&borassus&_&ailuropus&_&rhizotaxis
forcepslike&_&undecagon&_&betorcin&_&athetosic&_&require
filmer&_&uncontributed&_&bardiglio&_&ascophorous&_&rickeys

> python .\src\passgen.py -a "lmao" -m 7 -c 2
LAWBReakEr-MOULiNaGe-ABSorPtioMETRic-oNEbeRRY
```

## Acknowledgements:
1. Dataset containing ~370,000 words in English obtained from: https://github.com/dwyl/english-words
2. Inspiration for the project stems from the discussion at: https://fosstodon.org/@atoponce/110839994357941432
