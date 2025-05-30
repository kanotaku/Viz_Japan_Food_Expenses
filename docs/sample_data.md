# サンプルデータについて

## サンプルCSVファイル：SSDSE-C-2025.csv

このアプリケーションには、分析用のサンプルデータとして「SSDSE-C-2025.csv」が含まれています。このデータセットは、日本の都道府県別食料品支出に関する架空のデータです。

## データ内容

- **行**: 47都道府県
- **列**: 複数の食料品カテゴリ（米類、パン類、めん類など）
- **値**: 各都道府県の食料品カテゴリごとの支出金額（円）

## データ形式

```csv
都道府県,米類,パン類,めん類,その他穀類,生鮮魚介,塩干魚介,魚介加工品,牛肉,豚肉,鶏肉
北海道,25600,15300,12700,1800,12400,3200,4900,8300,6200,4100
青森県,28400,13200,11500,1600,16300,4500,5300,7100,7300,4800
...
```

## データの見方

- **各行**: 都道府県を表します
- **各列**: 食料品カテゴリを表します
- **セルの値**: その都道府県における、そのカテゴリの平均支出額（円）

## 独自データの準備方法

このアプリケーションで使用するためのオリジナルデータを作成する場合は、以下の手順に従ってください：

1. **CSVファイル形式で作成**
   - カンマ区切り（CSV）形式で保存
   - UTF-8またはShift-JISエンコーディングを使用

2. **適切なデータ構造**
   - 1行目：ヘッダー行（カテゴリ名）
   - 1列目：都道府県名
   - その他の列：各カテゴリの数値データ

3. **都道府県名の表記**
   - 「都」「府」「県」を含めた正式名称を使用（例：「東京都」、「大阪府」、「福岡県」）
   - 都道府県名は全国地図への表示のため、正確に記載してください

4. **数値データ**
   - 数値のみを入力（通貨記号やカンマなし）
   - 欠損値がある場合は空欄にすることも可能です

## サンプルデータの制限事項

サンプルデータは学習・デモ目的で提供されているため、以下の点にご注意ください：

- データは架空のものであり、実際の統計値と異なる場合があります
- 詳細な分析や研究目的には適していない場合があります
- データは最新の統計情報を反映していない場合があります

独自の分析には、政府統計などの信頼できる情報源からの最新データを使用することをお勧めします。