#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import argparse

import pandas as pd

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


def count_students_with_status(all_data, status):

    # Select all students with the given registration status
    STATUS_COLUMN = ' Reg Status'
    return all_data.loc[all_data[STATUS_COLUMN] == status]


def main():

    # read in filename as command line argument
    parser = argparse.ArgumentParser(description='Analysing MSc numbers in SIMS')
    parser.add_argument('-i', '--input', help='Input file to be analysed', required=True, action='store')
    args = parser.parse_args()

    # open and read the input file
    input_file = os.path.join(os.getcwd(), args.input)

    with open(input_file, 'r') as raw_data_file:
        sims_data = pd.read_csv(raw_data_file, header=6, index_col=False)
        print(sims_data.count())

        # restrict it to this academic year block 1
        filtered_data = filter_data(sims_data)
        print(filtered_data.count())

        registered_students = count_students_with_status(filtered_data, 'Registered')
        print('Registered Students: %s' % registered_students['Student Code'].count())
        registered_students = count_students_with_status(filtered_data, 'Registered - Not Collected ID Card')
        print('Registered - Not Collected ID Card Students: %s' % registered_students['Student Code'].count())
        registered_students = count_students_with_status(filtered_data, 'Pending Registration New Entrant')
        print('Pending Registration New Entrant Students: %s' % registered_students['Student Code'].count())


if __name__ == '__main__':
    main()
