from send_email import send_email

if __name__ == "__main__":
    recipient = "ایمیلتو_اینجا_بذار@example.com"  # جایگزین کن با ایمیل واقعی
    subject = "Test Email"
    body = "سلام! این یه ایمیل تستی هست 🌹"

    try:
        send_email(recipient, subject, body)
        print("✅ Email function executed")
    except Exception as e:
        print(f"❌ Error: {e}")
