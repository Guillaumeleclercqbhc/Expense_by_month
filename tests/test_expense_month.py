# -*- coding: utf-8 -*-

from openerp.tests import common


class Test_expense_month(common.TransactionCase):

    def setUp(self):
        """*****setUp*****"""
        super(Test_expense_month, self).setUp()
        print "Testing "
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