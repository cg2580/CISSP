import streamlit as st

st.set_page_config(
    page_title="CISSP备考笔记", 
    page_icon="☕", 
    layout="wide",
    initial_sidebar_state="auto", 
    menu_items=None
)

st.write("# 🚀 CISSP备考笔记 👋")

# st.subheader("考试范围")

"""
## 考试形式

2024年4月以后，中文版考试也和英文版一样，采用CAT（计算机自适应测试）考试形式，考题数量为100~150道题目，答对的难题数量越多，系统能越快的评估出考生的水平，需要回答的题目总数也越少，考试也能今早结束。考试总时长最多不会超过3小时，答题结束后，考生会立刻知道自己是否通过了考试。

## 考试范围

CISSP CBK的8个知识领域，分别是：

"""

row1_col1, row1_col2 = st.columns(2)
with row1_col1.container(height=300):
    """ 
    ### 🌻 安全和风险管理
    - 职业道德
    - 安全治理与合规
    - 法律法规和监管合规
    - 人员安全
    - 风险管理
    """
    bt = st.button("查看", key="安全和风险管理", use_container_width=True)
    if bt:
        st.switch_page("pages/1_🌻_安全和风险管理.py")

with row1_col2.container(height=300):
    """ 
    ### 🍂 资产安全
    - 识别和分类信息和资产
    - 建立信息和资产处置要求
    - 安全的配置资源
    - 管理数据生命周期
    - 确定数据安全控制措施和合规要求
    """
    bt = st.button("查看", key="资产安全", use_container_width=True)
    if bt:
        st.switch_page("pages/2_🍂_资产安全.py")


row2_col1, row2_col2 = st.columns(2)
with row2_col1.container(height=300):
    """ 
    ### 🍉 安全架构与工程
    - 安全设计原则
    - 安全模型
    - 选择有效的控制措施
    - 密码术
    - 物理安全
    """
    bt = st.button("查看", key="安全架构与工程", use_container_width=True)
    if bt:
        st.switch_page("pages/3_🍉_安全架构与工程.py")

with row2_col2.container(height=300):
    """ 
    ### 🍂 通信与网络安全
    - 安全网络架构
    - 安全网络组件
    - 安全通信信道
    """
    bt = st.button("查看", key="通信与网络安全", use_container_width=True)
    if bt:
        st.switch_page("pages/4_🍂_通信与网络安全.py")


row3_col1, row3_col2 = st.columns(2)
with row3_col1.container(height=300):
    """ 
    ### 🍉 身份和访问管理
    - 控制对资产的物理和逻辑访问
    - 标识和身份验证
    - 授权机制
    - 身份和访问配置生命周期
    - 实施身份验证系统
    """
    bt = st.button("查看", key="身份和访问管理", use_container_width=True)
    if bt:
        st.switch_page("pages/5_🍉_身份和访问管理.py")

with row3_col2.container(height=300):
    """ 
    ### 🍑 安全评估与测试
    - 评估与测试战略
    - 测试安全控制措施
    - 收集安全流程数据
    - 分析和报告结果
    - 开展和促进审计
    """
    bt = st.button("查看", key="安全评估与测试", use_container_width=True)
    if bt:
        st.switch_page("pages/6_🍑_安全评估与测试.py")


row4_col1, row4_col2 = st.columns(2)
with row4_col1.container(height=300):
    """ 
    ### 🍔 安全运营
    - 调查
    - 记录和持续监测
    - 变更和配置管理
    - 事件管理
    - 灾难恢复
    """
    bt = st.button("查看", key="安全运营", use_container_width=True)
    if bt:
        st.switch_page("pages/7_🍔_安全运营.py")

with row4_col2.container(height=300):
    """ 
    ### 🍕 软件研发安全
    - 软件研发生命周期
    - 软件研发种的安全控制措施
    - 评估软件安全
    - 评估所购软件的安全
    - 安全编码准则和标准
    """
    bt = st.button("查看", key="软件研发安全", use_container_width=True)
    if bt:
        st.switch_page("pages/8_🍕_软件研发安全.py")


"""
## 证书申领

待补充

"""