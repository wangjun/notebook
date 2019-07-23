#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.3 on Wed Jul  3 01:14:45 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade
from main import Robot

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((421, 317))
        self.list_box_1 = wx.ListBox(self, wx.ID_ANY, choices=["c"])
        self.button_1 = wx.Button(self, wx.ID_APPLY, "")
        
        # Tool Bar
        self.frame_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_toolbar)
        # Tool Bar end

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\Lizhen\\Pictures\\1560577296872_weibo.jpg", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetFocus()
        self.button_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.frame_toolbar.Realize()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        label_1 = wx.StaticText(self, wx.ID_ANY, u"\u8bf7\u9009\u62e9\u6267\u884c\u811a\u672c", style=wx.ALIGN_LEFT)
        label_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        sizer_1.Add(label_1, 0, 0, 0)
        sizer_1.Add(self.list_box_1, 0, wx.EXPAND | wx.LEFT, 0)
        sizer_1.Add(self.button_1, 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
