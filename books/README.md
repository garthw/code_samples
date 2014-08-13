Book Command Line Script
========================

USE:<br>
python books.py [-h or --help] [--filter] [--year] [--reverse]

OUTPUT:<br>
List of books sorted by last name.<br>
Year parameter sorts ascending by year.<br>
Reverse parameter sorts descending by year AND last name.<br>
Filter parameter requires an argument and only displays items containing that argument.

EXAMPLES:<br>
python books.py<br>
python books.py --filter er --year<br>
python books.py --filter 199 --reverse

IMPLEMENTATION:<br>
Reads from a set list of inputs with set delimiters:<br>
Double quotes "<br>
Pipe  |<br>
or Comma  ,

Filters and sorts the list given command line parameters/arguments.

INCLUDES UNIT TESTS
