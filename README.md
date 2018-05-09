# MSc Numbers from SIMS data

There is a script here to quickly calculate student numbers (or potential student numbers) on MSc Programmes which works on the csv files output from SIMS.

`msc_number_from_LOSOP.py` works on the output of the 'List of Students on a Programme (Excel version)'. The input options to generate this report are shown below. This will include all students in COMSC, including those where COMSC is not the home school.

![Course Code: P%, Programme Year: %, School: COMSC%](/docs/losop_input.png?raw=true "Parameters for LOSOP report")


This script reports on the number of students with each registration status (Registered, Registered - Not Collected ID Card, Pending Registration, Pending Registration - New Entrant, Absent) on each programme.

By default it will report the number of students on each programme, including all Registered Statuses for anyone on Block 1 in the current academic year.

It takes one required argument `-i INPUT`, the name of the `.csv` file output by SIMS.

The `-r` flag restricts output to only counting those students who have a status of 'Registered'. This does not include those who have 'Registered - Not Collected ID Card'. To also include these students, add the `-l` flag.

'Registered' students are definitely here, as they have collected their ID card. 'Registered - Not Collected ID Card' students have enrolled online, but may not actually show up. 'Pending Registration' and 'Pending Registration - New Entrant' students have not yet enrolled.


```
usage: msc_numbers.py [-h] -i INPUT [-b] [-r] [-l] [-g] [-c]

Analysing MSc numbers in SIMS

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file to be analysed
  -b, --breakdown       Breakdown by part/time & placement programme
  -r, --registered      show fully registered students only
  -l, --loose           show fully registered students and those who have
                        registered but not collected ID card  (if -r also provided)
  -g, --graphics        create visualisations of the data
  -c, --csv             output csv of enrolled status per programme
```

So, for example, to generate a breakdown of all statuses for all students on all programmes in COMSC (including joint programmes), creating both graphical and csv results, export the list of students on a programme from SIMS with the above parameters and run:

`python msc_numbers_from_LOSOP.py -i Students_on_Programme.csv -l -r -b -g -c`

# Requirements

[Pandas](https://pypi.python.org/pypi/pandas) is required for data input, manipulation and output

If graphical output is desired, [matplotlib](https://pypi.python.org/pypi/matplotlib/) is also required.

Both are pip installable.
