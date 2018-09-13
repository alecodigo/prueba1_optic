# -*- coding : utf-8 -*-

{
	
	'name' : 'To-do list',
    'version' : '0.1',
    "author" : "Alejandro Sanchez",
    'website' : 'https://github.com/alejandrohetaroi',
    'summary' : 'Modulo de tareas',
    'description' : """ Organice las tareas pendientes """,
    'depends': [
                'base'
	           ],

    'data': [
                'security/ir.model.access.csv',
                'views/todolist_view.xml'
            ],
    
    'installable': True,
    'auto_install': False,
    'application': True,


}