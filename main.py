import os
from pathlib import Path
from telegram import Bot
from dotenv import load_dotenv
from downland_comics import download_random_comic
from utils import download_image


def send_image(bot, chat_id, image_path):
    with open(image_path, "rb") as image:
        bot.send_photo(chat_id=chat_id, photo=image)


def main():
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print(
            "Ошибка: Убедитесь, что TELEGRAM_BOT_TOKEN и TELEGRAM_CHAT_ID заданы в .env файле"
        )
        return

    bot = Bot(token=token)
    comic_path = Path(__file__).parent / "comics" / "comics.jpg"
    folder_name = "comics"
    os.makedirs(folder_name, exist_ok=True)

    try:
        comic = download_random_comic()
        image_url = comic.get("img")
        comment = comic.get("alt")

        if image_url:
            download_image(image_url, comic_path)
            send_image(bot, chat_id, comic_path)

        if comment:
            bot.send_message(chat_id=chat_id, text=comment)

    finally:
        comic_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
