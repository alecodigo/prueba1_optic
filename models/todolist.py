# -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError



class ToDoList(models.Model):
	"""  Todo class permitirá crear nuestras tareas y listarlas """
	_name = "to.do.list"
	_description = "to-do list app"
	_rec_name = 'name'

	name = fields.Char('Tarea', required=True)
	date_end = fields.Date(string='Fecha de Finalizacion', help="Realizada en la Fecha Indicada por el usuario")
	date_deadline = fields.Date(string='Fecha Limite', required=True, help="Fecha limite para culminar las tareas")
	state = fields.Selection([('pendiente','Pendiente'),('resuelta','Resuelta')],string='Estado', default='pendiente')
	observacion = fields.Text(string='observacion', help="Ingrese algun comentario sobre la tarea")
	topics_ids = fields.One2many('formacion.plan.estudio', 'todo_id', string='Topics')
	formacion = fields.Boolean(string='Training')


	def formacion(self):
		self.formacion = True




class FormacionDificultades(models.Model):
	""" Dificultades encontradas en el proceso formativo"""
	_name = 'formacion.dificultades'
	#_rec_name =''
	#_description = ''
	
	dificultad = fields.Char(string='Dificultades', help="Ingrese dificultad")
	observacion = fields.Text(string='Observaciones')



class FormacionPlanEstudio(models.Model):
	""" Temas a estudiar """
	_name = 'formacion.plan.estudio'
	#_rec_name = ''
	#_description = ''

	name = fields.Char(string='Nombre', help="Nombre del tema a estudiar")
	date_expected = fields.Date(string='Fecha Estimada', help="Fecha esperada para estudiar un tema")
	date_start = fields.Date(string='Fecha de Inicio', help="Fecha real en la cual se empieza a estudiar un tema")
	date_end = fields.Date(string='Fecha de Termino', Help="Fecha de finalizacion de estudio de un tema")
	todo_id = fields.Many2one('to.do.list', string='Task')

# crear un modelo que me permita anotar para investigar un tema o algo 
# que me llame la atencion para no olvidarlo e investigarlo luego