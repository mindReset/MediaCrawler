from dotenv import load_dotenv

# 加载 .env.local 文件
load_dotenv(".env.local")

# 基础配置
PLATFORM = "xhs"
KEYWORDS = "python,golang"
LOGIN_TYPE = "qrcode"  # qrcode or phone or cookie
# 获取 COOKIES 环境变量
# COOKIES = os.getenv("COOKIES")
COOKIES = ""
SORT_TYPE = "popularity_descending"  # 具体值参见 media_platform.xxx.field 下的枚举值，展示只支持小红书
CRAWLER_TYPE = (
    "search"  # 爬取类型，search(关键词搜索) | detail(帖子相亲)| creator(创作者主页数据)
)

# 是否开启 IP 代理
ENABLE_IP_PROXY = False

# 代理 IP 池数量
IP_PROXY_POOL_COUNT = 2

# 设置为 True 不会打开浏览器（无头浏览器），设置 False 会打开一个浏览器（小红书如果一直扫码登录不通过，打开浏览器手动过一下滑动验证码）
HEADLESS = True

# 是否保存登录状态
SAVE_LOGIN_STATE = True

# 数据保存类型选项配置，支持三种类型：csv、db、json
SAVE_DATA_OPTION = "csv"  # csv or db or json

# 用户浏览器缓存的浏览器文件配置
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# 爬取视频/帖子的数量控制
CRAWLER_MAX_NOTES_COUNT = 20

# 并发爬虫数量控制
MAX_CONCURRENCY_NUM = 4

# 是否开启爬评论模式，默认不开启爬评论
ENABLE_GET_COMMENTS = False

# 指定小红书需要爬虫的笔记 ID 列表
XHS_SPECIFIED_ID_LIST = [
    "5fa8cab20000000001001d87",
    # ........................
]

# 指定抖音需要爬取的 ID 列表
DY_SPECIFIED_ID_LIST = [
    "7280854932641664319",
    "7202432992642387233",
    # ........................
]

# 指定快手平台需要爬取的 ID 列表
KS_SPECIFIED_ID_LIST = ["3xf8enb8dbj6uig", "3x6zz972bchmvqe"]

# 指定 B 站平台需要爬取的视频 bvid 列表
BILI_SPECIFIED_ID_LIST = [
    "BV1d54y1g7db",
    "BV1Sz4y1U77N",
    "BV14Q4y1n7jz",
    # ........................
]

# 指定微博平台需要爬取的帖子列表
WEIBO_SPECIFIED_ID_LIST = [
    "4982041758140155",
    # ........................
]

# 指定小红书创作者 ID 列表
XHS_CREATOR_ID_LIST = [
    "5c565834000000001b02f0d5",
    "5fc8880400000000010006b5",
    "5bb8e9f49bc81b0001178ef7",
]
