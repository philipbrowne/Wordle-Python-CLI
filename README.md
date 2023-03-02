# Python CLI Wordle Helper

Find words in Wordle using the Python CLI Wordle Helper

In the first command line argument, use underscores except for the known letter positions. This input must be exactly five characters or the Python will get mad, sorry 😢

```
$python3 wordle.py __per

['amper', 'asper', 'caper', 'coper', 'doper', 'duper', 'gaper', 'hiper', 'hyper','hoper',
'imper', 'japer','leper', 'loper', 'moper', 'neper', 'paper', 'piper', 'raper', 'riper',
'roper', 'siper', 'super', 'taper', 'typer', 'toper', 'upper', 'viper', 'wiper']
```

In any following command line arguments, indicate a letter that the word will also include (e.g. yellow letters in Wordle)

Example Use:

```
$ python3 wordle.py ___e_ h p

['cheep', 'hyped', 'hiper', 'hyper', 'hypes', 'hoped', 'hoper', 'hopes',
'phaet', 'phies', 'phren', 'sheep', 'shlep', 'sphex', 'upher', 'wheep']
```

Have fun!
