# Importa o discord.py, permitindo o acesso a API do discord
import discord

# Importa o módulo de OS
import os

# Importa a função LOAD_DOTENV do módulo DOTENV para ler variáveis de ambiente, eliminando a necessidade de adicionar o token no código.
from dotenv import load_dotenv

channel_list = []

intents = discord.Intents.default() # Usa as intenções padrões do Bot.
intents.message_content = True   # Permite que o Bot leia o conteúdo de mensagens

# Obtém o token da API na variável local DISCORD_TOKEN
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
	raise ValueError("Token não localizado.")

# Obtém o objeto do cliente do discord.py. O cliente é sinônimo do bot
bot = discord.Client(intents=intents)

# Função para gerenciar o acesso do bot aos canais de voz.
@bot.event
async def voice_channel(ctx,message):
	if message == "juntar":
		if ctx.author.voice:
			channel = ctx.author.voice.channel
			await channel.connect()
			await ctx.channel.send(f'Juntando ao canal {channel}')
	elif message == "desconectar":
		if ctx.voice_client:
			await channel.voice_client.disconnect()
			await ctx.channel.send(f'Saindo...')
	else:
		await ctx.channel.send('Você não está em um canal de voz')

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
	# Match para validar o tipo de mensagem enviada e decidir qual tarefa deve ser realizada.
	match message.content:
		case "oi":
			await message.channel.send("Olá")
				
		case "fechar":			
			await message.channel.send("Fechando")
			# Por algum motivo esse comando trigga um aviso, porém está funcional.
			await bot.close()
		
		# Apresenta a listagem de canais do servidor.
		case "lista":
			global channel_list
			if channel_list == []:
				await message.channel.send("Lista está vazia")
			else:
				await message.channel.send(f"Canais: {channel_list}")
		
		# Obtém a listagem de canais do servidor
		case "servers":
			guild = message.guild
			channel_list = [(channel.name, channel.id) for channel in guild.channels if not isinstance(channel,discord.CategoryChannel)]
			channel_info = '\n'.join([f"Canal: {name} | ID: {channel_id}" for name, channel_id in channel_list])
			await message.channel.send(f"Canais:\n{channel_info}")
	
		# Apresenta a listagem de canais do servidor e seus tipos (Voz, Texto, etc.)
		case "tipo":
			guild = message.guild
			if channel_list == []:
				await message.channel.send("Lista está vazia")	 
			else:
				channel_list = [(channel.name, channel.type) for channel in guild.channels if not isinstance(channel,discord.CategoryChannel)]
				channel_info = '\n'.join([f"Canal: {name} | ID: {channel_type}" for name, channel_type in channel_list])
				await message.channel.send(f"Canais:\n{channel_info}")

		# Faz um chamado na função de tratamento para conexão com canais de voz.
		case "juntar"  | "desconectar":
			msg = message.content
			await message.channel.send(f"Info:\n{msg}")
			await voice_channel(message,msg)
		
# Executa o bot com o token especificado.
bot.run(DISCORD_TOKEN)