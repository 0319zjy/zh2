import streamlit as st
import pandas as pd
import time

# 页面配置
st.set_page_config(
    page_title="多功能应用中心 - 顶部导航",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义CSS - 顶部导航栏
st.markdown("""
<style>
    .top-nav {
        display: flex;
        background-color: #2c3e50;
        padding: 0;
        margin: -1rem -1rem 1rem -1rem;
        border-bottom: 3px solid #3498db;
    }
    .nav-item {
        padding: 1rem 2rem;
        color: white;
        text-decoration: none;
        border-right: 1px solid #34495e;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .nav-item:hover {
        background-color: #34495e;
    }
    .nav-item.active {
        background-color: #3498db;
        font-weight: bold;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# 导航状态管理
if 'nav_choice' not in st.session_state:
    st.session_state.nav_choice = "🏠 首页"

# 创建顶部导航栏
nav_items = ["🏠 首页", "📚 书籍", "🎬 视频", "🌿 旅游", "📄 简历"]
nav_html = '<div class="top-nav">'
for item in nav_items:
    active_class = "active" if st.session_state.nav_choice == item else ""
    nav_html += f'<div class="nav-item {active_class}" onclick="setNavChoice(\'{item}\')">{item}</div>'
nav_html += '</div>'

# JavaScript处理导航点击
st.components.v1.html(f"""
<script>
function setNavChoice(choice) {{
    parent.window.postMessage({{type: 'streamlit:setComponentValue', value: choice}}, '*');
}}
</script>
{nav_html}
""", height=60)

# 使用隐藏的selectbox作为替代方案
nav_choice = st.selectbox("导航选择", nav_items, key="nav_select", label_visibility="collapsed")

# 更新导航状态
if nav_choice != st.session_state.nav_choice:
    st.session_state.nav_choice = nav_choice
    st.rerun()

# 首页内容
if st.session_state.nav_choice == "🏠 首页":
    st.title("🚀 多功能应用中心")
    st.markdown("---")
    
    # 功能卡片
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📚 书籍档案")
        st.write("Python编程学习进度管理")
        st.metric("当前进度", "72%", "+5%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🎬 视频中心")
        st.write("喜羊羊与灰太狼全集")
        st.metric("视频数量", "8集", "在线播放")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🌿 旅游探索")
        st.write("南宁景点数据分析")
        st.metric("景点数量", "5个", "实时推荐")
        st.markdown('</div>', unsafe_allow_html=True)

# 其他模块实现类似...
