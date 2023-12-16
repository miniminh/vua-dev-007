from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    # Process the image (you can do some image processing here)

    # Example data to send back
    image_data = [
  {
    "ID": "1",
    "name": "3-Stripes Low Cut Socks 3 Pairs",
    "brand": "adidas",
    "color": "Grey",
    "description": "Long sets of tuck-ups or leg presses, workouts feel just a little bit easier with the 3-Stripes on your side. Cut low for a comfort, these socks show off a touch of adidas love on the cuff for added motivation when you need it. Lightweight, moisture-wicking yarn keeps your feet feeling as good as they look.",
    "currency": "USD",
    "price": "10.0",
    "avg_rating": "4.8",
    "images": [
      "https://assets.adidas.com/images/w_600,f_auto,q_auto/9af3f275aac6437aaa68aca1006424e0_9366/3-Stripes_Low_Cut_Socks_3_Pairs_Grey_EX6581_03_standard.jpg",
      "https://assets.adidas.com/images/w_600,f_auto,q_auto/328ba4c724684d558860aca10066da4c_9366/3-Stripes_Low_Cut_Socks_3_Pairs_Grey_EX6581_41_detail_hover.jpg",
      "https://assets.adidas.com/images/w_600,f_auto,q_auto/8e0cede57c044d8f8d8caca10065e0ca_9366/3-Stripes_Low_Cut_Socks_3_Pairs_Grey_EX6581_42_detail.jpg",
      "https://assets.adidas.com/images/w_600,f_auto,q_auto/d86020d4c5984443a954aca100656432_9366/3-Stripes_Low_Cut_Socks_3_Pairs_Grey_EX6581_43_detail.jpg"
    ],
    "url": "https://www.adidas.com/us/3-stripes-low-cut-socks-3-pairs/EX6581.html"
  },
  {
    "ID": "2",
    "name": "3-Stripes Training Tee (Plus Size)",
    "brand": "adidas",
    "color": "Pink",
    "description": "Nearly light as air. This adidas training t-shirt is a simple tee for anyone who likes a barely-there feel. The fabric is not only ultralight, but semi-sheer. AEROREADY wicks moisture so you stay focused on the workout.",
    "currency": "USD",
    "price": "24.0",
    "avg_rating": "4.0",
    "images": [
      "https://assets.adidas.com/images/w_600,f_auto,q_auto/d69adf32de764f118161ad0f01833375_9366/3-Stripes_Training_Tee_(Plus_Size)_Pink_GR8267_21_model.jpg",
      "https://assets.adidas.com/images/w_600,f_auto,q_auto/93f0a145bd644bd8bb5cad0f018290b0_9366/3-Stripes_Training_Tee_(Plus_Size)_Pink_GR8267_23_hover_model.jpg",
      "https://assets.adidas.com/images/w_600,f_auto,q_auto/f2a398c7f6b949b2b2d8ad0f0180188d_9366/3-Stripes_Training_Tee_(Plus_Size)_Pink_GR8267_25_model.jpg",
      "https://assets.adidas.com/images/w_600,f_auto,q_auto/509b04503b8442158338ad0101699a28_9366/3-Stripes_Training_Tee_(Plus_Size)_Pink_GR8267_01_laydown.jpg",
      "https://assets.adidas.com/images/w_600,f_auto,q_auto/ccebd0c11bcd42479f28ad0f01809a5f_9366/3-Stripes_Training_Tee_(Plus_Size)_Pink_GR8267_41_detail.jpg",
      "https://assets.adidas.com/images/w_600,f_auto,q_auto/b6fc92fd45804113bb72ad0f01817c94_9366/3-Stripes_Training_Tee_(Plus_Size)_Pink_GR8267_42_detail.jpg"
    ],
    "url": "https://www.adidas.com/us/3-stripes-training-tee-plus-size/GR8267.html"
  }
    ]

    return jsonify(image_data)

if __name__ == '__main__':
    app.run(debug=True)
