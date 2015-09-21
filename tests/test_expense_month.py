# -*- coding: utf-8 -*-

from openerp.tests import common


class Test_expense_month(common.TransactionCase):

    def setUp(self):
        """*****setUp*****"""
        super(Test_expense_month, self).setUp()
        self.expense_obj = self.registry('hr.expense.expense')
        self.exp_line_obj = self.registry('hr.expense.line')
        self.product_obj = self.registry('product.product')
        self.tax_obj = self.registry('account.tax')
        self.code_obj = self.registry('account.tax.code')
        _, self.product_id = self.registry("ir.model.data").get_object_reference(cr, uid, "hr_expense", "air_ticket")
        _, self.employee_id = self.registry("ir.model.data").get_object_reference(cr, uid, "hr", "employee_mit")
        self.base_code_id = self.code_obj.create(cr, uid, {'name': 'Expense Base Code'})
        self.tax_id = self.tax_obj.create(cr, uid, {
            'name': 'Expense 10%',
            'amount': 0.10,
            'type': 'percent',
            'type_tax_use': 'purchase',
            'price_include': True,
            'base_code_id': self.base_code_id,
            'base_sign': -1,
        })
        self.product_obj.write(cr, uid, self.product_id, {'supplier_taxes_id': [(6, 0, [self.tax_id])]})
        self.expense_id = self.expense_obj.create(cr, uid, {
            'name': 'Expense for Minh Tran',
            'employee_id': self.employee_id,
            'months': 'Fevrier'
        })
        self.exp_line_obj.create(cr, uid, {
            'name': 'Car Travel Expenses',
            'product_id': self.product_id,
            'unit_amount': 700.00,
            'expense_id': self.expense_id
        })
        '''
        self.demo_user = self.env['res.users'].search([('name', '=', 'Demo User')])
        self.product_bolognese_ref = self.env['ir.model.data'].get_object_reference('lunch', 'product_Bolognese')
        self.product_Bolognese_id = self.product_bolognese_ref and self.product_bolognese_ref[1] or False
        self.new_id_order = self.env['lunch.order'].create({
            'user_id': self.demo_user.id,
            'order_line_ids': '[]',
            })
        self.new_id_order_line = self.env['lunch.order.line'].create({
            'order_id': self.new_id_order.id,
            'product_id': self.product_Bolognese_id,
            'note': '+Emmental',
            'cashmove': [],
            'price': self.env['lunch.product'].browse(self.product_Bolognese_id).price,
            })
        '''