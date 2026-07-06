import os
from datetime import datetime, timezone
import requests

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
LINK = "https://youssefdot.github.io/MdwnhPoints/"

LINKED_WORD = f'<a href="{LINK}">الموقع</a>'

MESSAGES = [
    f"""صباح الخير جميعاً، 👋✨
يوم جديد نستهله بتجديد النية بأن يكون سعينا وعملنا اليوم خالصاً لوجه الله تعالى وفي ميزان حسناتنا 🤍
تذكير سريع: لا تنسوا توثيق روتينكم اليومي عبر {LINKED_WORD}! 💾

أتمنى لكم جميعاً يوماً مباركاً، وموفقاً، ومليئاً بالإنجاز! 🚀🌟""",

    f"""صباح الخير للجميع، ☀️ حياكم الله في بداية يوم جديد، نبتغي فيه مرضات الله ونسأله البركة في أعمالنا وجهودنا 🤍
يرجى منكم عدم نسيان توثيق الروتين اليومي في {LINKED_WORD} المخصص: 📝

يومكم مليء بالإنتاجية والتوفيق والتيسير يا رب! 🚀✨""",

    f"""صباح الخير جميعاً، 👋
لنبدأ يومنا بتجديد النية ليكون عملنا اليوم خالصاً لوجه الله تعالى ومباركاً 🤍
تذكير لطيف: يرجى توثيق روتينكم اليومي الآن عبر {LINKED_WORD}: 💻

أتمنى لكم يوماً موفقاً، مثمراً، ومليئاً بالهمة والإنجاز! 🌟🚀""",

    f"""صباح الخير جميعاً، ✨
ما أجمل أن نبدأ صباحنا بتوجيه قلوبنا وعملنا خالصاً لوجه الله، طالبين منه الأجر والتوفيق 🤍
نذكركم بأهمية توثيق روتينكم اليومي عبر {LINKED_WORD} قبل أن تأخذكم مهام اليوم: 📊

أتمنى لكم يوماً طيباً ومباركاً يحمل لكم كل خير! 🚀🌟""",

    f"""صباح الخير جميعاً، 👋✨

• النية: عملنا وجهدنا اليوم خالصاً لوجه الله تعالى وابتغاءً لمرضاته 🤍
• التذكير: لا تنسوا خطوة توثيق روتينكم اليومي في {LINKED_WORD}: 📥

يومكم موفق، مبارك، ومفعم بالإنجازات الحلوة! 🚀🌟""",
]


def send():
    day_index = datetime.now(timezone.utc).timetuple().tm_yday
    message = MESSAGES[day_index % len(MESSAGES)]
    thread_id = os.environ.get("TELEGRAM_THREAD_ID")
    sticker_id = os.environ.get("TELEGRAM_STICKER_ID")

    if sticker_id:
        sticker_payload = {"chat_id": CHAT_ID, "sticker": sticker_id}
        if thread_id:
            sticker_payload["message_thread_id"] = thread_id
        sticker_response = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendSticker",
            data=sticker_payload,
            timeout=30,
        )
        sticker_response.raise_for_status()

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }
    if thread_id:
        payload["message_thread_id"] = thread_id
    response = requests.post(url, data=payload, timeout=30)
    response.raise_for_status()
    print("Sent variation", day_index % len(MESSAGES))


if __name__ == "__main__":
    send()
