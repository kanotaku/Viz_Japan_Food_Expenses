import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import json
import io
import chardet

# 0️⃣ 画面設定
st.set_page_config(
    page_title="都道府県別・食料品支出ダッシュボード",
    layout="wide"
)

# 1️⃣ データ読み込み関連の関数
@st.cache_data
def load_geojson():
    """GeoJSONデータを読み込む"""
    url = "https://raw.githubusercontent.com/dataofjapan/land/master/japan.geojson"
    response = requests.get(url)
    return json.loads(response.content)

@st.cache_data
def detect_encoding(uploaded_file):
    """ファイルのエンコーディングを検出する"""
    content = uploaded_file.read()
    detection = chardet.detect(content)
    return detection["encoding"]

@st.cache_data
def load_csv_data(uploaded_file):
    """CSVファイルを読み込み、DataFrameとして返す"""
    # エンコーディングを検出
    encoding = detect_encoding(uploaded_file)
    # ファイルポインタを先頭に戻す
    uploaded_file.seek(0)
    
    # CSVを読み込む
    try:
        df = pd.read_csv(uploaded_file, encoding=encoding)
        return df
    except Exception as e:
        st.error(f"CSVの読み込みに失敗しました: {e}")
        return None

# 2️⃣ メイン処理
def main():
    st.title("都道府県別・食料品支出ダッシュボード")
    
    # ファイルアップロード
    st.header("1. データファイルのアップロード")
    uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
    
    if uploaded_file is not None:
        # CSVデータの読み込み
        df = load_csv_data(uploaded_file)
        
        if df is not None:
            # データの表示
            st.subheader("アップロードされたデータ")
            st.dataframe(df.head())
            
            # 都道府県の列を特定
            prefecture_col = "Prefecture"  # デフォルトの列名
            if prefecture_col not in df.columns:
                # 都道府県が含まれる可能性のある列名
                possible_cols = [col for col in df.columns if "都道府県" in col or "prefecture" in col.lower()]
                if possible_cols:
                    prefecture_col = possible_cols[0]
                else:
                    prefecture_col = df.columns[0]  # 最初の列を都道府県列と仮定
            
            # カテゴリ選択
            st.header("2. 分析する食料品カテゴリの選択")
            # Prefecture列の次の列をデフォルトに設定
            idx = list(df.columns).index(prefecture_col)
            default_category = df.columns[idx + 1] if idx + 1 < len(df.columns) else df.columns[1]
            
            # カテゴリ選択ボックス
            category = st.selectbox(
                "分析するカテゴリを選択してください",
                options=[col for col in df.columns if col != prefecture_col],
                index=list([col for col in df.columns if col != prefecture_col]).index(default_category)
            )
            
            # 都道府県選択
            st.header("3. 比較する都道府県の選択")
            prefectures = sorted(df[prefecture_col].unique())
            
            # デフォルト選択の設定
            default_prefs = []
            if "東京都" in prefectures:
                default_prefs.append("東京都")
            if "大阪府" in prefectures:
                default_prefs.append("大阪府")
            
            selected_prefs = st.multiselect(
                "比較したい都道府県を選択してください（最大5つ）",
                options=prefectures,
                default=default_prefs
            )
            
            # 選択都道府県が5つを超える場合の警告
            if len(selected_prefs) > 5:
                st.warning("⚠️ 選択できる都道府県は最大5つまでです。選択数を減らしてください。")
            
            # 選択された都道府県のデータ表示
            if selected_prefs:
                st.header("4. 選択した都道府県の比較")
                
                # 選択された都道府県のデータを抽出
                filtered_df = df[df[prefecture_col].isin(selected_prefs)]
                
                # 棒グラフの作成
                fig_bar = px.bar(
                    filtered_df,
                    x=prefecture_col,
                    y=category,
                    title=f"選択した都道府県の{category}支出比較",
                    labels={prefecture_col: "都道府県", category: f"{category}支出額"}
                )
                st.plotly_chart(fig_bar, use_container_width=True)
                
                # 地図の作成
                st.header("5. 日本地図上での支出分布")
                
                # GeoJSONデータの読み込み
                geojson_data = load_geojson()
                
                # 地図作成用のデータフレーム準備
                map_df = df.copy()
                
                # GeoJSONのプロパティ名とデータフレームの都道府県名を一致させる
                map_df = map_df.rename(columns={prefecture_col: "prefecture"})
                
                # Choroplethマップの作成
                fig_map = px.choropleth(
                    map_df,
                    geojson=geojson_data,
                    locations="prefecture",
                    featureidkey="properties.nam_ja",
                    color=category,
                    color_continuous_scale="Viridis",
                    scope="asia",
                    labels={category: f"{category}支出額"},
                    title=f"都道府県別・{category}支出マップ"
                )
                
                # 日本に焦点を当てる
                fig_map.update_geos(
                    fitbounds="locations",
                    visible=False,
                    showcoastlines=True,
                    showland=True,
                    showocean=True,
                    oceancolor="LightBlue"
                )
                
                st.plotly_chart(fig_map, use_container_width=True)
                
                # 選択された都道府県のデータテーブル表示
                st.subheader("選択した都道府県のデータ詳細")
                st.dataframe(
                    filtered_df[[prefecture_col, category]].sort_values(by=category, ascending=False),
                    use_container_width=True
                )
    else:
        # ファイルがアップロードされていない場合のメッセージ
        st.info("👆 CSVファイルをアップロードして開始してください。")
        st.markdown("""
        ### 入力データについて:
        - CSV形式の家計食料品支出データ
        - 行: 都道府県
        - 列: 食料品カテゴリ
        
        ### 使用方法:
        1. CSVファイルをアップロード
        2. 分析したい食料品カテゴリを選択
        3. 比較したい都道府県を選択（最大5つ）
        4. 棒グラフとヒートマップで可視化結果を確認
        """)

# 3️⃣ アプリケーションの実行
if __name__ == "__main__":
    main()
