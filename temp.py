import requests

# Configuration
URL = "https://portal.nsbm.ac.lk/examtrack/backend/api/attendance.php"
PHPSESSID = "mgj39qlff0tjae357ji2k2aqee"  # Update if session changes

# List of UMIS IDs to mark attendance for
umisid_list = [
    # "36091",
    # "37800",
    # "38795",
    # "38796",
    # "38804",
    # "39340",
    # "39353",
    # "39362",
    # "39386",
    # "39406",
    # "39410",
    # "39433",
    # "39450",
    # "39451",
    # "39486",
    "39493",
    "39615",
    "42281",
    "42312",
    "42481",
    "42539",
    "42600",
    "42636",
    "42651",
    "42747",
    "42772",
    "42834",
    "43082",
    "43162",
    "43244",
    "43265",
    "37696",
    "37717",
    "38787",
    "39422",
    "39435",
    "39449",
    "39452",
    "39456",
    "39472",
    "39521",
    "39639",
    "39665",
    "39678",
    "39719",
    "42394",
    "42592",
    "42659",
    "42664",
    "42690",
    "42708",
    "42939",
    "42952",
    "43022",
    "43189",
    "43201",
    "43250",
    "43305",
    "43306",
    "38788",
    "39371",
    "39374",
    "39425",
    "39430",
    "39432",
    "39499",
    "39744",
    "42289",
    "42602",
    "42613",
    "42738",
    "42807",
]

# Common data (same for all requests)
common_data = {
    "action": "mark",
    "module_code": "AI 1102.2",
    "exam_date": "2026-09-21",
    "start_time": "13:30:00",
    "hall_id": "4",
    "status": "present",
}

# Headers
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://portal.nsbm.ac.lk",
    "Referer": "https://portal.nsbm.ac.lk/examtrack/student_track/students.php",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "User-Agent": (
        "Mozilla/5.0 (Linux; Android 15; Pixel 9) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/152.0.0.0 Mobile Safari/537.36"
    ),
    "sec-ch-ua": '"Chromium";v="152", "Not?A_Brand";v="24", "Brave";v="152"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
}

# Cookies
cookies = {
    "PHPSESSID": PHPSESSID,
}


def mark_attendance(umisid: str) -> dict:
    """Send a single attendance marking request for the given umisid."""
    payload = {**common_data, "umisid": umisid}

    try:
        response = requests.post(
            URL,
            headers=headers,
            cookies=cookies,
            json=payload,
            timeout=15,
        )
        return {
            "umisid": umisid,
            "status_code": response.status_code,
            "response": response.text,
        }
    except requests.RequestException as e:
        return {
            "umisid": umisid,
            "status_code": None,
            "response": f"ERROR: {e}",
        }


def main():
    for umisid in umisid_list:
        result = mark_attendance(umisid)
        print(
            f"[{result['status_code']}] UMIS ID {result['umisid']} -> {result['response']}"
        )


if __name__ == "__main__":
    main()