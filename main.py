from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/today", methods=["POST"])
def today_menu():
    try:
        # GitHub JSON에서 급식 정보 불러오기
        url = "https://raw.githubusercontent.com/Jihun07/Lunchcrawler/main/today_menu.json"
        res = requests.get(url)
        data = res.json()

        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": f"📅 {data['date']}\n🍱 {data['menu']}"
                        }
                    }
                ]
            }
        }
        return jsonify(response)

    except Exception as e:
        print("에러:", e)
        return jsonify({
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
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
