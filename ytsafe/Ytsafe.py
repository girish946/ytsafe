# -*- coding: utf-8 -*-
from  org.eclipse.swt.widgets import *
from  org.eclipse.swt.layout import *
from  org.eclipse.swt import SWT
from  org.eclipse.swt.graphics import Image
from java.lang import String
from java.lang.reflect import Array
import java
import threading

class start:
	
	class MyListener(Listener):
		def handleEvent(self, event):
			if event.widget == fetch:
				print "get_details clicked"
			if event.widget == down_load:
				print "download clicked"

	def __init__(self):
		self.display = Display.getDefault()
		self.shell = Shell() 
		self.shell.setSize(423, 362) 
		self.shell.setText("Youtube Video Downloader") 
		self.small = Image(self.display,"images/logo.JPG")
		self.shell.setImage(self.small)
		global urlText 
		urlText= Text (self.shell, SWT.BORDER)
		urlText.setText ("Enter Url Here....")
		urlText.setBounds(10, 36, 276, 29)
		#VideoUrl =self.urlText 
		
		global fetch
		fetch = Button(self.shell, SWT.NONE) 
		self.listener = start.MyListener()
		fetch.addListener(SWT.Selection, self.listener)

		fetch.setBounds(320, 36, 91, 29) 
		fetch.setText("Go") 
		
		global table
		table = Table(self.shell, SWT.BORDER | SWT.FULL_SELECTION) 
		table.setBounds(10, 82, 359, 188) 
		table.setHeaderVisible(True) 
		table.setLinesVisible(True) 
		
		self.tblclmnResolution = TableColumn(table, SWT.NONE) 
		self.tblclmnResolution.setText("Resolution") 
		self.tblclmnResolution.setWidth(100) 
		
		self.tblclmnFilesize = TableColumn(table, SWT.NONE) 
		self.tblclmnFilesize.setText("Extension") 
		self.tblclmnFilesize.setWidth(100) 
		
		self.tblclmnExtension = TableColumn(table, SWT.NONE) 
		self.tblclmnExtension.setText("FileSize") 
		self.tblclmnExtension.setWidth(100) 

		
		global down_load
		down_load = Button(self.shell, SWT.NONE);
		down_load.setBounds(278, 276, 91, 29);
		down_load.setText("Download");
		down_load.addListener(SWT.Selection, self.listener)
		
		self.shell.open()
		self.shell.layout()
		while ( not self.shell.isDisposed()):
			if (not self.display.readAndDispatch()):
				self.display.sleep()

