import asyncio
import plugins

from imgurpython import ImgurClient

client_id = '995be3f4c563098'
client_secret = 'bbf9f39de8ba64bfdd508cbfee79d9c1f432eabe'

client = ImgurClient(client_id, client_secret)


def _initialise(bot):
    plugins.register_handler(_handle_me_action)
    plugins.register_user_command(["post_image_plz"])


def _handle_me_action(bot, event, command):
    if event.text.startswith('https://lh3.googleusercontent.com/'):
        yield from asyncio.sleep(0.2)
        yield from command.run(bot, event, *["post_image_plz"])
        

def post_image_plz(bot, event, *args):
    image = client.upload_from_url(event.text)
    yield from bot.coro_send_message(event.conv, _("Here's your imgur URL Dean: " + image['link']))