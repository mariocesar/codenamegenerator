# namegenerator
A Name generator of the form "Adjetive Noun"

Test it by

```shell
$ python -m codenamegenerator 8
loving fermi
sick engelbart
hopeful babbage
distracted sinoussi
modest swartz
compassionate yalow
modest pike
furious babbage

$ python -m codenamegenerator --help
usage: __main__.py [-h] [-c] [-t] [-s] [--prefix PREFIX] [--suffix SUFFIX] [num]

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
from codenamegenerator import get_random_name
print(get_random_name)
```
## TODO:

 - [ ] Choice which collection of nouns and adjectives to use
 - [x] Command line interface with options
