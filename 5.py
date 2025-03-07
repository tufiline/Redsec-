import base64

payload = b"print('Evasión de antivirus')"
encoded = base64.b64encode(payload)
decoded = base64.b64decode(encoded)

exec(decoded)
