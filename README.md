# Python CLI Wordle Helper

Find words in Wordle using the Python CLI Wordle Helper

In the first command line argument, use underscores except for the known letter positions.

In any following command line arguments, indicate a letter that the word will also include (e.g. yellow letters in Wordle)

Example Use:

```
$ python3 wordle.py ___e_ h p
['cheep', 'hyped', 'hiper', 'hyper', 'hypes', 'hoped', 'hoper', 'hopes', 'phaet', 'phies', 'phren', 'sheep', 'shlep', 'sphex', 'upher', 'wheep']
```
