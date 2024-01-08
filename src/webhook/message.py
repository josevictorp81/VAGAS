from discord_webhook import DiscordEmbed, DiscordWebhook
from decouple import config
from datetime import datetime, date
from src.utils.get_webhok_urls import get_webhook_url


class JobWebHook:
    async def send_message(title: str, requirements: str, stack: str, link: str):
        url = await get_webhook_url(stack=stack)
        descritpion = f'{title} - {date.today()} - {datetime.now().hour}:{datetime.now().minute}'

        webhook = DiscordWebhook(url=url)
        msg = DiscordEmbed(
            title='VAGA', description=descritpion, color='03b2f8')
        msg.set_author(name='BAT', icon_url=config('WEBHOOK_IMAGE_URL'))
        msg.add_embed_field(name='Requisitos', value=requirements)
        msg.add_embed_field(name='Link da Vaga', value=link)

        webhook.add_embed(msg)
        webhook.execute(msg)
