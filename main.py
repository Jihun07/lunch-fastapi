from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/lunch")
async def get_lunch():
    async with httpx.AsyncClient() as client:
        res = await client.get("https://raw.githubusercontent.com/Jihun07/Lunchcrawler/main/today_menu.json")
        data = res.json()
        date = data["date"]
        menu = data["menu"]

        return {
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
