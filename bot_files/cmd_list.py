command_list_default = { #список стандартных команд
	'/darky reg': '/darky reg', #регистрация беседы
	'/darky chat settings': '/darky chat settings', #показать настройки беседы
	'/darky chat set': '/darky chat set', #изменить настройку беседы
	'/darky unreg': '/darky unreg', #убрать регистрацию беседы
	'/darky user settings': '/darky user settings', #показать настройки пользователя
	'/darky user set': '/darky user set', #изменить настройку пользователя
	'/darky assoc set': '/darky assoc set', #новая ассоциация для команды
	'/darky assoc del': '/darky assoc del', #удалить ассоциации
	'/darky choose': '/darky choose', #выбрать из предложенного
	'/darky prob': '/darky prob', #вероятность
	'/darky try': '/darky try', #попытка "выполнить"
	'/darky dist': '/darky dist', #исказить текст
	'/darky roll': '/darky roll', #бросить игральную кость
	'/darky random': '/darky random', #рандомное число из указанного диапазона
	'/darky greet': '/darky greet', #приветствие
	'/darky rules': '/darky rules', #правила
	'/darky speak': '/darky speak', #генерирует текст
	'/darky help': '/darky help', #вызов помощи
	'/darky bug report': '/darky bug report',
	'/darky kick': '/darky kick', #исключает пользователя или группу
	'/darky ban': '/darky ban', #забанить пользователя
	'/darky unban': '/darky unban', #разбанить пользователя
	'/darky warn': '/darky warn', #выдать предупреждение
	'/darky unwarn': '/darky unwarn', #снять предупреждение
	'/darky full unwarn': '/darky full unwarn', #снять все предупреждения
	'/darky warns': '/darky warns', #вывести количество предупреждений
	'/darky send m': '/darky send m', #рассылка
	'/darky verify settings': '/darky verify settings', #вывод настроек DarkyVerify
	'/darky verify set': '/darky verify set', #изменить настройку DarkyVerify
	'/darky nick': '/darky nick', #никнеймы
	'/darky rp list': '/darky rp list', #список рп команд
	'/darky rp new': '/darky rp new', #добавить рп команду
	'/darky rp del': '/darky rp del', #удалить рп команду
	'/darky random rp': '/darky random rp', #вызов рандомного рп ботом
	'/darky exc': '/darky exc', #вызов исключения напрямую через бота
	'/darky layout': '/darky layout', #изменение раскладки
	'/darky stats': '/darky stats', #статистика пользователя
	'/darky notes': '/darky notes', #заметки
	"/darky top": "/darky top", #топ участников
	"/darky settings": "/darky settings", #вывод внутренних настроек бота
	"/darky set": "/darky set", #изменение настроек бота
	"/darky admin": "/darky admin", #управление администраторами бота
	'info': {
		'/darky reg': {
			'args_count': 0,
			'access': 'chats' #[chatsusers/users/chats]
		},
		'/darky chat settings': {
			'args_count': 0,
			'access': 'chats'
		},
		'/darky chat set': {
			'args_count': 2,
			'access': 'chats'
		},
		'/darky unreg': {
			'args_count': 0,
			'access': 'chats'
		},
		'/darky user settings': {
			'args_count': 0,
			'access': 'userschats'
		},
		'/darky user set': {
			'args_count': 2,
			'access': 'userschats'
		},
		'/darky assoc set': {
			'args_count': 2,
			'access': 'userschats'
		},
		'/darky assoc del': {
			'args_count': 1,
			'access': 'userschats'
		},
		'/darky choose': {
			'args_count': 1,
			'access': 'userschats'
		},
		'/darky prob': {
			'args_count': 1,
			'access': 'userschats'
		},
		'/darky try': {
			'args_count': 1,
			'access': 'userschats'
		},
		'/darky dist': {
			'args_count': 1,
			'access': 'userschats'
		},
		'/darky roll': {
			'args_count': 1,
			'access': 'userschats'
		},
		'/darky random': {
			'args_count': 2,
			'access': 'userschats'
		},
		'/darky greet': {
			'args_count': 1,
			'access': 'chats'
		},
		'/darky rules': {
			'args_count': 1,
			'access': 'chats'
		},
		'/darky speak': {
			'args_count': 0,
			'access': 'userschats'
		},
		'/darky speak del data': {
			'args_count': 0,
			'access': 'userschats'
		},
		'/darky help': {
			'args_count': 0,
			'access': 'userschats'
		},
		'/darky kick': {
			'args_count': 1,
			'access': 'chats'
		},
		'/darky ban': {
			'args_count': 2,
			'access': 'chats'
		},
		'/darky unban': {
			'args_count': 1,
			'access': 'chats'
		},
		'/darky warn': {
			'args_count': 1,
			'access': 'chats'
		},
		'/darky unwarn': {
			'args_count': 1,
			'access': 'chats'
		},
		'/darky full unwarn': {
			'args_count': 1,
			'access': 'chats'
		},
		'/darky warns': {
			'args_count': 1,
			'access': 'chats'
		},
		'/darky bug report': {
			'args_count': 1,
			'access': 'userschats'
		},
		'/darky send m': {
			'args_count': 3,
			'access': 'userschats'
		},
		'/darky verify set': {
			'args_count': 2,
			'access': 'chats'
		},
		'/darky verify settings': {
			'args_count': 0,
			'access': 'chats'
		},
		'/darky nick': {
			'args_count': 1,
			'access': 'chats'
		},
		'/darky rp list': {
			'args_count': 0,
			'access': 'chats'
		},
		'/darky rp new': {
			'args_count': 3,
			'access': 'chats'
		},
		'/darky rp del': {
			'args_count': 1,
			'access': 'chats'
		},
		'/darky random rp': {
			'args_count': 0,
			'access': 'chats'
		},
		'/darky exc': {
			'args_count': 2,
			'access': 'userschats'
		},
		'/darky layout': {
			'args_count': 1,
			'access': 'userschats'
		},
		'/darky stats': {
			'args_count': 1,
			'access': 'chats'
		},
		'/darky notes': {
			'args_count': 1,
			'access': 'userschats'
		},
		"/darky top": {
			"args_count": 1,
			"access": "chats"
		},
		"/darky settings": {
			"args_count": 0,
			"access": "chatsusers"
		},
		"/darky set": {
			"args_count": 2,
			"access": "chatsusers"
		},
		"/darky admin": {
			"args_count": 2,
			"access": "chatsusers"
		}
	}
}

chat_settings_presets = { #пресеты настроек беседы
	"default": { #стандарт - выставляется при регистрации беседы
		"chat_settings": {
			"mention_in_greetings": True,
            "lvlup_mentions": True,
			"rp": True,
			"rp_access": "admins",
			"bot_rp": True,
			"random_messages": True,
			"nicknames": True,
			"nicknames_access": "off",
			"easy_commands_react": True,
			"kick_access": "admins",
			"warn_access": "admins",
			"ban_access": "admins",
			"warn_limit": 5,
			"warn_punishment": "ban",
			"autokick": False,
			"update_news": True
		}
	},
	"free": { #свободный - всё включено и везде полностью открыт доступ
		"chat_settings": {
			"mention_in_greetings": True,
            "lvlup_mentions": True,
			"rp": True,
			"rp_access": "all",
			"bot_rp": True,
			"random_messages": True,
			"nicknames": True,
			"nicknames_access": "all",
			"easy_commands_react": True,
			"kick_access": "all",
			"warn_access": "all",
			"ban_access": "all",
			"warn_limit": 5,
			"warn_punishment": "none",
			"autokick": False,
			"update_news": True
		}
	},
	"strict": { #строгий - только администрирование и ничего лишнего
		"chat_settings": {
			"mention_in_greetings": False,
            "lvlup_mentions": False,
			"rp": False,
			"rp_access": "off",
			"bot_rp": False,
			"random_messages": False,
			"nicknames": False,
			"nicknames_access": "off",
			"easy_commands_react": False,
			"kick_access": "admins",
			"warn_access": "admins",
			"ban_access": "admins",
			"warn_limit": 5,
			"warn_punishment": "ban",
			"autokick": True,
			"update_news": False
		}
	},
	"all_off": { #выключенный - все настройки отключены и доступ полностью закрыт
		"chat_settings": {
			"mention_in_greetings": False,
            "lvlup_mentions": False,
			"rp": False,
			"rp_access": "off",
			"bot_rp": False,
			"random_messages": False,
			"nicknames": False,
			"nicknames_access": "off",
			"easy_commands_react": False,
			"kick_access": "off",
			"warn_access": "off",
			"ban_access": "off",
			"warn_limit": 5,
			"warn_punishment": "none",
			"autokick": False,
			"update_news": False
		}
	}
}
