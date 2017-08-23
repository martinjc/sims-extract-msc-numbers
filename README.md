# MSc Numbers from SIMS data

This script quickly converts the contents of the 'List of Students on a Programme (Excel)' report from SIMS to a count of the enrollment status of students on each MSc programme in COMSC.

It reports on the number of students with each registration status (Registered, Registered - Not collected ID Card, Pending Registration, Pending Registration - New Entrant, Absent) on each programme.

By default it will report the number of students on each programme, including all Registered Statuses for anyone on Block 1 in the current academic year.


It takes one required argument '-i INPUT', the name of the `.csv` file output by SIMS.


```
usage: msc_numbers.py [-h] -i INPUT [-b] [-r] [-g] [-c]


Analysing MSc numbers in SIMS


optional arguments:
  -h, --help            show this help message and exit

  -i INPUT, --input INPUT
                        Input file to be analysed

  -b, --breakdown       Breakdown by part/time & placement programme

  -r, --registered      show fully registered students only

  -g, --graphics        create visualisations of the data

  -c, --csv             output csv of enrolled status per programme
```
