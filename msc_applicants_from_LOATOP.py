#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import argparse

import pandas as pd

from lib.programme_data import *

def filter_data(all_data):
    """
    Remove all the students not applying for this current year
    """
    # Remove all students not from this academic year
    YEAR_COLUMN = 'Entry Year'
    THIS_YEAR = '2018/9'
    filtered_data = all_data.loc[all_data[YEAR_COLUMN] == THIS_YEAR]

    return filtered_data


def filter_students_by_status(all_data, status):
    """
    Filter the data to all students with the given status
    """
    # Select all students with the given registration status
    STATUS_COLUMN = 'Dec/'
    return all_data.loc[all_data[STATUS_COLUMN] == status]


def group_and_count_by_status(all_data):
    """
    Group by programme code and registration status and then
    count how many of each combination there are
    """
    grouped = all_data.groupby(['Prog Code', 'Dec/', 'App Cat']).size()
    grouped = grouped.sort_index()
    return grouped


def print_no_breakdown(grouped_data, statuses_to_print):
    """
    Dump a count of each programme (grouped by 'real' programme)
    and status to command line
    """
    for prog_name in prog_names_short:
        prog_codes = prog_name_short_2_prog_codes[prog_name]
        total = 0
        home = 0
        international = 0
        for status in statuses_to_print:
            for prog_code in prog_codes:
                if prog_code in grouped_data.index:
                    if status in grouped_data.loc[prog_code]:
                        if 'O' in grouped_data.loc[prog_code][status]:
                            total += grouped_data.loc[prog_code][status]['O']
                            home += grouped_data.loc[prog_code][status]['O']
                    if status in grouped_data.loc[prog_code]:
                        if 'H' in grouped_data.loc[prog_code][status]:
                            total += grouped_data.loc[prog_code][status]['H']
                            international += grouped_data.loc[prog_code][status]['H']
        print('-----------------------------------------------------')
        print('%s (all): %d' % (prog_name, total))
        print('%s (home): %d' % (prog_name, home))
        print('%s (international): %d' % (prog_name, international))
        print('-----------------------------------------------------')

def print_no_breakdown_all_statuses(grouped_data):
    print_no_breakdown(grouped_data, application_statuses)

def print_no_breakdown_only_unconditional_and_conditional_firm(grouped_data):
    print_no_breakdown(grouped_data, ['UF', 'CFUF', 'CF'])

def print_no_breakdown_only_unconditional_firm(grouped_data):
    print_no_breakdown(grouped_data, ['UF', 'CFUF'])


def output_csvs(all_data):
    """
    Write out csv files containing the registration status counts for
    each programme code and also grouped by course title
    """
    grouped = all_data.groupby(['Prog Code', 'App Cat'])['Dec/'].value_counts()
    grouped = grouped.sort_index()

    csv_data = grouped.unstack(fill_value=0)

    no_breakdown_data = csv_data.groupby([prog_codes_2_prog_name_short, 'App Cat'], level=[0, 1]).sum()

    with open('application_status_per_programme_from_lotoap.csv', 'w') as output_file:
        no_breakdown_data.to_csv(output_file)


def main():

    # read in filename as command line argument
    parser = argparse.ArgumentParser(description='Analysing MSc numbers in SIMS')
    parser.add_argument('-i', '--input', help='Input file to be analysed', required=True, action='store')
    parser.add_argument('-u', '--unconditional', help='show unconditional firm students only', action='store_true')
    parser.add_argument('-l', '--conditional', help='show unconditional and conditional firm students', action='store_true')
    parser.add_argument('-c', '--csv', help='output csv of application status per programme', action='store_true')
    args = parser.parse_args()

    # open and read the input file
    input_file = os.path.join(os.getcwd(), args.input)

    with open(input_file, 'r') as raw_data_file:
        sims_data = pd.read_csv(raw_data_file)

        # restrict it to this academic year block 1
        filtered_data = filter_data(sims_data)
        grouped = group_and_count_by_status(filtered_data)

        if not args.unconditional:
            print_no_breakdown_all_statuses(grouped)
        elif args.unconditional and not args.conditional:
            print_no_breakdown_only_unconditional_firm(grouped)
        elif args.unconditional and args.conditional:
            print_no_breakdown_only_unconditional_and_conditional_firm(grouped)

        if args.csv:
            output_csvs(filtered_data)

if __name__ == '__main__':
    main()
