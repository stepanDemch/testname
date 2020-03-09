#модули

import discord
from discord.ext import commands
from discord.utils import get
#переменные
bad =["блять", "Блять", "БЛЯТЬ", "блядь", "Блядь", "БЛЯДЬ", "хуй", "Хуй", "ХУЙ","пидорас", "Пидорас", "ПИДОРАС", "нахуй", "Нахуй", "НАХУЙ", "пизда", "Пизда", "ПИЗДА", "пизду", "Пизду", "ПИЗДУ", "ебать", "Ебать", "ЕБАТЬ"]
client = commands.Bot(command_prefix='#')


@client.command(pass_context=True) 
async def hello(ctx): 
    await ctx.send("привет! Я бот, который поможет жить этому серверу, Гы")
@client.command(pass_context=True)
#комманда очистки
@commands.has_permissions(administrator=True)
async def clear(ctx,amount = 100):
	await ctx.channel.purge(limit = amount )
	emb = discord.Embed(title="✅ успешно удалено!", colour= discord.Colour.green())
	emb.set_author(name = client.user.name)
	emb.set_thumbnail(url = client.user.avatar_url)
	await ctx.send(embed = emb)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
#комманда кика
async def kick(ctx, member: discord.Member, *, reason = None):
	await ctx.channel.purge( limit=1)
	await member.kick(reason = reason)
	emb = discord.Embed(title="✅ игрок успешно выгонен!", colour= discord.Colour.blue())
	emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
	await ctx.send(embed = emb)
#комманда пинга
@client.command(pass_context=True) 
async def ping(ctx): 
    await ctx.send("@everyone")
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
#комманда бана
async def ban(ctx, member: discord.Member, *, reason = None):
	await ctx.channel.purge(limit= 1)
	await member.ban(reason=reason)
	emb= discord.Embed(title="✅ игрок успешно забанен!", colour= discord.Colour.red())
	emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
	await ctx.send(embed =emb)
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
	await ctx.channel.purge( limit=1)
	mute_role = discord.utils.get( ctx.message.guild.roles, name = "muted")
	await member.add_roles(mute_role)
	await ctx.send("успешно замучен!")
@client.command()
async def join(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild)
	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
		


@client.command()
async def leave(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild)
	if voice and voice.is_connected():
		await voice.disconnect()
	else:
		voice = await channel.disconnect()
		
@client.event
#событие автороли
async def on_member_join(member):
	channel = client.get_channel(685163940656971788)
	role = discord.utils.get(member.guild.roles, id =684463234119499800 )
	await member.add_roles( role)
	await channel.send(embed = discord.Embed(description =f"Пользователь {member.mention} присоеденился к нам!"))
	await ctx.author.send("приветствую тебя на нашем сервере, пацан!")
@client.command(pass_context=True)
async def commands(ctx):
	emb=discord.Embed(title ="навигация по командам", colour = discord.Colour.blue())

	emb.add_field(name ="#hello", value = "приветствие")
	emb.add_field(name ="#clear", value = "очистка чата")
	emb.add_field(name ="#kick", value = "кик игрока")
	emb.add_field(name ="#ban", value = "бан игрока")
	emb.add_field(name ="#ping", value = "пинг всех игроков")
	emb.add_field(name = "#mute", value = "мут участника")
	await ctx.author.send(embed = emb)

@client.event
async def on_ready():
	await client.change_presence(status = discord.Status.idle, activity = discord.Game("#commands"))
@client.event
async def on_message(message):
	await client.process_commands( message)
	msg = message.content.lower()
	if msg in bad:
		await message.delete()
		await message.author.send(f"так писать не нада!")













		

client.run("NjgxNTE3MDc1NDQ4OTg3NjYw.XlPmUg.45QTos0MVPHNePV47fTsSw4nHqM")
