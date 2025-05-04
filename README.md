# 都道府県別・食料品支出ダッシュボード

> **Upload any prefectural food‑expense CSV → get interactive bar‑chart, heat‑map, and scatter correlation in seconds.**
> Built with Streamlit + Plotly. Runs locally **or** 24/7 on Replit Reserved VM.

## 🔗 デモ

| 1 クリックで実行            |                                                                                                                                        |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Replit Live Demo** | Public URL (AutoScale deploy) [https://japan-food-expenses-dezikamuru.replit.app/](https://japan-food-expenses-dezikamuru.replit.app/) |

## 特長 ✨

* **CSV ドロップだけ** – 都道府県列を自動検出、文字コードも推定。
* **最大 5 県を比較** – マルチセレクトで棒グラフ比較。
* **日本地図ヒートマップ** – 47 都道府県の支出を視覚化。
* **散布図 + 相関係数** – 任意 2 カテゴリの相関を自動計算し解説。
* **OSS スタック** – Streamlit / pandas / Plotly / requests / chardet だけ。

---

## クイックスタート (ローカル)

```bash
# 1. clone
$ git clone https://github.com/<your‑name>/pref-food-dashboard.git
$ cd pref-food-dashboard

# 2. install  ※Python 3.9+
$ pip install -r requirements.txt

# 3. run
$ streamlit run app.py
# → ブラウザが http://localhost:8501 を開きます
```

### Replit で動かす

1. Replit → **Create Repl ➜ Import from GitHub** で本リポジトリを読み込み。
2. `.replit` は既に下記を設定済みです。

```ini
run = "streamlit run app.py --server.port $PORT --server.address 0.0.0.0"
```

3. **Run ▶** ボタンでローカルプレビュー。
4. **Deploy ➜ AutoScale (Always‑On)** を選択すると 24h 公開 URL が発行されます。

---

## ディレクトリ構成

```
├─ docs/                 # スクリーンショット / サンプルデータ.csv
│   ├─ bar.png
│   ├─ map.png
│   ├─ scatter.png
│   └─ sample_food_spend.csv
├─ app.py               # Streamlit アプリ本体
├─ main.py              # Replit デフォルト起動スクリプト (app.py を呼び出すだけ)
├─ requirements.txt     # 依存ライブラリ
├─ .replit              # Replit 実行設定
└─ pyproject.toml / uv.lock / .pythonlibs … (Replit パッケージャ生成ファイル)
```

### Sample CSV

`sample_food_spend.csv` をつかって試遊してみてください。

自前データは以下フォーマットで用意してください。

| 列名 (例) | 説明               |
| ------ | ---------------- |
| 都道府県   | 47 都道府県名 (必須)    |
| 米      | 食料品カテゴリ別支出額 (数値) |
| パン …   | 同上               |

---

## 今後のアップデート

*

---

## ライセンス

MIT License

## データソース
**Data Source**: 総務省統計局「家計調査」2022年～2024年 / GeoJSON © dataofjapan  (CC BY 4.0)

---

### Author

kanotaku
