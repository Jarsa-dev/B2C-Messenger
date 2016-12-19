# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class BtocUser(models.Model):
    _inherit = 'res.partner'
    _name = 'btoc.user'

    telegram_id = fields.Char(string='Telegram chat identifier')
