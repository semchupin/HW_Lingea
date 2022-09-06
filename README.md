# Home work for Lingea
There are two files 'main.py' regular analyzing and 'main_polar.py' that use Polars Library to speed up analyzing input but because it uses advanced threading some lines can be printed not in the right order but error lines have a correct line number.
## Task description
The program gets the words it saved as parameters on the command line. On standard input, it will read lines of text and look up the words from the command line. On the standard output, it will print those lines that contain at least one word from the command line as a separate word. The other lines will be printed to standard error output, in this case it will add the order of the non-matching line in the output to the beginning. The program must be able to handle very long files. Individual input lines are not limited in length, but we assume that each of the input lines will fit in memory. Assume the command line parameters and input are UTF-8 encoded.


## Example of using script:
```
cat .\alice29.txt | py .\main_polar.py alice with days
```
```
cat .\alice29.txt | py .\main.py alice with days
```

Scripts was tested on big text file (`alice29.txt`).

## Performants:
main_polar.py: Completed in 3.2996826171875 sec.

main.py: Completed in 4.505359411239624 sec.
