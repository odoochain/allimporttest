from odoo import models, fields, api

class SaleOrder_Data(models.Model):
    _inherit = 'sale.order'
    order_ref = fields.Float(string = 'Sales Order Ref')

class AccountMove_Data(models.Model):
    _inherit = 'account.move'
    salesorder_id = fields.Many2one('sale.order', string='Sales Order Id')
    sale_order_ref = fields.Float(related = 'salesorder_id.order_ref', store = True)

    @api.depends('line_ids')
    def _cal_total_discount(self):
        for order in self:
            cal_discount = 0
            for line_items in self:
                cal_discount = cal_discount + (line_items.price_unit * line_items.discount) / 100
            order.calculated_discount = cal_discount
        

    calculated_discount = fields.Float(string = 'Discount', compute = '_cal_total_discount', store = True)
