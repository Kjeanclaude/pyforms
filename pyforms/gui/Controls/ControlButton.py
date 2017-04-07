#!/usr/bin/python
# -*- coding: utf-8 -*-



from pysettings import conf

if conf.PYFORMS_USE_QT5:
	from PyQt5.QtWidgets import QPushButton
	from PyQt5.QtWidgets import QSizePolicy
	from PyQt5.QtGui import QIcon
	from PyQt5 import uic
else:
	from PyQt4.QtGui import QPushButton
	from PyQt4.QtGui import QSizePolicy
	from PyQt4.QtGui import QIcon
	from PyQt4 import uic

from pyforms.gui.Controls.ControlBase import ControlBase


class ControlButton(ControlBase):
	def __init__(self, label='', default=None, checkable=False, helptext=None):
		self._checkable = checkable
		super(ControlButton, self).__init__(label=label, default=default, helptext=helptext)

	def init_form(self):
		self._form = QPushButton()
		self._form.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
		self._form.setCheckable(self._checkable)
		self.label = self._label
		self._form.setToolTip(self.help)

	def click(self):
		self._form.click()

	def load_form(self, data, path=None):
		pass

	def save_form(self, data, path=None):
		pass

	##########################################################################

	@property
	def label(self):
		return ControlBase.label.fget(self)

	@label.setter
	def label(self, value):
		ControlBase.label.fset(self, value)
		self._form.setText(self._label)

	@property
	def icon(self):
		return self._form.icon()

	@icon.setter
	def icon(self, value):
		if isinstance(value, (str, bytes)):
			self._form.setIcon(QIcon(value))
		else:
			self._form.setIcon(value)

	##########################################################################

	@property
	def value(self):
		return None

	@value.setter
	def value(self, value):
		try:
			self._form.clicked.disconnect()  # ignore previous signals if any
		except TypeError as err:
			# http://stackoverflow.com/questions/21586643/pyqt-widget-connect-and-disconnect
			pass
		self._form.clicked[bool].connect(value)

	@property
	def checked(self):
		return self._form.isChecked()

	@checked.setter
	def checked(self, value):
		self._form.setChecked(value)
