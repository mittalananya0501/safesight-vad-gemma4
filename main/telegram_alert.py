import requests
from config import BOT_TOKEN, CHAT_ID

<<<<<<< HEAD

=======
>>>>>>> cd07ab0 (split merged)
def send_telegram_alert(video_path, category, description):
    """Sends the stitched anomaly video and Gemma-4's forensic JSON analysis to Telegram."""
    if not BOT_TOKEN or not CHAT_ID:
        print("⚠️ Telegram BOT_TOKEN or CHAT_ID is missing. Skipping alert.")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
    
    # Enhanced, highly scannable design format
    caption_text = (
<<<<<<< HEAD
        f"🚨 <b>Emergency Alert</b>\n"
        f"• <b>Category:</b> <code>{category}</code>\n"
        f"<b>FORENSIC ANALYSIS REPORT</b>\n"
        f"{description}\n"
=======
        f"🚨 <b>CRITICAL SECURITY EVENT</b> 🚨\n"
        f"<code>──────────────────────────────</code>\n\n"
        f"🏷️ <b>INCIDENT INFORMATION</b>\n"
        f"• <b>Category:</b> <code>{category}</code>\n"
        f"🔬 <b>FORENSIC ANALYSIS REPORT</b>\n"
        f"<blockquote>{description}</blockquote>\n"
        f"<code>──────────────────────────────</code>\n"
>>>>>>> cd07ab0 (split merged)
    )
    
    print(f"Uploading {video_path} to Telegram... (Max limit: 50MB)")
    try:
        with open(video_path, "rb") as video_file:
            response = requests.post(
                url,
                data={"chat_id": CHAT_ID, "parse_mode": "HTML", "caption": caption_text},
                files={"video": video_file}
            )
        if response.status_code == 200:
<<<<<<< HEAD
            print("Telegram alert sent successfully!")
        else:
            print(f"Failed to send Telegram alert: {response.status_code}\n{response.text}")
=======
            print("✓ Telegram alert sent successfully!")
        else:
            print(f"✗ Failed to send Telegram alert: {response.status_code}\n{response.text}")
>>>>>>> cd07ab0 (split merged)
    except FileNotFoundError:
        print(f"Error: Stitched file at {video_path} not found.")