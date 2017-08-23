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


def print_full_breakdown_all_statuses(grouped_data):
    for prog_name in prog_names_short:
        prog_codes = prog_name_short_2_prog_codes[prog_name]
        total = 0
        for prog_code in prog_codes:
            if prog_code in grouped_data.index:
                for status in statuses:
                    if status in grouped_data.loc[prog_code]:
                        total += grouped_data.loc[prog_code][status]
                        print('%s: %d - %s' % (prog_codes_2_prog_name_long[prog_code], grouped_data.loc[prog_code][status], status))
        print('-----------------------------------------------------')
        print('%s (all): %d' % (prog_name, total))
        print('-----------------------------------------------------')

def print_full_breakdown_only_registered(grouped_data):
    for prog_name in prog_names_short:
        prog_codes = prog_name_short_2_prog_codes[prog_name]
        total = 0
        for prog_code in prog_codes:
            if prog_code in grouped_data.index:
                if 'Registered' in grouped_data.loc[prog_code]:
                    total += grouped_data.loc[prog_code]['Registered']
                    print('%s: %d - %s' % (prog_codes_2_prog_name_long[prog_code], grouped_data.loc[prog_code]['Registered'], 'Registered'))
        print('-----------------------------------------------------')
        print('%s (all): %d' % (prog_name, total))
        print('-----------------------------------------------------')

def print_no_breakdown_all_statuses(grouped_data):
    for prog_name in prog_names_short:
        prog_codes = prog_name_short_2_prog_codes[prog_name]
        total = 0
        for status in statuses:
            for prog_code in prog_codes:
                if prog_code in grouped_data.index:
                    if status in grouped_data.loc[prog_code]:
                        total += grouped_data.loc[prog_code][status]
        print('-----------------------------------------------------')
        print('%s (all): %d' % (prog_name, total))
        print('-----------------------------------------------------')

def print_no_breakdown_only_registered(grouped_data):
    for prog_name in prog_names_short:
        prog_codes = prog_name_short_2_prog_codes[prog_name]
        total = 0
        for prog_code in prog_codes:
            if prog_code in grouped_data.index:
                if 'Registered' in grouped_data.loc[prog_code]:
                    total += grouped_data.loc[prog_code]['Registered']
        print('-----------------------------------------------------')
        print('%s (all): %d' % (prog_name, total))
        print('-----------------------------------------------------')


def main():

    # read in filename as command line argument
    parser = argparse.ArgumentParser(description='Analysing MSc numbers in SIMS')
    parser.add_argument('-i', '--input', help='Input file to be analysed', required=True, action='store')
    parser.add_argument('-b', '--breakdown', help='Breakdown by part/time & placement programme', action='store_true')
    parser.add_argument('-r', '--registered', help='show fully registered students only', action='store_true')
    args = parser.parse_args()

    # open and read the input file
    input_file = os.path.join(os.getcwd(), args.input)

    with open(input_file, 'r') as raw_data_file:
        sims_data = pd.read_csv(raw_data_file, header=6, index_col=False)

        # restrict it to this academic year block 1
        filtered_data = filter_data(sims_data)
        grouped = group_and_count_by_status(filtered_data)

        if not args.breakdown and not args.registered:
            print_no_breakdown_all_statuses(grouped)
        elif args.breakdown and not args.registered:
            print_full_breakdown_all_statuses(grouped)
        elif args.breakdown and args.registered:
            print_full_breakdown_only_registered(grouped)
        elif not args.breakdown and args.registered:
            print_no_breakdown_only_registered(grouped)


if __name__ == '__main__':
    main()
