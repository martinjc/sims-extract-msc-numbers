# MSc Numbers from SIMS data

There are two scripts here to quickly calculate student numbers (or potential student numbers) on MSc Programmes

Both work on the csv files output from SIMS.

`msc_number_from_LOSOP.py` works on the output of the 'List of Students on a Programme (Excel version)'. The input options to generate this report are shown below. This will include all students in COMSC, including those where COMSC is not the home school.

![Course Code: P%, Programme Year: %, School: COMSC%](/docs/losop_input.png?raw=true "Parameters for LOSOP report")

`msc_numbers_from_ECOPS.py` works on the output of the 'Enrolment/COPS Status Report (Excel version)'. The input options to generate this report are shown below. This will only include students on courses where COMSC is the home school. To get a true picture of student numbers, it is recommended the `msc_numbers_from_LOSOP.py` script is used.

![Student Code: %, Programme Code: P%, Programme Year: %, School Code: COMSC%](/docs/ecops_input.png?raw=true "Parameters for ECOPS report")

Both scripts report on the number of students with each registration status (Registered, Registered - Not Collected ID Card, Pending Registration, Pending Registration - New Entrant, Absent) on each programme.

By default they will report the number of students on each programme, including all Registered Statuses for anyone on Block 1 in the current academic year.

They take one required argument `-i INPUT`, the name of the `.csv` file output by SIMS.

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

`python msc_numbers_from_LOSOP.py i Students_on_Programme.csv -l -r -b -g -c`
