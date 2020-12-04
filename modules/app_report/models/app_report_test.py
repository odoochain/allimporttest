from odoo import models, fields, api


class Test_AccountMove(models.Model):
    _inherit = 'account.move'

    channel_order_no = fields.Float(string = 'Channel Order No.', readonly=True , tracking=True)
"""
    @api.depends('line_ids.price_unit', 'line_ids.invoice_seller_discount','line_ids.quantity')
    def _cal_total_seller_discount(self):
        for order in self:
            cal_seller_discount = 0
            for line_items in order.line_ids:
                cal_seller_discount = cal_seller_discount + (line_items.quantity * line_items.price_unit * line_items.invoice_seller_discount) / 100
            order.calculated_seller_discount = cal_seller_discount
        

    calculated_seller_discount = fields.Float(string = 'Total Seller Discount', compute = '_cal_total_seller_discount', store = True, digits=(12,4))
"""
class Test_AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    invoice_seller_discount = fields.Float(string = 'Seller Discount')    


class Test_SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    seller_discount = fields.Float(string = 'Seller Discount',readonly=True)


class Test_SaleOrder(models.Model):
    _inherit = 'sale.order'
"""
    def _prepare_invoice(self):
        
        #Prepare the dict of values to create the new invoice for a sales order. This method may be
        #overridden to implement custom invoice generation (making sure to call super() to establish
        #a clean extension chain).
        
        self.ensure_one()
        journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
        if not journal:
            raise UserError(_('Please define an accounting sales journal for the company %s (%s).') % (self.company_id.name, self.company_id.id))

        invoice_vals = {
            'ref': self.client_order_ref or '',
            'move_type': 'out_invoice',
            'narration': self.note,
            'currency_id': self.pricelist_id.currency_id.id,
            'campaign_id': self.campaign_id.id,
            'medium_id': self.medium_id.id,
            'source_id': self.source_id.id,
            'invoice_user_id': self.user_id and self.user_id.id,
            'team_id': self.team_id.id,
            'partner_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id.get_fiscal_position(self.partner_invoice_id.id)).id,
            'partner_bank_id': self.company_id.partner_id.bank_ids[:1].id,
            'journal_id': journal.id,  # company comes from the journal
            'invoice_origin': self.name,
            'invoice_payment_term_id': self.payment_term_id.id,
            'payment_reference': self.reference,
            'transaction_ids': [(6, 0, self.transaction_ids.ids)],
            'invoice_line_ids': ['invoice_seller_discount':self.seller_discount],
            'company_id': self.company_id.id,
        }
        return invoice_vals
"""
    







