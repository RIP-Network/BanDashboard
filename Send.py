import requests

def login(usuario, contrasena):
    url_login = "https://app.instasent.com/login_check/"

    headers_login = {
        "Host": "app.instasent.com",
        "Connection": "keep-alive",
        "Content-Length": "138",
        "Cache-Control": "max-age=0",
        "sec-ch-ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://app.instasent.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://app.instasent.com/login/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es-ES,es;q=0.9",
        "Cookie": "PHPSESSID=2e1ff964f08dc0ee7fe47985cc080503; _fbp=fb.1.1705017478939.2025193893; _ga=GA1.1.903931104.1705017479; _ga_F8R4NW0QHM=GS1.1.1705017478.1.0.1705017478.60.0.0; _ga=GA1.3.903931104.1705017479; _gid=GA1.3.1185417285.1705017479; _dc_gtm_UA-152711-18=1; _hjSessionUser_1760915=eyJpZCI6IjAxMWI2Mjg5LTg5MGMtNWE0YS05NWNlLWYxMmB0ZTg0ZmVkOSIsImNyZWF0ZWQiOjE3MDUwMTc0NzkwMzMsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_1760915=0; _hjSession_1760915=eyJpZCI6IjVhYTdiZjA3LTczZTctNDE2Ny04NTBjLTBiNGJkYTYxMDkyZSIsImMiOjE3MDUwMTc0NzkwMzMsInMiOjAsInIiOjAsInNiIjowfQ==; _hjAbsoluteSessionInProgress=0; _clck=pni23o%7C2%7Cfic%7C0%7C1471; _clsk=1920ujl%7C1705018175017%7C4%7C1%7Cp.clarity.ms%2Fcollect; intercom-id-uimj6d6t=0a4527df-315f-41f4-b062-15b4b0b8146d; intercom-device-id-uimj6d6t=e57d8515-1ee9-42ff-8ba5-861511363d3d; PHPSESSID=0264f2536aae6a7a3bdbef3ffca04e2d; REMEMBERME=V29iYmxlQ29kZVxVc2VyQnVuZGxlXERvY3VtZW50XFVzZXI6Y0c5eWIzUmhPVGd6TVVCNmFYSmhaMjlzWkM1amIyMD06MTczNjU1MzQ5Nzo2ZWYwMTczMzFkZTUzMTQ2YzJhN2IyOTExNzBlOTI5YmFhZjcxZGMzYzI3MDNmOTAwNGJkMjIxNGVmZTlhOTNj; _hjSessionUser_1760915=eyJpZCI6IjAxMWI2Mjg5LTg5MGMtNWE0YS05NWNlLWYxMmI0ZTg0ZmVkOSIsImNyZWF0ZWQiOjE3MDUwMTc0NzkwMzMsImV4aXN0aW5nIjp0cnVlfQ==; _clck=pni23o%7C2%7Cfic%7C0%7C1471; _dc_gtm_UA-152711-18=1; _ga_F8R4NW0QHM=GS1.1.1705017478.1.1.1705018174.59.0.0; _clsk=1920ujl%7C1705018175017%7C4%7C1%7Cp.clarity.ms%2Fcollect; intercom-session-uimj6d6t=bW9XbEdiSis3RDJzK1JBTHppMmpHazJqaUptaXpKYVlNaUpPVUhTcWpuWk5MMnE2UGR1dHY2ZGdEQWxEQnhkby0tZ0JYWHRieGlNVzJBU0lkRzRQbmhxZz09--bfda751a937290587cdf391dc8b1310a37f058c6"
    }

    data_login = {
        "_csrf_token": "zyOSU2Jmn0IJ2b6dOz3BkmOj3Jf6iKOCqHWCaJwcPNY",
        "_username": usuario,
        "_password": contrasena,
        "_remember_me": "on",
        "loginBtn": ""
    }

    response_login = requests.post(url_login, headers=headers_login, data=data_login)

    print("Código de estado (Inicio de sesión):", response_login.status_code)
    print("Contenido de la respuesta (Inicio de sesión):")
    print(response_login.text)

    # Obtener las cookies de la respuesta
    cookies = response_login.cookies

    return cookies

def enviar_sms(cookies):
    url_sms = "https://app.instasent.com/push/sms-send/quick/new"

    headers_sms = {
        "Host": "app.instasent.com",
        "Connection": "keep-alive",
        "Content-Length": "203",
        "Cache-Control": "max-age=0",
        "sec-ch-ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://app.instasent.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://app.instasent.com/push/sms-send/quick/new",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es-ES,es;q=0.9",
        "Cookie": "PHPSESSID=0264f2536aae6a7a3bdbef3ffca04e2d; REMEMBERME=V29iYmxlQ29kZVxVc2VyQnVuZGxlXERvY3VtZW50XFVzZXI6Y0c5eWIzUmhPVGd6TVVCNmFYSmhaMjlzWkM1amIyMD06MTczNjU1MzQ5Nzo2ZWYwMTczMzFkZTUzMTQ2YzJhN2IyOTExNzBlOTI5YmFhZjcxZGMzYzI3MDNmOTAwNGJkMjIxNGVmZTlhOTNj; _hjSessionUser_1760915=eyJpZCI6IjAxMWI2Mjg5LTg5MGMtNWE0YS05NWNlLWYxMmI0ZTg0ZmVkOSIsImNyZWF0ZWQiOjE3MDUwMTc0NzkwMzMsImV4aXN0aW5nIjp0cnVlfQ==; _clck=pni23o%7C2%7Cfic%7C0%7C1471; _dc_gtm_UA-152711-18=1; _ga_F8R4NW0QHM=GS1.1.1705017478.1.1.1705018174.59.0.0; _clsk=1920ujl%7C1705018175017%7C4%7C1%7Cp.clarity.ms%2Fcollect; intercom-session-uimj6d6t=bW9XbEdiSis3RDJzK1JBTHppMmpHazJqaUptaXpKYVlNaUpPVUhTcWpuWk5MMnE2UGR1dHY2ZGdEQWxEQnhkby0tZ0JYWHRieGlNVzJBU0lkRzRQbmhxZz09--bfda751a937290587cdf391dc8b1310a37f058c6"
    }

    data_sms = {
        "api_sms_quick[country]": "ES",
        "api_sms_quick[to]": "+34651714148",
        "api_sms_quick[from]": "Instagram",
        "api_sms_quick[text]": "RIP-Network 532-324",
        "api_sms_quick[allowUnicode]": "0",
        "api_sms_quick[save]": ""
    }

    response_sms = requests.post(url_sms, headers=headers_sms, cookies=cookies, data=data_sms)

    print("Código de estado (Envío de SMS):", response_sms.status_code)
    print("Contenido de la respuesta (Envío de SMS):")
    print(response_sms.text)

# Solicitar al usuario que ingrese su nombre de usuario y contraseña
usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

# Realizar el proceso de autenticación y obtener las cookies
cookies = login(usuario, contrasena)

# Realizar la solicitud POST después de iniciar sesión
enviar_sms(cookies)
