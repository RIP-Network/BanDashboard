import requests

def realizar_solicitud_telefono(numero_telefono):
    url = f"https://app.instasent.com/signup/valid/phone/{numero_telefono}/ES"

    headers = {
        "Host": "app.instasent.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.instasent.com/signup/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es-ES,es;q=0.9",
        "Cookie": "PHPSESSID=c6ffa57c3f40799a593e4f1f12fde3b9; _ga=GA1.3.1347250629.1702142366; _ga=GA1.1.1347250629.1702142366; _fbp=fb.1.1702142367474.1667201361; intercom-id-uimj6d6t=8d3bcef7-cef6-4e9a-9ec7-99ad17b6de39; intercom-session-uimj6d6t=; intercom-device-id-uimj6d6t=7fa62cfb-88cd-4d0e-b0be-3db2c6589039; _hjSessionUser_1760915=eyJpZCI6ImNkNWUzZTQ1LWZlNjgtNTdiMi1iODY4LTQ5YTkwMDkyNWFkMSIsImNyZWF0ZWQiOjE3MDIxNDIzNjcwMzUsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.3.792544947.1705016816; _hjIncludedInSessionSample_1760915=0; _hjSession_1760915=eyJpZCI6ImM4NjQ4OGQzLWYwNjMtNDgwOS1hODVkLWVmYTkzYjZjZGUyZiIsImMiOjE3MDUwMTY4MTU4MjAsInMiOjAsInIiOjAsInNiIjowfQ==; _hjAbsoluteSessionInProgress=0; _clck=30fk7k%7C2%7Cfib%7C0%7C1438; _dc_gtm_UA-152711-18=1; _ga_F8R4NW0QHM=GS1.1.1705016815.77.1.1705016952.47.0.0; _clsk=9b7d5%7C1705016953217%7C4%7C1%7Cp.clarity.ms%2Fcollect"
    }

    response = requests.get(url, headers=headers)

    print("Código de estado:", response.status_code)
    print("Contenido de la respuesta:")
    print(response.text)

if __name__ == "__main__":
    numero_telefono = input("Ingrese el número de teléfono: ")
    realizar_solicitud_telefono(numero_telefono)
