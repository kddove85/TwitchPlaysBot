import os
import time
import pywinauto
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

    def press_button(self, button, button_two=None):
        app = pywinauto.Application().connect(title="Chrono Trigger").top_window()
        app.set_focus()
        if button_two:
            with self.keyboard.pressed(button):
                self.keyboard.press(button_two)
                time.sleep(5)
                self.keyboard.release(button)
        else:
            self.keyboard.press(button)
            time.sleep(0.25)
            self.keyboard.release(button)

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def list_commands(self, ctx: commands.Context):
        message = f' +++++++ COMMANDS +++++++ ' \
                  f'!save ---------------------------------------. ' \
                  f'!confirm ------------------------------------. ' \
                  f'!cancel -------------------------------------. ' \
                  f'!menu --------------------------------------. ' \
                  f'!auto_battle --------------------------------. ' \
                  f'!flee ----------------------------------------. ' \
                  f'!left ----------------------------------------. ' \
                  f'!right ----------------------------------------. ' \
                  f'!up -----------------------------------------. ' \
                  f'!down ---------------------------------------. '
        await ctx.send(message)

    @commands.command()
    async def save(self, ctx: commands.Context):
        await self.menu(ctx)
        time.sleep(1)
        await self.up(ctx)
        time.sleep(1)
        await self.confirm(ctx)
        time.sleep(1)
        await self.confirm(ctx)
        time.sleep(1)
        await self.up(ctx)
        time.sleep(1)
        await self.confirm(ctx)
        time.sleep(2)
        await self.cancel(ctx)
        time.sleep(1)
        await self.cancel(ctx)

        self.press_button("x")

    @commands.command()
    async def confirm(self, ctx: commands.Context):
        self.press_button("x")

    @commands.command()
    async def cancel(self, ctx: commands.Context):
        self.press_button("c")

    @commands.command()
    async def menu(self, ctx: commands.Context):
        self.press_button("v")

    @commands.command()
    async def auto_battle(self, ctx: commands.Context):
        self.press_button("v")

    @commands.command()
    async def pause(self, ctx: commands.Context):
        self.press_button(Key.space)

    @commands.command()
    async def flee(self, ctx: commands.Context):
        self.press_button("g", button_two="h")

    @commands.command()
    async def left(self, ctx: commands.Context):
        self.press_button("a")

    @commands.command()
    async def right(self, ctx: commands.Context):
        self.press_button("d")

    @commands.command()
    async def up(self, ctx: commands.Context):
        self.press_button("w")

    @commands.command()
    async def down(self, ctx: commands.Context):
        self.press_button("s")


bot = Bot()
bot.run()
