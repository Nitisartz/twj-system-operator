from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

import random
import discord
from discord.ext import commands

# กำหนด intents
intents = discord.Intents.default()
intents.message_content = True  # ต้องเปิดเพื่อให้บอตสามารถอ่านข้อความได้

class JoinButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.players = []

    @discord.ui.button(label="เข้าร่วม", style=discord.ButtonStyle.primary)
    async def join(self, button: discord.ui.Button, interaction: discord.Interaction):
        user = interaction.user
        if user not in self.players:
            self.players.append(user)
            await interaction.response.send_message(f'{user.name} เข้าร่วมเกมแล้ว!', ephemeral=True)
        else:
            await interaction.response.send_message(f'คุณได้เข้าร่วมเกมแล้ว', ephemeral=True)

# สร้างอินสแตนซ์ของบอตพร้อมกับ intents
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def play(ctx):
    view = JoinButton()
    await ctx.send("เริ่มต้นเกม Werewolf! กดปุ่มด้านล่างเพื่อเข้าร่วม", view=view)

@bot.command()
async def assign_roles(ctx):
    roles = ["Werewolf", "Villager", "Seer"]  # เพิ่มบทบาทตามที่ต้องการ
    random.shuffle(view.players)

    assigned_roles = {}
    for player in view.players:
        role = roles.pop()
        assigned_roles[player] = role

    await send_roles_to_players(assigned_roles)

async def send_roles_to_players(assigned_roles):
    for player, role in assigned_roles.items():
        await player.send(f'บทบาทของคุณคือ: {role}')

bot.run(TOKEN)
