import traceback

from discord_logger import DiscordLogger


def get_traceback(e):
    tb = (
        "Traceback (most recent call last):\n"
        + "".join(traceback.format_list(traceback.extract_tb(e.__traceback__)))
        + type(e).__name__
        + ": "
        + str(e)
    )
    return tb


webhook_url = "https://discord.com/api/webhooks/792661592390238218/rXUEaHfLmD_nu8JjS0nw4BCIKQ3HTja_uTpyZPOVuBOWEkWgnYRVnTv58FlO63icaEl3"
options = {
    "application_name": "My Server",
    "service_name": "Backend API",
    "service_icon_url": "https://tenor.com/view/elraen-gif-19026761",
    "service_environment": "Production",
    "default_level": "info",
}

err = KeyError("`email` field cannot be None")

logger = DiscordLogger(webhook_url=webhook_url, **options)
logger.construct(
    title="Runtime Exception",
    description=err.__str__(),
    error=get_traceback(err),
    metadata={"email": None, "module": "auth", "method": "POST"},
)

response = logger.send()
