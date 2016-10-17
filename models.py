from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate
from datetime import datetime, timedelta, date
from dateutil import relativedelta
#Get the logger
_logger = logging.getLogger(__name__)

class account_tipo_tarjeta(models.Model):
	_name = 'account.tipo.tarjeta'
	_description = 'Tipo de tarjeta de credito'

	name = fields.Char('Nombre')


class account_voucher(models.Model):
	_inherit = 'account.voucher'

	nro_cupon = fields.Char('Nro Cupon')
	nro_tarjeta = fields.Char('Nro Tarjeta')
	tipo_tarjeta = fields.Many2one('account.tipo.tarjeta',string='Tipo Tarjeta')

