python
import streamlit as st
import random

def main():
    st.title("名言おみくじ")

    quotes = [
        "人生に失敗がないと、成功もない。",
        "夢を見ることができるなら、それは実現できる。",
        "失敗は成功のもと。",
        "人生は一度きり。",
        "今日という日は二度と来ない。",
        "明日死ぬかのように生きろ。永遠に生きるかのように学べ。",
        "人生は自分で作り上げるものだ。"
        "人生は短い。後悔しないように生きよう。",
        "成功するためには、まず失敗を恐れないことだ。",
        "人生は、自分が思っているよりもずっと短い。"
    ]

    quote = random.choice(quotes)
    st.write("あなたの運勢は...")
    st.write(quote)

if __name__ == "__main__":
    main()