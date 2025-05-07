from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

@app.post("/lunch")
async def get_lunch(request: Request):
    try:
        # 요청 데이터 파싱
        req_json = await request.json()
        user_utterance = req_json.get("userRequest", {}).get("utterance", "")

        # 급식 정보 가져오기
        async with httpx.AsyncClient() as client:
            res = await client.get("https://raw.githubusercontent.com/Jihun07/Lunchcrawler/main/today_menu.json")
            data = res.json()
            date = data.get("date", "")
            menu = data.get("menu", "")

        # 카카오톡 챗봇 응답 형식에 맞게 구성
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": f"📅 {date}\n🍱 {menu}"
                        }
                    }
                ]
            }
        }
        return JSONResponse(content=response)

    except Exception as e:
        # 에러 발생 시 응답
        error_response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "❌ 급식 정보를 불러올 수 없습니다."
                        }
                    }
                ]
            }
        }
        return JSONResponse(content=error_response)


#python -m uvicorn main:app --reload
