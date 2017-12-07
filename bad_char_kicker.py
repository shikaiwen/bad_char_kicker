import sublime
import sublime_plugin


class KPluginCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# self.view.insert(edit, 0, "Hello, World!")
		allcontent = sublime.Region(0,self.view.size())
		# print(allcontent)
		# 开河（愚痴や  this is good    
		# view = self.window.active_view()
		view = sublime.active_window().active_view()
		# word = view.word(view.sel()[0])
		region = view.sel()[0]
		selectedStr = view.substr(view.sel()[0])
		if len(selectedStr)==0 :
			return

		v = []
		for c in selectedStr:
			try:
				v.append(c.encode("ascii"))
			except UnicodeError:
				v.append(" ");
				# print("error")
		b = bytearray()
		b.extend(map(ord,v))
		resultStr = str(b,"utf-8")

		self.view.replace(edit,region,resultStr)
		# print(resultStr)
		# s = "".join(v)
		# res = selectedStr.encode("ascii","backslashreplace")
		# print(s)
		# self.view.replace(edit,allcontent,'                               ,|     \n                             //|                              ,|\n                           //,/                             -~ |\n                         // / |                         _-~   /  ,\n                       /\'/ / /                       _-~   _/_-~ |\n                      ( ( / /\'                   _ -~     _-~ ,/\'\n                       \\~\\/\'/|             __--~~__--\\ _-~  _/,\n               ,,)))))));, \\/~-_     __--~~  --~~  __/~  _-~ /\n            __))))))))))))));,>/\\   /        __--~~  \\-~~ _-~\n           -\\(((((\'\'\'\'(((((((( >~\\/     --~~   __--~\' _-~ ~|\n  --==//////((\'\'  .     `)))))), /     ___---~~  ~~\\~~__--~ \n          ))| @    ;-.     (((((/           __--~~~\'~~/\n          ( `|    /  )      )))/      ~~~~~__\\__---~~__--~~--_\n             |   |   |       (/      ---~~~/__-----~~  ,;::\'  \\         ,\n             o_);   ;        /      ----~~/           \\,-~~~\\  |       /|\n                   ;        (      ---~~/         `:::|      |;|      < >\n                  |   _      `----~~~~\'      /      `:|       \\;\\_____// \n            ______/\\/~    |                 /        /         ~------~\n          /~;;.____/;;\'  /          ___----(   `;;;/               \n         / //  _;______;\'------~~~~~    |;;/\\    /          \n        //  | |                        /  |  \\;;,\\              \n       (<_  | ;                      /\',/-----\'  _>\n        \\_| ||_                     //~;~~~~~~~~~ \n            `\\_|                   (,~~ \n                                    \\~\\ \n                                     ~~ \n')
		
