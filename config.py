TOKEN = '1117070347:AAFW-z66R9q8U9IuXPrSgfE38qdwZPEMVRE'
NGROK_URL = 'https://113b1ead.ngrok.io'
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(NGROK_URL)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'