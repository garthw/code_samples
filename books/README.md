Book Command Line Script
========================

USE:
python books.py [-h or --help] , [--filter], [--year], [--reverse]

OUTPUT:
List of books sorted by last name.
Year parameter sorts ascending by year.
Reverse parameter sorts descending by year AND last name.
Filter parameter requires an argument and only displays items containing that argument.

EXAMPLES:
python books.py
python books.py --filter er --year
python books.py --filter 199 --reverse

IMPLEMENTATION:
Reads from a set list of inputs with set delimiters:
Double quotes "
Pipe  |
or Comma  ,

Filters and sorts the list given command line parameters/arguments.

INCLUDES UNIT TESTS
