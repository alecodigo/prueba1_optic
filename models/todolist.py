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
	formacion = fields.Boolean('')




class formacion(models.Model):
	""" Modelo de Formacion """
	_name = 'formacion'
    #_rec_name = 'id_cliente'
    #_description = 'Cartera de Clientes de la empresa'


	formacion = fields.Char('Formacion', help="Indique nombre de la formacion")
	date = fields.Date('Fecha de Inicio', help="Indique la fecha de inicio")
	date_end = fields.Date('Fecha de culminacion', help="Indique la fecha de culminacion")
	state = fields.Selection([('encurso', 'En curso'),
								('finalizada','Finalizada'),
								('pausada','Pausada'),
								],"Estatus")
	notas = fields.Text('Observaciones', help="Indique alguna observacion")
	progreso = fields.Float('Progreso', help="progreso del aprendizaje")
	meta = fields.Char('Meta', help="Indique el objetivo el cual se plantea llegar para adquirir una habilidad")




class FormacionDificultades(models.Model):
	""" Dificultades encontradas en el proceso formativo"""
	_name = 'formacion.dificultades'
	#_rec_name =''
	#_description = ''
	
	dificultad = fields.Char('Dificultades', help="Ingrese dificultad")
	observacion = fields.Text('Observaciones')



class FormacionPlanEstudio(models.Model):
	""" Temas a estudiar """
	_name = 'formacion.plan.estudio'
	#_rec_name = ''
	#_description = ''

	name = fields.Char('name', help="Nombre del tema a estudiar")
	date_expected = fields.Date('Fecha Estimada', help="Fecha esperada para estudiar un tema")
	date_start = fields.Date('Fecha de Inicio', help="Fecha real en la cual se empieza a estudiar un tema")
	date_end = fields.Date('Fecha de Termino', Help="Fecha de finalizacion de estudio de un tema")


# crear un modelo que me permita anotar para investigar un tema o algo 
# que me llame la atencion para no olvidarlo e investigarlo luego