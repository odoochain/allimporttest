from odoo import models, fields, api

class SaleOrder_Data(models.Model):
    _inherit = 'sale.order'
    order_ref = fields.Float(string = 'Sales Order Ref')

class AccountMove_Data(models.Model):
    _inherit = 'account.move'
    salesorder_id = fields.Many2one('sale.order', string='Sales Order Id')
    sale_order_ref = fields.Float(related = 'salesorder_id.order_ref', store = True)
    line_items_id = fields.One2many('account.move.line', 'move_id_item', string='Invoice Items Line')

    @api.depends('line_items_id.price_unit', 'line_items_id.discount')
    def _cal_total_discount(self):
        for order in self:
            cal_discount = 0
            for line_items in order.line_items_id:
                cal_discount = cal_discount + (line_items.price_unit * line_items.discount) / 100
            order.calculated_discount = cal_discount
        

    calculated_discount = fields.Float(string = 'Discount', compute = '_cal_total_discount', store = True)
