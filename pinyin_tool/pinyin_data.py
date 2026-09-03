# 拼音打字练习题库（100 个常用字）
# 字段说明：
#   char  = 汉字
#   sm    = 声母        ym = 韵母      py = 带调全拼
#   input = 期望的键盘输入（无调，按真实拼音输入法规则）
#           ü 的两条规则已做进 input：
#           n/l 后打 v（女=nv 绿=lv）；j/q/x 后省点打 u（军=jun 学=xue）
# 注意：题库刻意避开了 16 个整体认读音节（zhi/yi/wu/yun...）和零声母字（爱安...），
#       那些拆不出"声母+韵母"结构；er 韵母只有零声母字（耳二），故不出现
# ── 关于介音字（2026-08-23 新增组）──
# u/i/ü 可以作"介音"垫在声母和韵母之间：kuo = k + [介音u] + o
# uo/ua/uai/uan/ia/iao/ian/iang/iong 这些组合不算独立韵母（不在 24 韵母表内），
# 它们 = 介音 + 表内韵母（如 iao = i + ao，uan = u + an）
# 本题库 ym 字段直接存"含介音的组合"整体，方便打字判定和反馈显示；
# 学/雪(x+üe)、军/裙(j/q+ün) 其实本来就是 ü 介音字

pin_list = [
    # ── 单韵母 ──
    {"char": "爸", "sm": "b",  "ym": "a",  "py": "bà",  "input": "ba"},
    {"char": "马", "sm": "m",  "ym": "a",  "py": "mǎ",  "input": "ma"},
    {"char": "大", "sm": "d",  "ym": "a",  "py": "dà",  "input": "da"},
    {"char": "坡", "sm": "p",  "ym": "o",  "py": "pō",  "input": "po"},
    {"char": "摸", "sm": "m",  "ym": "o",  "py": "mō",  "input": "mo"},
    {"char": "河", "sm": "h",  "ym": "e",  "py": "hé",  "input": "he"},
    {"char": "车", "sm": "ch", "ym": "e",  "py": "chē", "input": "che"},
    {"char": "乐", "sm": "l",  "ym": "e",  "py": "lè",  "input": "le"},
    {"char": "机", "sm": "j",  "ym": "i",  "py": "jī",  "input": "ji"},
    {"char": "七", "sm": "q",  "ym": "i",  "py": "qī",  "input": "qi"},
    {"char": "西", "sm": "x",  "ym": "i",  "py": "xī",  "input": "xi"},
    {"char": "图", "sm": "t",  "ym": "u",  "py": "tú",  "input": "tu"},
    {"char": "书", "sm": "sh", "ym": "u",  "py": "shū", "input": "shu"},
    {"char": "木", "sm": "m",  "ym": "u",  "py": "mù",  "input": "mu"},
    {"char": "女", "sm": "n",  "ym": "ü",  "py": "nǚ",  "input": "nv"},
    {"char": "绿", "sm": "l",  "ym": "ü",  "py": "lǜ",  "input": "lv"},
    # ── 复韵母 ──
    {"char": "白", "sm": "b",  "ym": "ai", "py": "bái", "input": "bai"},
    {"char": "海", "sm": "h",  "ym": "ai", "py": "hǎi", "input": "hai"},
    {"char": "菜", "sm": "c",  "ym": "ai", "py": "cài", "input": "cai"},
    {"char": "美", "sm": "m",  "ym": "ei", "py": "měi", "input": "mei"},
    {"char": "北", "sm": "b",  "ym": "ei", "py": "běi", "input": "bei"},
    {"char": "黑", "sm": "h",  "ym": "ei", "py": "hēi", "input": "hei"},
    {"char": "水", "sm": "sh", "ym": "ui", "py": "shuǐ", "input": "shui"},
    {"char": "对", "sm": "d",  "ym": "ui", "py": "duì", "input": "dui"},
    {"char": "包", "sm": "b",  "ym": "ao", "py": "bāo", "input": "bao"},
    {"char": "猫", "sm": "m",  "ym": "ao", "py": "māo", "input": "mao"},
    {"char": "草", "sm": "c",  "ym": "ao", "py": "cǎo", "input": "cao"},
    {"char": "头", "sm": "t",  "ym": "ou", "py": "tóu", "input": "tou"},
    {"char": "口", "sm": "k",  "ym": "ou", "py": "kǒu", "input": "kou"},
    {"char": "走", "sm": "z",  "ym": "ou", "py": "zǒu", "input": "zou"},
    {"char": "周", "sm": "zh", "ym": "ou", "py": "zhōu", "input": "zhou"},
    {"char": "球", "sm": "q",  "ym": "iu", "py": "qiú", "input": "qiu"},
    {"char": "牛", "sm": "n",  "ym": "iu", "py": "niú", "input": "niu"},
    {"char": "六", "sm": "l",  "ym": "iu", "py": "liù", "input": "liu"},
    {"char": "姐", "sm": "j",  "ym": "ie", "py": "jiě", "input": "jie"},
    {"char": "贴", "sm": "t",  "ym": "ie", "py": "tiē", "input": "tie"},
    {"char": "学", "sm": "x",  "ym": "üe", "py": "xué", "input": "xue"},
    {"char": "雪", "sm": "x",  "ym": "üe", "py": "xuě", "input": "xue"},
    # ── 前鼻韵母 ──
    {"char": "山", "sm": "sh", "ym": "an", "py": "shān", "input": "shan"},
    {"char": "蓝", "sm": "l",  "ym": "an", "py": "lán",  "input": "lan"},
    {"char": "三", "sm": "s",  "ym": "an", "py": "sān",  "input": "san"},
    {"char": "门", "sm": "m",  "ym": "en", "py": "mén",  "input": "men"},
    {"char": "人", "sm": "r",  "ym": "en", "py": "rén",  "input": "ren"},
    {"char": "本", "sm": "b",  "ym": "en", "py": "běn",  "input": "ben"},
    {"char": "心", "sm": "x",  "ym": "in", "py": "xīn",  "input": "xin"},
    {"char": "金", "sm": "j",  "ym": "in", "py": "jīn",  "input": "jin"},
    {"char": "林", "sm": "l",  "ym": "in", "py": "lín",  "input": "lin"},
    {"char": "春", "sm": "ch", "ym": "un", "py": "chūn", "input": "chun"},
    {"char": "村", "sm": "c",  "ym": "un", "py": "cūn",  "input": "cun"},
    {"char": "军", "sm": "j",  "ym": "ün", "py": "jūn",  "input": "jun"},
    {"char": "裙", "sm": "q",  "ym": "ün", "py": "qún",  "input": "qun"},
    # ── 后鼻韵母 ──
    {"char": "帮", "sm": "b",  "ym": "ang", "py": "bāng", "input": "bang"},
    {"char": "糖", "sm": "t",  "ym": "ang", "py": "táng", "input": "tang"},
    {"char": "狼", "sm": "l",  "ym": "ang", "py": "láng", "input": "lang"},
    {"char": "灯", "sm": "d",  "ym": "eng", "py": "dēng", "input": "deng"},
    {"char": "风", "sm": "f",  "ym": "eng", "py": "fēng", "input": "feng"},
    {"char": "梦", "sm": "m",  "ym": "eng", "py": "mèng", "input": "meng"},
    {"char": "星", "sm": "x",  "ym": "ing", "py": "xīng", "input": "xing"},
    {"char": "听", "sm": "t",  "ym": "ing", "py": "tīng", "input": "ting"},
    {"char": "明", "sm": "m",  "ym": "ing", "py": "míng", "input": "ming"},
    {"char": "中", "sm": "zh", "ym": "ong", "py": "zhōng", "input": "zhong"},
    {"char": "红", "sm": "h",  "ym": "ong", "py": "hóng",  "input": "hong"},
    {"char": "虫", "sm": "ch", "ym": "ong", "py": "chóng", "input": "chong"},
    {"char": "送", "sm": "s",  "ym": "ong", "py": "sòng",  "input": "song"},
    {"char": "茶", "sm": "ch", "ym": "a",   "py": "chá",   "input": "cha"},
    {"char": "从", "sm": "c",  "ym": "ong", "py": "cóng",  "input": "cong"},
    # ── 介音字：u 作介音 ──
    {"char": "多", "sm": "d",  "ym": "uo",  "py": "duō",  "input": "duo"},
    {"char": "错", "sm": "c",  "ym": "uo",  "py": "cuò",  "input": "cuo"},
    {"char": "说", "sm": "sh", "ym": "uo",  "py": "shuō", "input": "shuo"},
    {"char": "国", "sm": "g",  "ym": "uo",  "py": "guó",  "input": "guo"},
    {"char": "火", "sm": "h",  "ym": "uo",  "py": "huǒ",  "input": "huo"},
    {"char": "阔", "sm": "k",  "ym": "uo",  "py": "kuò",  "input": "kuo"},
    {"char": "所", "sm": "s",  "ym": "uo",  "py": "suǒ",  "input": "suo"},
    {"char": "花", "sm": "h",  "ym": "ua",  "py": "huā",  "input": "hua"},
    {"char": "瓜", "sm": "g",  "ym": "ua",  "py": "guā",  "input": "gua"},
    {"char": "刷", "sm": "sh", "ym": "ua",  "py": "shuā", "input": "shua"},
    {"char": "抓", "sm": "zh", "ym": "ua",  "py": "zhuā", "input": "zhua"},
    {"char": "快", "sm": "k",  "ym": "uai", "py": "kuài", "input": "kuai"},
    {"char": "怪", "sm": "g",  "ym": "uai", "py": "guài", "input": "guai"},
    {"char": "坏", "sm": "h",  "ym": "uai", "py": "huài", "input": "huai"},
    {"char": "帅", "sm": "sh", "ym": "uai", "py": "shuài", "input": "shuai"},
    {"char": "关", "sm": "g",  "ym": "uan", "py": "guān", "input": "guan"},
    {"char": "川", "sm": "ch", "ym": "uan", "py": "chuān", "input": "chuan"},
    {"char": "宽", "sm": "k",  "ym": "uan", "py": "kuān", "input": "kuan"},
    # ── 介音字：i 作介音 ──
    {"char": "家", "sm": "j",  "ym": "ia",   "py": "jiā",   "input": "jia"},
    {"char": "虾", "sm": "x",  "ym": "ia",   "py": "xiā",   "input": "xia"},
    {"char": "小", "sm": "x",  "ym": "iao",  "py": "xiǎo",  "input": "xiao"},
    {"char": "鸟", "sm": "n",  "ym": "iao",  "py": "niǎo",  "input": "niao"},
    {"char": "桥", "sm": "q",  "ym": "iao",  "py": "qiáo",  "input": "qiao"},
    {"char": "跳", "sm": "t",  "ym": "iao",  "py": "tiào",  "input": "tiao"},
    {"char": "点", "sm": "d",  "ym": "ian",  "py": "diǎn",  "input": "dian"},
    {"char": "天", "sm": "t",  "ym": "ian",  "py": "tiān",  "input": "tian"},
    {"char": "面", "sm": "m",  "ym": "ian",  "py": "miàn",  "input": "mian"},
    {"char": "先", "sm": "x",  "ym": "ian",  "py": "xiān",  "input": "xian"},
    {"char": "两", "sm": "l",  "ym": "iang", "py": "liǎng", "input": "liang"},
    {"char": "想", "sm": "x",  "ym": "iang", "py": "xiǎng", "input": "xiang"},
    {"char": "墙", "sm": "q",  "ym": "iang", "py": "qiáng", "input": "qiang"},
    {"char": "熊", "sm": "x",  "ym": "iong", "py": "xióng", "input": "xiong"},
    {"char": "穷", "sm": "q",  "ym": "iong", "py": "qióng", "input": "qiong"},
    # ── 介音字：ü 作介音（j/q/x 后省点打 u）──
    {"char": "全", "sm": "q",  "ym": "üan", "py": "quán", "input": "quan"},
]
