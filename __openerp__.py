# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution	
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'HR Expenses Upgrade',
    'version': '1.0',
    'category': 'Generic Modules/Human Resources',
    'description': """
    This module aims to manage employee's expenses.

    This module is an addons to add a dropdown list with the different months of a year
	
	This module is for BHC because the report is on the module BHC_report.
    """,
    'author': 'BHC',
    'website': 'www.bhc.be',
    'depends': ['base','hr_expense'],
    'data': ['hr_expense_bhc_months_view.xml'],
    'installable': True,
    'active': False,
}
