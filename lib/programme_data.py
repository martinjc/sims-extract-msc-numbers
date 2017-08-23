#!/usr/bin/python
# -*- coding: utf-8 -*-

prog_codes = [
    'PFMSCMPA',
    'PFMSCMPB',
    'PPMSCMPA',
    'PFMSCITA',
    'PFMSCITB',
    'PPMSCITA',
    'PFMSADSA',
    'PFMSADSB',
    'PPMSADSA',
    'PFMSISPA',
    'PPMSISPA',
    'PFMSCOJA',
    'PFMSCDJA',
    'PFMSDSYA',
    'PPMSDSYA'
]

prog_names_short = [
    'MSc Computing',
    'MSc Computing and IT Management',
    'MSc Advanced Computer Science',
    'MSc Information Security and Privacy',
    'MSc Computational and Data Journalism',
    'MSc Data Science and Analytics',
]

prog_codes_2_prog_name_long = {
    'PFMSCMPA': 'MSc Computing',
    'PFMSCMPB': 'MSc Computing with Placement',
    'PPMSCMPA': 'MSc Computing (Part Time)',
    'PFMSCITA': 'MSc Computing and IT Management',
    'PFMSCITB': 'MSc Computing and IT Management with Placement',
    'PPMSCITA': 'MSc Computing and IT Management (Part Time)',
    'PFMSADSA': 'MSc Advanced Computer Science',
    'PFMSADSB': 'MSc Advanced Computer Science with Placement',
    'PPMSADSA': 'MSc Advanced Computer Science (Part Time)',
    'PFMSISPA': 'MSc Information Security and Privacy',
    'PPMSISPA': 'MSc Information Security and Privacy (Part Time)',
    'PFMSCOJA': 'MSc Computational Journalism',
    'PFMSCDJA': 'MSc Computational and Data Journalism',
    'PFMSDSYA': 'MSc Data Science and Analytics',
    'PPMSDSYA': 'MSc Data Science and Analytics (Part Time)',
}

prog_codes_2_prog_name_short = {
    'PFMSCMPA': 'MSc Computing',
    'PFMSCMPB': 'MSc Computing',
    'PPMSCMPA': 'MSc Computing',
    'PFMSCITA': 'MSc Computing and IT Management',
    'PFMSCITB': 'MSc Computing and IT Management',
    'PPMSCITA': 'MSc Computing and IT Management',
    'PFMSADSA': 'MSc Advanced Computer Science',
    'PFMSADSB': 'MSc Advanced Computer Science',
    'PPMSADSA': 'MSc Advanced Computer Science',
    'PFMSISPA': 'MSc Information Security and Privacy',
    'PPMSISPA': 'MSc Information Security and Privacy',
    'PFMSCOJA': 'MSc Computational and Data Journalism',
    'PFMSCDJA': 'MSc Computational and Data Journalism',
    'PFMSDSYA': 'MSc Data Science and Analytics',
    'PPMSDSYA': 'MSc Data Science and Analytics',
}

prog_name_short_2_prog_codes = {
    'MSc Computing': ['PFMSCMPA', 'PFMSCMPB', 'PPMSCMPA'],
    'MSc Computing and IT Management': ['PFMSCITA', 'PFMSCITB', 'PPMSCITA'],
    'MSc Advanced Computer Science': ['PFMSADSA', 'PFMSADSB', 'PPMSADSA'],
    'MSc Information Security and Privacy' : ['PFMSISPA', 'PPMSISPA'],
    'MSc Computational and Data Journalism': ['PFMSCOJA', 'PFMSCDJA'],
    'MSc Data Science and Analytics': ['PFMSDSYA', 'PPMSDSYA']
}


computing = ['PFMSCMPA', 'PFMSCMPB', 'PPMSCMPA']
computingit = ['PFMSCITA', 'PFMSCITB', 'PPMSCITA']
advanced = ['PFMSADSA', 'PFMSADSB', 'PPMSADSA']
compj = ['PFMSCOJA', 'PFMSCDJA']
datasci = ['PFMSDSYA', 'PPMSDSYA']
infsec = ['PFMSISPA', 'PPMSISPA']

statuses = [
    'Registered',
    'Registered - Not Collected ID Card',
    'Pending Registration New Entrant',
    'Pending Registration',
    'Absent'
]
