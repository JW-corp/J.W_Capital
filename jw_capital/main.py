from flask import Flask, render_template_string

app = Flask(__name__)

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
           background-size: 40px 40px;
           background-image: 
               linear-gradient(to right, rgb(32, 32, 32) 1px, transparent 1px),
               linear-gradient(to bottom, rgb(32, 32, 32) 1px, transparent 1px);
       }
   </style>
</head>
<body class="bg-black min-h-screen grid-bg">
   <div class="relative">
       <!-- 네비게이션 -->
       <nav class="bg-black border-b border-gray-800">
           <div class="container mx-auto px-6 py-4">
               <div class="text-2xl font-bold text-white">
                   JW Corp
               </div>
           </div>
       </nav>

       <!-- 메인 섹션 -->
       <section class="container mx-auto px-6 py-24">
           <div class="max-w-4xl">
               <h1 class="text-5xl md:text-7xl font-bold text-white mb-8 leading-tight">
                   AI-Powered<br/>Hedge Fund
               </h1>
               <p class="text-xl md:text-2xl text-gray-400 mb-12 max-w-2xl">
                   Maximizing returns through advanced AI trading algorithms. Let your capital work smarter with JW Corp.
               </p>

               <!-- 투자 현황 -->
               <div class="mt-16 bg-gray-900 rounded-xl p-8 border border-gray-800">
                   <h2 class="text-xl font-bold mb-8 bg-gradient-to-r from-indigo-500 via-purple-500 to-cyan-500 text-transparent bg-clip-text">
                       Investment Status
                   </h2>

                   <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                       <div class="p-6 rounded-xl bg-black glow-border">
                           <div class="text-gray-400">Initial Investment</div>
                           <div class="text-2xl font-bold mt-2 text-white">₩2,000,000</div>
                       </div>

                       <div class="p-6 rounded-xl bg-black glow-border">
                           <div class="text-gray-400">Current Value</div>
                           <div class="text-2xl font-bold mt-2 text-white">₩2,093,975</div>
                       </div>

                       <div class="p-6 rounded-xl bg-black glow-border">
                           <div class="text-gray-400">Return</div>
                           <div class="text-2xl font-bold mt-2 text-green-400">+4.70%</div>
                       </div>
                   </div>

                   <div class="mt-8 p-6 rounded-xl bg-black border border-gray-800">
                       <div class="flex justify-between items-center">
                           <div class="text-gray-400">AI Engine Status</div>
                           <div class="px-3 py-1 rounded-full bg-green-500/20 text-green-400 border border-green-500/30">
                               TESTING
                           </div>
                       </div>
                   </div>
               </div>
           </div>
       </section>
   </div>
</body>
</html>
'''


@app.route('/')
def home():
    return render_template_string(HTML)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False, port=5001)