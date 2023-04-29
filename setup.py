import instagrapi

cl = instagrapi.Client()

cl.login("user", "password")
cl.dump_settings("session.json")