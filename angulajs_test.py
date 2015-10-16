# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta
from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
from openerp.tools.translate import _
import simplejson

try:
    from openerp import SUPERUSER_ID
except ImportError:
    SUPERUSER_ID = SUPERUSER_ID
 
class angulajs_test(osv.Model):
    _name = "angulajs.test"
    _description = "angulaJS_test"

    _columns = {
                 'name' : fields.char(u'编码',size=64,  help="编码")
    }