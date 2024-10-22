# Importa o discord.py, permitindo o acesso a API do discord
import discord
# Gerenciador de erros de Timeout
import asyncio  
# Importa o módulo de OS
import os

# Importa a função LOAD_DOTENV do módulo DOTENV para ler variáveis de ambiente, eliminando a necessidade de adicionar o token no código.
from dotenv import load_dotenv

channel_list = []

intents = discord.Intents.default() # Usa as intenções padrões do Bot.
intents.message_content = True   # Permite que o Bot leia o conteúdo de mensagens

# DISCORD_TOKEN = "MTI5NTcxODMwOTE2MDk0Nzc5NQ.Gs8FAx.YegUu3HgdxqwVUDqKI9Qno4AwoRkZLwUWI8jD8"

# Obtém o token da API localizado no arquivo .env
# DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
# if DISCORD_TOKEN is None:
# 	raise ValueError("Token não localizado.")

# Obtém o objeto do cliente do discord.py. O cliente é sinônimo do bot
bot = discord.Client(intents=intents)

# Listener de evento que ativa quando o bot é ligado
@bot.event
async def on_ready():
	# Cria um contador para acompanhar quantos servers o bot está conectado
	guild_count = 0

	# Faz um loop de todos os servers que o bot está conectado
	for guild in bot.guilds:
		# Mostra o nome e id dos servidores
		print(f"- {guild.id} (name: {guild.name})")

		# Acrescenta no contador de servidores.
		guild_count = guild_count + 1

	# Imprime a quantidade de servidores que o bot está conectado
	print("Teste está em " + str(guild_count) + " servers.")

# Listener de evento que ativa quando uma mensagem é enviada ao canal
@bot.event
async def on_message(message):
	# lista de IFs para checar o conteúdo da mensagem
	if message.content == "oi":
		await message.channel.send("Olá")
		
	if message.content == "fechar":
		await message.channel.send("Fechando")
		await bot.close()

	if message.content == "lista":
		global channel_list
		if channel_list == []:
			await message.channel.send("Lista está vazia")
		else:
			await message.channel.send(f"Canais: {channel_list}")

	if message.content == "servers":
		guild = message.guild
		channel_list = [(channel.name, channel.id) for channel in guild.channels if not isinstance(channel,discord.CategoryChannel)]
		channel_info = '\n'.join([f"Canal: {name} | ID: {channel_id}" for name, channel_id in channel_list])
		await message.channel.send(f"Canais:\n{channel_info}")

	if message.content == "tipo":
		# await message.channel.send("Chegou aqui")	 
		guild = message.guild
		if channel_list == []:
			await message.channel.send("Lista está vazia")	 
		else:
			channel_list = [(channel.name, channel.type) for channel in guild.channels if not isinstance(channel,discord.CategoryChannel)]
			channel_info = '\n'.join([f"Canal: {name} | ID: {channel_type}" for name, channel_type in channel_list])
			await message.channel.send(f"Canais:\n{channel_info}")

	if message.content == "juntar":
		await message.channel.send(f"Canais:\n{channel_list}")
		await message.channel.send("Qual canal deseja se juntar(nome)?")
		try:
			msg = await bot.wait_for("message",timeout=3.0)
			channel_name = msg.content
			await message.channel.send(f"Canal {channel_name} foi selecionado") 
			if channel_name in channel_list:
				await bot.connect(channel_name)
			else:
				await message.channel.send("Falha ao conectar")
				
		except asyncio.TimeoutError:
			await message.channel.send("Demorou muito a responder")
	
	if message.content == "desconectar":
		await bot.disconnect()

# Executa o bot com o token especificado.
bot.run(DISCORD_TOKEN)