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
    grouped = all_data.groupby(['Prog Code', 'Dec/']).size()
    grouped = grouped.sort_index()
    return grouped

def print_full_breakdown(grouped_data, statuses_to_print):
    """
    Dump a count of each programme and status to command line
    """
    for prog_name in prog_names_short:
        prog_codes = prog_name_short_2_prog_codes[prog_name]
        total = 0
        for prog_code in prog_codes:
            if prog_code in grouped_data.index:
                for status in statuses_to_print:
                    if status in grouped_data.loc[prog_code]:
                        total += grouped_data.loc[prog_code][status]
                        print('%s: %d - %s' % (prog_codes_2_prog_name_long[prog_code], grouped_data.loc[prog_code][status], status))
        print('-----------------------------------------------------')
        print('%s (all): %d' % (prog_name, total))
        print('-----------------------------------------------------')


def print_full_breakdown_all_statuses(grouped_data):
    print_full_breakdown(grouped_data, application_statuses)

def print_full_breakdown_only_unconditional_firm(grouped_data):
    print_full_breakdown(grouped_data, ['UF', 'CFUF'])

def print_full_breakdown_only_unconditional_and_conditional_firm(grouped_data):
    print_full_breakdown(grouped_data, ['UF', 'CFUF', 'CF'])

def print_no_breakdown(grouped_data, statuses_to_print):
    """
    Dump a count of each programme (grouped by 'real' programme)
    and status to command line
    """
    for prog_name in prog_names_short:
        prog_codes = prog_name_short_2_prog_codes[prog_name]
        total = 0
        for status in statuses_to_print:
            for prog_code in prog_codes:
                if prog_code in grouped_data.index:
                    if status in grouped_data.loc[prog_code]:
                        total += grouped_data.loc[prog_code][status]
        print('-----------------------------------------------------')
        print('%s (all): %d' % (prog_name, total))
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
    grouped = all_data.groupby('Prog Code')['Dec/'].value_counts()

    csv_data = grouped.unstack(fill_value=0)
    csv_data = csv_data.reindex(prog_codes, fill_value=0)
    breakdown_data = csv_data.rename(prog_codes_2_prog_name_long)

    with open('application_status_per_programme_breakdown_from_lotoap.csv', 'w') as output_file:
        breakdown_data.to_csv(output_file)

    no_breakdown_data = csv_data.groupby(prog_codes_2_prog_name_short).sum()

    with open('application_status_per_programme_from_lotoap.csv', 'w') as output_file:
        no_breakdown_data.to_csv(output_file)


def create_breakdown_graphic(grouped_data):
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    mpl.rcdefaults()
    mpl.rcParams['font.size'] = 16
    mpl.rcParams['figure.figsize'] = (14,10)
    mpl.rcParams['axes.grid'] = True

    index = list(range(len(prog_codes)))

    data = {}
    for status in application_statuses:
        data[status] = []
        for prog_code in prog_codes:
            if prog_code in grouped_data.index:
                if status in grouped_data.loc[prog_code]:
                    data[status].append(grouped_data.loc[prog_code][status])
                else:
                    data[status].append(0)
            else:
                data[status].append(0)

    fig, ax = plt.subplots()
    bottom = [0]*len(prog_codes)

    for i, status in enumerate(application_statuses):
        ax.bar(index, data[status], label=status, bottom=bottom)
        bottom = [sum(v) for v in zip(bottom, data[status])]

    ax.set_xticks(list(range(len(prog_codes))))
    ax.set_xticklabels([prog_codes_2_prog_name_long[p] for p in prog_codes], rotation=90)
    ax.set_ylim(top=max(bottom)+10)
    ax.legend(loc='upper left', bbox_to_anchor=(0.1, 1.0), framealpha=0.5)

    plt.savefig('application_status_per_programme_breakdown_from_lotoap.png', bbox_inches='tight')


def create_no_breakdown_graphic(grouped_data):
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    mpl.rcdefaults()
    mpl.rcParams['font.size'] = 16
    mpl.rcParams['figure.figsize'] = (14,10)
    mpl.rcParams['axes.grid'] = True

    index = list(range(len(prog_names_short)))

    data = {}
    for status in application_statuses:

        data[status] = []

        for prog_name in prog_names_short:
            prog_codes = prog_name_short_2_prog_codes[prog_name]
            total = 0
            for prog_code in prog_codes:
                if prog_code in grouped_data.index:
                    if status in grouped_data.loc[prog_code]:
                        total += grouped_data.loc[prog_code][status]
            data[status].append(total)

    fig, ax = plt.subplots()
    bottom = [0]*len(prog_names_short)

    for i, status in enumerate(application_statuses):
        ax.bar(index, data[status], label=status, bottom=bottom)
        bottom = [sum(v) for v in zip(bottom, data[status])]

    ax.set_xticks(list(range(len(prog_names_short))))
    ax.set_xticklabels(prog_names_short, rotation=90)
    ax.set_ylim(top=max(bottom)+10)
    ax.legend(loc='upper left', bbox_to_anchor=(0.2, 1.0), framealpha=0.5)

    plt.savefig('application_status_per_programme_from_lotoap.png', bbox_inches='tight')


def main():

    # read in filename as command line argument
    parser = argparse.ArgumentParser(description='Analysing MSc numbers in SIMS')
    parser.add_argument('-i', '--input', help='Input file to be analysed', required=True, action='store')
    parser.add_argument('-b', '--breakdown', help='Breakdown by part/time & placement programme', action='store_true')
    parser.add_argument('-u', '--unconditional', help='show unconditional firm students only', action='store_true')
    parser.add_argument('-l', '--conditional', help='show unconditional and conditional firm students', action='store_true')
    parser.add_argument('-g', '--graphics', help='create visualisations of the data', action='store_true')
    parser.add_argument('-c', '--csv', help='output csv of application status per programme', action='store_true')
    args = parser.parse_args()

    # open and read the input file
    input_file = os.path.join(os.getcwd(), args.input)

    with open(input_file, 'r') as raw_data_file:
        sims_data = pd.read_csv(raw_data_file)

        # restrict it to this academic year block 1
        filtered_data = filter_data(sims_data)
        grouped = group_and_count_by_status(filtered_data)

        if not args.breakdown and not args.unconditional:
            print_no_breakdown_all_statuses(grouped)
        elif args.breakdown and not args.unconditional:
            print_full_breakdown_all_statuses(grouped)
        elif args.breakdown and args.unconditional and not args.conditional:
            print_full_breakdown_only_unconditional_firm(grouped)
        elif args.breakdown and args.unconditional and args.conditional:
            print_full_breakdown_only_unconditional_and_conditional_firm(grouped)
        elif not args.breakdown and args.unconditional and not args.conditional:
            print_no_breakdown_only_unconditional_firm(grouped)
        elif not args.breakdown and args.unconditional and args.conditional:
            print_no_breakdown_only_unconditional_and_conditional_firm(grouped)

        if args.graphics and args.breakdown:
            create_breakdown_graphic(grouped)
        elif args.graphics and not args.breakdown:
            create_no_breakdown_graphic(grouped)

        if args.csv:
            output_csvs(filtered_data)

if __name__ == '__main__':
    main()
