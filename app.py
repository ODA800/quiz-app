import streamlit as st
import random

# 総合テスト完全版のQ&A読み込み
qa_pairs = []
with open("総合テスト完全版（問題＋解答）.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    current_q = ""
    current_a = ""
    for line in lines:
        if line.startswith("Q"):
            current_q = line.strip()
        elif line.startswith("A"):
            current_a = line.strip()
            qa_pairs.append((current_q, current_a))

# タイトル
st.title("総合テスト ランダム一問一答")

# セッション状態初期化
if "question" not in st.session_state:
    st.session_state.question = None
    st.session_state.answer = None

# 新しい問題を出すボタン
if st.button("問題を出す"):
    q, a = random.choice(qa_pairs)
    st.session_state.question = q
    st.session_state.answer = a

# 問題表示
if st.session_state.question:
    st.subheader(st.session_state.question)

    # 答えを見るボタン
    if st.button("答えを見る"):
        st.write(st.session_state.answer)
