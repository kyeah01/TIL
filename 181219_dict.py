ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}

# ssafy의 semester1의 기간을 출력하세요

print(ssafy["duration"]["semester1"])

# ssafy dictionary 안에 들어 있는 '대전'을 출력하세요

print(ssafy["location"][1])

# daejoen 의 매니저 이름을 출력하세요.

print(ssafy["classes"]["daejeon"]["manager"])