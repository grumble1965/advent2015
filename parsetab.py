
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA LCURLY LSQUARE MINUS NAME NUMBER QUOTE RCURLY RSQUAREelem : list\n            | dict\n            | number\n            | nameempty :number : MINUS NUMBER\n              | NUMBERname : QUOTE NAME QUOTElist : LSQUARE list_elem RSQUARElist_elem : empty\n                 | elem\n                 | elem COMMA list_elemdict : LCURLY dict_list RCURLYdict_list : empty\n                 | dict_elem\n                 | dict_elem COMMA dict_listdict_elem : name COLON elem'
    
_lr_action_items = {'LSQUARE':([0,6,21,24,],[6,6,6,6,]),'LCURLY':([0,6,21,24,],[7,7,7,7,]),'MINUS':([0,6,21,24,],[8,8,8,8,]),'NUMBER':([0,6,8,21,24,],[9,9,18,9,9,]),'QUOTE':([0,6,7,19,21,23,24,],[10,10,10,25,10,10,10,]),'$end':([1,2,3,4,5,9,18,20,22,25,],[0,-1,-2,-3,-4,-7,-6,-9,-13,-8,]),'COMMA':([2,3,4,5,9,13,16,18,20,22,25,28,],[-1,-2,-3,-4,-7,21,23,-6,-9,-13,-8,-17,]),'RSQUARE':([2,3,4,5,6,9,11,12,13,18,20,21,22,25,26,],[-1,-2,-3,-4,-5,-7,20,-10,-11,-6,-9,-5,-13,-8,-12,]),'RCURLY':([2,3,4,5,7,9,14,15,16,18,20,22,23,25,27,28,],[-1,-2,-3,-4,-5,-7,22,-14,-15,-6,-9,-13,-5,-8,-16,-17,]),'NAME':([10,],[19,]),'COLON':([17,25,],[24,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'elem':([0,6,21,24,],[1,13,13,28,]),'list':([0,6,21,24,],[2,2,2,2,]),'dict':([0,6,21,24,],[3,3,3,3,]),'number':([0,6,21,24,],[4,4,4,4,]),'name':([0,6,7,21,23,24,],[5,5,17,5,17,5,]),'list_elem':([6,21,],[11,26,]),'empty':([6,7,21,23,],[12,15,12,15,]),'dict_list':([7,23,],[14,27,]),'dict_elem':([7,23,],[16,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> elem","S'",1,None,None,None),
  ('elem -> list','elem',1,'p_elem','day12.py',65),
  ('elem -> dict','elem',1,'p_elem','day12.py',66),
  ('elem -> number','elem',1,'p_elem','day12.py',67),
  ('elem -> name','elem',1,'p_elem','day12.py',68),
  ('empty -> <empty>','empty',0,'p_empty','day12.py',73),
  ('number -> MINUS NUMBER','number',2,'p_number','day12.py',78),
  ('number -> NUMBER','number',1,'p_number','day12.py',79),
  ('name -> QUOTE NAME QUOTE','name',3,'p_name','day12.py',87),
  ('list -> LSQUARE list_elem RSQUARE','list',3,'p_list','day12.py',95),
  ('list_elem -> empty','list_elem',1,'p_list_elem','day12.py',100),
  ('list_elem -> elem','list_elem',1,'p_list_elem','day12.py',101),
  ('list_elem -> elem COMMA list_elem','list_elem',3,'p_list_elem','day12.py',102),
  ('dict -> LCURLY dict_list RCURLY','dict',3,'p_dict','day12.py',120),
  ('dict_list -> empty','dict_list',1,'p_dict_list','day12.py',128),
  ('dict_list -> dict_elem','dict_list',1,'p_dict_list','day12.py',129),
  ('dict_list -> dict_elem COMMA dict_list','dict_list',3,'p_dict_list','day12.py',130),
  ('dict_elem -> name COLON elem','dict_elem',3,'p_dict_elem','day12.py',141),
]
