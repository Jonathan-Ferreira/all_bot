# Importa o discord.py, permitindo o acesso a API do discord
import discord
from discord.ext import commands

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
bot = commands.Bot(command_prefix="!",intents=intents)


class VoiceHandler:
	def __init__(self,bot):
		self.bot = bot

	async def juntar(self,ctx):
		if ctx.author.voice:
			canal = ctx.author.voice.channel
			await canal.connect()
			await ctx.channel.send(f'Juntando ao canal {canal}')			
		else:
			await ctx.channel.send('Você não está em um canal de voz')

	async def sair(self,ctx):
		if ctx.voice_client:
			await ctx.voice_client.disconnect()
			await ctx.channel.send(f'Saindo...')
		else:
			await ctx.channel.send("Não estou conectado em um canal")

class MessageHandler:
	def __init__(self,bot):
		self.bot = bot

	async def gerenciador_msg(self,ctx):
		# Match para validar o tipo de mensagem enviada e decidir qual tarefa deve ser realizada.

		match ctx.message.content:
			case "oi":
				await ctx.channel.send("Olá")
					
			case "fechar":			
				await ctx.channel.send("Fechando")
				# Por algum motivo esse comando trigga um aviso, porém está funcional.
				await bot.close()
			
			# Apresenta a listagem de canais do servidor.
			case "lista":
				global channel_list
				if channel_list == []:
					await ctx.channel.send("Lista está vazia")
				else:
					await ctx.channel.send(f"Canais: {channel_list}")
			
			# Obtém a listagem de canais do servidor
			case "servers":
				guild = ctx.guild
				channel_list = [(channel.name, channel.id) for channel in guild.channels if not isinstance(channel,discord.CategoryChannel)]
				channel_info = '\n'.join([f"Canal: {name} | ID: {channel_id}" for name, channel_id in channel_list])
				await ctx.channel.send(f"Canais:\n{channel_info}")
		
			# Apresenta a listagem de canais do servidor e seus tipos (Voz, Texto, etc.)
			case "tipo":
				guild = ctx.guild
				if channel_list == []:
					await ctx.channel.send("Lista está vazia")	 
				else:
					channel_list = [(channel.name, channel.type) for channel in guild.channels if not isinstance(channel,discord.CategoryChannel)]
					channel_info = '\n'.join([f"Canal: {name} | ID: {channel_type}" for name, channel_type in channel_list])
					await ctx.channel.send(f"Canais:\n{channel_info}")

	

voice_handler = VoiceHandler(bot)
message_handler = MessageHandler(bot)


@bot.command()
async def juntar(ctx):
	await voice_handler.juntar(ctx)

@bot.command()
async def sair(ctx):
	await voice_handler.sair(ctx)

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

# Gerenciar erros
@bot.event
async def on_command_error(ctx, erro):
    # Check if the error is because the command was not found
    if isinstance(erro, commands.CommandNotFound):
        await ctx.send(f"{ctx.message.content} é um comando inválido. Caso possua alguma dúvida, digitar '!ajuda' para obter a lista de todos os comandos disponíveis.")
    else:
        # Handle other types of errors (if any)
        await ctx.send(f"Um erro ocorreu: {str(erro)}")


@bot.event
async def on_message(mensagem):
	ctx = await bot.get_context(mensagem)
	await message_handler.gerenciador_msg(ctx)
	await bot.process_commands(mensagem)
# Listener de evento que ativa quando uma mensagem é enviada ao canal


		# Faz um chamado na função de tratamento para conexão com canais de voz.
		 # Process commands after your custom logic
		
# Executa o bot com o token especificado.
bot.run(DISCORD_TOKEN)