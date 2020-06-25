# namegenerator
A Name generator of the form "Adjetive Noun"

Test it by

```shell
$ python -m codenamegenerator 8
admiring ride
unruffled williams
compassionate franklin
frosty torvalds
youthful blackwell
distracted pike
nostalgic curran
stoic hopper

$ python -m codenamegenerator --help
usage: codenamegenerator [-h] [-c] [-t] [-s] [--prefix PREFIX] [--suffix SUFFIX] num

Code name generator

positional arguments:
  num

optional arguments:
  -h, --help        show this help message and exit
  -c, --capitalize
  -t, --title
  -s, --slugify
  --prefix PREFIX   Prefix dictionary
  --suffix SUFFIX   Suffix dictionary
```

or

```python
from codenamegenerator import generate_codenames
print(generate_codenames())
```
## TODO:

 - [ ] Choice which collection of nouns and adjectives to use
 - [x] Command line interface with options
