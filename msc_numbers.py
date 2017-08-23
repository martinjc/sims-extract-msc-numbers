#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import argparse

import pandas as pd

from lib.programme_data import *

def filter_data(all_data):
    """
    Takes the data from SIMS and removes all students not in
    block 1 of the current academic year.

    This should remove any students on placement (block 1S),
    doing a dissertation (block D1/D2) or repeating something (block 2)
    """
    # Remove all students not from this academic year
    YEAR_COLUMN = 'Acad Year'
    THIS_YEAR = '2017/8'
    filtered_data = all_data.loc[all_data[YEAR_COLUMN] == THIS_YEAR]

    # Remove all students not currently in block 1 (so those doing placement or dissertation)
    BLOCK_COLUMN = 'Block'
    filtered_data = filtered_data.loc[filtered_data[BLOCK_COLUMN] == '1']

    return filtered_data


def filter_students_by_status(all_data, status):
    """
    Filter the data to all students with a given status
    """
    # Select all students with the given registration status
    STATUS_COLUMN = ' Reg Status'
    return all_data.loc[all_data[STATUS_COLUMN] == status]


def group_and_count_by_status(all_data):
    grouped = all_data.groupby(['Course', ' Reg Status']).size()
    grouped = grouped.sort_index()
    return grouped


def print_registered_status_count(all_data):
    registered_students = filter_students_by_status(all_data, 'Registered')
    print('Registered Students: %s' % registered_students['Student Code'].count())
    registered_students = filter_students_by_status(all_data, 'Registered - Not Collected ID Card')
    print('Registered - Not Collected ID Card Students: %s' % registered_students['Student Code'].count())
    registered_students = filter_students_by_status(all_data, 'Pending Registration New Entrant')
    print('Pending Registration New Entrant Students: %s' % registered_students['Student Code'].count())


def count_by_programme(all_data):

    PROG_COLUMN = 'Course'
    return all_data[PROG_COLUMN].value_counts()


def print_programme_counts(programme_counts):
    print('Code\t | Title & Count')
    for p in programme_counts.axes[0]:
        print('%s | %s: %d' % (p, prog_codes_2_prog_name_long[p], programme_counts[p]))


def print_programme_counts_with_title(programme_counts):
    count_data = {}

    for p_name, p_codes in prog_name_short_2_prog_codes.items():
        print('-----------------------------------------------------')
        count = 0
        for p_code in p_codes:
            count += programme_counts.get(p_code, 0)
        print('| %s (all): %d' % (p_name, count))
        print('-----------------------------------------------------')
        for p_code in p_codes:
            name = prog_codes_2_prog_name_long[p_code]
            count = programme_counts.get(p_code, 0)
            print(' %s: %d' % (prog_codes_2_prog_name_long[p_code], programme_counts.get(p_code, 0)))


def main():

    # read in filename as command line argument
    parser = argparse.ArgumentParser(description='Analysing MSc numbers in SIMS')
    parser.add_argument('-i', '--input', help='Input file to be analysed', required=True, action='store')
    args = parser.parse_args()

    # open and read the input file
    input_file = os.path.join(os.getcwd(), args.input)

    with open(input_file, 'r') as raw_data_file:
        sims_data = pd.read_csv(raw_data_file, header=6, index_col=False)

        # restrict it to this academic year block 1
        filtered_data = filter_data(sims_data)

        print_registered_status_count(filtered_data)

        # counts by programme
        programme_counts = count_by_programme(filtered_data)
        print_programme_counts_with_title(programme_counts)

        grouped = group_and_count_by_status(filtered_data)
        print(grouped)

if __name__ == '__main__':
    main()
