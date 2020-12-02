from odoo import models, fields, api
import logging


_logger = logging.getLogger(__name__)

class SaleOrder_Data(models.Model):
    _inherit = 'sale.order'
    order_ref = fields.Float(string = 'Sales Order Ref')

class AccountMove_Data(models.Model):
    _inherit = 'account.move'
    salesorder_id = fields.Many2one('sale.order', string='Sales Order Id')
    sale_order_ref = fields.Float(related = 'salesorder_id.order_ref', store = True)
    # line_items_id = fields.One2many('account.move.line', 'move_id', string='Invoice Items Line')

    # line_items_ids = fields.One2many('account.move.line', 'move_line_id', string='Invoice Items')

    @api.depends('line_ids.price_unit', 'line_ids.discount','line_ids.quantity')
    def _cal_total_discount(self):
        for order in self:
            cal_discount = 0
            for line_items in order.line_ids:
                cal_discount = cal_discount + (line_items.quantity * line_items.price_unit * line_items.discount) / 100
            # _logger.warning('*************************************')
            # _logger.warning("IT IS warn")
            # _logger.warning(cal_discount)
            order.calculated_discount = cal_discount
        

    calculated_discount = fields.Float(string = 'Discount', compute = '_cal_total_discount', store = True)

class AccountMove_Line_Data(models.Model):
    _inherit = 'account.move.line'
    move_line_id = fields.Many2one('account.move', string='Move Id')

