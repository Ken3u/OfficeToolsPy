import io
import html
import os.path
import codecs

import uno
import unohelper

from com.sun.star.awt.FontWeight import (NORMAL, BOLD)
from com.sun.star.awt.FontUnderline import (SINGLE, NONE)
from com.sun.star.awt.FontSlant import (NONE, ITALIC)

from com.sun.star.task import XJobExecutor

class FindSources(unohelper.Base, XJobExecutor):
	def __init__(self, ctx):
		'''Конструктор класса'''
		# Сохранение контекста компонента для последующего использования 
		self.ctx = ctx
	
	
	def trigger(self, event):
		'''Обработчик события'''
		# Получение объекта рабочего стола
		desktop = self.ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", self.ctx)
		# Получение объекта текущего документа
		document = desktop.getCurrentComponent()
		# Проверка возможности доступа к тексту документа
		if not hasattr(document, "Text"):
			return
		controller = document.getCurrentController()
		select = controller.getSelection()
		count = select.getCount()
		for i in range(count) :
			symbol = select.getByIndex(i)
			theString = symbol.getString()
			if len(theString)!=0 :
				#get the XText interface
				text = document.Text
				#create an XTextRange at the end of the document
				tRange = text.End
				#and set the string
				tRange.String = str(3)
		
		
# Регистрация реализации службы
g_ImplementationHelper = unohelper.ImplementationHelper()

g_ImplementationHelper.addImplementation( \
		FindSources,                                # Имя класса UNO
		"org.openoffice.comp.pyuno.exp.FindSources",# Имя реализации
		("com.sun.star.task.Job",),)                # Список реализованных служб
