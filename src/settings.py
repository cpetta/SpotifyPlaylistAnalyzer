import os

print(os.listdir("./api_keys/"))

client_id_file = open("./api_keys/spotify_client_id.txt", "r")
client_secret_file = open("./api_keys/spotify_client_secret.txt", "r")


class Settings:
	def __init__(self):
		self.id:str = client_id_file.read()
		self.secret:str = client_secret_file.read()
