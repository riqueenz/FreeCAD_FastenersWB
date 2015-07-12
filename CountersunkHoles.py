﻿# -*- coding: utf-8 -*-
###################################################################################
#
#  CountersunkHoles.py
#  
#  Copyright 2015 Shai Seger <shaise at gmail dot com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
###################################################################################

###################################################################################
# replace below with generated code from pyuic4
###################################################################################


from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DlgCountersunktHoles(object):
    def setupUi(self, DlgCountersunktHoles):
        DlgCountersunktHoles.setObjectName(_fromUtf8("DlgCountersunktHoles"))
        DlgCountersunktHoles.resize(424, 426)
        self.gridLayout_2 = QtGui.QGridLayout(DlgCountersunktHoles)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(DlgCountersunktHoles)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.hboxlayout = QtGui.QHBoxLayout(self.groupBox)
        #self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.labelBaseObject = QtGui.QLabel(self.groupBox)
        self.labelBaseObject.setObjectName(_fromUtf8("labelBaseObject"))
        self.hboxlayout.addWidget(self.labelBaseObject)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(DlgCountersunktHoles)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hboxlayout1 = QtGui.QHBoxLayout()
        #self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.labelRadius = QtGui.QLabel(self.groupBox_2)
        self.labelRadius.setObjectName(_fromUtf8("labelRadius"))
        self.hboxlayout1.addWidget(self.labelRadius)
        self.comboDiameter = QtGui.QComboBox(self.groupBox_2)
        self.comboDiameter.setObjectName(_fromUtf8("comboDiameter"))
        self.comboDiameter.addItem(_fromUtf8(""))
        self.hboxlayout1.addWidget(self.comboDiameter)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.gridLayout.addLayout(self.hboxlayout1, 2, 0, 1, 6)
        self.selectNoneButton = QtGui.QPushButton(self.groupBox_2)
        self.selectNoneButton.setObjectName(_fromUtf8("selectNoneButton"))
        self.gridLayout.addWidget(self.selectNoneButton, 0, 5, 1, 1)
        self.treeView = QtGui.QTreeView(self.groupBox_2)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout.addWidget(self.treeView, 1, 0, 1, 6)
        self.selectAllButton = QtGui.QPushButton(self.groupBox_2)
        self.selectAllButton.setObjectName(_fromUtf8("selectAllButton"))
        self.gridLayout.addWidget(self.selectAllButton, 0, 4, 1, 1)
        self.selectFaces = QtGui.QRadioButton(self.groupBox_2)
        self.selectFaces.setObjectName(_fromUtf8("selectFaces"))
        self.gridLayout.addWidget(self.selectFaces, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(221, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.selectEdges = QtGui.QRadioButton(self.groupBox_2)
        self.selectEdges.setChecked(True)
        self.selectEdges.setObjectName(_fromUtf8("selectEdges"))
        self.gridLayout.addWidget(self.selectEdges, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.retranslateUi(DlgCountersunktHoles)
        QtCore.QMetaObject.connectSlotsByName(DlgCountersunktHoles)

    def retranslateUi(self, DlgCountersunktHoles):
        DlgCountersunktHoles.setWindowTitle(_translate("DlgCountersunktHoles", "Countersunk screw holes", None))
        self.groupBox.setTitle(_translate("DlgCountersunktHoles", "Shape", None))
        self.label.setText(_translate("DlgCountersunktHoles", "Base shape:", None))
        self.labelBaseObject.setText(_translate("DlgCountersunktHoles", "Base", None))
        self.groupBox_2.setTitle(_translate("DlgCountersunktHoles", "Fillet Parameter", None))
        self.labelRadius.setText(_translate("DlgCountersunktHoles", "Diameter:", None))
        self.comboDiameter.setItemText(0, _translate("DlgCountersunktHoles", "No selection", None))
        self.selectNoneButton.setText(_translate("DlgCountersunktHoles", "None", None))
        self.selectAllButton.setText(_translate("DlgCountersunktHoles", "All", None))
        self.selectFaces.setText(_translate("DlgCountersunktHoles", "Select faces", None))
        self.selectEdges.setText(_translate("DlgCountersunktHoles", "Select edges", None))

        ###################################################################################
        # End position for generated code from pyuic4
        ###################################################################################

    def fillTable(self, parent, baseObj, edgelist):
        #DiamModel = FSDiameterModel(FSFilletDialog)
        DiamModel = FSDiameterModel(parent)
        DiamModel.insertColumns(0,2);
        DiamModel.setHeaderData(0, QtCore.Qt.Horizontal, "Edges to chamfer", QtCore.Qt.DisplayRole)
        DiamModel.setHeaderData(1, QtCore.Qt.Horizontal, "Diameter", QtCore.Qt.DisplayRole)
        edges = []
        for i in range(len(baseObj.Shape.Edges)):
          edge = 'Edge' + str(i + 1)
          if FSIsValidEdge(baseObj, edge):
            edges.append(edge)
        nedges = len(edges)
        DiamModel.insertRows(0, nedges)
        
        self.treeView.setRootIsDecorated(False)
        self.treeView.setItemDelegate(FSDiameterDelegate(parent))
        self.treeView.setModel(DiamModel)
        self.model = DiamModel

        header = self.treeView.header()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setDefaultAlignment(QtCore.Qt.AlignLeft)
        header.setMovable(False)
        
        edgediams = {}
        for edgediam in edgelist:
           edge,diam,invert = edgediam.split(':')
           edgediams[edge] = diam

        for i in range(nedges):
          edge = edges[i]
          DiamModel.setData(DiamModel.index(i,0), edge)
          if edge in edgediams:
            DiamModel.setData(DiamModel.index(i,0), QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)
            DiamModel.setData(DiamModel.index(i,1), edgediams[edge])
          else:
            #DiamModel.setData(DiamModel.index(i,0), i, QtCore.Qt.UserRole)
            DiamModel.setData(DiamModel.index(i,0), QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
            DiamModel.setData(DiamModel.index(i,1), "M2")
          
    def GetData(self):
        DiamModel = self.model
        nedges = DiamModel.rowCount()
        listEdges = []
        for i in range (nedges):
            if DiamModel.data(DiamModel.index(i,0), QtCore.Qt.CheckStateRole) == QtCore.Qt.Unchecked:
                continue
            listEdges.append(DiamModel.data(DiamModel.index(i,0)) + ':' + DiamModel.data(DiamModel.index(i,1)) + ':0')
        return listEdges
        
    def AddEdges(self, edges):
        DiamModel = self.model
        nedges = DiamModel.rowCount()
        self.treeView.selectionModel().clearSelection()
        for edge in edges:
            for i in range (nedges):
                if DiamModel.data(DiamModel.index(i,0)) == edge:
                    DiamModel.setData(DiamModel.index(i,0), QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)
                    index = DiamModel.index(i, 0);
                    self.treeView.selectionModel().select(index, QtGui.QItemSelectionModel.Select)

from FreeCAD import Gui
from FreeCAD import Base
import FreeCAD, FreeCADGui, Part, os, math
__dir__ = os.path.dirname(__file__)
iconPath = os.path.join( __dir__, 'Icons' )

import FastenerBase
from FastenerBase import FSBaseObject


class FSDiameterDelegate(QtGui.QItemDelegate):
    def createEditor(self, parent, option, index):
        if index.column() < 1:
            return None

        editor = QtGui.QComboBox(parent)
        editor.addItems(FSCSHSizes)
        return editor;

    def setEditorData(self, editor, index):
        value = index.data(QtCore.Qt.EditRole)
        index = editor.findText(value)
        if index >= 0:
          editor.setCurrentIndex(index)

    def setModelData(self, editor, model, index):
        value = editor.currentText()
        model.setData(index, value, QtCore.Qt.EditRole)

    def pdateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
        

class FSDiameterModel(QtGui.QStandardItemModel):
    def updateCheckStates(self):
        self.layoutChanged()

    def flags(self, index):
        #fl = QtGui.QStandardItemModel.flags(index)
        fl = super(FSDiameterModel, self).flags(index)
        if index.column() == 0:
            #FreeCAD.Console.PrintLog(str(fl) + "\n")
            fl = fl | QtCore.Qt.ItemIsUserCheckable
        return fl
    
    def setData(self, index, value, role = QtCore.Qt.EditRole):
        #ok = QStandardItemModel::setData(index, value, role);
        ok = super(FSDiameterModel, self).setData(index, value, role)
        #if role == QtCore.Qt.CheckStateRole:
        #    self.toggleCheckState(index)
        return ok
        
   
        
#    connect(model, SIGNAL(toggleCheckState(const QModelIndex&)),
#            this, SLOT(toggleCheckState(const QModelIndex&)));
#    // timer for highlighting
#    d->highlighttimer = new QTimer(this);
#    d->highlighttimer->setSingleShot(true);
#    connect(d->highlighttimer,SIGNAL(timeout()),
#            this, SLOT(onHighlightEdges()));


def FSIsValidEdge(obj, edge):
  #FreeCAD.Console.PrintLog("IsValid " + str(obj) + ":" + str(edge) + "\n")
  shape = obj.Shape.getElement(edge)
  if shape == None:
    return False
  if not(hasattr(shape,"Curve")):
    return False
  if not(hasattr(shape.Curve,"Center")):
    return False
  return True
  
        
class FSSelectionFilter:
  ''' A selection filter that let the user select only the edges that are circular '''
  def allow(self,doc,obj,sub):
    if obj == None or sub == None or len(sub) == 0:
      return True
    if sub[0:4] == 'Face':
      return True
    #FreeCAD.Console.PrintLog("testing " + str(obj) + ":" + str(sub) + str(len(sub)) + "\n")
    if FSIsValidEdge(obj, sub) == False:
      return False
    #self.lastobj = obj.Name
    #self.lastedge = sub
    return True
    
    
FSSelectionFilterGate = FSSelectionFilter()

class FSSelObserver:
  ''' monitor selection changes to update the task form '''
  def __init__(self, dialog):
    self.dialog = dialog
    self.disableObserver = False
    
  def addSelection(self,doc,obj,sub,pnt):
    if self.disableObserver:
      return
    FreeCAD.Console.PrintLog("FSO-AddSel:" +str(obj) + ":" + str(sub) + "\n")
    #if len(sub) == 0 and obj == FSSelectionFilterGate.lastobj:
    #  self.dialog.addSelection(FSSelectionFilterGate.lastedge)
    if sub[0:4] == 'Edge':
      self.dialog.addSelectionEdge(sub)
    elif sub[0:4] == 'Face':
      self.dialog.addSelectionFace(sub)
    return True
      
  def removeSelection(self,doc,obj,sub):                # Delete the selected object
    FreeCAD.Console.PrintLog("FSO-RemSel:" +str(obj) + ":" + str(sub) + "\n")
    
  def setSelection(self,doc):                           # Selection in ComboView
    FreeCAD.Console.PrintLog("FSO-SetSel:" + "\n")
    
  def clearSelection(self,doc):                         # If click on the screen, clear the selection
    FreeCAD.Console.PrintLog("FSO-ClrSel:" + "\n")
    

import sys

#FSFilletDialog.ui.FillData()

class FSTaskFilletDialog:
    def __init__(self, obj):
        self.object = obj
        if obj == None:
            self.baseObj = Gui.Selection.getSelection()[0]
            edgelist = []
        else:
            edgelist = obj.diameters
            self.baseObj = obj.baseObject[0]
            Gui.ActiveDocument.getObject(obj.Name).Visibility = False
            Gui.ActiveDocument.getObject(self.baseObj.Name).Visibility = True
        FSFilletDialog = QtGui.QWidget()
        FSFilletDialog.ui = Ui_DlgCountersunktHoles()
        FSFilletDialog.ui.setupUi(FSFilletDialog)
        FreeCAD.Console.PrintLog(str(self.baseObj) + "\n")
        FSFilletDialog.ui.fillTable(FSFilletDialog, self.baseObj, edgelist)
        FSFilletDialog.ui.labelBaseObject.setText(self.baseObj.Name)
        FSFilletDialog.ui.model.itemChanged.connect(self.onItemChanged)
                
        self.form = FSFilletDialog
        self.form.setWindowTitle("Chamfer holes for countersunk screws")
        Gui.Selection.addSelectionGate(FSSelectionFilterGate)
        self.selobserver = FSSelObserver(self) 
        Gui.Selection.addObserver(self.selobserver) 
        self.RefreshSelection()
        
    def accept(self):
        if (self.object == None):
          a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Countersunks")
          FSCountersunkObject(a, self.baseObj)
          #a.ViewObject.Proxy = 0
          FSViewProviderCountersunk(a.ViewObject)
        else:
          a = self.object
        a.diameters = self.form.ui.GetData()
        FreeCAD.Console.PrintLog(str(a.diameters) + "\n")
        FreeCAD.ActiveDocument.recompute()
        self.DialogClosing()
        return True
        
    def reject(self):
        self.DialogClosing()
        return True
        
    def DialogClosing(self):
        if self.object != None:
          Gui.ActiveDocument.getObject(self.object.Name).Visibility = True
          Gui.ActiveDocument.getObject(self.baseObj.Name).Visibility = False
        Gui.ActiveDocument.resetEdit()
        Gui.Selection.removeSelectionGate()
        Gui.Selection.removeObserver(self.selobserver) 
    
    def getStandardButtons(self):
        return int(QtGui.QDialogButtonBox.Ok) + int(QtGui.QDialogButtonBox.Cancel)
        
    def addSelectionEdge(self, edge):
        self.form.ui.AddEdges([edge])
        self.RefreshSelection()

    def addSelectionFace(self, name):
        obj = self.baseObj
        face = obj.Shape.getElement(name)
        if face == None:
            return
        edges = []
        for edge in face.Edges:
            if not(hasattr(edge,"Curve")):
                continue
            if not(hasattr(edge.Curve,"Center")):
                continue
            edges.append(FastenerBase.GetEdgeName(obj.Shape, edge))
        self.form.ui.AddEdges(edges)
        self.RefreshSelection()        
        
    def RefreshSelection(self):
        FreeCAD.Console.PrintLog("Refresh: " "\n")
        self.selobserver.disableObserver = True
        Gui.Selection.clearSelection()
        edges = self.form.ui.GetData()
        FreeCAD.Console.PrintLog("Reselect: " +str(edges) + "\n")
        for edge in edges:
          Gui.Selection.addSelection(self.baseObj, edge)
        self.selobserver.disableObserver = False

    def onItemChanged(self, item):
        #FreeCAD.Console.PrintLog("Item change 1: " +str(item) + "\n")
        #try:
        self.RefreshSelection()
        #except:
        #  e = sys.exc_info()[1]
        #FreeCAD.Console.PrintLog("Err: " + str(e) + "\n")
        #FreeCAD.Console.PrintLog("Item change: " +str(item) + "\n")

        
class FSViewProviderCountersunk:
  "A View provider for countersunk holes"
      
  def __init__(self, obj):
    obj.Proxy = self
    self.Object = obj.Object
      
  def attach(self, obj):
    self.Object = obj.Object
    return

  #def updateData(self, fp, prop):
  #  return

  def getDisplayModes(self,obj):
    modes=[]
    return modes

  def setDisplayMode(self,mode):
    return mode

  def onChanged(self, vp, prop):
    return

  def __getstate__(self):
    #        return {'ObjectName' : self.Object.Name}
    return None

  def __setstate__(self,state):
    if state is not None:
      import FreeCAD
      doc = FreeCAD.ActiveDocument #crap
      self.Object = doc.getObject(state['ObjectName'])
 
  def claimChildren(self):
    objs = []
    if hasattr(self.Object,"baseObject"):
      objs.append(self.Object.baseObject[0])
    return objs

  def getIcon(self):
    return os.path.join( iconPath , 'IconCSHole.svg')
    return None

  def setEdit(self,vobj,mode=0):
    #FreeCADGui.runCommand("Draft_Edit")
    Gui.Control.showDialog(FSTaskFilletDialog(self.Object))
    return True

  def unsetEdit(self,vobj,mode=0):
    #self.__vobject__.finishEditing()
    FreeCAD.Console.PrintLog("Finish edit\n")
    #self.finishEditing();
    Gui.Control.closeDialog()
    return False

FSCDSHSizes = ['M3', 'M4', 'M5', 'M6', 'M8', 'M10', 'M12', 'M14', 'M16', 'M20']
FSCSHTable={
    #       d     k
    'M3':  (6.0,  1.86),
    'M4':  (8.0,  2.48),
    'M5':  (10.0, 3.10),
    'M6':  (12.0, 3.72),
    'M8':  (16.0, 4.96),
    'M10': (20.5, 6.20),
    'M12': (25.0, 7.44),
    'M14': (28.4, 8.40),
    'M16': (31.0, 8.80),
    'M20': (38.0, 10.16)}

def cshMakeFace(m, d, k):
  m = m / 2
  d = d / 2
  h1 = m + k
  h2 = k - (d - m)
  
  fm = FastenerBase.FSFaceMaker()
  fm.AddPoint(0, h1)
  fm.AddPoint(d, h2)
  fm.AddPoint(d, -h2)
  fm.AddPoint(0, -h1)
  return fm.GetFace()

def cshMakeCSHole(diam):
  if not(diam in FSCSHTable):
    return None

  (key, shape) = FastenerBase.FSGetKey('CSHole', diam, 0)
  if shape != None:
    return shape
  
  m = float(diam.lstrip('M'))
  d, k = FSCSHTable[diam]
  
  f = cshMakeFace(m, d, k)
  p = f.revolve(Base.Vector(0.0,0.0,0.0),Base.Vector(0.0,0.0,1.0),360)
  FastenerBase.FSCache[key] = p
  return p

    
class FSCountersunkObject:
  def __init__(self, obj, attachTo):
    '''"Add StandOff (self clinching) type fastener" '''
    
    obj.addProperty("App::PropertyStringList","diameters","Parameters","Countersunk diameters").diameters = []
    #obj.addProperty("Part::PropertyFilletEdges","diameters","Parameters","Countersunk diameters").diameters = [(1,1,1), (2,1,1)]
    obj.addProperty("App::PropertyLinkSub", "baseObject", "Parameters", "Base object").baseObject = attachTo
    obj.setEditorMode("diameters", 2)
    obj.Proxy = self
 
  def execute(self, fp):
    '''"Print a short message when doing a recomputation, this method is mandatory" '''
    #fp.Shape = Part.makeBox(1,1,1 + len(fp.diameters))
    fp.Shape = cshMakeCSHole(FSCDSHSizes[len(fp.diameters)])


class FSFilletCommand:
  """Make holes for countersunk screws"""

  def GetResources(self):
    icon = os.path.join( iconPath , 'IconCSHole.svg')
    return {'Pixmap'  : icon , # the name of a svg file available in the resources
            'MenuText': "Make countersunk" ,
            'ToolTip' : "Chamfer holes for countersunk screws"}
 
  def Activated(self):
    Gui.Control.showDialog(FSTaskFilletDialog(None))
    return
   
  def IsActive(self):
    return len(Gui.Selection.getSelectionEx()) == 1

Gui.addCommand("FSFillet", FSFilletCommand())
#FastenerBase.FSCommands.append("FSFillet", "command")

# to monitor selections: add SelObserver http://www.freecadweb.org/wiki/index.php?title=Code_snippets#Function_resident_with_the_mouse_click_action
# to filter selections: use Gui.Selection.SelectionGate