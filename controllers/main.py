# -*- coding: utf-8 -*-
##############################################################################
#
#    Better WYSIWYG Cleditor
#    Copyright 2014 wangbuke <wangbuke@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request
from openerp.tools.translate import _


class angulaJS(http.Controller):
    @http.route('/angula/index', type='http', auth="public")
    def liuhao(self,  **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        
        return http.local_redirect('/angulaJS/static/src/index.html')
