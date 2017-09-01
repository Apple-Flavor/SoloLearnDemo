# _*_  coding:utf-8 _*__
'''''
创建者：shan
创建日期：2012/11/9
'''
import  wx
app = wx.App()
win = wx.Frame(None,title="简单编辑器",size=(410,335))
loadbtn = wx.Button(win,label="打开",pos=(225,5),size=(80,25))
savebtn =wx.Button(win,label="保存",pos=(315,5),size=(80,25))
filename = wx.TextCtrl(win,pos=(5,5),size=(210,25))
contents = wx.TextCtrl(win,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE|wx.HSCROLL)
win.Show()
app.MainLoop()  
