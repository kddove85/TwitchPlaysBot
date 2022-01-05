import os
import time
import pywinauto
from pywinauto.keyboard import send_keys
from pynput.keyboard import Key, Controller
from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=os.getenv('token'),
                         prefix=os.getenv('prefix'),
                         initial_channels=[os.getenv('initial_channel')]
                         )
        self.keyboard = Controller()

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def do_something(self, ctx: commands.Context):
        # app = pywinauto.Application().connect(title="FINAL FANTASY V")
        # app = pywinauto.Application().connect(title="Chrono Trigger").top_window()
        # app.set_focus()
        time.sleep(2)

        # pynput
        self.keyboard.press('v')
        self.keyboard.release('v')

        # pywinauto
        # app.type_keys("v")
        # send_keys("v")

    @commands.command()
    async def do_something_else(self, ctx: commands.Context):
        app = pywinauto.Application().connect(title="Chrono Trigger").top_window()
        app.set_focus()
        self.keyboard.press('v')
        time.sleep(1)
        self.keyboard.release('v')


bot = Bot()
bot.run()
