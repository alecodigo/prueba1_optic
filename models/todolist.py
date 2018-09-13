# -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError



class ToDoList(models.Model):
	"""  Todo class permitirá crear nuestras tareas y listarlas """
	_name = "to.do.list"
	_description = "to-do list app"
	#_rec_name =

	name = fields.Char('Tarea', required=True)
	date_end = fields.Date('Fecha de Finalizacion', help="Realizada en la Fecha Indicada por el usuario")
	date_deadline = fields.Date('Fecha Limite', required=True, help="Fecha limite para culminar las tareas")
	state = fields.Selection([('pendiente','Pendiente'),('resuelta','Resuelta')],'Estado', default='pendiente')
	observacion = fields.Text('observacion', help="Ingrese algun comentario sobre la tarea")




#class ResUsersExtended(models.Model):
#    _name = 'res.users'
#    _inherit = 'res.users'
