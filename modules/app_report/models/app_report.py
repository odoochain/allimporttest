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
        

    calculated_discount = fields.Float(string = 'Discount', compute = '_cal_total_discount', store = True, digits=(12,4))

    @api.depends('line_ids.price_unit','line_ids.quantity')
    def _cal_total_price(self):
        for order in self:
            cal_discount = 0
            for line_items in order.line_ids:
                cal_discount = cal_discount + (line_items.quantity * line_items.price_unit )
            # _logger.warning('*************************************')
            # _logger.warning("IT IS warn")
            # _logger.warning(cal_discount)
            order.total_price = cal_discount
        

    total_price = fields.Float(string = 'Total Price', compute = '_cal_total_price', store = True, digits=(12,4))

    @api.depends('calculated_discount', 'total_price')
    def _cal_total_baht_escl_vat(self):
        for orders in self:
            orders.total_baht_excl_VAT = orders.total_price - orders.calculated_discount

    total_baht_excl_VAT = fields.Float(string = 'Total Baht Excl VAT', compute = '_cal_total_baht_escl_vat', store= True, digits=(12,4))

    @api.depends('total_baht_excl_VAT')
    def _cal_total_baht_incl_vat(self):
        for orders in self:
            orders.total_baht_incl_VAT = orders.total_baht_excl_VAT / 1.07

    total_baht_incl_VAT = fields.Float(string = 'Total Baht Incl VAT', compute = '_cal_total_baht_incl_vat', store = True, digits=(12,4))

    @api.depends('total_baht_excl_VAT','total_baht_incl_VAT')
    def _cal_total_vat(self):
        for orders in self:
            orders.vat = orders.total_baht_incl_VAT - orders.total_baht_excl_VAT

    vat = fields.Float(string = 'Vat', compute = '_cal_total_vat', store = True, digits=(12,4))

    



class AccountMove_Line_Data(models.Model):
    _inherit = 'account.move.line'
    move_line_id = fields.Many2one('account.move', string='Move Id')

