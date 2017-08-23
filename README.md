# MSc Numbers from SIMS data

This script quickly converts the contents of the 'List of Students on a Programme (Excel)' report from SIMS to a count of the enrollment status of students on each MSc programme in COMSC.

It reports on the number of students with each registration status (Registered, Registered - Not Collected ID Card, Pending Registration, Pending Registration - New Entrant, Absent) on each programme.

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
                        registered but not collected ID card
  -g, --graphics        create visualisations of the data
  -c, --csv             output csv of enrolled status per programme
```
