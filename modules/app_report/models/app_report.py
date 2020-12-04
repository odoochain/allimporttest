from odoo import models, fields, api



class SaleOrder_Data(models.Model):
    _inherit = 'sale.order'

    channel_order_number = fields.Char(string = 'Channel Order No.')

    def _prepare_invoice(self):
        
        #Prepare the dict of values to create the new invoice for a sales order. This method may be
        #overridden to implement custom invoice generation (making sure to call super() to establish
        #a clean extension chain).
        
        self.ensure_one()
        journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
        if not journal:
            raise UserError(('Please define an accounting sales journal for the company %s (%s).') % (self.company_id.name, self.company_id.id))

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
            'channel_order_number':self.channel_order_number,
            'partner_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id.get_fiscal_position(self.partner_invoice_id.id)).id,
            'partner_bank_id': self.company_id.partner_id.bank_ids[:1].id,
            'journal_id': journal.id,  # company comes from the journal
            'invoice_origin': self.name,
            'invoice_payment_term_id': self.payment_term_id.id,
            'payment_reference': self.reference,
            'transaction_ids': [(6, 0, self.transaction_ids.ids)],
            'invoice_line_ids': [],
            'company_id': self.company_id.id,
        }
        return invoice_vals

class AccountMove_Data(models.Model):
    _inherit = 'account.move'

    seller_discount = fields.Float(string = 'Seller Discount',readonly=True, tracking=True)

    channel_order_number = fields.Char(string = 'Channel Order No.',readonly=True, tracking=True)
    
    @api.depends('line_ids.price_unit', 'line_ids.discount','line_ids.quantity')
    def _cal_total_discount(self):
        for order in self:
            cal_discount = 0
            for line_items in order.line_ids:
                cal_discount = cal_discount + (line_items.quantity * line_items.price_unit * line_items.discount) / 100
            order.calculated_discount = cal_discount
        

    calculated_discount = fields.Float(string = 'Discount', compute = '_cal_total_discount', store = True, digits=(12,4))

    @api.depends('amount_untaxed','calculated_discount')
    def _cal_grand_total(self):
        for order in self:
            order.grand_total = order.amount_untaxed + order.calculated_discount

    grand_total = fields.Float(string = 'Grand Total', store = True, compute = '_cal_grand_total')

    @api.depends('calculated_discount', 'grand_total')
    def _cal_total_baht_escl_vat(self):
        for orders in self:
            orders.total_baht_excl_VAT = orders.grand_total - orders.calculated_discount

    total_baht_excl_VAT = fields.Float(string = 'Total Baht Excl VAT', compute = '_cal_total_baht_escl_vat', store= True, digits=(12,4))

    @api.depends('total_baht_excl_VAT')
    def _cal_total_baht_incl_vat(self):
        for orders in self:
            orders.total_baht_incl_VAT = orders.total_baht_excl_VAT * 1.07

    total_baht_incl_VAT = fields.Float(string = 'Total Baht Incl VAT', compute = '_cal_total_baht_incl_vat', store = True, digits=(12,4))

    @api.depends('total_baht_excl_VAT','total_baht_incl_VAT')
    def _cal_total_vat(self):
        for orders in self:
            orders.vat = orders.total_baht_incl_VAT - orders.total_baht_excl_VAT

    vat = fields.Float(string = 'Vat', compute = '_cal_total_vat', store = True, digits=(12,4))

    



class AccountMove_Line_Data(models.Model):
    _inherit = 'account.move.line'
    move_line_id = fields.Many2one('account.move', string='Move Id')

