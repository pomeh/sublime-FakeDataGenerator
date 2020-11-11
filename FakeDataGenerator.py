import re, os, sys
import sublime
import sublime_plugin

# global settings container
s = {}
Pref = {}
faker = {}
debug = False

class Pref:
	def load(self):
		Pref.seed = s.get('seed', 'yep')
		Pref.locale = s.get('locale', 'en_GB')

class FakeDataGenerator(sublime_plugin.TextCommand):
	def run(self, edit):

		if debug:
			self.on_done(1)
		else:
			Window().run_command('hide_panel');
			view = Window().show_input_panel("Repeat:", "1", self.on_done, None, None)
			view.sel().clear()
			view.sel().add(sublime.Region(0, view.size()))

	def on_done(self, repeat):
		global faker
		repeat = int(repeat or 0)
		if repeat>0:

			view = View()
			faker = self._faker()

			if Pref.seed:
				faker.seed(Pref.seed)

			def index(_counter_index = -1):
				if not _counter_index in index.counter:
					index.counter[_counter_index] = -1
				index.counter[_counter_index]+=1
				return index.counter[_counter_index]
			index.counter = {}; faker.index = index;

			try:
				from .Edit import Edit as Edit
			except:
				from Edit import Edit as Edit

			with Edit(view) as edit:

				for region in reversed(view.sel()):
					if region.empty():
						continue

					content = view.substr(region)*repeat
					functions_and_modifiers = re.findall('{{(.*?)(\|[^}]+)?}}', content, re.U | re.I)
					for function, modifiers in functions_and_modifiers:
						find_for = str('{{'+function+modifiers+'}}')

						modifiers = modifiers.split('|'); modifiers.pop(0)

						callable = lambda:self.value(lambda:eval('faker.'+function))
						value = None
						if not modifiers:
							try:
								value = callable()
							except  Exception as e:
								print('FakeDataGenerator: Error evaluating faker expression "'+function+'" : '+ str(e).strip())
						else:
							for modifier in modifiers:
								if not value:
									# the first modifier receive the faker object, and may whish to call it multiple times.
									pass
								else:
									# faker object already applied, just send the value
									callable = lambda:self._return(value)
								try:
									value = eval('self.'+(modifier.replace('(', '(callable,', 1)))
								except  Exception as e:
									print('FakeDataGenerator: Error evaluating modifier expression "'+modifier+'", or faker expression : '+ str(e).strip())

						content = content.replace(find_for, value, 1)

					edit.replace(region, content)

	# normalize a value from faker
	def normalize(self, value):
		return str(value).replace('True', 'true').replace('False', 'false').replace('None', 'null')
	def value(self, value):
		_value = value()
		if type(_value) is list:
			return self.normalize(' '.join(_value))
		else:
			return self.normalize(_value)

	# modifiers
	def repeat(self, callable, nTimes = 1, separator = ','):
		value = []
		if type(nTimes) is tuple:
			import random
			random.seed()
			nTimes = random.randint(nTimes[0], nTimes[1])
		for i in range(0, int(str(nTimes))):
			value.append(callable())
		return separator.join(value)

	def encode(self, callable):
		try:
			from urllib import quote as urlquote
		except ImportError:
			from urllib.parse import quote as urlquote

		return urlquote(callable().encode('utf8'), '')

	def escape(self, callable):
		return callable().encode('ascii', 'backslashreplace').decode('utf-8')

	# utils
	def _faker(self):
		Faker = self._import_path(os.path.dirname(__file__)+'/faker/faker')
		return Faker.Factory.create(Pref.locale)

	def _import_path(self, fullpath):
		"""
		Import a file with full path specification. Allows one to
		import from anywhere, something __import__ does not do.
		"""
		path, filename = os.path.split(fullpath)
		filename, ext = os.path.splitext(filename)
		sys.path.append(path)
		module = __import__(filename)
		#reload(module) # Might be out of date
		sys.path.remove(path)
		return module

	def _return(self, value):
		return value


class FakeDataGeneratorInsert(sublime_plugin.TextCommand):
	def run(self, edit, content):
		view = View()
		view.run_command('insert',  {'characters': '{{'+content+'}}'})

def Window():
	return sublime.active_window()

def View():
	return Window().active_view()

def plugin_loaded():
	global s, Pref
	s = sublime.load_settings('FakeDataGenerator.sublime-settings')
	Pref = Pref()
	Pref.load()
	s.add_on_change('reload_prefs', lambda:Pref.load())

if int(sublime.version()) < 3000:
	plugin_loaded()
