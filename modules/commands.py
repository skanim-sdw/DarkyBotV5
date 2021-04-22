import random
from modules import darkyExceptions
from modules.assocs import command_assocs
from modules.darkyVk import bot
from modules.botSettings import chat_settings, user_settings

class main_commands:
	
	def multiply_mess(args, chatSettings, userSettings): #рассылка сообщений
		#args - параметры к команде. Должны включать:
			#1 - список peer_ids кому назначено сообщение(перечисленые через запятую)
			#2 - текст рассылки
			#3 - какой нибудь прикреплённый объект в текстовом виде(photo507365405_1_accesskey123)
		ids_arg = args.split('; ')[0]
		txt_arg = args.split('; ')[1]
		att_arg = args.split('; ')[2]
		#распределение идентификаторов и формирование списка
		ids = []
		for i in range(len(ids_arg.split(', '))):
			if int(ids_arg.split(', ')[i]) > 2000000000:
				if str(int(ids_arg.split(', ')[i]) - 2000000000) not in chatSettings or str(int(ids_arg.split(', ')[i]) - 2000000000) in chatSettings and chatSettings[str(int(ids_arg.split(', ')[i]) - 2000000000)]["chat_settings"]["update_news"] == True:
					ids.append(int(ids_arg.split(', ')[i]))
			elif int(ids_arg.split(', ')[i]) > 0:
				if ids_arg.split(', ')[i] not in userSettings or ids_arg.split(', ')[i] in userSettings and userSettings[ids_arg.split(', ')[i]]["update_news"] == True:
					ids.append(int(ids_arg.split(', ')[i]))
		return ids, txt_arg, att_arg
	
	def choose(args): #функция выбора одного варианта из предложенных
		#args - параметры содержащие в себе вариации выбора включая разделители
		#доступные разделители: ";", " или ", "/", " or "
		choose_list = []
		splitters = [';', ' или ', '/', ' or ']
		for curr_split in range(len(splitters)):
			if splitters[curr_split] in args:
				choose_list = args.split(splitters[curr_split])
				break
			else:
				choose_list = args.split()
		if len(choose_list) > 1:
			choose_rep = random.choice(choose_list)
			darky_resp = 'Я выбираю ' + str(choose_rep).lstrip(' ').rstrip(' ')
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(252))
		return darky_resp
	
	def probably(args): #вероятность высказывания
		#args - высказывание
		if args == '':
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(250))
		darky_resp = 'Вероятность того, что ' + args + ' составляет ' + str(random.randint(0, 100)) + '%'
		return darky_resp
	
	def trying(args): #функция "попытки выполнить" действие в высказывании
		#args - высказывание
		if args == '':
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(250))
		resp_list = ['❌Попытка ' + args + ' вышла неудачной', '✅Попытка ' + args + ' удачна']
		darky_resp = random.choice(resp_list)
		return darky_resp
	
	def distort(args): #функция искажения текста
		#посимвольно переписывает строку изменяя рандомные символы
		out = ''
		dist_symb_list = ['█', '▒', '□', '?', '[]']
		if args == '':
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(250))
		for i in range(len(list(args))):
			#если рандом даст число выше 5 будет ставиться символ из оригинала
			dist_symb_probably = random.randint(1, 18)
			if dist_symb_probably > 5 or list(args)[i] == ' ':
				out += list(args)[i]
			else:
				out += dist_symb_list[dist_symb_probably - 1]
		return out
	
	def roll(args): #игральные кости
		#args - количество костей которые нужно бросить (1-5)
		#(по умолчанию 1)
		darky_resp = ''
		total_roll = 0
		if args == '':
			args = '1'
		if args.isdigit() == True and int(args) - 1 in range(5):
			args = int(args)
			for i in range(1, args + 1):
				roll_rand = random.randint(1, 6)
				total_roll += roll_rand
				darky_resp += '🎲На кубике ' + str(i) + ' выпало: ' + str(roll_rand) + '\n'
			darky_resp += 'Итого выпало: ' + str(total_roll)
		else:
			darky_resp = '⚠️Нужно указать количество кубиков числом, от 1 до 5(по умолчанию - 1)'
		return darky_resp
	
	def random_int(args): #рандомное число
		#args - список параметров к команде
		#(0; 100) - значит рандом от 0 до 100
		#ПЕРВОЕ ЗНАЧЕНИЕ ДОЛЖНО БЫТЬ МЕНЬШЕ ВТОРОГО!
		args = args.split('; ')
		try:
			darky_resp = 'Рандомное число: ' + str(random.randint(int(args[0]), int(args[1])))
		except ValueError:
			darky_resp = '⚠️Неверные параметры команды. Параметрами должны быть два числа указывающие диапазон в котором будет выбрано рандомное число. Второй параметр должен превышать первый'
		return darky_resp
	
	def layout(text): #измененте раскладки текста англ/рус
		layout_en = "`~@#$%^&qwertyuiop[]QWERTYUIOP{}asdfghjkl;'\\ASDFGHJKL:\"|zxcvbnm,./ZXCVBNM<>?"
		layout_ru = "ёЁ\"№;%:?йцукенгшщзхъЙЦУКЕНГШЩЗХЪфывапролджэ\\ФЫВАПРОЛДЖЭ/ячсмитьбю.ЯЧСМИТЬБЮ,"
		text_list = list(text)
		out = ""
		for c in range(len(text_list)):
			#если символ написан на английской раскладке
			if text_list[c] in list(layout_en):
				for i in range(len(list(layout_en))):
					if list(layout_en)[i] == text_list[c]:
						out += list(layout_ru)[i]
			#если на русской
			elif text_list[c] in list(layout_ru):
				for i in range(len(list(layout_ru))):
					if list(layout_ru)[i] == text_list[c]:
						out += list(layout_en)[i]
			else:
				out += text_list[c]
		return out



class greeting:
	
	def set(vk, event, chatSettings): #установка приветствия
		#проверка есть ли сообщение с приветствием в личных сообщениях
		greeting_from_dm = False
		if event.obj.message['fwd_messages'] != []:
			greet_mess = vk.messages.getHistory(count=100, user_id = event.obj.message['from_id'])
			#сравнение идентификаторов сообщений
			for curr_mess in range(len(greet_mess['items'])):
				if greet_mess['items'][curr_mess]['conversation_message_id'] == event.obj.message['fwd_messages'][0]['conversation_message_id']:
					greeting_from_dm = True
					break
		else:
			greeting_from_dm = False
		#сообщение с командой должно обязательно содержать пересланное сообщение(fwd_messages)
		if greeting_from_dm == True:
			greeting_text = event.obj.message['fwd_messages'][0]['text']
			#получение ключа доступа к прикреплённому объекту
			if event.obj.message['fwd_messages'][0]['attachments'] != []:
				greet_mess = vk.messages.getHistoryAttachments(peer_id = event.obj.message['from_id'], media_type = event.obj.message['fwd_messages'][0]['attachments'][0]['type'], count = 50)
				for curr_att in range(len(greet_mess['items'])):
					if event.obj.message['fwd_messages'][0]['attachments'][0][event.obj.message['fwd_messages'][0]['attachments'][0]['type']]['id'] == greet_mess['items'][curr_att]['attachment'][greet_mess['items'][curr_att]['attachment']['type']]['id']:
						greet_accss_key = ''
						if 'access_key' in greet_mess['items'][curr_att]['attachment'][greet_mess['items'][curr_att]['attachment']['type']]:
							greet_accss_key = greet_mess['items'][curr_att]['attachment'][greet_mess['items'][curr_att]['attachment']['type']]['access_key']
						#формирование привычного вида прикреплённого объекта <type><owner_id>_<attachment_id> ('_<access_key>' если есть)
						greeting_attachment = greet_mess['items'][curr_att]['attachment']['type'] + str(greet_mess['items'][curr_att]['attachment'][greet_mess['items'][curr_att]['attachment']['type']]['owner_id']) + '_' + str(greet_mess['items'][curr_att]['attachment'][greet_mess['items'][curr_att]['attachment']['type']]['id'])
						if greet_accss_key != '':
							greeting_attachment += '_' + greet_accss_key
						break
			else:
				greeting_attachment = ''
			chatSettings[str(event.chat_id)]["greeting"]["text"] = greeting_text
			chatSettings[str(event.chat_id)]["greeting"]["attachment"] = greeting_attachment
			return chatSettings
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(152))
	
	def delete(event, chatSettings): #удаление приветствия
		if chatSettings[str(event.chat_id)]["greeting"] != {}:
			chatSettings[str(event.chat_id)]["greeting"] = {}
			return chatSettings
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(150))
	
	def display(event, chatSettings): #отображение приветствия
		settings = chatSettings[str(event.chat_id)]
		if settings["greeting"] != {}:
			text = settings["greeting"]["text"]
			attachment = settings["greeting"]["attachment"]
			return text, attachment
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(150))
	
	def upd_att_accsskey(vk, event, chatSettings):
		settings = chatSettings[str(event.chat_id)]
		if settings["greeting"] != {}:
			#парсинг информации о текущем приветствии
			att_type = settings["greeting"]["attachment"].split('_')[0].rstrip('0123456789')
			att_owner_id = int(settings["greeting"]["attachment"].split('_')[0].lstrip('qwertyuiopasdfghjklzxcvbnm_-.,'))
			att_id = int(settings["greeting"]["attachment"].split('_')[1])
			if settings["greeting"]["attachment"].split('_')[-1].isdigit() != True:
				#поиск актуальной информации об прикреплённом объекте
				atts_list = vk.messages.getHistoryAttachments(peer_id = att_owner_id, media_type = att_type, count = 50)
				#пролистывание списка обьектов в поисках нужного
				new_att = ''
				for curr_att in range(len(atts_list["items"])):
					if atts_list["items"][curr_att]["attachment"][atts_list['items'][curr_att]['attachment']['type']]['id'] == att_id:
						new_att = att_type + str(att_owner_id) + '_' + str(att_id) + '_' + atts_list['items'][curr_att]['attachment'][atts_list['items'][curr_att]['attachment']['type']]['access_key']
					else:
						pass
				if new_att != '':
					chatSettings[str(event.chat_id)]["greeting"]["attachment"] = new_att
				else:
					raise darkyExceptions.DarkyError(darkyExceptions.get_error(154))
			return chatSettings
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(150))



class rules:
	
	def set(event, chatSettings):
		if event.obj.message['fwd_messages'] != [] and event.obj.message['fwd_messages'][0]['text'] != '':
			chatSettings[str(event.chat_id)]["rules"] = event.obj.message['fwd_messages'][0]['text']
			return chatSettings
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(153))
			
	def delete(event, chatSettings):
		if chatSettings[str(event.chat_id)]["rules"] != "":
			chatSettings[str(event.chat_id)]["rules"] = ""
			return chatSettings
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(151))
	
	def display(event, chatSettings):
		if chatSettings[str(event.chat_id)]["rules"] != "":
			return chatSettings[str(event.chat_id)]["rules"]
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(151))



class chat: #работа с беседой и её участниками
	
	def add_lvl_exp(vk, peer_id, text, id, members, lvlup_mentions, users): #добавить опыт уровня пользователя
		#peer_id - чат в котором было событие
		#text - текст сообщения
		#id - идентификатор пользователя
		#members - объект пользователей в настройках беседы
		#lvlup_mentions - boolean, включены ли оповещения о новых уровнях
		#users - объект пользователей в настройках пользователей
		if id > 0:
			text = text.lower()
			chars = len(list(text)) + members[str(id)]["level_xp"]
			members[str(id)]["chars_count"] += len(list(text))
			members[str(id)]["words_count"] += len(text.split(" "))
			if "прив" in text or "здраст" in text or "преет" in text or "преть" in text or "хай" in text:
				members[str(id)]["hi_count"] += 1
			if "пока" in text or "до встречи" in text or "до скорого" in text or "увидимся" in text or "до свидания" in text or "проща" in text or "досвидания" in text:
				members[str(id)]["bye_count"] += 1
			if "сук" in text or "бля" in text or "пизд" in text or "еба" in text or "хуй" in text or "хер" in text:
				members[str(id)]["bad_words_count"] += 1
			while chars >= 200 * members[str(id)]["level"]:
				chars -= (200 * members[str(id)]["level"])
				members[str(id)]["level"] += 1
				if lvlup_mentions == True:
					#определение никнейма
					if members[str(id)]["nickname"] != "":
						username = members[str(id)]["nickname"]
					else:
						username = vk.users.get(user_ids=id)[0]["first_name"]
					#определение разрешения на упоминание
					if users[str(id)]["mentions"] == True:
						username = "[id" + str(id) + "|" + username + "]"
					bot.send_mess(vk, peer_id, "🎉" + username + " только что достиг " + str(members[str(id)]["level"]) + " уровня!")
			members[str(id)]["level_xp"] = chars
			return members
			
	
	def user_info(event, command_args, chatSettings, userSettings, botInfo): #статистика пользователя
		#получение идентификатора
		if command_args == 'myself':
			id = event.obj.message['from_id']
		else:
			id = bot.search_id(event, command_args, chatSettings[str(event.chat_id)]["members"])
		#сбор информации и формирование статистики
		out = "📊Статистика пользователя:\n"
		if id > 0:
			if str(id) in chatSettings[str(event.chat_id)]["members"]:
				out += "🔹ID пользователя: " + str(id) + "\n"
				out += "🔹Забанен: " + str(chatSettings[str(event.chat_id)]["members"][str(id)]["is_banned"]) + "\n"
				out += "🔹Никнейм: " + chatSettings[str(event.chat_id)]["members"][str(id)]["nickname"] + "\n"
				out += "🔹Уровень: " + str(chatSettings[str(event.chat_id)]["members"][str(id)]["level"]) + "\n"
				out += "🔹Опыт: " + str(chatSettings[str(event.chat_id)]["members"][str(id)]["level_xp"]) + " exp/" + str(200 * chatSettings[str(event.chat_id)]["members"][str(id)]["level"]) + " exp\n"
				out += "🔹Всего опыта: " + str(chatSettings[str(event.chat_id)]["members"][str(id)]["chars_count"]) + " exp\n"
				out += "🔹Предупреждения: " + str(chatSettings[str(event.chat_id)]["members"][str(id)]["warns"]) + "\n"
				out += "🔹Количество слов: " + str(chatSettings[str(event.chat_id)]["members"][str(id)]["words_count"]) + "\n"
				out += "🔹Количество приветствий: " + str(chatSettings[str(event.chat_id)]["members"][str(id)]["hi_count"]) + "\n"
				out += "🔹Количество прощаний: " + str(chatSettings[str(event.chat_id)]["members"][str(id)]["bye_count"]) + "\n"
				out += "🔹Количество нецензурных слов: " + str(chatSettings[str(event.chat_id)]["members"][str(id)]["bad_words_count"]) + "\n"
			else:
				raise darkyExceptions.DarkyError(darkyExceptions.get_error(102))
		elif id == -192784148:
			out = "📊Статистика Дарки-бота:\n"
			out += "🔹ID бота: -192784148\n"
			out += "🔹Работает и разрабатывается с 9 марта 2020г.\n"
			out += "🔹Последнее обновление получено: " + botInfo["last_update"] + "\n"
			out += "🔹Создатель: Дарки(https://vk.com/id507365405)\n"
			out += "🔹Зарегистрировано бесед: "
			registered_chats = 0
			for i in range(len(list(chatSettings))):
				if list(chatSettings)[i] != "0":
					registered_chats += 1
			out += str(registered_chats) + '\n'
			out += "🔹Зарегистрировано пользователей: "
			registered_users = 0
			for i in range(len(list(userSettings))):
				if not list(userSettings)[i].startswith("-"):
					registered_users += 1
			out += str(registered_users) + "\n"
			out += "🔹Зарегистрировано пользователей в чатах: "
			registere_users = 0
			for i in range(len(list(chatSettings))):
				if list(chatSettings)[i] != "0":
					for u in range(len(list(chatSettings[list(chatSettings)[i]]["members"]))):
						if not list(list(chatSettings[list(chatSettings)[i]]["members"]))[u].startswith("-"):
							registered_users += 1
			out += str(registered_users) + "\n"
			out += "🔹Обработано команд: " + str(botInfo["commands"]) + "\n"
		elif id < 0:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(8))
		return out
	
	def kick(vk, event, command_args, chatSettings): #исключает пользователя из беседы
		#получение идентификатора
		if command_args == 'myself':
			id = event.obj.message['from_id']
		else:
			id = bot.search_id(event, command_args, chatSettings[str(event.chat_id)]["members"])
		if id == -192784148:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(5))
		#кик пользователя
		vk.messages.removeChatUser(chat_id = event.chat_id, member_id = id)
	
	def ban(vk, event, command_args, chatSettings): #бан пользователя в беседе
		#получение идентификатора
		if command_args == 'myself':
			id = event.obj.message['from_id']
		else:
			id = bot.search_id(event, command_args, chatSettings[str(event.chat_id)]["members"])
		if id == -192784148:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(5))
		if id < 0:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(8))
		#пользователь должен хотя бы один раз присутствовать в беседе при боте
		if str(id) not in chatSettings[str(event.chat_id)]["members"]:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(102))
		#если пользователь в чате - кик
		if bot.is_chat_member(vk, event, id) == True:
			chat.kick(vk, event, command_args, chatSettings)
			bot.send_mess(vk, peer_ids = id, text = '⚠️Вы были исключены из беседы "' + chatSettings[str(event.chat_id)]["chat_info"]["title"] + '" так как вы забанены в ней')
		#запись в настройки о том что этот пользователь был забанен
		if chatSettings[str(event.chat_id)]["members"][str(id)]["is_banned"] != True:
			chatSettings[str(event.chat_id)]["members"][str(id)]["is_banned"] = True
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(200))
		return chatSettings
	
	def unban(event, command_args, chatSettings): #разбан пользователя в беседе
		id = bot.search_id(event, command_args, chatSettings[str(event.chat_id)]["members"])
		if id < 0:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(8))
		if str(id) not in chatSettings[str(event.chat_id)]["members"]:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(102))
		if chatSettings[str(event.chat_id)]["members"][str(id)]["is_banned"] != False:
			chatSettings[str(event.chat_id)]["members"][str(id)]["is_banned"] = False
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(201))
		return chatSettings
	
	def unban_all(event, chatSettings): #разбан всех пользователей в беседе
		for curr_member in range(len(list(chatSettings[str(event.chat_id)]["members"]))):
			chatSettings[str(event.chat_id)]["members"][list(chatSettings[str(event.chat_id)]["members"])[curr_member]]["is_banned"] = False
		return chatSettings
	
	def get_banned_list(members): #получить список забаненных
		#members - список участников беседы в ее настройках(ключ members)
		ids = []
		for curr_user in range(len(list(members))):
			if members[list(members)[curr_user]]["is_banned"] == True:
				ids.append(list(members)[curr_user])
		return ids
	
	def warn(vk, event, command_args, chatSettings): #выдать одно предупреждение пользователю
		out = ''
		if command_args == 'myself':
			id = event.obj.message['from_id']
		else:
			id = bot.search_id(event, command_args, chatSettings[str(event.chat_id)]["members"])
		if id == -192784148:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(5))
		if id < 0:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(8))
		if bot.is_chat_member(vk, event, id) == True:
			if chatSettings[str(event.chat_id)]["members"][str(id)]["warns"] < chatSettings[str(event.chat_id)]["chat_settings"]["warn_limit"]:
				chatSettings[str(event.chat_id)]["members"][str(id)]["warns"] += 1
				out = '❕[id' + str(id) + '|Вам] выдали предупреждение(' + str(chatSettings[str(event.chat_id)]["members"][str(id)]["warns"]) + '/' + str(chatSettings[str(event.chat_id)]["chat_settings"]["warn_limit"]) + ')\nПри достижении максимального количества вы получите наказание'
			if chatSettings[str(event.chat_id)]["members"][str(id)]["warns"] == chatSettings[str(event.chat_id)]["chat_settings"]["warn_limit"]:
				out = '❗Количество [id' + str(id) + '|ваших] предупреждений достигло предела. Вы понесёте установленное в этой беседе наказание'
				bot.send_mess(vk, event.obj.message['peer_id'], out)
				out = ''
				if chatSettings[str(event.chat_id)]["chat_settings"]["warn_punishment"] == 'ban':
					chatSettings = chat.ban(vk, event, command_args, chatSettings)
				elif chatSettings[str(event.chat_id)]["chat_settings"]["warn_punishment"] == 'kick':
					chat.kick(vk, event, command_args, chatSettings)
				elif chatSettings[str(event.chat_id)]["chat_settings"]["warn_punishment"] == 'none':
					out = '⚠️Наказание на достижение максимального числа предупреждений не установлено. Количество предупреждений обнулено'
				chatSettings[str(event.chat_id)]["members"][str(id)]["warns"] = 0
			return chatSettings, out
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(21))
	
	def unwarn(vk, event, command_args, chatSettings, full=False): #снять предупреждение
		#full - полностью снять все предупреждения у данного пользователя или нет
		if command_args == 'myself':
			id = event.obj.message['from_id']
		else:
			id = bot.search_id(event, command_args, chatSettings[str(event.chat_id)]["members"])
		if id == -192784148:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(5))
		if id < 0:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(8))
		if bot.is_chat_member(vk, event, id) == True:
			if full == False:
				if chatSettings[str(event.chat_id)]["members"][str(id)]["warns"] > 0:
					chatSettings[str(event.chat_id)]["members"][str(id)]["warns"] -= 1
			else:
				chatSettings[str(event.chat_id)]["members"][str(id)]["warns"] = 0
			return chatSettings
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(21))
	
	def unwarn_all(event, chatSettings):
		for curr_member in range(len(list(chatSettings[str(event.chat_id)]["members"]))):
			chatSettings[str(event.chat_id)]["members"][list(chatSettings[str(event.chat_id)]["members"])[curr_member]]["warns"] = 0
		return chatSettings
	
	def get_warn_list(members):
		ids = []
		for curr_user in range(len(list(members))):
			if members[list(members)[curr_user]]["warns"] > 0:
				ids.append(list(members)[curr_user])
		return ids



class nicknames:
	
	def set(id, membs_of_chat, nick): #установить никнейм
		#membs_of_chat - объект members в chatSettings
		#проверка занят ли данный никнейм
		for curr_mem in range(len(list(membs_of_chat))):
			if membs_of_chat[list(membs_of_chat)[curr_mem]]["nickname"] == nick:
				raise darkyExceptions.DarkyError(darkyExceptions.get_error(400))
		membs_of_chat[str(id)]["nickname"] = nick
		return membs_of_chat
		
	def delete(id, membs_of_chat): #удалить никнейм
		membs_of_chat[str(id)]["nickname"] = ""
		return membs_of_chat
	
	def get_list(members):
		ids = []
		for curr_user in range(len(list(members))):
			if members[list(members)[curr_user]]["nickname"] != "":
				ids.append(list(members)[curr_user])
		return ids



class roleplay:
	
	def get_user(vk, id, chat_obj, users, need_sex=False):
		#chat_obj - объект настроек беседы у бота(chatSettings с ключём идентификатора беседы)
		#users - объект настроек пользователей
		#need_sex - необходимость в возвращении пола
		out = ''
		username = 'null'
		can_mention = True
		if id > 0:
			#проверка запрещены ли упоминания этого пользователя
			if str(id) in users:
				can_mention = users[str(id)]["mentions"]
			user = vk.users.get(user_ids=id, fields="sex")[0]
			sex = user["sex"]
			#проверка есть ли у этого пользователя никнейм
			if str(id) in chat_obj["members"] and chat_obj["members"][str(id)]["nickname"] != "" and chat_obj["chat_settings"]["nicknames"] == True:
				username = chat_obj["members"][str(id)]["nickname"]
			else:
				#получение его имени и фамилии
				username = user["first_name"] + ' ' + user["last_name"]
		elif id < 0:
			#получение названия группы
			username = vk.groups.getById(group_id=-id)[0]["name"]
			sex = 2
		if can_mention == True:
			out = '['
			if id > 0:
				out += 'id' + str(id)
			elif id < 0:
				out += 'club' + str(-id)
			out += '|' + username + ']'
		else:
			out = username
		if need_sex == True:
			return out, sex
		else:
			return out
	
	def get_rp(message, rp_list):
		#message - текст сообщения с рп командой
		#rp_list - список рп команд сохранённых в боте
		#поиск команды
		rp, rp_to = command_assocs.check(message, rp_list)
		if rp != "":
			return rp, rp_to
	
	def do_rp(vk, event, rp_from, message, chat_obj, users, check_member=True): #выполнение рп
		#получение читабельного вида рп действия
		rp_act, rp_to = roleplay.get_rp(message, chat_obj["rp_commands"])
		#определение идентификатора пользователя, которому назначена рп команда
		if rp_to == 'myself':
			rp_to = rp_from
		else:
			rp_to = bot.search_id(event, rp_to, chat_obj["members"])
		if check_member == True:
			if rp_to > 0 and bot.is_chat_member(vk, event, rp_to) == False:
				raise darkyExceptions.DarkyError(darkyExceptions.get_error(6))
		#получение читабельного вида пользователя которому назначена рп команда
		rp_to_str = roleplay.get_user(vk, rp_to, chat_obj, users)
		#получение читабельного вида пользователя от которого пришёл запрос рп команды
		rp_from_str, usersex = roleplay.get_user(vk, rp_from, chat_obj, users, True)
		#определение пола пользователя которому назначена рп команда
		if '-' in rp_act:
			if rp_from > 0:
				if usersex == 1:
					rp_act = rp_act.split('-')[1]
				else:
					rp_act = rp_act.split('-')[0]
			else:
				rp_act = rp_act.split('-')[0]
		darky_resp = rp_from_str + ' ' + rp_act + ' ' + rp_to_str
		return darky_resp
	
	def add(command_args, rp_list):
		#command_args - аргументы идущие вместе с командой
		#rp_list - список рп команд сохранённых в боте
		rp_name = command_args.split('; ')[0].lower()
		rp_acts = command_args.split('; ')[1].lower() + '-' + command_args.split('; ')[2].lower()
		if rp_name in ["буп", "кусь", "обнять", "поцеловать", "ударить"]:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(453))
		if rp_name in rp_list and rp_list[rp_name] == rp_acts:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(450))
		rp_list[rp_name] = rp_acts
		return rp_list
	
	def delete(command_args, rp_list):
		#command_args - аргументы идущие вместе с командой
		#rp_list - список рп команд сохранённых в боте
		rp_name = command_args.lower()
		if rp_name in ["буп", "кусь", "лизнуть", "обнять", "поцеловать", "ударить"]:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(453))
		if rp_name not in rp_list:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(451))
		del(rp_list[rp_name])
		return rp_list
	
	def get_list(rp_list):
		out = ''
		index = 1
		for curr_rp in range(len(list(rp_list))):
			out += str(index) + '. ' + list(rp_list)[curr_rp].capitalize() + '\n'
			index += 1
		return out
	
	def rand_rp(vk, event, chatSettings, userSettings, called_from_chat=False):
		#определение рандомного чата
		rand_chat = "0"
		if called_from_chat == True:
			rand_chat = str(event.chat_id)
		while rand_chat == "0":
			rand_chat = random.choice(list(chatSettings))
		if chatSettings[rand_chat]["chat_settings"]["rp"] == True and chatSettings[rand_chat]["chat_settings"]["bot_rp"] == True:
			#поулчение рандомного участника из беседы
			chat_members = vk.messages.getConversationMembers(peer_id=2000000000 + int(rand_chat))
			rand_member = chat_members["items"][random.randint(0, chat_members["count"] - 1)]["member_id"]
			if rand_member > 0:
				rand_member = "[id" + str(rand_member) + "|@id" + str(rand_member) + "]"
			elif rand_member < 0:
				rand_member = "[club" + str(-rand_member) + "|@club" + str(-rand_member) + "]"
			#получение рандомной рп команды
			rand_rp = random.choice(list(chatSettings[rand_chat]["rp_commands"]))
			#отправка запроса на рп команду
			darky_resp = roleplay.do_rp(vk, event, -192784148, rand_rp + ' ' + rand_member, chatSettings[rand_chat], userSettings, False)
			if called_from_chat == True:
				return darky_resp
			else:
				return darky_resp, 2000000000 + int(rand_chat)
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(10))



class easter_eggs:
	
	def ee1(vk, event, bd_date):
		id = event.obj.message["from_id"]
		message = event.obj.message["text"]
		peer_id = event.obj.message["peer_id"]
		#получение списка тех кто уже находится в секретной беседе
		secret_taken = False
		users_with_secret = vk.messages.getConversationMembers(peer_id = 2000000004)
		for i in range(len(users_with_secret["profiles"])):
			if id == users_with_secret['profiles'][i]['id']:
				secret_taken = True
				break
		if secret_taken == False:
			if message.lower() in ['test2310', 'тест2310']:
				bot.send_mess(vk, peer_id, 'Поздравляю! Вы получили секрет - ссылка на беседу где проводятся мои тесты, там вы можете раньше всех узнать о том, что будет добавлено в меня и увидеть часть процесса разработки')
				bot.send_mess(vk, peer_id, 'https://vk.me/join/AJQ1d7SbHhdQs8BxnX7faLXp')
			elif message.lower() == 'тест' + str(bd_date) or message.lower() == 'test' + str(bd_date):
				bot.send_mess(vk, peer_id, 'Хорошая попытка, но подумайте лучше')
			else:
				bd_day_str = ''
				bd_month_str = ''
				bd_month = random.randint(1, 12)
				if not bd_month == 2:
					bd_day = random.randint(1, 31)
				else:
					bd_day = random.randint(1, 29)
				if bd_day == 23 and bd_month == 10:
					while bd_day == 23 and bd_month == 10:
						bd_month = random.randint(1, 12)
						if not bd_month == 2:
							bd_day = random.randint(1, 31)
						else:
							bd_day = random.randint(1, 29)
				if bd_day < 10:
					bd_day_str = '0' + str(bd_day)
				else:
					bd_day_str = str(bd_day)
				if bd_month < 10:
					bd_month_str = '0' + str(bd_month)
				else:
					bd_month_str = str(bd_month)
				bd_date = bd_day_str + bd_month_str
				bot.send_mess(vk, peer_id, 'Вы почти у цели! Введите "тест" приписав к нему день рождения моего создателя без пробелов и точек.\nНапример "тест' + bd_date + '"')
		return bd_date



class notes:
	
	def get(notes, command_args): #вывод списка заметок/подробной информации
		out = ''
		if notes == []:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(600))
		#проверка количества переданных аргументов
		if len(command_args.split('; ')) != 1:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(250))
		if command_args != "list" and command_args.isdigit() != True:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(254))
		if command_args == "list":
			out += "🧾Список ваших заметок:\n"
			index = 1
			for i in range(len(notes)):
				out += str(index) + '. ' + notes[i]["name"] + '<' + str(notes[i]["id"]) + '>\n'
				index += 1
		elif command_args.isdigit() == True:
			for i in range(len(notes)):
				if notes[i]["id"] == int(command_args):
					out += "🆔Информация о заметке с идентификатором " + str(notes[i]["id"]) + "\n"
					out += "💬Заголовок: " + notes[i]["name"] + "\n"
					out += "💭Описание: " + notes[i]["desc"] + "\n"
			if out == "":
				raise darkyExceptions.DarkyError(darkyExceptions.get_error(601))
		else:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(253))
		return out
	
	def add(notes, command_args): #добавление заметки в список заметок
		#проверка количества переданных аргументов
		#/darky notes add; <name>; <desc>
		if len(command_args.split('; ')) != 3:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(250))
		#распределение данных
		name = command_args.split('; ')[1]
		description = command_args.split('; ')[2]
		if name in ["-", ".", "null", ""]:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(602))
		#поиск заголовка среди уже установленных
		if notes != []:
			last_note_id = notes[-1]["id"]
			for i in range(len(notes)):
				if name == notes[i]["name"]:
					raise darkyExceptions.DarkyError(darkyExceptions.get_error(603))
		else:
			last_note_id = -1
		#подготовка объекта
		note_obj = {
			"id": last_note_id + 1,
			"name": name,
			"desc": description
		}
		#запись заметки в список
		notes.append(note_obj)
		return notes
	
	def delete(notes, command_args):
		deleted = False
		if notes == []:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(600))
		#проверка количества переданных аргументов
		#/darky notes del; <id>
		if len(command_args.split('; ')) != 2:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(250))
		if command_args.split('; ')[1].isdigit() != True:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(253))
		note_id = int(command_args.split('; ')[1])
		#поиск арта с указанным идентификатором
		for i in range(len(notes)):
			if notes[i]["id"] == note_id:
				del(notes[i])
				deleted = True
				break
		if deleted == False:
			raise darkyExceptions.DarkyError(darkyExceptions.get_error(604))
		return notes