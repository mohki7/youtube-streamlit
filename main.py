#streamlitで爆速Webアプリ開発

import streamlit as st
import numpy as np
import pandas as pd
import time
#画像表示のためにインストール
from PIL import Image

#タイトルの追加
st.title("Streamlit 超入門")

#テキストの追加
st.write("DataFrame")

df = pd.DataFrame({
    "1列目" : [1, 2, 3, 4],
    "2列目" : [10, 20, 30, 40]
})

#データフレームの追加。動的な表を作りたい時に用いる。
#writeでもデータフレームを表示できるが、dataframeを使えばwidthやheightも指定可能。
#.style.highlight_maxで最大値をハイライト
st.dataframe(df.style.highlight_max(axis = 0))

#静的な表を作りたいときは.tableを用いる。
st.table(df.style.highlight_max(axis = 0))

#マジックコマンド
"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

#折れ線グラフ
df_2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ["a", "b", "c"]
)
st.write("ノーマル折れ線グラフ")
st.line_chart(df_2)
st.write("線の下を塗った折れ線グラフ")
st.area_chart(df_2)
st.write("棒グラフ")
st.bar_chart(df_2)

#マップのプロット
#新宿付近の座標を示すようにする
df_3 = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    #新宿付近の緯度と経度が35.69度と139.7度
    #ランダムな数を標準正規分布に従って生成し、それぞれを緯度と経度とみなす
    columns = ["lat", "lon"],
)
st.write("新宿付近のドット")
st.map(df_3)

#画像表示
#st.write("Display Image")

#画像読み込み
#img = Image.open("2.jpg")

#表示
#st.image(img, caption = "Hikaru Morita", use_column_width = True)

#チェックボックス
#.checkboxはチェックが入れられていたらTrue、なかったらFalseを返す
#if st.checkbox("Show Image"):
#    st.image(img, caption = "Hikaru Morita")

#セレクトボックス
option = st.selectbox(
    "あなたの好きな数字は？",
    list(range(1, 11))
)

"あなたの好きな数字の税込み価格は", option * 1.1, "です。"

#テキストボックス
st.write("Interactive Widgets")

option_text = st.text_input("あなたの趣味を教えてください")
"あなたの趣味は", option_text, "です。"

#スライダー
condition = st.slider("あなたの今の調子は？", 0, 100, 50)
"コンディション:", condition

#サイドバーの追加はstの後に.sidebarをつける

#2カラム表示
left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです。")

#イクスパンダー
expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")

#プログレスバー
#progressの処理が終わるまで下の処理は実行されない
st.write("プログレスバーの表示")
"Start!!!"
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress( i + 1 )
    time.sleep(0.1)

