from flask import Flask, render_template_string, jsonify
from pycoingecko import CoinGeckoAPI
from datetime import datetime

app = Flask(__name__)
cg = CoinGeckoAPI()

def get_btc_price():
   try:
       bitcoin_data = cg.get_price(ids='bitcoin', vs_currencies='krw')
       price = format(int(bitcoin_data['bitcoin']['krw']), ',')
       timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       return price, timestamp
   except Exception as e:
       print(f"Error: {e}")
       return "Error", datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@app.route('/get_price')
def get_price():
   price, timestamp = get_btc_price()
   return jsonify({'price': price, 'timestamp': timestamp})

HTML = '''
<!DOCTYPE html>
<html>
<head>
  <title>JW Corp | AI Trading Engine</title>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
      body {
          font-family: 'Inter', sans-serif;
      }
      .grid-bg {
          background-size: 20px 20px;
          background-image: 
              linear-gradient(to right, rgb(32, 32, 32) 1px, transparent 1px),
              linear-gradient(to bottom, rgb(32, 32, 32) 1px, transparent 1px);
      }
      @media (min-width: 768px) {
          .grid-bg {
              background-size: 40px 40px;
          }
      }
  </style>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body class="bg-black min-h-screen grid-bg">
  <div class="relative">
      <!-- 네비게이션 -->
      <nav class="bg-black border-b border-gray-800">
          <div class="container mx-auto px-4 py-4 md:px-6">
              <div class="text-xl md:text-2xl font-bold text-white">
                  JW Corp
              </div>
          </div>
      </nav>

      <!-- 메인 섹션 -->
      <section class="container mx-auto px-4 py-12 md:px-6 md:py-24">
          <div class="max-w-4xl mx-auto">
              <h1 class="text-4xl md:text-5xl lg:text-7xl font-bold text-white mb-6 md:mb-8 leading-tight">
                  AI-Powered<br/>Hedge Fund
              </h1>
              <p class="text-lg md:text-xl lg:text-2xl text-gray-400 mb-8 md:mb-12 max-w-2xl">
                  Maximizing returns through advanced AI trading algorithms. Let your capital work smarter with JW Corp.
              </p>

              <!-- 투자 현황 -->
              <div class="mt-8 md:mt-16 bg-gray-900 rounded-xl p-4 md:p-8 border border-gray-800">
                  <h2 class="text-lg md:text-xl font-bold mb-6 md:mb-8 bg-gradient-to-r from-indigo-500 via-purple-500 to-cyan-500 text-transparent bg-clip-text">
                      Investment Status
                  </h2>

                  <div class="grid grid-cols-1 gap-4 md:grid-cols-3 md:gap-6">
                      <div class="p-4 md:p-6 rounded-xl bg-black glow-border">
                          <div class="text-sm md:text-base text-gray-400">BTC Price</div>
                          <div id="btc-price" class="text-xl md:text-2xl font-bold mt-2 text-white">Loading...</div>
                          <div id="timestamp" class="text-xs text-gray-500 mt-1">Updating...</div>
                      </div>

                      <div class="p-4 md:p-6 rounded-xl bg-black glow-border">
                          <div class="text-sm md:text-base text-gray-400">AUM</div>
                          <div class="text-xl md:text-2xl font-bold mt-2 text-white">₩2,000,000</div>
                      </div>

                      <div class="p-4 md:p-6 rounded-xl bg-black glow-border">
                          <div class="text-sm md:text-base text-gray-400">Return</div>
                          <div class="text-xl md:text-2xl font-bold mt-2 text-green-400">+4.70%</div>
                      </div>
                  </div>

                  <div class="mt-4 md:mt-8 p-4 md:p-6 rounded-xl bg-black border border-gray-800">
                      <div class="flex justify-between items-center">
                          <div class="text-sm md:text-base text-gray-400">AI Engine Status</div>
                          <div class="px-2 py-1 md:px-3 rounded-full bg-green-500/20 text-green-400 border border-green-500/30 text-sm">
                              TESTING
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </section>
  </div>

  <script>
      function updatePrice() {
          fetch('/get_price')
              .then(response => response.json())
              .then(data => {
                  document.getElementById('btc-price').innerText = '₩' + data.price;
                  document.getElementById('timestamp').innerText = data.timestamp;
              })
              .catch(error => console.error('Error:', error));
      }

      // 초기 로드
      updatePrice();

      // 60초마다 가격 업데이트
      setInterval(updatePrice, 60000);
  </script>
</body>
</html>
'''

@app.route('/')
def home():
   return render_template_string(HTML)

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=False, port=5001)