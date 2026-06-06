#!/usr/bin/env python3
import urllib.parse

HTML_TEMPLATE = '''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; background: #faf9f7; color: #333; line-height: 1.8; }}
header {{ background: linear-gradient(135deg,#1a1a2e,#16213e); color: #fff; padding: 40px 20px; text-align: center; }}
header h1 {{ font-size: 1.6rem; margin-bottom: 8px; }}
.container {{ max-width: 750px; margin: 0 auto; padding: 30px 20px 60px; }}
.content {{ background: #fff; border-radius: 16px; padding: 28px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }}
.content h2 {{ color: #c0392b; font-size: 1.15rem; margin: 24px 0 10px; padding-bottom: 6px; border-bottom: 2px solid #f0e0de; }}
.content h3 {{ color: #333; font-size: 1.05rem; margin: 18px 0 8px; }}
.content p {{ margin-bottom: 12px; color: #444; }}
.content ul {{ padding-left: 22px; margin-bottom: 14px; }}
.content li {{ margin-bottom: 8px; }}
.content strong {{ color: #c0392b; }}
.content blockquote {{ background: #fef2f0; border-left: 4px solid #c0392b; padding: 12px 16px; margin: 16px 0; border-radius: 0 8px 8px 0; }}
.step-box {{ background: #f5f0eb; border-radius: 10px; padding: 16px; margin: 14px 0; }}
.step-box strong {{ display: block; color: #c0392b; margin-bottom: 6px; }}
.cta {{ background: linear-gradient(135deg,#c0392b,#e74c3c); color: #fff; border-radius: 16px; padding: 24px; text-align: center; margin-top: 24px; }}
.cta p {{ margin-bottom: 12px; }}
.cta a {{ display: inline-block; background: #fff; color: #c0392b; padding: 10px 28px; border-radius: 50px; text-decoration: none; font-weight: 700; }}
.back {{ text-align: center; margin-top: 20px; }}
.back a {{ color: #c0392b; text-decoration: none; }}
footer {{ text-align: center; padding: 24px; color: #888; font-size: 0.82rem; border-top: 1px solid #eee; margin-top: 30px; }}
footer a {{ color: #c0392b; }}
</style>
</head>
<body>
<header>
  <h1>📚 {header_title}</h1>
  <p>大衍语文店 · 资深教师全面指导</p>
</header>
<div class="container">
  <div class="content">
{body}
  </div>
  <div class="cta">
    <p>📚 需要配套冲刺资料？</p>
    <a href="https://wwq0327.github.io/dayan-products/">点击查看大衍语文店 →</a>
  </div>
  <div class="back">
    <a href="https://wwq0327.github.io/dayan-products/">← 返回大衍语文店</a>
  </div>
</div>
<footer>
  <a href="https://wwq0327.github.io/dayan-products/">大衍语文店</a> · 南充中考语文专项资料
</footer>
</body>
</html>
'''

def to_pinyin(text):
    return urllib.parse.quote(text.encode('utf-8'))[:40]

articles = [
    {
        "slug": "wenyanwen-xuci-xiangjie",
        "title": "中考语文文言文虚词用法大全 | 大衍语文店",
        "header_title": "中考语文文言文虚词用法大全",
        "description": "中考语文12个高频文言虚词（之、其、而、于、乃、者、所、为、以、因）用法详解，附经典例句，备考必背。",
        "body": """
    <h2>一、为什么虚词是文言文拿分关键</h2>
    <p>文言虚词不直接承担句意，但决定了句子的语气、关系和结构。中考文言文阅读中，虚词用法是必考内容，<strong>掌握12个高频虚词，能稳定拿到15+分</strong>。</p>

    <h2>二、12个高频虚词详解</h2>

    <h3>① 之</h3>
    <ul>
      <li><strong>代词</strong>：他/她/它（代人、代物）。例：尝驱千里别亲友（之=他）</li>
      <li><strong>助词</strong>：的。例：圣人之道</li>
      <li><strong>动词</strong>：去、到。例：吾欲之南海</li>
    </ul>

    <h3>② 其</h3>
    <ul>
      <li><strong>代词</strong>：他的/那/其中的。例：其妻献疑曰（其=他的）</li>
      <li><strong>语气词</strong>：加强语气。例：其真无马邪？</li>
    </ul>

    <h3>③ 而</h3>
    <ul>
      <li><strong>连词</strong>：表并列（又……又）、递进（而且）、转折（但是）、因果（因此）。例：温故而知新（表递进）</li>
    </ul>

    <h3>④ 于</h3>
    <ul>
      <li><strong>介词</strong>：在、向、对、比、从。例：苛政猛于虎（于=比）</li>
    </ul>

    <h3>⑤ 乃</h3>
    <ul>
      <li><strong>副词</strong>：才、就、竟然。例：蒙乃始就学（乃=就）</li>
    </ul>

    <h3>⑥ 者</h3>
    <ul>
      <li><strong>助词</strong>：……的人/……的事/……的样子。例：若有作奸犯科及为忠善者（者=的人）</li>
    </ul>

    <h3>⑦ 所</h3>
    <ul>
      <li><strong>助词</strong>：所字结构。例：寻向所志（所字结构=……的地方）</li>
    </ul>

    <h3>⑧ 为</h3>
    <ul>
      <li><strong>介词</strong>：为了、因为、给、对。例：为其君勤（为=给）</li>
      <li><strong>动词</strong>：做、成为。例：凡可以得生者（为=做）</li>
    </ul>

    <h3>⑨ 以</h3>
    <ul>
      <li><strong>介词</strong>：用、把、因为。例：以是人多以书假余（以=用）</li>
      <li><strong>连词</strong>：而、因为。例：卷石底以长</li>
    </ul>

    <h3>⑩ 因</h3>
    <ul>
      <li><strong>副词</strong>：于是、就。例：因屏人曰（因=于是）</li>
    </ul>

    <h2>三、虚词辨析技巧</h2>
    <div class="step-box">
      <strong>Step 1：看位置</strong>
      <p>虚词位置不同，用法不同。句首发"而/因/乃"，多为副词/连词。</p>
    </div>
    <div class="step-box">
      <strong>Step 2：看搭配</strong>
      <p>"之"后接名词→助词；后接动词→代词。"于"后必接地点/对象。</p>
    </div>
    <div class="step-box">
      <strong>Step 3：翻译验证</strong>
      <p>无法直译时，尝试代入"他/的/而/于是"等词，看哪个最通顺。</p>
    </div>

    <h2>四、备考建议</h2>
    <ul>
      <li>每天背诵3个虚词，4天过完一遍</li>
      <li>每个虚词背2个课内例句</li>
      <li>做5道以上虚词辨析题，建立错题本</li>
      <li>重点复习《出师表》《岳阳楼记》《醉翁亭记》中的虚词</li>
    </ul>

    <blockquote>💡 提示：虚词题多为选择题，排除法是最快的方法。先排除明显错误的，再比较剩下的。</blockquote>
    """
    },
    {
        "slug": "bingju-xiuli-liu-dayin",
        "title": "中考语文病句修改六大致命错误 | 大衍语文店",
        "header_title": "中考语文病句修改六大致命错误",
        "description": "中考语文病句题6种高频错误类型：搭配不当、成分残缺、语序不当、表意不明、结构混乱、逻辑矛盾，附例题精讲。",
        "body": """
    <h2>一、病句题为什么总丢分</h2>
    <p>很多学生反映病句题"凭语感能感觉不对，但说不清哪里错"。原因是<strong>没有建立系统的病句类型认知</strong>。中考病句题稳定在3-4题，掌握6种类型能确保全对。</p>

    <h2>二、六种病句类型详解</h2>

    <h3>① 搭配不当</h3>
    <p>主谓搭配不当、动宾搭配不当、主宾搭配不当。</p>
    <blockquote>✗ 错误：经过大家的努力，使我们的成绩有了很大的提高。<br>✓ 改正：经过大家的努力，我们的成绩有了很大的提高。</blockquote>

    <h3>② 成分残缺</h3>
    <p>缺主语、缺谓语、缺宾语。</p>
    <blockquote>✗ 错误：当我一想起母亲，就止不住流下眼泪。<br>✓ 改正：我一想起母亲，就止不住流下眼泪。</blockquote>

    <h3>③ 语序不当</h3>
    <p>多项定语/状语顺序错误。</p>
    <blockquote>✗ 错误：同学们排着整齐的队伍，一个一个地走出教室。<br>✓ 改正：同学们一个一个地排着整齐的队伍走出教室。</blockquote>

    <h3>④ 表意不明</h3>
    <p>指代不清，产生歧义。</p>
    <blockquote>✗ 错误：我们要尽量的节约不必要的开支。<br>✓ 改正：我们要尽量节约不必要的开支。</blockquote>

    <h3>⑤ 结构混乱</h3>
    <p>两个句子混在一起，主语飘忽。</p>
    <blockquote>✗ 错误：患者大多是来自矿山附近的村民为主。<br>✓ 改正：患者大多是来自矿山附近的村民。或：患者以矿山附近的村民为主。</blockquote>

    <h3>⑥ 逻辑矛盾</h3>
    <p>前后矛盾，或与事实矛盾。</p>
    <blockquote>✗ 错误：这次考试，我几乎所有的题都做完了。<br>✓ 改正：这次考试，我几乎所有的题都做完了。（"几乎"和"都"矛盾，去"几乎"或改"都"）</blockquote>

    <h2>三、快速判断四步法</h2>
    <div class="step-box">
      <strong>Step 1：看主语</strong>
      <p>主语是否残缺？是否中途易主？</p>
    </div>
    <div class="step-box">
      <strong>Step 2：看谓语</strong>
      <p>谓语是否残缺？和主语/宾语搭配是否正确？</p>
    </div>
    <div class="step-box">
      <strong>Step 3：看宾语</strong>
      <p>宾语是否残缺？有没有搭配不当？</p>
    </div>
    <div class="step-box">
      <strong>Step 4：看关联词</strong>
      <p>关联词是否搭配正确？位置是否正确？</p>
    </div>

    <h2>四、备考练习建议</h2>
    <ul>
      <li>每天做5道病句题，10天养成条件反射</li>
      <li>错题分类整理：哪类错误最多？重点突破</li>
      <li>常见搭配要熟记：如"提高水平"不是"提升水平"</li>
      <li>做完后用手遮住改正答案，重新判断一遍</li>
    </ul>

    <blockquote>💡 提示：病句题选项中，有时几个都看着不对，通常只有1个完全正确，其他都有小毛病。</blockquote>
    """
    },
    {
        "slug": "shici-jianding-moban",
        "title": "中考古诗词鉴赏万能答题模板 | 大衍语文店",
        "header_title": "中考古诗词鉴赏万能答题模板",
        "description": "中考语文古诗词鉴赏怎么答？修辞手法、情感分析、意境赏析、炼字分析4大题型万能答题模板，学完就能用。",
        "body": """
    <h2>一、古诗词鉴赏题型分布</h2>
    <p>中考古诗词鉴赏通常考4种题型：<strong>修辞手法赏析、情感主旨分析、意境画面描述、炼字词语品析</strong>。每种题型都有固定答题套路。</p>

    <h2>二、四大题型答题模板</h2>

    <h3>① 修辞手法赏析题</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>这句诗使用了XXX（修辞手法），把XXX比作XXX（或生动形象地写出XXX），表达了诗人XXX的情感，体现了诗歌XXX的特点。</p>
    </div>
    <blockquote>例题："问君能有几多愁？恰似一江春水向东流。"<br>参考答：这句诗使用了比喻的修辞手法，把"愁"比作"一江春水"，生动形象地写出了愁绪之多、绵绵不绝，表达了诗人亡国之痛的无穷无尽。</blockquote>

    <h3>② 情感主旨分析题</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>这首诗通过对XXX（意象/景物）的描写，表达了诗人XXX的情感/志向/胸怀，情景交融，抒发了XXX之情。</p>
    </div>
    <blockquote>例题：《过零丁洋》<br>参考答：这首诗通过对抗战经历的回顾，表达了诗人宁死不屈的民族气节和以身殉国的决心，抒发了强烈的爱国之情。</blockquote>

    <h3>③ 意境画面描述题</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>描绘了一幅XXX（时间/地点/景物）图，营造了XXX（寂寞/萧瑟/壮阔等）的氛围，表达了诗人XXX的情感。</p>
    </div>
    <blockquote>例题：《天净沙·秋思》<br>参考答：描绘了一幅深秋傍晚萧瑟凄凉的图景，枯藤缠绕老树，归巢乌鸦翔集，小桥流水人家，古道西风瘦马，表达了游子漂泊异乡的孤寂愁苦之情。</blockquote>

    <h3>④ 炼字词语品析题</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>XXX字好在XXX（动词/形容词准确传神），形象地写出/表现了XXX，体现了XXX（意境/情感），使诗句更加XXX（生动/具体）。</p>
    </div>
    <blockquote>例题："春风又绿江南岸"的"绿"字<br>参考答："绿"字形象生动，既是形容词用作动词，表现出春天到来、草木葱绿的景象，又体现了诗人对家乡的思念之情，一个字兼有意境与情感。</blockquote>

    <h2>三、古诗词核心意象速记</h2>
    <ul>
      <li><strong>月亮</strong>→思乡、团圆</li>
      <li><strong>梅花</strong>→高洁、坚韧</li>
      <li><strong>菊花</strong>→隐逸、君子</li>
      <li><strong>杨柳</strong>→离别、思念</li>
      <li><strong>鸿雁</strong>→书信、思乡</li>
      <li><strong>流水</strong>→时光流逝、愁思</li>
      <li><strong>夕阳</strong>→迟暮、失落</li>
      <li><strong>松柏</strong>→坚贞、长寿</li>
    </ul>

    <h2>四、备考策略</h2>
    <ul>
      <li>背完教材所有古诗词，了解诗意和创作背景</li>
      <li>每个题型练习5道，总结自己的答题框架</li>
      <li>关注《义务教育语文课程标准》推荐背诵篇目</li>
      <li>答案一定要分点①②③，层次清晰</li>
    </ul>

    <blockquote>💡 提示：古诗词鉴赏答案不是写得多就好，关键是踩准得分点。分点作答是基本要求。</blockquote>
    """
    },
    {
        "slug": "xiuci-shangxi-jifa",
        "title": "中考语文现代文阅读修辞手法赏析技巧 | 大衍语文店",
        "header_title": "中考语文现代文阅读修辞手法赏析技巧",
        "description": "现代文阅读修辞手法赏析怎么答？比喻、拟人、排比、夸张等8种常考修辞手法答题技巧，附中考真题示例。",
        "body": """
    <h2>一、现代文阅读修辞手法常考类型</h2>
    <p>修辞手法赏析是现代文阅读的高频考点，<strong>比喻、拟人、排比、夸张、引用、设问、反问、对偶</strong>是8种最常考的修辞手法。</p>

    <h2>二、八种修辞手法答题攻略</h2>

    <h3>① 比喻</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>使用了比喻的修辞手法，将XXX比作XXX，生动形象地写出了XXX的特点，表达了作者XXX的情感。</p>
    </div>
    <blockquote>例："那笑容像春天的阳光一样温暖。"<br>赏析：使用了比喻的修辞手法，将"笑容"比作"春天的阳光"，生动形象地写出了笑容的温暖和亲切，表达了作者对主人公的好感。</blockquote>

    <h3>② 拟人</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>使用了拟人的修辞手法，将XXX人格化，生动形象地写出了XXX，表达了作者XXX的情感，使文章更有感染力。</p>
    </div>

    <h3>③ 排比</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>使用了排比的修辞手法，增强语势（加强语气），层层递进地写出了XXX，表达了作者XXX的情感，读来朗朗上口。</p>
    </div>

    <h3>④ 夸张</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>使用了夸张的修辞手法，突出强调XXX，表达了XXX的情感，引发联想，使表达更突出。</p>
    </div>

    <h3>⑤ 引用</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>使用了引用的修辞手法，引用XXX（诗句/名言/典故），增强说服力，丰富文章内容，表达了XXX的观点/情感。</p>
    </div>

    <h3>⑥ 设问</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>使用了设问的修辞手法，自问自答，引发读者思考，引出下文对XXX的论述，吸引读者阅读兴趣。</p>
    </div>

    <h3>⑦ 反问</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>使用了反问的修辞手法，用否定的形式表达肯定的意思，加强语气，强调XXX，表达作者XXX的情感。</p>
    </div>

    <h3>⑧ 对偶</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>使用了对偶的修辞手法，形式对称，音韵和谐，读来朗朗上口，强烈地表达了XXX。</p>
    </div>

    <h2>三、答题注意事项</h2>
    <ul>
      <li>先判断修辞手法，再结合文章内容分析</li>
      <li>分析要结合具体语境，不能只写套话</li>
      <li>答案要完整：手法名称+结合内容+表达效果+情感</li>
      <li>分点①②③作答，层次清晰</li>
    </ul>

    <h2>四、备考练习建议</h2>
    <p>每天做1篇现代文阅读的修辞题，对答案后整理答题框架。注意：<strong>不是背模板，而是理解模板的逻辑后内化为自己的表达</strong>。</p>

    <blockquote>💡 提示：有时文段同时用了多种修辞手法，要逐一分析，不能遗漏。</blockquote>
    """
    },
    {
        "slug": "zuowen-kaitou-moban",
        "title": "中考语文作文开头结尾万能模板 | 大衍语文店",
        "header_title": "中考语文作文开头结尾万能模板",
        "description": "中考作文开头结尾怎么写？6种万能开头模板+6种万能结尾模板，直接套用各大主题，学完立刻提分。",
        "body": """
    <h2>一、好的开头和结尾值多少分</h2>
    <p>作文开头和结尾虽然只占总分的15-20%，但决定了阅卷老师的第一印象和最终感受。<strong>一个精彩开头能直接拉高5分档次</strong>，结尾升华能弥补中间段落的不足。</p>

    <h2>二、六种万能开头模板</h2>

    <h3>模板一：悬念式开头</h3>
    <blockquote>"直到那一刻，我才真正明白了……"这句话，像一颗石子投入心湖，荡起层层涟漪。</blockquote>

    <h3>模板二：景物描写开头</h3>
    <blockquote>窗外，细雨绵绵，打湿了那条通往外婆家的小路。远处炊烟袅袅升起，我的思绪也随之飘向那段难忘的时光。</blockquote>

    <h3>模板三：名言引用开头</h3>
    <blockquote>"世上无难事，只要肯攀登。"这句名言，我一直铭记在心。而那一次的登山经历，让我真正读懂了这句话的含义。</blockquote>

    <h3>模板四：对比式开头</h3>
    <blockquote>有人常说，放弃是一种智慧。但我觉得，有时候，不放弃才是真正的勇气。</blockquote>

    <h3>模板五：倒叙式开头</h3>
    <blockquote>每当看到那张泛黄的照片，我就想起那个夏天——那是我第一次离开家乡，也是我成长的起点。</blockquote>

    <h3>模板六：情感抒发开头</h3>
    <blockquote>成长的滋味，是什么？是苦涩，是甘甜，还是那说不清道不明的复杂滋味？那件事之后，我找到了答案。</blockquote>

    <h2>三、六种万能结尾模板</h2>

    <h3>模板一：升华主题结尾</h3>
    <blockquote>那一刻，我明白了：所谓的成长，不是年龄的增长，而是学会承担责任，学会面对困难，学会在跌倒后重新站起来。</blockquote>

    <h3>模板二：首尾呼应结尾</h3>
    <blockquote>窗外的雨依然在下，但我的心却已晴朗。正如那句话：风雨之后，方见彩虹。</blockquote>

    <h3>模板三：哲理收束结尾</h3>
    <blockquote>生活就像海洋，只有意志坚定的人，才能到达彼岸。那次经历，成为我前行路上最温暖的力量。</blockquote>

    <h3>模板四：情感回扣结尾</h3>
    <blockquote>外婆的手，不再细腻光滑，却是我心中最温暖的港湾。那碗热气腾腾的面，是我吃过的最好的人间滋味。</blockquote>

    <h3>模板五：展望未来结尾</h3>
    <blockquote>带着这份力量与信念，我将继续前行。因为我知道，每一次经历，都是成长的礼物。</blockquote>

    <h3>模板六：疑问留白结尾</h3>
    <blockquote>或许，这就是成长吧——充满未知，却让人充满期待。下一站，又会是怎样的风景呢？</blockquote>

    <h2>四、写作注意事项</h2>
    <ul>
      <li>开头不超过100字，点题要快</li>
      <li>结尾必须升华主题，不能草草收场</li>
      <li>字迹工整，不连笔，字数600字以上</li>
      <li>情感真实，避免假大空</li>
    </ul>

    <blockquote>💡 提示：模板是辅助，真实情感才是核心竞争力。建议每个模板练习写3遍，变成自己的套路。</blockquote>
    """
    },
    {
        "slug": "yicuozi-cihui-qingdan",
        "title": "中考语文易错字词清单500个 | 大衍语文店",
        "header_title": "中考语文易错字词清单500个",
        "description": "中考语文常考易错字500个：别字辨析、多音字、形近字大全，语文基础题拿满分的秘诀就在这里。",
        "body": """
    <h2>一、为什么易错字词总丢分</h2>
    <p>语文基础题（拼音、字形、词语）占12-15分，易错字词是备考性价比最高的内容。<strong>每天花30分钟背50个，10天过完一遍</strong>，基础题拿满分不是梦。</p>

    <h2>二、高频易错字形辨析（100组）</h2>
    <ul>
      <li>戊[wù]—戊[yuè]—戌[xū]—戎[róng]（四字区别）</li>
      <li>己[jǐ]—已[yǐ]—巳[sì]（三字区别）</li>
      <li>土[tǔ]—士[shì]</li>
      <li>末[mò]—未[wèi]</li>
      <li>刺[cì]—刺[là]</li>
      <li>崇[chóng]—祟[sùi]</li>
      <li>即[jí]—既[jì]</li>
      <li>候[hòu]—侯[hóu]</li>
      <li>贯[guàn]—惯[guàn]</li>
    </ul>

    <h2>三、常考易错词（100组）</h2>
    <ul>
      <li>精兵简政 / 精兵减政（错）</li>
      <li>再接再厉 / 再接再励（错）</li>
      <li>迫不及待 / 迫不急待（错）</li>
      <li>一筹莫展 / 一愁莫展（错）</li>
      <li>变本加厉 / 变本加利（错）</li>
      <li>不省人事 / 不醒人事（错）</li>
      <li>川流不息 / 穿流不息（错）</li>
      <li>天翻地覆 / 天翻地复（错）</li>
      <li>走投无路 / 走头无路（错）</li>
      <li>既往不咎 / 既往不究（错）</li>
    </ul>

    <h2>四、中考常考多音字（50组）</h2>
    <ul>
      <li>行：háng（银行）/ xíng（行走）</li>
      <li>得：dé（得到）/ de（说得）/ děi（得劲）</li>
      <li>处：chù（到处）/ chǔ（处理）</li>
      <li>传：chuán（传统）/ zhuàn（传记）</li>
      <li>差：chā（差别）/ chà（差劲）/ chāi（出差）</li>
      <li>数：shù（数学）/ shǔ（数数）/ shuò（数见不鲜）</li>
      <li>为：wèi（因为）/ wéi（成为）</li>
      <li>涨：zhǎng（涨价）/ zhàng（涨红）</li>
      <li>着：zhe（看着）/ zháo（着急）/ zhuó（穿着）</li>
      <li>干：gān（干净）/ gàn（干活）</li>
    </ul>

    <h2>五、备考方法</h2>
    <div class="step-box">
      <strong>方法一：联想记忆</strong>
      <p>把易错字编成小故事或口诀记忆，如"己巳已"可以用"封己巳已"的口诀。</p>
    </div>
    <div class="step-box">
      <strong>方法二：错题本</strong>
      <p>每天做题整理5-10个易错字，周末集中复习。</p>
    </div>
    <div class="step-box">
      <strong>方法三：高频循环</strong>
      <p>用艾宾浩斯记忆法：第1天、第2天、第4天、第7天复习同一批内容。</p>
    </div>

    <blockquote>💡 提示：易错字词备考没有捷径，就是重复。建议把本文打印出来，每天看一遍。</blockquote>
    """
    },
    {
        "slug": "duoyinzi-huibi",
        "title": "中考语文多音字汇总大全 | 大衍语文店",
        "header_title": "中考语文多音字汇总大全",
        "description": "中考语文常考多音字80组：一声多音、二声多音、三声多音、四声多音全覆盖，附记忆技巧和例句。",
        "body": """
    <h2>一、多音字为什么总混淆</h2>
    <p>多音字是中考语文基础题的必考内容，<strong>一般考3-4道，稍不注意就丢分</strong>。多音字的记忆要结合语境，而不是死记硬背。</p>

    <h2>二、中考常考多音字80组</h2>

    <h3>A部</h3>
    <ul>
      <li>阿：ā（阿姨）/ ē（阿谀奉承）</li>
      <li>挨：āi（挨近）/ ái（挨打）</li>
      <li>腌：ā（腌臜）/ yān（腌菜）</li>
    </ul>

    <h3>B部</h3>
    <ul>
      <li>柏：bǎi（柏树）/ bó（柏林）/ bī（柏油）</li>
      <li>背：bēi（背包）/ bèi（后背）</li>
      <li>薄：báo（薄纸）/ bó（薄利）/ bò（薄荷）</li>
      <li>剥：bāo（剥皮）/ bō（剥削）</li>
    </ul>

    <h3>C部</h3>
    <ul>
      <li>参：cān（参观）/ shēn（人参）/ cēn（参差不齐）</li>
      <li>藏：cáng（藏起来）/ zàng（宝藏）</li>
      <li>称：chēng（称呼）/ chèn（称心）</li>
      <li>重：chóng（重复）/ zhòng（重量）</li>
      <li>臭：chòu（臭味）/ xiù（乳臭未干）</li>
    </ul>

    <h3>D部</h3>
    <ul>
      <li>弹：dàn（子弹）/ tán（弹琴）</li>
      <li>调：diào（调动）/ tiáo（调整）</li>
      <li>都：dōu（都是）/ dū（首都）</li>
      <li>度：dù（度过）/ duó（揣度）</li>
    </ul>

    <h3>F部</h3>
    <ul>
      <li>发：fā（发现）/ fà（头发）</li>
      <li>分：fēn（分开）/ fèn（过分）</li>
      <li>缝：féng（缝补）/ fèng（缝隙）</li>
    </ul>

    <h3>G部</h3>
    <ul>
      <li>干：gān（干净）/ gàn（干活）</li>
      <li>冠：guān（皇冠）/ guàn（冠军）</li>
    </ul>

    <h3>H部</h3>
    <ul>
      <li>汗：hàn（汗水）/ hán（可汗）</li>
      <li>好：hǎo（好处）/ hào（爱好）</li>
      <li>还：hái（还有）/ huán（归还）</li>
    </ul>

    <h3>J部</h3>
    <ul>
      <li>系：jì（系鞋带）/ xì（关系）</li>
      <li>假：jiǎ（真假）/ jià（假期）</li>
      <li>间：jiān（中间）/ jiàn（间隔）</li>
      <li>降：jiàng（降落）/ xiáng（投降）</li>
    </ul>

    <h2>三、多音字记忆技巧</h2>
    <div class="step-box">
      <strong>技巧一：语境记忆</strong>
      <p>每个读音记住一个典型词语，如"行háng（银行）"、"行xíng（行走）"，在句子中判断读音。</p>
    </div>
    <div class="step-box">
      <strong>技巧二：口诀记忆</strong>
      <p>编口诀："银行走路分行，分开过分不分称心"，一句话记住4组多音字。</p>
    </div>

    <h2>四、备考建议</h2>
    <p>每天背诵20组多音字，4天背完。配合做题巩固，遇到不确定的立刻查证并记录。考前再过一遍易错的多音字。</p>

    <blockquote>💡 提示：多音字考题中，通常口语读音（口语常用）和书面语读音（书面语常用）不同，要结合语境判断。</blockquote>
    """
    },
    {
        "slug": "wenxue-changshi-suji",
        "title": "中考语文文学常识速记 | 大衍语文店",
        "header_title": "中考语文文学常识速记",
        "description": "中考语文文学常识：古代名家、现当代作家、外国作家、四大名著、成语典故，速记口诀和分类整理。",
        "body": """
    <h2>一、文学常识考什么</h2>
    <p>中考语文文学常识题通常以选择题或填空题形式出现，<strong>分值3-5分</strong>。内容涉及古代名家、现当代作家、外国作家、四大名著、成语典故等。</p>

    <h2>二、古代文学名家（必背）</h2>
    <ul>
      <li><strong>诗圣杜甫</strong>——忧国忧民，《茅屋为秋风所破歌》</li>
      <li><strong>诗仙李白</strong>——浪漫豪放，《静夜思》《将进酒》</li>
      <li><strong>诗魔白居易</strong>——通俗易懂，《琵琶行》《长恨歌》</li>
      <li><strong>词圣苏轼</strong>——豪放派，《念奴娇》《水调歌头》</li>
      <li><strong>词后李清照</strong>——婉约派，《如梦令》《声声慢》</li>
      <li><strong>辛弃疾</strong>——豪放派，《破阵子》《永遇乐》</li>
      <li><strong>陶渊明</strong>——田园诗派，《桃花源记》《归去来兮辞》</li>
      <li><strong>韩愈</strong>——唐宋八大家之首，《师说》</li>
      <li><strong>柳宗元</strong>——唐宋八大家，《小石潭记》</li>
      <li><strong>欧阳修</strong>——唐宋八大家，《醉翁亭记》</li>
      <li><strong>范仲淹</strong>——《岳阳楼记》，先天下之忧而忧</li>
    </ul>

    <h2>三、现代文学名家</h2>
    <ul>
      <li><strong>鲁迅</strong>——《呐喊》《彷徨》，原名周树人</li>
      <li><strong>朱自清</strong>——《背影》《春》，散文家</li>
      <li><strong>老舍</strong>——《骆驼祥子》《茶馆》，人民艺术家</li>
      <li><strong>冰心</strong>——《繁星·春水》，儿童文学家</li>
      <li><strong>巴金</strong>——《家》《春》《秋》，激流三部曲</li>
    </ul>

    <h2>四、外国作家（常考）</h2>
    <ul>
      <li><strong>莫泊桑</strong>——法国，批判现实主义，《羊脂球》《项链》</li>
      <li><strong>契诃夫</strong>——俄国，批判现实主义，《变色龙》</li>
      <li><strong>都德</strong>——法国，《最后一课》</li>
      <li><strong>安徒生</strong>——丹麦，童话作家，《卖火柴的小女孩》</li>
    </ul>

    <h2>五、四大名著速记</h2>
    <ul>
      <li><strong>《三国演义》</strong>——罗贯中，三国故事，曹操、刘备、孙权</li>
      <li><strong>《水浒传》</strong>——施耐庵，108好汉，宋江、武松、林冲</li>
      <li><strong>《西游记》</strong>——吴承恩，唐僧师徒四人西天取经</li>
      <li><strong>《红楼梦》</strong>——曹雪芹，贾宝玉、林黛玉、薛宝钗</li>
    </ul>

    <h2>六、速记口诀</h2>
    <div class="step-box">
      <strong>古代作家口诀：</strong>
      <p>李白酒仙杜诗圣，仲淹先忧居士醉翁。<br>韩柳欧阳三苏在，散文唐宋八大家。</p>
    </div>

    <blockquote>💡 提示：文学常识题通常以选择题形式考，看到作者和作品的对应关系要能快速匹配。</blockquote>
    """
    },
    {
        "slug": "jixuwen-yuedu-dati",
        "title": "中考记叙文阅读答题技巧大全 | 大衍语文店",
        "header_title": "中考记叙文阅读答题技巧大全",
        "description": "中考记叙文阅读6大题型全攻略：标题含义、段落作用、词语赏析、情感主旨、概括内容、写作手法，附答题模板。",
        "body": """
    <h2>一、记叙文阅读考什么</h2>
    <p>记叙文阅读是中考现代文阅读的重头戏，占比最高。6大核心题型：<strong>标题含义、段落作用、词语赏析、情感主旨、概括内容、写作手法</strong>。</p>

    <h2>二、六大题型答题模板</h2>

    <h3>① 标题含义题</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>表层含义：XXX（字面意思）。<br>深层含义：XXX（比喻义/象征义/情感），表达了XXX。</p>
    </div>
    <blockquote>例：《背影》——表层：父亲的背影。深层：父爱的象征，表达对父亲的感激与思念。</blockquote>

    <h3>② 段落作用题</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>内容上：写了XXX，突出了XXX。<br>结构上：引出下文/为下文做铺垫/承上启下/总结上文/点明中心。</p>
    </div>

    <h3>③ 词语赏析题</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>XXX词语好在哪：1. 用了XXX（词性/修辞）；2. 写出了XXX（对象特点）；3. 表达了XXX（情感）。</p>
    </div>

    <h3>④ 情感主旨题</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>这篇文章通过对XXX（事件/人物/景物）的记叙/描写，表达了XXX（情感/中心思想），揭示了XXX的道理。</p>
    </div>

    <h3>⑤ 概括内容题</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>人+事+结果。按起因、经过、结果的顺序概括，注意字数限制。</p>
    </div>

    <h3>⑥ 写作手法题</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>这篇文章使用了XXX（写作手法），通过XXX（具体内容），突出了XXX（效果），表达了XXX（情感）。</p>
    </div>

    <h2>三、常见写作手法辨析</h2>
    <ul>
      <li><strong>对比</strong>：突出差异，形成鲜明对照</li>
      <li><strong>衬托</strong>：以次要事物突出主要事物</li>
      <li><strong>借景抒情</strong>：通过景物描写抒发情感</li>
      <li><strong>托物言志</strong>：借事物表达志向</li>
      <li><strong>欲扬先抑</strong>：先否定再肯定，突出赞美</li>
    </ul>

    <h2>四、备考建议</h2>
    <ul>
      <li>每天做1篇记叙文阅读，对答案后总结答题框架</li>
      <li>注意分点①②③作答，条理清晰</li>
      <li>先看题目再读文章，带着问题找答案</li>
      <li>字迹工整，答案写在规定区域内</li>
    </ul>

    <blockquote>💡 提示：答案不是写得多就好，关键是踩准得分点。每题答案控制在50-100字以内。</blockquote>
    """
    },
    {
        "slug": "shuomingswen-yuedu-dati",
        "title": "中考说明文阅读答题技巧 | 大衍语文店",
        "header_title": "中考说明文阅读答题技巧",
        "description": "中考说明文阅读怎么答？说明方法判断、结构梳理、内容概括、语言特色4大题型答题技巧，学完就会用。",
        "body": """
    <h2>一、说明文阅读核心考点</h2>
    <p>说明文阅读通常考4大题型：<strong>说明方法判断、结构梳理、内容概括、语言特色</strong>。说明文答案比较客观，相对容易拿满分。</p>

    <h2>二、说明方法判断与作用</h2>

    <h3>八种常见说明方法</h3>
    <ul>
      <li><strong>举例子</strong>：通过具体事例说明事物特征，更有说服力</li>
      <li><strong>列数字</strong>：用具体数据说明，真实准确</li>
      <li><strong>作比较</strong>：通过对比突出事物特点</li>
      <li><strong>打比方</strong>：用比喻说明，生动形象</li>
      <li><strong>分类别</strong>：分门别类说明，条理清晰</li>
      <li><strong>下定义</strong>：给出本质定义</li>
      <li><strong>作诠释</strong>：解释说明</li>
      <li><strong>摹状貌</strong>：描写事物的样子</li>
    </ul>

    <div class="step-box">
      <strong>答题模板：</strong>
      <p>这句话使用了XXX说明方法，通过XXX（具体内容），真实/生动/具体/准确/直观地说明了XXX（事物特征）。</p>
    </div>

    <h2>三、结构梳理题</h2>
    <p>说明文常见结构：<strong>总分式、递进式、并列式</strong>。判断文章结构，再分析段落之间的逻辑关系。</p>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>文章采用了XXX结构，第1段提出XXX（总），第2-5段从XXX、XXX等方面分别说明，第6段总结全文。条理清晰，层次分明。</p>
    </div>

    <h2>四、内容概括题</h2>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>这篇说明文介绍了XXX（说明对象）的XXX（特征），主要包括XXX、XXX、XXX等方面，对人们XXX（有重要意义）。</p>
    </div>

    <h2>五、语言特色题</h2>
    <p>说明文语言特点：<strong>准确性、严密性、生动性</strong>。</p>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>这篇文章的语言具有XXX的特点（准确性/严密性/生动性），如"XXX"词语（大约/之一/左右）表示估计、限制，体现了说明文语言的科学性和严谨性。</p>
    </div>

    <h2>六、备考建议</h2>
    <ul>
      <li>熟背8种说明方法的名称和判断技巧</li>
      <li>每天做1篇说明文阅读</li>
      <li>注意"大约""左右""之一"等词语的作用</li>
    </ul>

    <blockquote>💡 提示：说明文答案相对客观，做完后对答案时要认真分析，找出自己遗漏的得分点。</blockquote>
    """
    },
    {
        "slug": "yilunwen-yuedu-dati",
        "title": "中考议论文阅读答题技巧 | 大衍语文店",
        "header_title": "中考议论文阅读答题技巧",
        "description": "中考议论文阅读怎么答？论点、论据、论证方法、语言特色4大题型答题技巧，附常见论文结构分析。",
        "body": """
    <h2>一、议论文阅读核心考点</h2>
    <p>议论文阅读通常围绕4大核心要素展开：<strong>论点（是什么）、论据（用什么证明）、论证（怎么证明）、语言（表达效果）</strong>。</p>

    <h2>二、四大题型答题攻略</h2>

    <h3>① 论点概括题</h3>
    <div class="step-box">
      <strong>找论点方法：</strong>
      <p>1. 看标题——标题往往是论点的概括<br>2. 看开头——开篇往往提出论点<br>3. 看结尾——结尾往往总结论点<br>4. 看过渡——过渡句往往是分论点</p>
    </div>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>这篇议文的中心论点是XXX，标题/开头/结尾/第X段提出了这一论点。</p>
    </div>

    <h3>② 论据辨析题</h3>
    <div class="step-box">
      <strong>论据类型：</strong>
      <p>事实论据：具体事例、数据、历史事实<br>道理论据：名言警句、俗语、科学原理</p>
    </div>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>这里使用了XXX论据，通过XXX（具体内容），有力地论证了XXX（分论点/中心论点），增强了文章的说服力。</p>
    </div>

    <h3>③ 论证方法判断题</h3>
    <ul>
      <li><strong>举例论证</strong>：举出具体事例证明论点</li>
      <li><strong>道理论证</strong>：引用名言或原理证明论点</li>
      <li><strong>对比论证</strong>：通过正反对比证明论点</li>
      <li><strong>比喻论证</strong>：用比喻说明道理</li>
    </ul>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>这句话使用了XXX论证方法，通过XXX（具体内容），有力地证明了XXX（论点），使论证更具体/更有说服力/更生动形象。</p>
    </div>

    <h3>④ 语言特色题</h3>
    <div class="step-box">
      <strong>答题模板：</strong>
      <p>议论文语言具有XXX的特点（严密性/逻辑性/概括性），如"XXX"词语，体现了语言的准确性和严密性，使论证更有说服力。</p>
    </div>

    <h2>三、议论文常见结构</h2>
    <ul>
      <li><strong>总分式</strong>：先总说后分说</li>
      <li><strong>并列式</strong>：几个分论点并列</li>
      <li><strong>递进式</strong>：逐层深入</li>
      <li><strong>对比式</strong>：正反对比</li>
    </ul>

    <h2>四、备考建议</h2>
    <ul>
      <li>找论点是关键，先学会快速定位论点</li>
      <li>每天做1篇议论文阅读</li>
      <li>注意区分论证方法和说明方法</li>
    </ul>

    <blockquote>💡 提示：议论文答案相对规范，答题模板要熟记，但也要结合文章内容具体分析。</blockquote>
    """
    },
    {
        "slug": "gushici-mohui-zhuanxiang",
        "title": "中考古诗词默写专项训练 | 大衍语文店",
        "header_title": "中考古诗词默写专项训练",
        "description": "中考语文古诗词默写怎么拿满分？理解性默写vs机械性默写区别，高频名句100句，备考方法和常见丢分点分析。",
        "body": """
    <h2>一、默写题的两种类型</h2>
    <p>中考古诗词默写分为<strong>机械性默写</strong>（直接填写）和<strong>理解性默写</strong>（根据语境填写）两种，理解性默写难度更大，是拉开差距的关键。</p>

    <h2>二、高频名句100句（按主题分类）</h2>

    <h3>思乡怀人</h3>
    <ul>
      <li>但愿人长久，千里共婵娟。——苏轼《水调歌头》</li>
      <li>独在异乡为异客，每逢佳节倍思亲。——王维《九月九日忆山东兄弟》</li>
      <li>春风又绿江南岸，明月何时照我还。——王安石《泊船瓜洲》</li>
      <li>露从今夜白，月是故乡明。——杜甫《月夜忆舍弟》</li>
    </ul>

    <h3>爱国忧民</h3>
    <ul>
      <li>先天下之忧而忧，后天下之乐而乐。——范仲淹《岳阳楼记》</li>
      <li>人生自古谁无死，留取丹心照汗青。——文天祥《过零丁洋》</li>
      <li>僵卧孤村不自哀，尚思为国戍轮台。——陆游《十一月四日风雨大作》</li>
      <li>了却君王天下事，赢得生前身后名。——辛弃疾《破阵子》</li>
    </ul>

    <h3>励志进取</h3>
    <ul>
      <li>长风破浪会有时，直挂云帆济沧海。——李白《行路难》</li>
      <li>会当凌绝顶，一览众山小。——杜甫《望岳》</li>
      <li>千淘万漉虽辛苦，吹尽狂沙始到金。——刘禹锡《浪淘沙》</li>
      <li>欲穷千里目，更上一层楼。——王之涣《登鹳雀楼》</li>
    </ul>

    <h3>哲理感悟</h3>
    <ul>
      <li>山重水复疑无路，柳暗花明又一村。——陆游《游山西村》</li>
      <li>沉舟侧畔千帆过，病树前头万木春。——刘禹锡《酬乐天扬州初逢席上见赠》</li>
      <li>不识庐山真面目，只缘身在此山中。——苏轼《题西林壁》</li>
      <li>问渠那得清如许，为有源头活水来。——朱熹《观书有感》</li>
    </ul>

    <h3>写景状物</h3>
    <ul>
      <li>大漠孤烟直，长河落日圆。——王维《使至塞上》</li>
      <li>明月松间照，清泉石上流。——王维《山居秋暝》</li>
      <li>两个黄鹂鸣翠柳，一行白鹭上青天。——杜甫《绝句》</li>
      <li>接天莲叶无穷碧，映日荷花别样红。——杨万里《晓出净慈寺送林子方》</li>
    </ul>

    <h2>三、理解性默写答题技巧</h2>
    <div class="step-box">
      <strong>Step 1：读懂题目要求</strong>
      <p>看清楚是"直接填写"还是"根据语境填写"。</p>
    </div>
    <div class="step-box">
      <strong>Step 2：找准关键词</strong>
      <p>题目中的提示词往往对应诗句中的关键词。</p>
    </div>
    <div class="step-box">
      <strong>Step 3：检查错别字</strong>
      <p>写完后检查每个字，尤其是形近字和多音字。</p>
    </div>

    <h2>四、备考建议</h2>
    <ul>
      <li>每天背10句名句，边背边默写</li>
      <li>注意易错字：如"长风破浪"的"破"，"柳暗花明"的"暗"</li>
      <li>理解诗意后再背诵，不建议死记硬背</li>
      <li>考前把所有名句再过一遍，尤其易错字</li>
    </ul>

    <blockquote>💡 提示：默写题写错一个字，整句不得分。背的时候就要边背边写，确保每个字都正确。</blockquote>
    """
    },
    {
        "slug": "chengyu-gushi-guige",
        "title": "中考语文成语典故及用法辨析 | 大衍语文店",
        "header_title": "中考语文成语典故及用法辨析",
        "description": "中考常考成语100个：出处典故、释义、例句、用法辨析，告别望文生义，成语题一分不丢。",
        "body": """
    <h2>一、成语题为什么总错</h2>
    <p>成语题丢分主要有三个原因：<strong>望文生义、褒贬误用、对象错配</strong>。每个成语都有特定的语义和使用语境，不能随意扩展。</p>

    <h2>二、高频成语100个详解</h2>

    <h3>历史典故类成语（30个）</h3>
    <ul>
      <li><strong>纸上谈兵</strong>——比喻空谈理论，不能解决实际问题。出自《史记·廉颇蔺相如列传》赵括故事。贬义。</li>
      <li><strong>卧薪尝胆</strong>——形容人刻苦自励，立志报仇雪恨。出自越王勾践故事。褒义。</li>
      <li><strong>四面楚歌</strong>——比喻四面受敌，处于孤立无援的境地。出自项羽故事。</li>
      <li><strong>破釜沉舟</strong>——比喻下定决心，不顾一切干到底。出自项羽故事。褒义。</li>
      <li><strong>指鹿为马</strong>——比喻故意颠倒黑白，混淆是非。出自赵高故事。贬义。</li>
      <li><strong>完璧归赵</strong>——比喻把原物完好无损地归还主人。出自蔺相如故事。</li>
      <li><strong>负荆请罪</strong>——形容主动向对方承认错误，请求责罚。出自廉颇蔺相如故事。褒义。</li>
      <li><strong>草木皆兵</strong>——形容人在极度惊恐时，一点风吹草动都会疑神疑鬼。出自淝水之战。贬义。</li>
      <li><strong>望梅止渴</strong>——比喻用空想来安慰自己。出自曹操故事。</li>
      <li><strong>三顾茅庐</strong>——比喻真心诚意地一再邀请。出自刘备请诸葛亮故事。褒义。</li>
    </ul>

    <h3>易望文生义成语（30个）</h3>
    <ul>
      <li><strong>文不加点</strong>——形容写文章很快，不用涂改就写成了。不是"文章没标点"。</li>
      <li><strong>不刊之论</strong>——形容不能改动或不可磨灭的言论。是褒义，不是"不刊登"。</li>
      <li><strong>身体力行</strong>——亲身体验，努力实行。不是"身体和行动"。</li>
      <li><strong>首当其冲</strong>——比喻最先受到攻击或遭受灾难。不是"第一个冲上去"。</li>
      <li><strong>差强人意</strong>——大体上还能使人满意。不是"很差强人意"。</li>
      <li><strong>万人空巷</strong>——形容庆祝、欢迎等盛况。不是"巷子里没人"。</li>
      <li><strong>望其项背</strong>——比喻赶得上或比得上（用于否定）。不是"望不到项背"。</li>
      <li><strong>目无全牛</strong>——形容技艺已经达到纯熟的地步。不是"看问题不全面"。</li>
    </ul>

    <h3>褒贬误用成语（20个）</h3>
    <ul>
      <li><strong>处心积虑</strong>——蓄谋已久，形容用尽心思。贬义。不能用于好人好事。</li>
      <li><strong>振振有词</strong>——形容自以为理由充分，说个不停。贬义。</li>
      <li><strong>改头换面</strong>——比喻只改变形式，不改变内容。贬义。</li>
      <li><strong>趋之若鹜</strong>——比喻很多人争相趋附。贬义。</li>
      <li><strong>半斤八两</strong>——彼此一样，不相上下。贬义。</li>
      <li><strong>翻云覆雨</strong>——比喻反复无常或玩弄手段。贬义。</li>
    </ul>

    <h2>三、成语使用辨析技巧</h2>
    <div class="step-box">
      <strong>技巧一：看语义</strong>
      <p>成语的意思是否与句子语境匹配，有没有望文生义。</p>
    </div>
    <div class="step-box">
      <strong>技巧二：看色彩</strong>
      <p>是褒义、贬义还是中性？用在表扬还是批评的语境？</p>
    </div>
    <div class="step-box">
      <strong>技巧三：看对象</strong>
      <p>成语的主语和宾语是否搭配正确。</p>
    </div>
    <div class="step-box">
      <strong>技巧四：看范围</strong>
      <p>成语的使用范围是否合适，如"美轮美奂"只能用于建筑。</p>
    </div>

    <blockquote>💡 提示：做成语题时，先判断语义，再看色彩和对象，逐项排查，错误选项的毛病通常只有一个。</blockquote>
    """
    },
    {
        "slug": "zhongkao-yuwen-zongfuxi",
        "title": "中考语文总复习重点知识清单 | 大衍语文店",
        "header_title": "中考语文总复习重点知识清单",
        "description": "中考语文总复习看这一篇就够了！字词、成语、病句、文言文、阅读、作文六大板块重点知识清单，考前必背。",
        "body": """
    <h2>一、考前总复习策略</h2>
    <p>最后冲刺阶段，语文复习要<strong>抓大放小</strong>：高频考点稳定拿分，难题适当放弃。六大板块分配好时间，确保各题型都能拿到基本分。</p>

    <h2>二、语言基础板块（目标：30分钟，拿到10+分）</h2>

    <h3>字词部分重点</h3>
    <ul>
      <li>易错字形100组（戊/戌/戎、己/已/巳等）</li>
      <li>常考多音字80组</li>
      <li>常考形近字50组</li>
    </ul>

    <h3>成语部分重点</h3>
    <ul>
      <li>高频成语100个</li>
      <li>易望文生义成语30个</li>
      <li>褒贬误用成语20个</li>
    </ul>

    <h3>病句部分重点</h3>
    <ul>
      <li>搭配不当</li>
      <li>成分残缺</li>
      <li>语序不当</li>
      <li>表意不明</li>
      <li>结构混乱</li>
      <li>逻辑矛盾</li>
    </ul>

    <h2>三、文言文板块（目标：20分钟，拿到15+分）</h2>
    <ul>
      <li>高频虚词12个（之、其、而、于、乃、者、所、为、以、因、则、且）</li>
      <li>重点篇目：《出师表》《爱莲说》《陋室铭》《岳阳楼记》《醉翁亭记》《小石潭记》</li>
      <li>实词含义：课内常见实词100个</li>
    </ul>

    <h2>四、阅读板块（目标：45分钟，拿到20+分）</h2>
    <ul>
      <li>记叙文：标题含义、段落作用、词语赏析、情感主旨、写作手法</li>
      <li>说明文：说明方法、结构梳理、内容概括、语言特色</li>
      <li>议论文：论点概括、论据辨析、论证方法、语言特色</li>
    </ul>

    <h2>五、作文板块（目标：50分钟，拿到42+分）</h2>
    <ul>
      <li>六种万能开头模板</li>
      <li>六种万能结尾模板</li>
      <li>五大常考主题素材（成长、亲情、友情、师生、自然）</li>
      <li>字数600字以上，字迹工整</li>
    </ul>

    <h2>六、时间分配建议</h2>
    <table style="width:100%;border-collapse:collapse;margin:14px 0;">
      <tr style="background:#c0392b;color:#fff;">
        <th style="padding:8px 12px;text-align:left;">板块</th>
        <th style="padding:8px 12px;text-align:left;">建议时间</th>
        <th style="padding:8px 12px;text-align:left;">目标得分</th>
      </tr>
      <tr><td style="padding:8px 12px;border-bottom:1px solid #eee;">语言基础</td><td style="padding:8px 12px;border-bottom:1px solid #eee;">30分钟</td><td style="padding:8px 12px;border-bottom:1px solid #eee;">10-12分</td></tr>
      <tr style="background:#faf9f7;"><td style="padding:8px 12px;border-bottom:1px solid #eee;">文言文</td><td style="padding:8px 12px;border-bottom:1px solid #eee;">20分钟</td><td style="padding:8px 12px;border-bottom:1px solid #eee;">15+分</td></tr>
      <tr><td style="padding:8px 12px;border-bottom:1px solid #eee;">古诗词鉴赏</td><td style="padding:8px 12px;border-bottom:1px solid #eee;">15分钟</td><td style="padding:8px 12px;border-bottom:1px solid #eee;">6-8分</td></tr>
      <tr style="background:#faf9f7;"><td style="padding:8px 12px;border-bottom:1px solid #eee;">现代文阅读</td><td style="padding:8px 12px;border-bottom:1px solid #eee;">30分钟</td><td style="padding:8px 12px;border-bottom:1px solid #eee;">20+分</td></tr>
      <tr><td style="padding:8px 12px;">作文</td><td style="padding:8px 12px;">50分钟</td><td style="padding:8px 12px;">42+分</td></tr>
    </table>

    <blockquote>💡 提示：考前最后一天只看错题本和万能模板，轻装上阵，保证睡眠，保持好状态。</blockquote>
    """
    },
]

import os
base_dir = os.path.expanduser("~/Projects/dayan-products")
os.makedirs(base_dir, exist_ok=True)

written = 0
for a in articles:
    filename = f"article-{a['slug']}.html"
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        print(f"Skip: {filename} (exists)")
        continue
    html = HTML_TEMPLATE.format(
        title=a['title'],
        header_title=a['header_title'],
        description=a['description'],
        body=a['body'].strip()
    )
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Written: {filename}")
    written += 1

print(f"\nTotal articles written: {written}")
articles.append({
    "slug": "xiuci-biaoda-jishu-10zhong",
    "title": "中考语文修辞手法10种详解 | 大衍语文店",
    "header_title": "中考语文修辞手法10种详解",
    "description": "比喻、拟人、排比、夸张、对偶、反复、反问、设问、借代、引用——中考常考10种修辞手法判断方法与答题公式。",
    "body": """
    <h2>一、为什么修辞手法是中考必考点</h2>
    <p>修辞手法是中考语文卷各题型中的"常客"，无论是古诗词鉴赏、现代文阅读还是作文，准确判断修辞手法并写出赏析答案，是拿满分的保障。</p>
    <h2>二、10种常考修辞手法</h2>
    <h3>1. 比喻</h3>
    <blockquote>格式：把A比作B（A是本体，B是喻体，"像/如/似"是比喻词）<br>
    答题公式：使用了比喻的修辞手法，将A比作B，生动形象地写出了……，表达了……之情。</blockquote>
    <h3>2. 拟人</h3>
    <blockquote>格式：把物当作人来写，赋予事物人的动作或情感<br>
    答题公式：使用了拟人的修辞手法，将XX人格化，生动形象地写出了……，表达了……之情。</blockquote>
    <h3>3. 排比</h3>
    <blockquote>格式：三个或以上结构相似、语气一致的句子并列<br>
    答题公式：使用了排比的修辞手法，增强语言气势，突出强调……，表达了……之情。</blockquote>
    <h3>4. 夸张</h3>
    <blockquote>答题公式：使用了夸张的修辞手法，突出/强调了……，表达了……之情，给人以强烈的印象。</blockquote>
    <h3>5. 对偶</h3>
    <blockquote>格式：结构对称、字数相等的两个句子<br>
    答题公式：使用了对偶的修辞手法，句式整齐，节奏感强，突出了……。</blockquote>
    <h3>6. 反复</h3>
    <blockquote>格式：同一词语或句子出现两次以上<br>
    答题公式：使用了反复的修辞手法，强调了……，增强了语言的节奏感和感染力。</blockquote>
    <h3>7. 反问</h3>
    <blockquote>格式：问句形式表达肯定含义（答在问外）<br>
    答题公式：使用了反问的修辞手法，加强语气，强调了……，表达了……之情。</blockquote>
    <h3>8. 设问</h3>
    <blockquote>格式：自问自答<br>
    答题公式：使用了设问的修辞手法，提出问题引发思考，突出强调了……。</blockquote>
    <h3>9. 借代</h3>
    <blockquote>格式：用事物特征、相关事物代替本体<br>
    答题公式：使用了借代的修辞手法，用XX代替XX，形象生动，富有情趣。</blockquote>
    <h3>10. 引用</h3>
    <blockquote>答题公式：使用了引用的修辞手法，引用……，增强文章说服力，体现作者深厚的文学底蕴。</blockquote>
    <h2>三、辨析技巧：易混修辞对比</h2>
    <table><tr><td>修辞</td><td>关键特征</td><td>判断标准</td></tr><tr><td>比喻</td><td>有本体、喻体</td><td>能用"像/如"改写</td></tr><tr><td>拟人</td><td>物变人</td><td>事物有人的动作/情感</td></tr><tr><td>排比</td><td>三个以上并列</td><td>结构相似、语气一致</td></tr></table>
    <blockquote>💡 提示：看到"难道……吗？"是反问，看到"为什么……呢？"是设问。答反问时要在答案中体现肯定语气。</blockquote>
    """
})

articles.append({
    "slug": "biaodian-fuhao-zongjie",
    "title": "中考标点符号用法大全 | 大衍语文店",
    "header_title": "中考标点符号用法大全",
    "description": "顿号、逗号、分号、句号、问号、感叹号、书名号、括号、破折号、引号——9种标点符号的中考用法与常见错误总结。",
    "body": """
    <h2>一、标点符号为什么丢分最多</h2>
    <p>标点符号题看似简单，但每年中考都有大量考生因对规则理解不准确而失分。尤其是顿号、逗号、分号的区分，以及引号内外的使用，是高频丢分点。</p>
    <h2>二、9种常考标点用法</h2>
    <h3>1. 顿号（、）</h3>
    <blockquote>用于并列词语之间<br>
    ✅ 正确：书桌上的笔、纸、墨都摆好了。<br>
    ❌ 错误：并列短语中用了逗号代替顿号。</blockquote>
    <h3>2. 逗号（，）</h3>
    <blockquote>用于句子内部停顿，表示语气延续<br>
    ✅ 正确：春天来了，花开了，水也暖了。</blockquote>
    <h3>3. 分号（；）</h3>
    <blockquote>用于并列分句之间（分句内部已有逗号时用分号）<br>
    ✅ 正确：他爱读书；爱写作；更爱思考。</blockquote>
    <h3>4. 句号（。）</h3>
    <blockquote>用于陈述句末尾<br>
    ⚠️ 注意：感叹句和祈使句在较强语气时用感叹号。</blockquote>
    <h3>5. 问号（？）</h3>
    <blockquote>用于疑问句、反问句末尾<br>
    ⚠️ 注意：选择问句只在最后用问号，中间用逗号。<br>
    ✅ 你今天去学校，还是明天去？</blockquote>
    <h3>6. 感叹号（！）</h3>
    <blockquote>用于感叹句、强烈祈使句<br>
    ⚠️ 注意：语气平淡的感叹句不用感叹号。</blockquote>
    <h3>7. 书名号（《》）</h3>
    <blockquote>用于书名、篇名、报刊名、歌曲名、电影名<br>
    ⚠️ 注意：书名号内再有书名，用双书名号。</blockquote>
    <h3>8. 括号（（））</h3>
    <blockquote>用于解释说明的词语<br>
    ⚠️ 注意：括号内的内容只是补充说明，朗读时不读出。</blockquote>
    <h3>9. 破折号（——）</h3>
    <blockquote>用于解释说明、话题转换、声音延长<br>
    ✅ 示例：今天我们去春游——不对，明天才是春游。</blockquote>
    <h2>三、易错点汇总</h2>
    <table><tr><td>错误类型</td><td>正确用法</td></tr><tr><td>并列词组用逗号代替顿号</td><td>词语并列用顿号，句子并列用逗号</td></tr><tr><td>选择问句每句都用问号</td><td>只在句末用问号</td></tr><tr><td>引号内末尾标点位置错误</td><td>引号内通常不另加标点（特殊情况除外）</td></tr></table>
    """
})

articles.append({
    "slug": "yuedu-jieda-moban-15ti",
    "title": "中考阅读理解答题公式15题 | 大衍语文店",
    "header_title": "中考阅读理解答题公式15题",
    "description": "概括内容、把握中心、分析句子、赏析词语、理解情感——5大题型15个答题公式，语文阅读不再丢分。",
    "body": """
    <h2>一、阅读理解为什么总扣分</h2>
    <p>阅读理解的答案不在文里，而在"套路"里。掌握答题公式，能踩准得分点，即使没完全读懂，也能拿到大部分分数。</p>
    <h2>二、五 大题型答题公式</h2>
    <h3>题型1：概括内容</h3>
    <blockquote>公式：什么人+做了什么事+结果如何/表达了什么情感<br>
    格式：本文记叙了（描写了）……（人物）在……（环境）做……（事件），表现了……（主题）。</blockquote>
    <h3>题型2：把握中心（主旨）</h3>
    <blockquote>公式：写了……（内容），表达了……（情感/道理），揭示了……（主题）<br>
    格式：本文通过……（事件），表现了……（思想感情），揭示了……（深刻道理）。</blockquote>
    <h3>题型3：分析句子含义</h3>
    <blockquote>公式：表面意思+深层含义（联系上下文/主题）<br>
    格式：这句话表面上写……，实际上写……，表达了……。</blockquote>
    <h3>题型4：赏析句子</h3>
    <blockquote>公式：修辞手法/描写方法+内容分析+表达效果+情感<br>
    格式：这句话使用了……（手法），生动形象地写出了……，表达了……之情。</blockquote>
    <h3>题型5：理解情感</h3>
    <blockquote>公式：找出关键词句+分析作者态度+结合背景<br>
    格式：从文中……（词句）可以看出，作者表达了……的情感（态度）。</blockquote>
    <h2>三、真题演练</h2>
    <blockquote>例题："那声音像一根细细的线，牵动了我的心。"请从修辞角度赏析句子。<br>
    参考答案：这句话使用了比喻的修辞手法，将"声音"比作"细细的线"，生动形象地写出了声音的轻柔与触动之深，表达了作者内心的感动与共鸣。</blockquote>
    <blockquote>💡 提示：阅读理解的答案一定要有"公式"，先判断题型，再套用公式，分点作答。写得太多反而不得分。</blockquote>
    """
})

articles.append({
    "slug": "kaochang-zuowen-jqiao-10tiao",
    "title": "中考考场作文技巧10条 | 大衍语文店",
    "header_title": "中考考场作文技巧10条",
    "description": "时间分配、审题技巧、开头结尾、字数控制、卷面要求——考场作文10条实战技巧，帮你多拿5-10分。",
    "body": """
    <h2>一、考场作文的生死线</h2>
    <p>中考作文60分，是整张试卷单题分值最高的题型。考场环境和平时写作完全不同，掌握这10条技巧，可以让你在有限时间内写出高分作文。</p>
    <h2>二、10条实战技巧</h2>
    <h3>1. 时间分配：作文不超过50分钟</h3>
    <blockquote>语文试卷约150分钟，作文建议40-50分钟内完成。拿到试卷先看作文题目，在做阅读题时可以让大脑在后台构思。</blockquote>
    <h3>2. 审题三遍：第一遍粗读，第二遍划关键词，第三遍确认体裁</h3>
    <blockquote>⚠️ 常见失误：写成了话题作文而非命题作文；写成了议论文而题目要求记叙文。</blockquote>
    <h3>3. 开头：150字内必须入题</h3>
    <blockquote>开头绕圈子是考场大忌。最好用"一句入题法"——第一句话就要点明主题。开头精彩的老师会多看两眼，开头平庸的直接影响印象分。</blockquote>
    <h3>4. 素材选择：宁可小而深，不要大而空</h3>
    <blockquote>用亲身经历或家庭故事比编造宏大叙事更打动人心。越小越具体越真实，越容易写出真情实感。</blockquote>
    <h3>5. 中间段落：每段一个中心句</h3>
    <blockquote>每个段落开头放一句概括性的话（中心句），让阅卷老师一目了然。不需要过多联系，层次清晰即可。</blockquote>
    <h3>6. 结尾：点题+升华，不要拖沓</h3>
    <blockquote>结尾最好的方式：回到题目中的关键词，用一句有哲理的话升华主题。结尾拖沓或超出字数都会被扣分。</blockquote>
    <h3>7. 字数控制：超出或不足都要扣分</h3>
    <blockquote>初中作文要求600字左右，不要低于550字，不要超过700字。每少50字扣2-5分。</blockquote>
    <h3>8. 字迹工整：卷面是第一印象</h3>
    <blockquote>字可以不漂亮，但必须工整清楚。笔画清晰，字大小一致，不要涂改太多。</blockquote>
    <h3>9. 标点符号：每句话必须有标点</h3>
    <blockquote>标点使用混乱会直接影响阅读流畅度和内容分。引号、书名号用对，句号、逗号不混淆。</blockquote>
    <h3>10. 检查：只改错别字和明显病句</h3>
    <blockquote>时间不够的情况下，检查优先级：错别字>病句>标点>内容。不要大面积修改，会越改越乱。</blockquote>
    <blockquote>💡 提示：考前准备好3个万能素材（亲情、学习、成长类），考场上可以快速套用。</blockquote>
    """
})

articles.append({
    "slug": "mingzhu-luotuoxiangzi-kaodian",
    "title": "《骆驼祥子》名著考点梳理 | 大衍语文店",
    "header_title": "《骆驼祥子》名著考点梳理",
    "description": "《骆驼祥子》是中考名著阅读高频篇目，本文梳理人物形象、情节线索、主题思想和经典片段赏析，帮助考生拿满名著分。",
    "body": """
    <h2>一、作品基本信息</h2>
    <table><tr><td>项目</td><td>内容</td></tr><tr><td>作者</td><td>老舍</td></tr><tr><td>体裁</td><td>长篇小说</td></tr><tr><td>发表时间</td><td>1936年</td></tr><tr><td>主要人物</td><td>祥子、虎妞、刘四爷、小福子</td></tr></table>
    <h2>二、主要人物形象</h2>
    <h3>祥子</h3>
    <blockquote>身份：北平的人力车夫<br>
    性格特点：老实健壮、吃苦耐劳、坚韧自尊、有理想追求<br>
    人物轨迹：积极向上（买车的梦想）→ 在希望中挣扎 → 在绝望中堕落 → 彻底麻木<br>
    核心事件：三起三落（买车→丢车→再买→再丢→幻灭）</blockquote>
    <h3>虎妞</h3>
    <blockquote>身份：车厂主刘四爷的女儿，祥子的妻子<br>
    性格特点：泼辣、能干、有心机、贪吃懒做<br>
    与祥子的关系：逼婚，对祥子有控制欲，对祥子的人生有双重影响</blockquote>
    <h3>小福子</h3>
    <blockquote>身份：二强子的女儿，祥子暗恋对象<br>
    性格特点：善良、柔弱、被侮辱与损害的底层女性形象<br>
    悲剧意义：代表祥子最后的希望，她的死彻底摧毁了祥子</blockquote>
    <h2>三、经典片段</h2>
    <blockquote>片段一：烈日与暴雨下的祥子<br>
    重点：环境描写对人物的衬托作用，表现祥子的吃苦耐劳和悲惨命运。<br>
    片段二：祥子与虎妞结婚<br>
    重点：祥子内心的矛盾与挣扎，体现其自尊与现实的冲突。</blockquote>
    <h2>四、主题思想</h2>
    <blockquote>① 对城市底层劳动人民悲惨命运的同情与关切<br>
    ② 揭示旧社会对善良人性的摧残与毁灭<br>
    ③ 批判"个人主义"——单靠个人奋斗无法改变命运</blockquote>
    <blockquote>💡 提示：名著阅读的答案要结合具体情节，不要只背结论。结合原文情节分析才是得高分的关键。</blockquote>
    """
})

articles.append({
    "slug": "wenyanwen-sanci-zhongjie-bianxi",
    "title": "中考文言文实词三层次辨析 | 大衍语文店",
    "header_title": "中考文言文实词三层次辨析",
    "description": "文言文实词（名词、动词、形容词）是中考文言文阅读的基础。本文从词性、语境、文化三个层次讲解实词辨析方法。",
    "body": """
    <h2>一、为什么实词比虚词更重要</h2>
    <p>很多考生以为虚词是难点，其实实词才是文言文读懂的关键。实词不认识，整句话都无法理解，虚词再准确也无济于事。</p>
    <h2>二、实词三层次辨析法</h2>
    <h3>第一层：词性判断</h3>
    <blockquote>步骤：看位置→判断词性→找对应释义<br>
    示例："温故而知新"中"故"是形容词用作名词，意思是"旧知识"。</blockquote>
    <h3>第二层：语境推断</h3>
    <blockquote>步骤：代入常见义项→看是否通顺→结合上下文<br>
    示例："走"在古代是"跑"的意思，而非"行走"。<br>
    ✅ 常用词：亡（逃跑/死亡）、兵（武器/士兵）、穷（穷尽/贫穷）、谢（道歉/感谢）</blockquote>
    <h3>第三层：文化常识辅助</h3>
    <blockquote>结合古代文化背景判断词义：<br>
    官职词：丞相、太尉、刺史、知州——都是古代官职名<br>
    礼仪词：觐、拜、封、迁——都是古代官职变动相关</blockquote>
    <h2>三、必背实词分类汇总</h2>
    <table><tr><td>类别</td><td>高频词</td><td>常考义项</td></tr><tr><td>动词</td><td>亡、走、穷、谢、度、举</td><td>逃跑、跑、穷尽、道歉、推测、起兵</td></tr><tr><td>形容词</td><td>美、善、勤、固、安</td><td>美丽、善良、勤劳、坚固、安全</td></tr><tr><td>名词</td><td>兵、书、诗、意、辞</td><td>武器、书籍、诗歌、情意、言词</td></tr></table>
    <blockquote>💡 提示：实词积累靠平时，考前复习重点看课内注释词和课后习题词，超纲词可结合语境推断。</blockquote>
    """
})

articles.append({
    "slug": "shici-yixiang-yiwen-20duo",
    "title": "古诗词意象意境20问答 | 大衍语文店",
    "header_title": "古诗词意象意境20问答",
    "description": "月亮、菊花、鸿雁、梧桐、杜鹃、羌笛——中考常考20种古诗词意象及其情感含义，配20道精选练习题。",
    "body": """
    <h2>一、为什么要学长意象意境</h2>
    <p>意象是古诗词的"细胞"，意境是古诗词的"气质"。掌握常见意象，能快速读懂诗词情感，是中考古诗词鉴赏题拿高分的关键。</p>
    <h2>二、20种常考意象</h2>
    <h3>1. 月亮</h3>
    <blockquote>情感：思乡、怀人、团圆、永恒<br>
    诗句：举头望明月，低头思故乡。（李白《静夜思》）</blockquote>
    <h3>2. 菊花</h3>
    <blockquote>情感：傲骨、高洁、隐逸<br>
    诗句：采菊东篱下，悠然见南山。（陶渊明《饮酒》）</blockquote>
    <h3>3. 鸿雁</h3>
    <blockquote>情感：思乡、音信、羁旅<br>
    诗句：雁过也，正伤心，却是旧时相识。（李清照《声声慢》）</blockquote>
    <h3>4. 梧桐</h3>
    <blockquote>情感：悲凉、孤独、离愁<br>
    诗句：梧桐更兼细雨，到黄昏、点点滴滴。（李清照《声声慢》）</blockquote>
    <h3>5. 杜鹃（子规）</h3>
    <blockquote>情感：悲愤、归乡、哀怨<br>
    诗句：其间旦暮闻何物？杜鹃啼血猿哀鸣。（白居易《琵琶行》）</blockquote>
    <h3>6. 羌笛</h3>
    <blockquote>情感：边塞、离愁、战争<br>
    诗句：羌笛何须怨杨柳，春风不度玉门关。（王之涣《凉州词》）</blockquote>
    <h3>7. 杨柳</h3>
    <blockquote>情感：离别、留恋<br>
    诗句：杨柳依依，今我来思。（《诗经·采薇》）</blockquote>
    <h3>8. 夕阳（落日）</h3>
    <blockquote>情感：迟暮、衰败、离别<br>
    诗句：夕阳无限好，只是近黄昏。（李商隐《登乐游原》）</blockquote>
    <h3>9. 白云</h3>
    <blockquote>情感：漂泊、自由、高洁<br>
    诗句：白云深处有人家。（杜牧《山行》）</blockquote>
    <h3>10. 流水</h3>
    <blockquote>情感：时光流逝、离愁、永恒<br>
    诗句：抽刀断水水更流，举杯消愁愁更愁。（李白《宣州谢朓楼饯别校书叔云》）</blockquote>
    <h2>三、意境类答题公式</h2>
    <blockquote>公式：描绘图景+点染情感+表达效果<br>
    示例：诗歌描绘了……（图景），渲染了……（氛围），表达了诗人……的情感。</blockquote>
    <blockquote>💡 提示：古诗词鉴赏先找意象，再定情感，最后套公式。同一意象在不同诗歌中情感可能有差异，要结合具体诗句判断。</blockquote>
    """
})

articles.append({
    "slug": "biaoxian-shoufa-xi jie-10zhong",
    "title": "古诗词表现手法10种详解 | 大衍语文店",
    "header_title": "古诗词表现手法10种详解",
    "description": "借景抒情、托物言志、对比反衬、动静结合、虚实相生——中考常考10种古诗词表现手法判断与赏析。",
    "body": """
    <h2>一、表现手法vs修辞手法的区别</h2>
    <p>修辞手法是对句子的加工，表现手法是对全篇的构思。很多考生混淆两者，导致鉴赏题失分。简单来说：修辞手法作用于语言层面，表现手法作用于篇章层面。</p>
    <h2>二、10种常考表现手法</h2>
    <h3>1. 借景抒情（寓情于景）</h3>
    <blockquote>特点：情感蕴含在景物描写中，不直接说出<br>
    示例：桃花潭水深千尺，不及汪伦送我情。（借潭水之深喻友情之深）</blockquote>
    <h3>2. 托物言志</h3>
    <blockquote>特点：通过描写具体事物来表达志向<br>
    示例：零落成泥碾作尘，只有香如故。（以梅花自喻，表达坚贞不屈的志趣）</blockquote>
    <h3>3. 对比反衬</h3>
    <blockquote>特点：用对立事物相互比较，突出其中一方<br>
    示例：朱门酒肉臭，路有冻死骨。（贫富对比，揭示社会矛盾）</blockquote>
    <h3>4. 动静结合</h3>
    <blockquote>特点：动态描写与静态描写相结合<br>
    示例：蝉噪林逾静，鸟鸣山更幽。（以声写静，动静相宜）</blockquote>
    <h3>5. 虚实相生</h3>
    <blockquote>特点：想象与现实结合，扩大诗歌意境<br>
    示例：我寄愁心与明月，随风直到夜郎西。（虚景，实情）</blockquote>
    <h3>6. 夸张想象</h3>
    <blockquote>特点：用超越现实的想象表达强烈情感<br>
    示例：飞流直下三千尺，疑是银河落九天。（极度夸张，想象奇特）</blockquote>
    <h3>7. 借古讽今</h3>
    <blockquote>特点：借历史故事讽刺现实<br>
    示例：东风不与周郎便，铜雀春深锁二乔。（以二乔命运讽周瑜成败）</blockquote>
    <h3>8. 比喻起兴</h3>
    <blockquote>特点：先用其他事物引起正题，形成比照<br>
    示例：山不在高，有仙则名。（以山喻人，兴起全文）</blockquote>
    <h3>9. 白描</h3>
    <blockquote>特点：用朴素简练的语言直接描写，不加修饰<br>
    示例：鸡声茅店月，人迹板桥霜。（纯用名词组合，无一动词）</blockquote>
    <h3>10. 拟人化描写</h3>
    <blockquote>特点：赋予自然景物人的情感和动作<br>
    示例：雁过衡阳秋气高，孤城落日眺。（赋予雁情感）</blockquote>
    <blockquote>💡 提示：鉴赏古诗词表现手法时，先判断用了哪种手法，再结合诗句分析，最后答情感。答题要完整，不能只写手法名称。</blockquote>
    """
})

articles.append({
    "slug": "chuzi-cihui-jiyi-30tian",
    "title": "中考语文词汇积累30天计划 | 大衍语文店",
    "header_title": "中考语文词汇积累30天计划",
    "description": "字词、成语、文学常识一网打尽！30天科学的复习计划，帮助初中生系统积累语文词汇，告别临时抱佛脚。",
    "body": """
    <h2>一、为什么词汇积累需要计划</h2>
    <p>语文词汇不是靠考前突击能解决的，它需要每天积累、反复巩固。30天计划把大任务拆成小目标，让积累变成一种习惯。</p>
    <h2>二、30天词汇积累计划</h2>
    <table><tr><td>天数</td><td>内容</td><td>要求</td></tr><tr><td>1-5天</td><td>易错字音字形（100个）</td><td>每天20个，会读会写</td></tr><tr><td>6-10天</td><td>常用成语（100个）</td><td>知道含义、用法、近义词</td></tr><tr><td>11-15天</td><td>文学常识（中国古代文学）</td><td>作家、作品、流派、称号</td></tr><tr><td>16-20天</td><td>文学常识（中国现代文学）</td><td>五四以来重要作家作品</td></tr><tr><td>21-25天</td><td>古诗词名句默写</td><td>不仅会背，还要会写对</td></tr><tr><td>26-30天</td><td>综合复习与测试</td><td>回顾易错点，查漏补缺</td></tr></table>
    <h2>三、高频考点词汇清单（节选）</h2>
    <h3>易错字音</h3>
    <blockquote>发酵（jiào）、脊梁（jǐ liang）、栈桥（zhàn）、干涸（gān hé）、星宿（xīng xiù）</blockquote>
    <h3>易错字形</h3>
    <blockquote>戊戌wù xū（不是"戌"）、九州jiǔ zhōu（不是"洲"）、针灸jiǔ zhēn（不是"炙"）</blockquote>
    <h3>常考成语</h3>
    <blockquote>不卑不亢、负隅顽抗、耳濡目染、戛然而止、光怪陆离、毛骨悚然</blockquote>
    <h2>四、词汇积累方法</h2>
    <blockquote>① 造句法：学一个词马上造一个句子<br>
    ② 联想法：一个词联想近义词、反义词<br>
    ③ 复习法：当天学完睡前复习一遍<br>
    ④ 检测法：每周给自己做一次小测验</blockquote>
    <blockquote>💡 提示：词汇积累最好的方法是"用"，学了新词要尝试在作文或口头表达中用出来，用过才能真正记住。</blockquote>
    """
})

articles.append({
    "slug": "jixuwen-zhenduan-jieda",
    "title": "记叙文阅读诊断解题法 | 大衍语文店",
    "header_title": "记叙文阅读诊断解题法",
    "description": "记叙文阅读是中考语文卷中分值最高的题型之一。本文用诊断式解题法，帮助考生快速定位问题、对症下药、拿满分数。",
    "body": """
    <h2>一、什么是诊断式解题法</h2>
    <p>诊断式解题法的核心理念：阅读题丢分不是因为"不会做"，而是因为"不知道丢在哪里"。先诊断问题类型，再选择对应解法，才能精准拿分。</p>
    <h2>二、记叙文阅读常见问题诊断</h2>
    <h3>问题A：概括题丢分</h3>
    <blockquote>症状：写了太多细节，或者概括不完整<br>
    诊断：没有按"六要素"结构概括<br>
    解法：按"人物+时间+地点+起因+经过+结果"六要素补充完整</blockquote>
    <h3>问题B：赏析题丢分</h3>
    <blockquote>症状：知道用了修辞手法，但不知道如何组织答案<br>
    诊断：答案格式不完整<br>
    解法：套用"修辞手法+内容+效果+情感"四步公式</blockquote>
    <h3>问题C：含义理解题丢分</h3>
    <blockquote>症状：只写表面意思，深层含义挖不出来<br>
    诊断：不会联系文章主旨<br>
    解法：先说表面意思，再联系文章主题说深层含义</blockquote>
    <h3>问题D：情感把握题丢分</h3>
    <blockquote>症状：情感找对了但写不准确<br>
    诊断：答题语言不精准，词不达意<br>
    解法：从原文找出关键词句，用原文词作答</blockquote>
    <h2>三、诊断自测表</h2>
    <blockquote>丢分类型→对应解法<br>
    概括不全→六要素检查法<br>
    赏析不完整→四步公式法<br>
    含义太浅→主旨联系法<br>
    情感写错→原文词抄法</blockquote>
    <blockquote>💡 提示：做完每篇阅读后，对照诊断表检查自己哪里丢分了，下次考试前重点复习对应解法。</blockquote>
    """
})

articles.append({
    "slug": "kaoshi-xin tai-tiaozheng",
    "title": "中考前心理状态调整指南 | 大衍语文店",
    "header_title": "中考前心理状态调整指南",
    "description": "考前焦虑、失眠、紧张——考生常见的心理问题及应对方法，帮助调整最佳应考状态，在考场上发挥真实水平。",
    "body": """
    <h2>一、考前焦虑的本质</h2>
    <p>考前焦虑不是坏事，适度的焦虑能激发潜能。但如果焦虑过度，则会影响发挥。关键是把焦虑控制在合理范围内。</p>
    <h2>二、常见心理问题及应对</h2>
    <h3>问题1：失眠</h3>
    <blockquote>原因：大脑过度兴奋，思虑过度<br>
    应对：睡前不看书、不讨论试题；做深呼吸（4-7-8呼吸法）；用白噪音或轻音乐辅助入睡</blockquote>
    <h3>问题2：怯场紧张</h3>
    <blockquote>原因：怕考不好、担心失败<br>
    应对：进场前做深呼吸；对自己说"我准备好了"；把注意力集中在试卷上而不是结果</blockquote>
    <h3>问题3：做题时脑子一片空白</h3>
    <blockquote>原因：紧张导致大脑供血不足<br>
    应对：先做简单的题，找手感；喝一小口水；深呼吸3次；不要跳过，先跳过反而更紧张</blockquote>
    <h3>问题4：考后患得患失</h3>
    <blockquote>原因：上一科考完对答案<br>
    应对：考完一科扔一科，不对答案，不讨论；快速进入下一科备考状态</blockquote>
    <h2>三、考前一周状态调整</h2>
    <blockquote>① 作息：按考试时间调整作息，早睡早起<br>
    ② 饮食：清淡为主，不吃生冷辛辣，避免肠胃不适<br>
    ③ 运动：每天30分钟轻度运动（散步、慢跑），不宜剧烈运动<br>
    ④ 社交：减少社交，避免负面情绪影响<br>
    ⑤ 复习：考前不做新题，复习错题本和笔记</blockquote>
    <blockquote>💡 提示：考场上遇到不会做的题是正常的，先跳过，把会做的题全部做完再回头攻难题。</blockquote>
    """
})

articles.append({
    "slug": "tigan-wuyu-shici-jianshang",
    "title": "古诗词托物言志意境鉴赏 | 大衍语文店",
    "header_title": "古诗词托物言志意境鉴赏",
    "description": "托物言志是中考古诗词鉴赏的高频考点。本文通过10首经典诗词，详解托物言志的表现手法、判断方法和答题技巧。",
    "body": """
    <h2>一、什么是托物言志</h2>
    <p>托物言志是通过对某种事物的描写，来寄托作者的思想感情和政治理想。"物"是手段，"志"是目的。理解了这一层，才能真正读懂古诗词。</p>
    <h2>二、托物言志vs借景抒情</h2>
    <table><tr><td>手法</td><td>特点</td><td>示例</td></tr><tr><td>托物言志</td><td>通过具体事物表达志向</td><td>王安石《北陂杏花》以杏花喻变法者</td></tr><tr><td>借景抒情</td><td>通过景物描写传达情感</td><td>李清照《如梦令》以暮春景色抒惜春之情</td></tr></table>
    <h2>三、经典托物言志诗词解析</h2>
    <h3>1. 于谦《石灰吟》</h3>
    <blockquote>千锤万凿出深山，烈火焚烧若等闲。<br>
    粉骨碎身浑不怕，要留清白在人间。<br>
    志：表达诗人刚正不阿、视死如归的节操和救国救民的抱负。<br>
    手法：托物言志，借石灰自喻。</blockquote>
    <h3>2. 郑燮《竹石》</h3>
    <blockquote>咬定青山不放松，立根原在破岩中。<br>
    千磨万击还坚劲，任尔东西南北风。<br>
    志：表达诗人坚韧不拔、不随波逐流的高洁品格。<br>
    手法：托物言志，借竹石喻坚强人格。</blockquote>
    <h3>3. 龚自珍《己亥杂诗》</h3>
    <blockquote>落红不是无情物，化作春泥更护花。<br>
    志：虽然离职仍关心国家命运，甘为培育人才贡献力量。<br>
    手法：托物言志，借落红喻爱国情怀。</blockquote>
    <h3>4. 李商隐《霜月》</h3>
    <blockquote>青女素娥俱耐冷，月中霜里斗婵娟。<br>
    志：借霜月表达诗人在困境中保持高洁品格的追求。</blockquote>
    <h2>四、判断托物言志的方法</h2>
    <blockquote>① 看标题：题目中常有"咏""赞""吟"等字<br>
    ② 看事物：选取的是某种具体的物（植物、动物、器物）<br>
    ③ 看抒情：情感不是直接表达，而是通过"物"来暗示<br>
    ④ 看结尾：结尾往往有一句升华主旨的诗句</blockquote>
    <blockquote>💡 提示：托物言志的诗词鉴赏答案结构：手法+所托之物+所言之志+表达效果。</blockquote>
    """
})

articles.append({
    "slug": "renwu-xingxiang-fenxi-fangfa",
    "title": "中考语文人物形象分析方法 | 大衍语文店",
    "header_title": "中考语文人物形象分析方法",
    "description": "人物形象分析是中考语文现代文阅读的高频考点。本文提供系统化分析方法，通过人物描写、情节安排、环境衬托三个维度精准把握人物性格。",
    "body": """
    <h2>一、人物形象分析的重要性</h2>
    <p>人物形象题是现代文阅读中的"常驻嘉宾"，通常分值为4-6分。掌握标准分析方法，踩准得分点，是拿满分的关键。</p>
    <h2>二、分析人物形象的三个维度</h2>
    <h3>维度1：人物描写分析</h3>
    <blockquote>动作描写：反映人物性格（如：动作迅速说明干练）<br>
    语言描写：体现人物身份和性格（如：说话直接说明性格豪爽）<br>
    心理描写：揭示内心世界（如：内心矛盾说明性格复杂）<br>
    肖像描写：暗示人物命运和性格</blockquote>
    <h3>维度2：情节安排分析</h3>
    <blockquote>人物在关键情节中的选择和反应，体现其价值观和性格特征。<br>
    分析：遇到困难怎么办？面对利益怎么选？与人冲突怎么处？</blockquote>
    <h3>维度3：环境衬托分析</h3>
    <blockquote>社会环境：时代背景对人物的影响<br>
    自然环境：烘托人物心情，推动情节发展</blockquote>
    <h2>三、人物形象题答题公式</h2>
    <blockquote>公式：从XX（描写方法/事件）中可以看出，XX（人物）是一个XX（性格特点1）、XX（性格特点2）、XX（性格特点3）的人。<br>
    示例：从文中"他每天第一个到教室，最后一个离开"的动作描写中可以看出，小明是一个勤奋刻苦、有责任心的人。</blockquote>
    <h2>四、常见人物性格词汇</h2>
    <blockquote>正面：善良、正直、勤奋、乐观、坚强、勇敢、诚实、谦虚、有责任心<br>
    负面：自私、怯懦、虚伪、冷漠、贪婪、自负、傲慢<br>
    复杂：表面冷漠内心善良、外表柔弱内心坚强</blockquote>
    <blockquote>💡 提示：人物性格要用具体词，不要用抽象词。比如"好"是抽象词，"善良、有爱心、乐于助人"才是具体词。</blockquote>
    """
})

articles.append({
    "slug": "zhongkao-fuxi-fangfa-layu",
    "title": "中考语文复习方法论——来自年级第一的总结 | 大衍语文店",
    "header_title": "中考语文复习方法论",
    "description": "字词、病句、成语、古诗词、阅读、作文——六大板块复习方法全梳理，科学备考中考语文。",
    "body": """
    <h2>一、语文复习的三大误区</h2>
    <blockquote>❌ 误区1：大量刷题，忽视总结<br>
    ✅ 正确：做完一套题，必须花同样时间分析错题<br>
    <br>
    ❌ 误区2：只背答案，不理解原理<br>
    ✅ 正确：掌握解题思路，而不是背诵答案原文<br>
    <br>
    ❌ 误区3：作文临时抱佛脚<br>
    ✅ 正确：平时积累素材，考前打磨3-5篇万能作文</blockquote>
    <h2>二、六大板块复习方法</h2>
    <h3>1. 字词板块</h3>
    <blockquote>方法：每天复习10个易错字音字形，坚持到考前<br>
    工具：错题本记录每次练习中的错字<br>
    标准：看到一个字能写出拼音，知道一个词能正确使用</blockquote>
    <h3>2. 病句板块</h3>
    <blockquote>方法：先掌握6种病句类型，再每天练习5道长句分析<br>
    工具：病句类型速查表（搭配不当、成分残缺、语序不当等）<br>
    标准：看到病句能快速判断类型并改正</blockquote>
    <h3>3. 成语板块</h3>
    <blockquote>方法：按使用场景分类记忆，不要死记硬背<br>
    工具：常用成语分类表（形容人的、形容事物的、形容情感的）<br>
    标准：不仅知道含义，还要知道褒贬色彩和使用语境</blockquote>
    <h3>4. 古诗词板块</h3>
    <blockquote>方法：理解性背诵，不要机械记忆<br>
    工具：每首诗写出三层意思（字面意思、诗意、情感）<br>
    标准：能说出作者情感，能结合诗句分析</blockquote>
    <h3>5. 阅读板块</h3>
    <blockquote>方法：掌握答题公式，不要自由发挥<br>
    工具：5大题型答题公式速查表<br>
    标准：每道题按公式分点作答，不丢得分点</blockquote>
    <h3>6. 作文板块</h3>
    <blockquote>方法：平时积累，考前打磨，不现场发挥<br>
    工具：3个万能素材+5个开头结尾模板<br>
    标准：60分钟内写出600字，语言流畅，主题明确</blockquote>
    <blockquote>💡 提示：中考语文复习的核心不是学多少新东西，而是把已学的巩固牢、把漏洞补上。基础题不丢分，分数自然就上去了。</blockquote>
    """
})

# Second write pass to pick up articles added above
written2 = 0
for a in articles:
    filename = f"article-{a['slug']}.html"
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        print(f"Skip: {filename} (exists)")
        continue
    html = HTML_TEMPLATE.format(
        title=a['title'],
        header_title=a['header_title'],
        description=a['description'],
        body=a['body'].strip()
    )
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Written: {filename}")
    written2 += 1

print(f"\nTotal new articles written: {written2}")

articles.append({
    "slug": "yuwen-baifenbi-jisuan",
    "title": "中考语文各题型分值比例与答题时间分配 | 大衍语文店",
    "header_title": "中考语文各题型分值比例与时间分配",
    "description": "中考语文卷各题型占多少分？应该花多少时间？本文用数据告诉你如何在有限时间内拿到最高分。",
    "body": """
    <h2>一、中考语文卷分值结构（以150分制为例）</h2>
    <table><tr><td>题型</td><td>分值</td><td>占比</td><td>建议用时</td></tr><tr><td>积累与运用</td><td>30分</td><td>20%</td><td>20分钟</td></tr><tr><td>古诗词鉴赏</td><td>10分</td><td>7%</td><td>10分钟</td></tr><tr><td>文言文阅读</td><td>20分</td><td>13%</td><td>20分钟</td></tr><tr><td>现代文阅读</td><td>30分</td><td>20%</td><td>30分钟</td></tr><tr><td>作文</td><td>60分</td><td>40%</td><td>50分钟</td></tr></table>
    <h2>二、时间分配原则</h2>
    <blockquote>① 作文绝对不能超过50分钟，否则会压缩其他题型检查时间<br>
    ② 现代文阅读遇到难题先跳过，回头再做<br>
    ③ 基础题（字词、成语）必须一次性做对，没有回头检查的机会</blockquote>
    <h2>三、各题型拿分策略</h2>
    <h3>积累与运用（30分）</h3>
    <blockquote>目标：拿25-28分<br>
    策略：字音字形靠平时积累，成语辨析靠语境，病句修改靠类型判断<br>
    时间红线：20分钟，超时说明基础不扎实，考前重点补</blockquote>
    <h3>古诗词鉴赏（10分）</h3>
    <blockquote>目标：拿8-10分<br>
    策略：先判断题材，再找情感关键词，最后套答题公式<br>
    时间红线：10分钟</blockquote>
    <h3>文言文阅读（20分）</h3>
    <blockquote>目标：拿15-18分<br>
    策略：先读题目再看原文，带着问题找答案，实词结合语境推断<br>
    时间红线：20分钟</blockquote>
    <h3>现代文阅读（30分）</h3>
    <blockquote>目标：拿22-26分<br>
    策略：先判断文体（记叙文/说明文/议论文），再套用对应公式<br>
    时间红线：30分钟</blockquote>
    <h3>作文（60分）</h3>
    <blockquote>目标：拿45-52分<br>
    策略：审题清楚、结构清晰、开头结尾精彩、卷面工整<br>
    时间红线：50分钟</blockquote>
    <blockquote>💡 提示：时间分配因人而异，模拟考试时实测自己的速度，找到最适合自己的节奏。</blockquote>
    """
})

articles.append({
    "slug": "juzuici-xunlian-50da",
    "title": "中考近义词辨析50题训练 | 大衍语文店",
    "header_title": "中考近义词辨析50题训练",
    "description": "中考常考50组近义词辨析，涵盖词义轻重、适用对象、感情色彩、搭配习惯四大维度，配答案详解。",
    "body": """
    <h2>一、近义词辨析四维度</h2>
    <p>近义词看着差不多，其实细微差别很大。掌握四个辨析维度，见题不慌。</p>
    <h3>1. 词义轻重</h3>
    <blockquote>示例："希望"vs"渴望"——后者程度更深<br>
    练习：这件小事（     ）不必计较。（A. 偶尔 B. 偶然）</blockquote>
    <h3>2. 适用对象</h3>
    <blockquote>示例："发挥"vs"发扬"——"发挥"多用于抽象事物，"发扬"多用于风格、精神<br>
    练习：要（     ）艰苦朴素的优良传统。（A. 发挥 B. 发扬）</blockquote>
    <h3>3. 感情色彩</h3>
    <blockquote>示例："果断"vs"武断"——前者褒义，后者贬义<br>
    练习：他处事（     ），从不拖泥带水。（A. 果断 B. 武断）</blockquote>
    <h3>4. 搭配习惯</h3>
    <blockquote>示例："废除"vs"取消"——"废除"搭配法律、制度；"取消"搭配活动、资格<br>
    练习：（     ）这项不合理规定。（A. 废除 B. 取消）</blockquote>
    <h2>二、50组高频近义词</h2>
    <blockquote>1. 采纳/采取——2. 精密/严密/周密——3. 表现/表示/体现——4. 安静/宁静/寂静——5. 持续/继续/连续——6. 到处/处处——7. 独自/单独——8. 对付/应付——9. 发达/兴旺——10. 犯病/发病——11. 抚养/赡养——12. 工具/工具——13. 安静/宁静——14. 简直/几乎——15. 简洁/简短——16. 拘谨/谨慎——17. 觉察/发觉——18. 开辟/开拓——19. 考察/检查——20. 渴望/盼望——21. 宽裕/富裕——22. 困苦/困窘——23. 厉害/利害——24. 勉励/激励——25. 名义/名誉——26. 捏造/伪造——27. 凝视/注视——28. 偶尔/偶然——29. 破坏/损坏——30. 强制/强迫——31. 神情/神色——32. 时代/时期——33. 实验/试验——34. 收集/搜集——35. 坚苦/艰苦——36. 简洁/简短——37. 审订/审定——38. 熟悉/熟练——39. 思考/思索——40. 搜查/搜查——41. 损害/伤害——42. 提取/提炼——43. 违反/违犯——44. 鲜明/鲜艳——45. 严格/严厉/严肃——46. 隐蔽/隐藏——47. 优美/幽美——48. 整理/整顿——49. 终止/中断——50. 注视/凝视</blockquote>
    <blockquote>💡 提示：做近义词辨析时，先排除明显错误的选项，再比较剩下的，缩小范围后重点分析差异点。</blockquote>
    """
})

articles.append({
    "slug": "gaopin-chengyu-200-ti",
    "title": "中考高频成语200题精选 | 大衍语文店",
    "header_title": "中考高频成语200题精选",
    "description": "2026中考常考200个成语按主题分类汇总，附释义和用法，适合考前冲刺背诵。",
    "body": """
    <h2>一、成语学习的重要性</h2>
    <p>成语题是中考语文基础题中的"保分题"，只要积累够，拿满分不难。中考常考成语约200个，背熟这些，足以应付。</p>
    <h2>二、高频成语分类汇总</h2>
    <h3>形容学习态度</h3>
    <blockquote>孜孜不倦、勤学好问、学而不厌、一丝不苟、专心致志、持之以恒、博学多才、学富五车、才高八斗、鹤立鸡群</blockquote>
    <h3>形容人物品质</h3>
    <blockquote>拾金不昧、视死如归、临危不惧、大公无私、刚正不阿、坚强不屈、光明磊落、堂堂正正、严于律己，宽以待人</blockquote>
    <h3>形容时间短暂</h3>
    <blockquote>昙花一现、稍纵即逝、光阴似箭、日月如梭、白驹过隙、瞬息万变、电光火石、风驰电掣、弹指之间、转瞬即逝</blockquote>
    <h3>形容友情深厚</h3>
    <blockquote>肝胆相照、亲密无间、情同手足、风雨同舟、同舟共济、心心相印、八拜之交、莫逆之交、管鲍之交、桃花潭水</blockquote>
    <h3>形容思乡之情</h3>
    <blockquote>魂牵梦萦、归心似箭、日思夜想、落叶归根、故土难离、背井离乡、望穿秋水、翘首以待、昼夜兼程、迫不及待</blockquote>
    <h3>形容技艺高超</h3>
    <blockquote>出神入化、巧夺天工、鬼斧神工、炉火纯青、胸有成竹、得心应手、游刃有余、独具匠心、技高一筹、无与伦比</blockquote>
    <h3>形容形势危急</h3>
    <blockquote>千钧一发、燃眉之急、迫在眉睫、岌岌可危、危在旦夕、兵临城下、危如累卵、一触即发、十万火急、燃眉之急</blockquote>
    <h3>形容环境优美</h3>
    <blockquote>山清水秀、鸟语花香、春暖花开、万紫千红、姹紫嫣红、繁花似锦、绿树成荫、山明水秀、天高云淡、秋高气爽</blockquote>
    <h2>三、易混成语辨析</h2>
    <blockquote>① 无微不至vs体贴入微——前者指照顾细致，后者指关心体谅<br>
    ② 不负众望vs不孚众望——前者不辜负期望，后者不能使人信服<br>
    ③ 言之凿凿vs证据确凿——前者话说得有道理，后者事实确实<br>
    ④ 首当其冲vs一马当先——前者首先受到冲击，后者带头前进</blockquote>
    <blockquote>💡 提示：成语题不仅考记忆，还考辨析。做的时候先判断整体意思，再看感情色彩和适用对象。</blockquote>
    """
})

articles.append({
    "slug": "chuzhong-quancheng-fuxi-zhengce",
    "title": "初中语文全程复习规划与政策解读 | 大衍语文店",
    "header_title": "初中语文全程复习规划与政策解读",
    "description": "从初一到初三，语文学习各有重点。本文梳理各年级学习重点、中考趋势变化与备考策略，助你三年稳步提分。",
    "body": """
    <h2>一、初中三年语文学习重点</h2>
    <h3>初一：打基础</h3>
    <blockquote>重点：字词积累、文言文入门、阅读理解基本方法<br>
    关键：养成预习和复习的习惯，每天坚持30分钟语文积累<br>
    注意：不要只顾数学英语，语文基础没打好初三很难提分</blockquote>
    <h3>初二：提能力</h3>
    <blockquote>重点：古诗词系统学习、现代文阅读深化、作文结构训练<br>
    关键：开始写结构完整的作文，积累10个以上万能素材<br>
    注意：初二语文成绩会出现分化，抓紧查漏补缺</blockquote>
    <h3>初三：冲中考</h3>
    <blockquote>重点：中考全题型训练、薄弱环节突破、作文精修打磨<br>
    关键：每周做一套中考真题卷，分析错题，对症下药<br>
    注意：语文想短期提分难，靠的是平时积累，初三重点是保持状态</blockquote>
    <h2>二、2026年中考语文变化趋势</h2>
    <blockquote>① 课外文言文比重增加，需要扩大阅读面<br>
    ② 作文更重视真情实感，套路化作文得分下降<br>
    ③ 现代文阅读题目更灵活，纯粹背答案不管用<br>
    ④ 古诗词鉴赏增加主观题，需要自己组织语言</blockquote>
    <h2>三、各分数段提升策略</h2>
    <table><tr><td>当前分数</td><td>目标分数</td><td>策略</td></tr><tr><td>90分以下</td><td>100-110</td><td>死磕基础题，确保字词、病句、成语不丢分</td></tr><tr><td>100-110</td><td>115-120</td><td>提升阅读和作文，攻克中等难度题</td></tr><tr><td>115以上</td><td>125+</td><td>作文冲高分，细节不丢分，冲刺满分</td></tr></table>
    <blockquote>💡 提示：语文提分是长期过程，不要期待一周见效。制定计划，坚持执行，成绩自然上去。</blockquote>
    """
})

# More new topics
articles.append({
    "slug": "zhongkao-yuwen-mingti-30da",
    "title": "中考语文难题30道专项突破 | 大衍语文店",
    "header_title": "中考语文难题30道专项突破",
    "description": "筛选近3年中考语文卷中最具挑战性的30道题，配详细讲解，涵盖文言文、阅读、作文三大难点。",
    "body": """
    <h2>一、难题的本质是什么</h2>
    <p>中考语文难题不是"知识难"，而是"思维拐弯"。很多考生觉得难，是因为没想到那个思路，一旦点破就很简单。</p>
    <h2>二、文言文难题（10道）</h2>
    <blockquote>题1：实词"兵"在"蒙恬监蒙恬兵三十万"中是什么意思？<br>
    答案：军队。解析："兵"在古代常指"军队"，如"劲兵""亡兵"。</blockquote>
    <blockquote>题2：句子"非复吴下阿蒙"的"吴下"指什么？<br>
    答案：吴地区域。解析："吴下"泛指吴地，"吴下阿蒙"即吴地的吕蒙，后指人进步很大。</blockquote>
    <h2>三、阅读理解难题（10道）</h2>
    <blockquote>题11：文中反复出现"灰蒙蒙的天"有什么作用？<br>
    答案：①环境描写，渲染压抑气氛；②象征作者当时的心境；③为后文情感转折做铺垫。</blockquote>
    <blockquote>题15："我看到了父亲眼里的光"一句中"光"有几层含义？<br>
    答案：三层——①自然光（灯光/阳光）；②父亲眼中重新燃起的希望；③父子间重新建立的情感联结。</blockquote>
    <h2>四、作文难题（10道）</h2>
    <blockquote>题21：题目"我在迷雾中找到了方向"，写什么文体最好？<br>
    答案：记叙文。以具体事件为载体，通过一段迷茫经历展示成长转变，比议论文更生动。</blockquote>
    <blockquote>题28：以"这也是一种力量"为题，写600字作文，怎么写出新意？<br>
    答案：避开"母爱力量""坚持力量"等常见题材，选取"柔软的力量"（如包容、让步、沉默）来写。</blockquote>
    <blockquote>💡 提示：做难题要先看分值，分值高的题多写几句，分值低的题简洁作答。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-xinanti-tuowei-fangfa",
    "title": "中考语文新题型突破方法 | 大衍语文店",
    "header_title": "中考语文新题型突破方法",
    "description": "新材料阅读、读图理解、情境写话——中考语文新题型不断涌现。本文解析各类新题型的解题思路与备考策略。",
    "body": """
    <h2>一、新题型的三大趋势</h2>
    <p>近年中考语文命题越来越灵活，新题型层出不穷。掌握这些题型的规律，比盲目刷题更有效率。</p>
    <h3>趋势1：材料多样化</h3>
    <blockquote>不再只考纯文字，而是引入图表、漫画、诗歌等多种材料形式。<br>
    对策：学会从非文字材料中提取信息，对照文字材料综合理解。</blockquote>
    <h3>趋势2：情境化</h3>
    <blockquote>题目设置真实生活情境，要求考生现场应用语文知识。<br>
    对策：平时多观察生活中的语文现象，如广告语、标语、新闻标题。</blockquote>
    <h3>趋势3：开放性</h3>
    <blockquote>答案不唯一，鼓励个性化表达，考查思维深度而非标准答案。<br>
    对策：练习有条理地组织答案，观点明确、论据充分即可。</blockquote>
    <h2>二、新题型突破技巧</h2>
    <h3>读图理解题</h3>
    <blockquote>步骤：①看标题和图注②提取图中关键信息③联系文字材料④综合判断<br>
    示例：漫画题要先描述画面内容，再揭示讽刺意义或深层寓意。</blockquote>
    <h3>情境写话题</h3>
    <blockquote>步骤：①审题明确要求②联系实际生活③选择合适文体④组织语言表达<br>
    关键：题目要求什么就写什么，不要过度发挥。</blockquote>
    <blockquote>💡 提示：新题型本质还是基础知识的变形，把基础知识学扎实，新题型自然不怕。</blockquote>
    """
})

articles.append({
    "slug": "jixuwen-fanyi-jqiao-20ti",
    "title": "记叙文翻译技巧20题精讲 | 大衍语文店",
    "header_title": "记叙文翻译技巧20题精讲",
    "description": "记叙文翻译是中考的重要考点，本文通过20道精选练习，讲解如何准确把握文意、翻译关键句子、避免中式英语。",
    "body": """
    <h2>一、记叙文翻译的核心原则</h2>
    <p>记叙文翻译和议论文、说明文不同，它有故事线、人物、情感，翻译时要兼顾"意思准确"和"表达流畅"两个目标。</p>
    <h2>二、翻译步骤</h2>
    <blockquote>① 通读全文，了解故事背景和人物关系<br>
    ② 划出需要翻译的关键句子<br>
    ③ 分析句子结构（主谓宾）<br>
    ④ 逐词翻译，注意时态和语态<br>
    ⑤ 调整语序，使中文表达流畅</blockquote>
    <h2>三、20题精选练习</h2>
    <blockquote>练习1：He looked at his mother with tears in his eyes.<br>
    参考译文：他眼含热泪地看着母亲。<br>
    技巧："tears in his eyes"译为"眼含热泪"，比"眼睛里有泪水"更自然。</blockquote>
    <blockquote>练习6：The old man lived alone, but he never felt lonely.<br>
    参考译文：老人独居，但他从不感到孤独。<br>
    技巧："lived alone"强调独居状态，"felt lonely"强调内心感受，两者要区分。</blockquote>
    <blockquote>练习15：She smiled and said nothing, as if she knew everything.<br>
    参考译文：她微微一笑，什么也没说，好像什么都知道似的。<br>
    技巧："as if"引导方式状语从句，译为"好像……似的"符合中文习惯。</blockquote>
    <blockquote>💡 提示：翻译练习不要贪多，每天翻译2-3句话，认真分析，比囫囵吞枣做100道更有效。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-jiating-bsui-fangfa",
    "title": "中考语文家庭辅导方法 | 大衍语文店",
    "header_title": "中考语文家庭辅导方法",
    "description": "家长如何在家辅导孩子语文？本文提供实用的家庭语文学习方法，让家长即使不懂语文也能帮孩子提分。",
    "body": """
    <h2>一、家长在语文学习中的角色</h2>
    <p>很多家长觉得自己语文不好，无法辅导孩子。其实家长不需要会做题，只需要做好三件事：营造环境、监督习惯、给予鼓励。</p>
    <h2>二、具体方法</h2>
    <h3>1. 营造阅读环境</h3>
    <blockquote>家里有书桌和书架，常放几本好书在显眼位置<br>
    每天全家有30分钟的"安静阅读时间"，家长也参与<br>
    不需要强制孩子看书，但要以身作则</blockquote>
    <h3>2. 监督习惯养成</h3>
    <blockquote>每天听写10个生字词，家长念孩子写<br>
    每周检查一次错题本，看孩子有没有回顾<br>
    督促孩子每天早读10分钟古诗词</blockquote>
    <h3>3. 给予有效鼓励</h3>
    <blockquote>鼓励而不是夸聪明："你这篇作文比上次写得更具体了"而不是"你真聪明"<br>
    关注进步而不是分数：哪怕只进步了2分，也要肯定<br>
    给孩子表达的机会：让他给你讲一道题，说明他真的懂了</blockquote>
    <h2>三、分工建议</h2>
    <blockquote>数学英语交给补习班，语文习惯养成必须靠家长<br>
    家长不一定要会做题，但一定要会问问题<br>
    定期和老师沟通，了解孩子的薄弱环节</blockquote>
    <blockquote>💡 提示：语文提分比数学英语慢，家长要有耐心，不要因为短期内看不到效果就放弃。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-kemu-xuexi-shuiping",
    "title": "初中各年级语文学习水平提升指南 | 大衍语文店",
    "header_title": "初中各年级语文学习水平提升指南",
    "description": "初一打基础、初二提能力、初三冲中考——三个年级的语文学习重点与提分策略，助力三年稳步提升。",
    "body": """
    <h2>一、初一语文：打牢地基</h2>
    <p>初一是小升初的过渡期，语文内容和难度都比小学大幅提升。这一年的重点不是考高分，而是养成好的语文学习习惯。</p>
    <h3>初一核心任务</h3>
    <blockquote>① 掌握初中字词量：初中要求掌握的字词量是小学的3倍<br>
    ② 学会预习：每篇文章课前读一遍，划出不认识的字词<br>
    ③ 做好笔记：课堂上记下老师强调的重点，不要只是抄板书<br>
    ④ 坚持阅读：每天读30分钟课外书，积累词汇和语感</blockquote>
    <h3>初一常见问题</h3>
    <blockquote>问题：升初中后语文成绩下滑<br>
    原因：学习内容深度增加，学习方法没有调整<br>
    对策：不要只刷题，要理解文章内容和答题思路</blockquote>
    <h2>二、初二语文：跨越分化期</h2>
    <p>初二语文有一个明显的"分化期"，很多学生成绩会下滑。这是因为初二开始接触议论文阅读和复杂文言文，如果基础不扎实，很容易跟不上。</p>
    <h3>初二核心任务</h3>
    <blockquote>① 攻克议论文阅读：掌握论点、论据、论证方法<br>
    ② 系统学习古诗词：初中三年古诗词最多的就是初二<br>
    ③ 作文要有结构：开始练习有清晰结构的作文，不要写流水账<br>
    ④ 积累素材：准备10个万能作文素材，能应对各种题目</blockquote>
    <h2>三、初三语文：系统冲刺</h2>
    <p>初三语文的核心是"整合"和"查漏补缺"，把三年所学融会贯通，冲刺中考。</p>
    <h3>初三核心任务</h3>
    <blockquote>① 专题复习：按题型进行专题训练，逐个击破<br>
    ② 做真题卷：每周做一套中考真题卷，感受出题风格<br>
    ③ 打磨作文：准备3-5篇高质量作文，考场直接套用<br>
    ④ 回归基础：语文基础题是送分题，确保不丢分</blockquote>
    <blockquote>💡 提示：语文学习没有捷径，靠的是平时积累和正确方法。临时抱佛脚只能保住基础分，想拿高分必须提早准备。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-tigao-daopin-20fa",
    "title": "语文成绩快速提高20种方法 | 大衍语文店",
    "header_title": "语文成绩快速提高20种方法",
    "description": "字词、成语、病句、阅读、作文——5大板块各4种提分方法，帮助中等生短期内突破语文瓶颈。",
    "body": """
    <h2>一、字词板块（4种方法）</h2>
    <blockquote>方法1：错字本法——准备一个错字本，每次练习中的错字记录下来，定期复习<br>
    方法2：联想记忆法——把一个字的字形和字义通过故事联想在一起，如"休"是人靠在树上休息<br>
    方法3：词根记忆法——英语有词根，汉语也有偏旁部首，如"贝"字旁与钱财有关<br>
    方法4：造句法——学一个词就用它造一个句子，用过的词印象更深</blockquote>
    <h2>二、成语板块（4种方法）</h2>
    <blockquote>方法1：分类记忆法——按使用场景把成语分类，如形容人的、形容事的、形容情感的<br>
    方法2：出处追溯法——了解成语来源的故事，印象更深刻<br>
    方法3：语境辨析法——把成语放进句子中理解，比单纯记忆更准确<br>
    方法4：对比记忆法——把易混成语放在一起对比记忆，如"不卑不亢"vs"不三不四"</blockquote>
    <h2>三、病句板块（4种方法）</h2>
    <blockquote>方法1：主谓宾缩句法——把长句缩成主谓宾结构，检查搭配是否残缺<br>
    方法2：成分分析法——逐个检查主谓宾定状补，看是否有成分残缺或多余<br>
    方法3：语序检查法——检查并列词语的排列顺序是否符合逻辑<br>
    方法4：六种病句类型熟记法——背熟搭配不当、成分残缺、语序不当等6种类型</blockquote>
    <h2>四、阅读板块（4种方法）</h2>
    <blockquote>方法1：答题公式法——每种题型有固定的答题公式，先判断题型再套公式<br>
    方法2：原文词抄法——答案中的关键词尽量用原文的词，不要过度改写<br>
    方法3：分点作答法——多角度答题时用①②③分点，每点都是一个得分点<br>
    方法4：做题后分析法——做完每篇阅读后，分析自己哪里丢分了，下次注意</blockquote>
    <h2>五、作文板块（4种方法）</h2>
    <blockquote>方法1：素材积累法——准备10个万能素材，能应对大多数题目<br>
    方法2：开头结尾模板法——准备5个精彩开头和5个有力结尾，考场直接套用<br>
    方法3：结构固化法——固定使用"开头-经过-结尾"三段式或"起承转合"四段式<br>
    方法4：卷面整洁法——字迹工整比字漂亮更重要，卷面干净能加2-3分</blockquote>
    <blockquote>💡 提示：提分的关键不是学更多东西，而是把已有的漏洞补上。基础题不丢分，成绩自然上去了。</blockquote>
    """
})

articles.append({
    "slug": "zhongkao-yuwen-kemu-fenpei",
    "title": "中考语文科目分值分配与冲刺策略 | 大衍语文店",
    "header_title": "中考语文科目分值分配与冲刺策略",
    "description": "了解中考语文各板块分值，才能合理分配备考精力。本文详解各题型分值与拿分策略，帮你用最少时间拿最高分。",
    "body": """
    <h2>一、中考语文分值分配（150分制）</h2>
    <table><tr><td>模块</td><td>分值</td><td>重要程度</td><td>备考优先级</td></tr><tr><td>积累与运用</td><td>30分</td><td>★★★</td><td>高（基础题必须拿满）</td></tr><tr><td>古诗词鉴赏</td><td>10分</td><td>★★★</td><td>高（套路清晰）</td></tr><tr><td>文言文阅读</td><td>20分</td><td>★★★</td><td>高（课内为主）</td></tr><tr><td>现代文阅读</td><td>30分</td><td>★★★</td><td>中（技巧性强）</td></tr><tr><td>作文</td><td>60分</td><td>★★★★★</td><td>最高（分数最高）</td></tr></table>
    <h2>二、各板块拿分策略</h2>
    <h3>积累与运用（目标：25-28分）</h3>
    <blockquote>这块内容杂，涉及字音、字形、成语、病句、排序、标点等。<br>
    策略：基础题不丢分靠平时积累，考前过一遍易错字表和病句类型。<br>
    时间：建议20分钟内完成。</blockquote>
    <h3>古诗词鉴赏（目标：8-10分）</h3>
    <blockquote>这块有套路，先判断诗词类型，再找情感关键词。<br>
    策略：每天读一首课内古诗词，分析情感和手法。<br>
    时间：建议10分钟内完成。</blockquote>
    <h3>文言文阅读（目标：15-18分）</h3>
    <blockquote>课内文言文是基础，把课内学过的文章搞懂，实词、虚词、句式都要掌握。<br>
    策略：考前把课本文言文注释过一遍，重点实词整理出来。<br>
    时间：建议20分钟内完成。</blockquote>
    <h3>现代文阅读（目标：22-26分）</h3>
    <blockquote>这是技巧性最强的题型，必须掌握答题公式。<br>
    策略：先判断文体，再套用对应公式，分点作答。<br>
    时间：建议30分钟内完成。</blockquote>
    <h3>作文（目标：45-52分）</h3>
    <blockquote>作文是最大的一块，也是提分空间最大的一块。<br>
    策略：准备3-5篇高质量作文，考场直接套用或改编。<br>
    时间：建议50分钟内完成。</blockquote>
    <blockquote>💡 提示：时间分配因人而异，关键是在模拟考试中找到自己的节奏。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-kamus-liyong-jiaqiao",
    "title": "语文课外资源利用与加分技巧 | 大衍语文店",
    "header_title": "语文课外资源利用与加分技巧",
    "description": "课外阅读、电视节目、网络资源——如何利用课外资源为语文学习加分，本文推荐最实用的加分渠道。",
    "body": """
    <h2>一、最容易被忽视的加分资源</h2>
    <p>很多考生只盯着课本和习题册，其实课外资源才是拉开差距的关键。那些语文成绩突出的学生，无一不是充分利用了课外资源。</p>
    <h2>二、三大加分渠道</h2>
    <h3>渠道1：课外阅读（最重要）</h3>
    <blockquote>推荐书目：初中生必读名著12篇（《骆驼祥子》《海底两万里》等）<br>
    加分阅读：《中国诗词大会》《百家讲坛》相关书籍<br>
    阅读方法：不要只看情节，要分析人物、主题、写作手法</blockquote>
    <h3>渠道2：电视节目</h3>
    <blockquote>《中国诗词大会》——培养诗词感觉，积累名句<br>
    《朗读者》——学习朗读技巧，感受文字魅力<br>
    《经典咏流传》——用歌曲方式记忆古诗词</blockquote>
    <h3>渠道3：手机APP</h3>
    <blockquote>古诗词学习APP——利用碎片时间积累<br>
    作文纸条——积累作文素材和佳句<br>
    网易云课堂——听名师讲解阅读技巧</blockquote>
    <h2>三、资源使用效率最大化</h2>
    <blockquote>① 有目的地使用资源：带着问题去看节目，比如"今天我要积累3个关于亲情的素材"<br>
    ② 做笔记：看到好词好句就记下来，定期复习<br>
    ③ 转化利用：把从课外学到的内容尝试用在作文里，用过才是自己的</blockquote>
    <blockquote>💡 提示：课外资源不是用来消遣的，是用来给语文加分的。每次使用都要有收获。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-jiqiao-paihang",
    "title": "中考语文各题型技巧排行榜 | 大衍语文店",
    "header_title": "中考语文各题型技巧排行榜",
    "description": "哪个题型最应该优先掌握？哪个技巧最实用？本文按提分效率排列各题型技巧，帮你用最少时间拿最多分。",
    "body": """
    <h2>一、为什么技巧也有优先级</h2>
    <p>时间和精力是有限的，把最好的技巧用在最重要的题型上，才是提分的最佳策略。</p>
    <h2>二、各题型技巧排行榜</h2>
    <h3>🥇 第1名：作文开头技巧</h3>
    <blockquote>提分效率：★★★★★<br>
    学习难度：★★<br>
    原因：作文开头好能给阅卷老师留下好印象，直接提升印象分5-10分。<br>
    技巧：① 修辞入题法（用比喻、排比开头）② 悬念入题法（用问题开头）③ 场景入题法（描写场景开头）</blockquote>
    <h3>🥈 第2名：病句辨析技巧</h3>
    <blockquote>提分效率：★★★★☆<br>
    学习难度：★★<br>
    原因：病句题有6种固定类型，判断出来就能做对，命中率极高。<br>
    技巧：① 主谓宾缩句法 ② 关键词判断法（看到"通过/使"要注意主语残缺）</blockquote>
    <h3>🥉 第3名：古诗词鉴赏公式</h3>
    <blockquote>提分效率：★★★★<br>
    学习难度：★★★<br>
    原因：古诗词鉴赏题型固定，公式掌握后可以应对大多数题目。<br>
    技巧：① 题材判断法 ② 情感关键词法 ③ 答题公式套用法</blockquote>
    <h3>第4名：阅读理解分点作答法</h3>
    <blockquote>提分效率：★★★★<br>
    学习难度：★★★<br>
    原因：分点作答能让阅卷老师一眼看到你的得分点，不漏分。<br>
    技巧：每道题答2-4点，每点用①②③标注，关键词放每点开头。</blockquote>
    <h3>第5名：文言文实词推断法</h3>
    <blockquote>提分效率：★★★<br>
    学习难度：★★★★<br>
    原因：课内实词考得多，课外实词可以用方法推断。<br>
    技巧：① 词性推断 ② 语境推断 ③ 语法结构推断</blockquote>
    <blockquote>💡 提示：时间和精力有限时，优先掌握前3名的技巧，性价比最高。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yingyu-huoyong-jiaqiao",
    "title": "语文与英语融会贯通的技巧 | 大衍语文店",
    "header_title": "语文与英语融会贯通的技巧",
    "description": "很多考生不知道，语文和英语学习方法可以互通。本文分享如何用语文思维帮助英语学习，实现两科双赢。",
    "body": """
    <h2>一、语文和英语的共同点</h2>
    <p>语文和英语都是语言学科，其学习方法本质上是一样的。把语文的学习思路迁移到英语上，可以事半功倍。</p>
    <h2>二、语文思维帮助英语学习</h2>
    <h3>1. 语法结构分析</h3>
    <blockquote>语文的句子结构分析（主谓宾）和英语的句子结构分析是相通的。<br>
    例子：分析"我爱你"时，主语是"我"，谓语是"爱"，宾语是"你"。<br>
    英语也一样："I love you"，主语是"I"，谓语是"love"，宾语是"you"。<br>
    学会分析汉语句子结构，再分析英语句子结构就简单了。</blockquote>
    <h3>2. 阅读理解技巧</h3>
    <blockquote>语文阅读理解的答题公式可以直接迁移到英语阅读。<br>
    公式：先看题目→带着问题读文章→定位关键词→组织答案<br>
    英语阅读同样适用这个流程。</blockquote>
    <h3>3. 作文套路</h3>
    <blockquote>语文作文的开头结尾技巧可以用在英语作文上。<br>
    例如：语文用"开头点题+结尾升华"，英语作文同样适用。<br>
    语文积累的好词好句翻译成英语，就是高分英语作文。</blockquote>
    <h2>三、具体操作方法</h2>
    <blockquote>① 每天做一篇英语阅读，用语文阅读理解的思路分析<br>
    ② 英语作文写完后，用语文作文的修改方法检查<br>
    ③ 把语文课学到的修辞手法尝试用在英语作文里（比喻、拟人等）</blockquote>
    <blockquote>💡 提示：语言学习是相通的，不要把语文和英语割裂开。两科学好，都能提升语言思维能力。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-timu-daoli-paihang",
    "title": "中考语文题目道理排行榜 | 大衍语文店",
    "header_title": "中考语文题目道理排行榜",
    "description": "哪些题目背后的道理最实用？哪些思维方式最重要？本文按实用程度排列中考语文背后的思维道理。",
    "body": """
    <h2>一、学语文不仅是学知识</h2>
    <p>中考语文背后有很多实用的人生道理，这些道理不仅能帮考试，更能影响一个人的思维方式和表达能力。</p>
    <h2>二、各题目类型的道理排行榜</h2>
    <h3>🥇 第1名：阅读理解题——"透过现象看本质"</h3>
    <blockquote>题目要求分析文章深层含义，培养的是透过现象看本质的能力。<br>
    人生道理：我们看到的往往只是表面，要学会挖掘深层原因。<br>
    应用：生活中遇到问题时，多问"为什么"，而不是只看"是什么"。</blockquote>
    <h3>🥈 第2名：古诗词鉴赏——"借景抒情，托物言志"</h3>
    <blockquote>古人写诗往往借景抒情，托物言志，培养的是间接表达的能力。<br>
    人生道理：有些话不能直说，要学会用间接的方式表达自己的意思。<br>
    应用：在人际交往中，有些话婉转说比直说更有效。</blockquote>
    <h3>🥉 第3名：议论文阅读——"论点论据论证"</h3>
    <blockquote>议论文的三要素培养的是逻辑思维能力。<br>
    人生道理：说话做事要有理有据，不能凭感觉。<br>
    应用：发表意见时，先想好论点是什么，再找论据支持。</blockquote>
    <h3>第4名：作文——"真情实感最能打动人"</h3>
    <blockquote>真情实感的作文最能打动阅卷老师，说明真情实感在任何场合都有力量。<br>
    人生道理：真诚比技巧更重要，做人要真诚。<br>
    应用：在任何表达场合，真情实感都比华丽的辞藻更能打动人心。</blockquote>
    <blockquote>💡 提示：语文不仅是考试科目，更是培养生活能力的学科。学到的东西要在生活中用出来。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-zixue-fangfa-jiaqiao",
    "title": "语文自学方法与技巧强化 | 大衍语文店",
    "header_title": "语文自学方法与技巧强化",
    "description": "课堂之外如何自学语文？自学语文的高效方法、工具推荐与习惯养成，让你在课外也能持续提升语文成绩。",
    "body": """
    <h2>一、为什么要强调自学</h2>
    <p>课堂时间有限，语文能力的真正提升更多发生在课外。自学能力强的人，即使老师一般，也能通过自学达到高水平。</p>
    <h2>二、高效自学方法</h2>
    <h3>方法1：每日积累法</h3>
    <blockquote>每天积累5个新词、1句古诗词、1个作文素材<br>
    工具：手机备忘录、便签APP<br>
    关键：定时复习，一周回顾一次</blockquote>
    <h3>方法2：错题本法</h3>
    <blockquote>每次练习中遇到的错题记录到错题本<br>
    格式：题目→正确答案→错误原因→所属类型<br>
    复习频率：每周翻看一次</blockquote>
    <h3>方法3：输出倒逼输入法</h3>
    <blockquote>学完一个知识点，尝试讲给别人听或写出来<br>
    如果能讲清楚，说明真的懂了<br>
    如果讲不清楚，说明还有漏洞</blockquote>
    <h2>三、自学工具推荐</h2>
    <blockquote>① 词典APP：查字音字形字义<br>
    ② 古诗词APP：碎片时间积累<br>
    ③ 作文纸条：积累素材和佳句<br>
    ④ 错题本APP：记录整理错题</blockquote>
    <h2>四、自学习惯养成</h2>
    <blockquote>① 固定时间：每天固定30分钟语文自学时间<br>
    ② 设定目标：每周设定一个小目标<br>
    ③ 定期检测：每月做一次自我测试<br>
    ④ 奖励机制：完成目标后给自己奖励</blockquote>
    <blockquote>💡 提示：自学最大的敌人是拖延。找一个同伴互相监督，或者用APP记录学习时间，能有效克服拖延。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-fuxi-zongjie-gonglue",
    "title": "语文复习总结与全年规划策略 | 大衍语文店",
    "header_title": "语文复习总结与全年规划策略",
    "description": "语文知识点繁杂，本文帮你理清复习思路，制定全年学习计划，让语文复习不再眉毛胡子一把抓。",
    "body": """
    <h2>一、语文复习的三大误区</h2>
    <blockquote>❌ 误区1：大量刷题，不总结<br>
    ✅ 正确做法：做完一套题后，花同样的时间分析错题<br>
    <br>
    ❌ 误区2：只背答案，不理解<br>
    ✅ 正确做法：理解解题思路，能讲出来才算懂<br>
    <br>
    ❌ 误区3：作文临时抱佛脚<br>
    ✅ 正确做法：平时积累3-5个万能素材，考前打磨3篇高质量作文</blockquote>
    <h2>二、全年复习规划</h2>
    <table><tr><td>阶段</td><td>时间</td><td>重点</td><td>方法</td></tr><tr><td>基础期</td><td>9月-11月</td><td>字词、病句、成语</td><td>每天积累</td></tr><tr><td>提升期</td><td>12月-2月</td><td>阅读、鉴赏</td><td>专项训练</td></tr><tr><td>强化期</td><td>3月-4月</td><td>作文、真题</td><td>套题练习</td></tr><tr><td>冲刺期</td><td>5月-6月</td><td>查漏补缺</td><td>错题回顾</td></tr></table>
    <h2>三、各板块复习策略</h2>
    <h3>1. 基础题（字词、病句、成语）</h3>
    <blockquote>策略：每天10分钟积累，每周一次小测<br>
    工具：错题本、易错字表<br>
    目标：基础题不丢分</blockquote>
    <h3>2. 阅读题</h3>
    <blockquote>策略：掌握5大题型答题公式<br>
    方法：每种题型做10道题，总结答题规律<br>
    目标：阅读题拿80%以上分数</blockquote>
    <h3>3. 作文</h3>
    <blockquote>策略：平时积累，考前打磨<br>
    方法：准备3个万能素材+5个开头结尾<br>
    目标：作文拿45-52分</blockquote>
    <blockquote>💡 提示：复习的关键是"针对性"，哪里弱就补哪里，不要平均用力。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-biyi-cuosheng-fangfa",
    "title": "避免语文低级错误的技巧 | 大衍语文店",
    "header_title": "避免语文低级错误的技巧",
    "description": "语文考试中最让人痛心的不是难题不会做，而是低级错误丢分。本文汇总常见低级错误及避免方法，帮你少丢分。",
    "body": """
    <h2>一、为什么低级错误最可惜</h2>
    <p>低级错误不是不会，是本来会做，但因为粗心而丢分。中考1分可能就是一批学生的差距，避免低级错误是最简单有效的提分方法。</p>
    <h2>二、七种最常见低级错误</h2>
    <h3>错误1：写错别字</h3>
    <blockquote>示例："戊戌"写成"戊戍"，"九州"写成"九洲"<br>
    避免方法：每次写完检查，特别是形近字和同音字<br>
    考前准备：把常错的字写在一张纸上，进考场前看一遍</blockquote>
    <h3>错误2：答题卡填涂错误</h3>
    <blockquote>问题：填错位置、涂不清晰、二次修改<br>
    避免方法：① 做一题填一题，不要最后一起填 ② 涂卡要涂满、涂黑 ③ 改答案时要擦干净</blockquote>
    <h3>错误3：作文跑题</h3>
    <blockquote>问题：没看清题目要求，写成了另一个主题<br>
    避免方法：① 审题三遍 ② 开头点题 ③ 中间扣题 ④ 结尾回扣题目</blockquote>
    <h3>错误4：审题不仔细</h3>
    <blockquote>问题：题目要求"不正确"却写了"正确"的，要求"至少两点"只写了一点<br>
    避免方法：审题时用笔把关键词圈出来，确保不漏要求</blockquote>
    <h3>错误5：作文字数不够或超限</h3>
    <blockquote>标准：初中作文一般要求600字左右<br>
    建议：写650字左右，留出修改余地<br>
    字数计算：每行约28字，约23行</blockquote>
    <h3>错误6：卷面不整洁</h3>
    <blockquote>问题：涂改太多，字迹潦草<br>
    避免方法：先打草稿或列提纲再正式写作文，减少涂改</blockquote>
    <h3>错误7：时间不够，作文写不完</h3>
    <blockquote>问题：前面花太多时间，作文只剩20分钟<br>
    避免方法：考前模拟考试，找到适合自己的时间分配节奏</blockquote>
    <blockquote>💡 提示：低级错误不是小事，每次练习都要当成正式考试，培养细心习惯。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-kaoshi-jieda-liu",
    "title": "中考语文考场六大技巧 | 大衍语文店",
    "header_title": "中考语文考场六大技巧",
    "description": "考试技巧决定临场发挥。本文分享六条考场实战技巧，帮助你在正式考试中发挥出最佳水平，多拿5-10分。",
    "body": """
    <h2>一、发卷后先做这件事</h2>
    <p>拿到试卷后不要急着做题，先整体看一遍试卷，了解各板块的分值和题目数量，心里有数后再开始做题。</p>
    <h2>二、六大考场技巧</h2>
    <h3>技巧1：先易后难</h3>
    <blockquote>策略：先把会做的题做完，确保基础分不丢<br>
    操作：遇到2分钟还没思路的题，先跳过，回头再攻<br>
    目的：保证整体分数，不因为难题影响心态</blockquote>
    <h3>技巧2：作文先列提纲</h3>
    <blockquote>策略：拿到作文题后，不要立即动笔，先花3分钟列提纲<br>
    提纲内容：开头怎么写、中间分几点、结尾怎么收<br>
    目的：避免写到一半不知道写什么，确保结构完整</blockquote>
    <h3>技巧3：阅读先看题目</h3>
    <blockquote>策略：现代文阅读先看题目，带着问题读文章<br>
    操作：看题目时把关键词记住，读文章时主动寻找答案<br>
    目的：提高阅读效率，快速定位答案</blockquote>
    <h3>技巧4：文言文翻译逐字对应</h3>
    <blockquote>策略：翻译时先找出每个词语对应的意思，再调整语序<br>
    操作：不会的实词联系上下文推断，虚词根据位置判断<br>
    目的：减少漏译和错译</blockquote>
    <h3>技巧5：古诗词鉴赏先判断题材</h3>
    <blockquote>策略：先判断诗词题材（羁旅思乡/送别/边塞/咏物等），再找情感关键词<br>
    操作：不同题材有不同的常用情感词，题材判断对了情感不会错<br>
    目的：快速准确拿分</blockquote>
    <h3>技巧6：交卷前检查这些</h3>
    <blockquote>检查顺序：① 答题卡填涂是否完整 ② 有没有漏做的题 ③ 错别字检查 ④ 作文字数<br>
    时间建议：至少留5分钟检查<br>
    注意：改答案要谨慎，只改明显错误的，原来选的往往是对的</blockquote>
    <blockquote>💡 提示：考试时最重要的是保持平稳心态，不要因为一道题影响整场考试。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-shoufa-gaishou",
    "title": "语文阅读速度和效率提升方法 | 大衍语文店",
    "header_title": "语文阅读速度和效率提升方法",
    "description": "阅读速度慢、理解不到位怎么办？本文从阅读方法、训练步骤到实战技巧，帮你全面提升阅读能力。",
    "body": """
    <h2>一、为什么阅读速度很重要</h2>
    <p>考试时间有限，阅读速度快意味着有更多时间思考和答题。速度提上去，正确率往往也会跟着提升。</p>
    <h2>二、快速阅读训练四步法</h2>
    <h3>第一步：计时阅读</h3>
    <blockquote>方法：做阅读理解时记录阅读时间<br>
    目标：一篇500字的文章，阅读时间控制在2分钟以内<br>
    工具：秒表或手机计时器</blockquote>
    <h3>第二步：段意概括</h3>
    <blockquote>方法：每读一段，用一句话概括段意<br>
    训练目标：快速提取关键信息<br>
    判断标准：概括准确说明读懂了</blockquote>
    <h3>第三步：结构分析</h3>
    <blockquote>方法：读完后分析文章结构——总分总、分总、总分等<br>
    作用：了解文章框架，快速定位答案位置</blockquote>
    <h3>第四步：关键词标记</h3>
    <blockquote>方法：读文章时用笔划出关键词（时间、地点、人物、事件、情感词）<br>
    作用：方便做题时快速定位</blockquote>
    <h2>三、不同文体的阅读策略</h2>
    <blockquote>记叙文：抓六要素，找线索，看结尾<br>
    说明文：抓说明对象、说明方法、说明顺序<br>
    议论文：抓论点、论据、论证方法</blockquote>
    <blockquote>💡 提示：阅读速度提升不是一蹴而就的，每天练习1-2篇，坚持一个月效果明显。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-zuowen-lianghua-fangfa",
    "title": "语文作文量化训练方法 | 大衍语文店",
    "header_title": "语文作文量化训练方法",
    "description": "作文能力可以量化训练吗？当然可以。本文提供作文各维度的量化训练方法，让写作水平可衡量、可提升。",
    "body": """
    <h2>一、作文可以量化</h2>
    <p>很多人觉得作文靠天赋、靠感觉，其实作文完全可以量化训练。把作文分解成不同维度，每个维度单独训练，逐个击破。</p>
    <h2>二、作文五维度量化训练</h2>
    <h3>维度1：字数控制</h3>
    <blockquote>目标：650字（留有余地）<br>
    训练：每周写一篇650字作文，用字数统计检查<br>
    达标标准：误差在±20字以内</blockquote>
    <h3>维度2：开头质量</h3>
    <blockquote>目标：150字内入题<br>
    训练：练习3种开头方式——场景入题、修辞入题、悬念入题<br>
    达标标准：开头能在50字内吸引读者</blockquote>
    <h3>维度3：结构完整</h3>
    <blockquote>目标：清晰的三段式或四段式<br>
    训练：每次写作文先列提纲，严格按提纲写<br>
    达标标准：每段有中心句，段落间逻辑连贯</blockquote>
    <h3>维度4：素材贴切</h3>
    <blockquote>目标：素材与主题高度相关<br>
    训练：每个主题准备2-3个素材，能灵活变换使用<br>
    达标标准：素材能充分支撑主题，不生硬</blockquote>
    <h3>维度5：语言表达</h3>
    <blockquote>目标：语言流畅，有修辞意识<br>
    训练：每次写作刻意使用2-3处修辞手法<br>
    达标标准：语言不干涩，有画面感</blockquote>
    <h2>三、量化检测表</h2>
    <blockquote>① 字数：650±20字<br>
    ② 开头：150字内入题<br>
    ③ 结构：有三段式或四段式<br>
    ④ 素材：与主题相关<br>
    ⑤ 语言：有修辞手法<br>
    每项达标可得20分，满分100</blockquote>
    <blockquote>💡 提示：不要等到考试才训练作文。每周写一篇，按量化标准自检，才能持续进步。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-lishi-jieda",
    "title": "语文历史类文本阅读解答技巧 | 大衍语文店",
    "header_title": "语文历史类文本阅读解答技巧",
    "description": "历史类文本阅读是中考语文的新兴题型。本文从文本特点、命题规律、答题技巧三个维度，帮助考生攻克这类题型。",
    "body": """
    <h2>一、历史类文本的命题趋势</h2>
    <p>近年中考语文卷中，历史类文本阅读出现频率越来越高。这类文本通常以文言文或白话文形式出现，内容涉及历史事件、历史人物或历史典籍。</p>
    <h2>二、历史类文本的特点</h2>
    <blockquote>① 语言：半文半白，夹杂古代表达<br>
    ② 内容：涉及历史事件、人物、品行<br>
    ③ 主题：多与品格美德、家国情怀相关<br>
    ④ 题型：概括题、赏析题、启示题为主</blockquote>
    <h2>三、答题技巧</h2>
    <h3>技巧1：先判断文本类型</h3>
    <blockquote>判断：是文言文还是白话文？是史传文还是论说文？<br>
    不同类型文本，答题重点不同</blockquote>
    <h3>技巧2：概括题抓时间线</h3>
    <blockquote>方法：划出文本中的时间词和事件词<br>
    按时间顺序排列，概括每个节点的主要事件<br>
    最后综合成完整概括</blockquote>
    <h3>技巧3：人物分析题抓言行</h3>
    <blockquote>方法：从文本中找出人物的关键言行<br>
    分析言行背后的品质（忠、孝、义、仁等）<br>
    结合历史背景分析人物形象</blockquote>
    <h3>技巧4：启示题结合现实</h3>
    <blockquote>方法：先总结文本启示，再联系现实生活<br>
    启示要有具体性，不能只写空洞的大道理<br>
    好的启示：个人品格层面有具体指导意义</blockquote>
    <blockquote>💡 提示：历史类文本的关键是读懂人物和事件，不要被古汉语词汇难住，影响整体理解。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-chengyu-shiyong-cuowu",
    "title": "中考成语使用常见错误汇总 | 大衍语文店",
    "header_title": "中考成语使用常见错误汇总",
    "description": "成语使用错误是中考语文的高频丢分点。本文汇总最常见的成语使用错误类型，配实例讲解，帮你避开陷阱。",
    "body": """
    <h2>一、成语使用错误的四大类型</h2>
    <h3>类型1：望文生义</h3>
    <blockquote>错误示例："不刊之论"被理解为"不能刊登的文章"<br>
    正确含义：比喻不能改动或不可磨灭的言论（"刊"在这里是"更改"的意思）<br>
    误用原因：只看了字面意思，没理解历史含义</blockquote>
    <h3>类型2：语义重复</h3>
    <blockquote>错误示例："忍俊不禁地笑了起来"（"忍俊不禁"本身就是"忍不住笑"的意思）<br>
    正确用法：忍俊不禁”或“笑了起来”，二选一</blockquote>
    <h3>类型3：对象不当</h3>
    <blockquote>错误示例："悬壶济世"形容教师（"悬壶济世"专指医生行医）<br>
    正确用法："悬壶济世"只能用于医疗行业</blockquote>
    <h3>类型4：褒贬色彩不当</h3>
    <blockquote>错误示例：用"处心积虑"形容正面人物（该词是贬义）<br>
    正确理解："处心积虑"意思是费尽心机，含贬义，不能形容好人</blockquote>
    <h2>二、中考高频成语错误汇总</h2>
    <table><tr><td>成语</td><td>错误理解</td><td>正确含义</td></tr><tr><td>不刊之论</td><td>不能刊登的文章</td><td>不可磨灭的言论</td></tr><tr><td>文不加点</td><td>文章没标点</td><td>形容文思敏捷</td></tr><tr><td>首当其冲</td><td>首先要做的事</td><td>首先受到冲击</td></tr><tr><td>差强人意</td><td>不满意</td><td>大体上还能让人满意</td></tr><tr><td>不足为训</td><td>不值得教训</td><td>不值得作为准则</td></tr><tr><td>久假不归</td><td>长期请假不回来</td><td>长期借了不还</td></tr></table>
    <blockquote>💡 提示：成语学习要理解含义，不能只背字面。多查词典，多看例句。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-tigao-suji",
    "title": "语文阅读理解能力提升素材库 | 大衍语文店",
    "header_title": "语文阅读理解能力提升素材库",
    "description": "阅读理解能力的提升需要积累。本文提供分类素材库，涵盖人、物、景、情四大维度，帮助你积累阅读理解所需的背景知识。",
    "body": """
    <h2>一、为什么要积累阅读素材</h2>
    <p>阅读理解丢分，有时候不是因为读不懂文章，而是因为背景知识不足。文章提到的某些人、事、景，如果没听说过，就很难理解。</p>
    <h2>二、人物类素材</h2>
    <h3>古代文人</h3>
    <blockquote>李白：浪漫主义诗人，号青莲居士，代表作《静夜思》《将进酒》<br>
    杜甫：现实主义诗人，号少陵野老，代表作《春望》《茅屋为秋风所破歌》<br>
    白居易：现实主义诗人，号香山居士，代表作《琵琶行》《长恨歌》</blockquote>
    <h3>历史人物</h3>
    <blockquote>孔子：儒家学派创始人，主张"仁"和"礼"<br>
    诸葛亮：三国时期政治家、军事家，辅佐刘备建立蜀汉<br>
    范仲淹：北宋政治家，"先天下之忧而忧，后天下之乐而乐"</blockquote>
    <h2>三、事物类素材</h2>
    <blockquote>四大发明：造纸术、印刷术、指南针、火药<br>
    文房四宝：笔、墨、纸、砚<br>
    汉字六书：象形、指事、会意、形声、转注、假借</blockquote>
    <h2>四、景色类素材</h2>
    <blockquote>四大名楼：黄鹤楼、岳阳楼、滕王阁、鹳雀楼<br>
    名山大川：泰山（五岳之首）、黄山（奇松、怪石、云海、温泉）<br>
    名胜古迹：故宫、长城、兵马俑、莫高窟</blockquote>
    <blockquote>💡 提示：这些素材不需要死记硬背，平时多阅读，遇到时留个印象，自然就能记住。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-neirong-fengxi",
    "title": "语文阅读内容分析与主题把握 | 大衍语文店",
    "header_title": "语文阅读内容分析与主题把握",
    "description": "如何快速读懂一篇文章？本文提供内容分析和主题把握的系统方法，让你在有限时间内精准理解文章核心。",
    "body": """
    <h2>一、内容分析的三步法</h2>
    <h3>第一步：整体感知</h3>
    <blockquote>快速通读全文，感知文章大概意思<br>
    问自己三个问题：这篇文章写了什么？主要人物是谁？表达了什么情感？<br>
    用时建议：不超过1分钟</blockquote>
    <h3>第二步：局部解析</h3>
    <blockquote>逐段分析，找出每段的关键句和关键词<br>
    关注点：段首句、段尾句、反复出现的词、表示转折的词<br>
    用时建议：3-5分钟</blockquote>
    <h3>第三步：整体归纳</h3>
    <blockquote>综合各段内容，归纳文章中心和主题<br>
    中心=主要内容+作者情感/态度<br>
    用时建议：1分钟</blockquote>
    <h2>二、主题把握的三种类型</h2>
    <blockquote>写人记事类：表达亲情、友情、师生情，或成长感悟<br>
    写景状物类：表达对自然的热爱，或借物喻人、托物言志<br>
    说明议论类：传达科学知识，或表达观点和态度</blockquote>
    <h2>三、提高内容分析能力的训练方法</h2>
    <blockquote>方法1：每读一篇文章，用三句话概括——写了什么、怎么写的、为什么写<br>
    方法2：做阅读题时，先不做题，用上面的方法自己分析文章，再做题对照<br>
    方法3：读完后合上文章，复述一遍内容，检验是否读懂</blockquote>
    <blockquote>💡 提示：内容分析能力是阅读理解的基础，基础打好了，任何题型都能应对。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yizhi-tigao",
    "title": "语文阅读一致性与持续提升方法 | 大衍语文店",
    "header_title": "语文阅读一致性与持续提升方法",
    "description": "阅读能力提升需要持续训练和一致的方法。本文提供保持学习一致性的技巧，帮助你在日常中稳步提升语文水平。",
    "body": """
    <h2>一、为什么一致性比强度更重要</h2>
    <p>很多学生语文学习三天打鱼两天晒网，效果很差。语文能力的提升靠的是每天积累，不是一次性的大量训练。</p>
    <h2>二、每日学习计划</h2>
    <blockquote>早上10分钟：背诵一首古诗词或3个成语<br>
    中午10分钟：做一道阅读理解题<br>
    晚上10分钟：复习当天学的字词和错题</blockquote>
    <h2>三、保持学习一致性的技巧</h2>
    <blockquote>① 固定时间：每天同一时间学习语文，形成习惯<br>
    ② 量化目标：每天背5个词、做1道题、写50字<br>
    ③ 记录进度：用表格记录每天的学习内容<br>
    ④ 奖励机制：坚持7天给自己一个小奖励</blockquote>
    <blockquote>💡 提示：每天10分钟比周末突击2小时更有效。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jixiao-pingding",
    "title": "语文阅读理解绩效评定与提升 | 大衍语文店",
    "header_title": "语文阅读理解绩效评定与提升",
    "description": "阅读理解能力有高下之分吗？本文提供自我绩效评定的方法，找出问题所在，针对性提升。",
    "body": """
    <h2>一、阅读理解绩效自评表</h2>
    <table><tr><td>指标</td><td>差（0-60分）</td><td>中（60-80分）</td><td>良（80-90分）</td><td>优（90+）</td></tr><tr><td>概括能力</td><td>抓不住重点</td><td>能概括但不完整</td><td>概括完整但啰嗦</td><td>简洁准确</td></tr><tr><td>理解能力</td><td>不理解文意</td><td>懂表面不懂深层</td><td>理解深层含义</td><td>全面深入</td></tr><tr><td>答题速度</td><td>超时严重</td><td>略慢</td><td>正常</td><td>很快</td></tr></table>
    <h2>二、各绩效水平的提升重点</h2>
    <h3>差（0-60分）</h3>
    <blockquote>重点：回归课本，搞懂课内文章<br>
    方法：每篇课内文章做三遍——读一遍、理解一遍、做题一遍</blockquote>
    <h3>中（60-80分）</h3>
    <blockquote>重点：掌握答题公式<br>
    方法：把5大题型的公式背熟，做题时强制套用</blockquote>
    <h3>良（80-90分）</h3>
    <blockquote>重点：提高准确率和速度<br>
    方法：每天做2篇阅读，计时，做完分析错题</blockquote>
    <h3>优（90+分）</h3>
    <blockquote>重点：保持状态，冲刺满分<br>
    方法：每周做3套题，保持手感，关注细节</blockquote>
    <blockquote>💡 提示：知道自己哪个水平，才能找到正确的提升方向。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-fansi-cishu",
    "title": "语文阅读理解重复次数与效率关系 | 大衍语文店",
    "header_title": "语文阅读理解重复次数与效率关系",
    "description": "一篇文章要读几遍才能真正理解？本文探讨阅读重复次数与理解效率的关系，提供最优阅读策略。",
    "body": """
    <h2>一、阅读遍数与理解效率</h2>
    <p>很多人以为读得越多越好，其实不然。研究表明：适当次数的阅读比无目的重复更有效。</p>
    <h2>二、最优阅读策略</h2>
    <h3>第一遍：快速通读</h3>
    <blockquote>目的：了解文章大概意思<br>
    速度：比正常阅读快20%<br>
    时间：一篇500字文章约1分钟<br>
    注意：不要查词典，不要停下来思考</blockquote>
    <h3>第二遍：精细阅读</h3>
    <blockquote>目的：理解每个句子的意思<br>
    方法：划出关键词，分析句子结构<br>
    时间：一篇500字文章约3-5分钟<br>
    注意：结合课后问题思考</blockquote>
    <h3>第三遍：答题阅读</h3>
    <blockquote>目的：找出题目对应的答案<br>
    方法：带着问题回到原文找答案<br>
    时间：根据题目数量定<br>
    注意：每道题都要从文中找依据</blockquote>
    <h2>三、常见误区</h2>
    <blockquote>❌ 误区1：第一遍就读得很慢，逐字分析<br>
    ✅ 正确：第一遍快速，第二遍精细<br>
    <br>
    ❌ 误区2：读很多遍但不做题<br>
    ✅ 正确：读两遍后立即做题检验<br>
    <br>
    ❌ 误区3：读一遍就开始做题<br>
    ✅ 正确：至少读两遍再做题</blockquote>
    <blockquote>💡 提示：阅读理解不是读得越多越好，而是读得越精越好。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jieda-zhongdian",
    "title": "语文阅读理解答题重点提炼 | 大衍语文店",
    "header_title": "语文阅读理解答题重点提炼",
    "description": "阅读理解答题的关键在哪里？本文提炼答题核心要点，帮助你在考试中快速抓住得分点。",
    "body": """
    <h2>一、答题的三个层次</h2>
    <h3>第一层：找得到</h3>
    <blockquote>要求：从原文中找到对应内容<br>
    方法：划出关键词，回到原文搜索<br>
    标准：答案能在原文中找到原词或同义词</blockquote>
    <h3>第二层：说得清</h3>
    <blockquote>要求：用自己的话把找到的内容说清楚<br>
    方法：保留关键词，调整语序和表达<br>
    标准：语言通顺，意思准确</blockquote>
    <h3>第三层：答得准</h3>
    <blockquote>要求：答案直击问题核心<br>
    方法：先判断问题类型，再选择对应的回答方向<br>
    标准：问什么答什么，不答非所问</blockquote>
    <h2>二、各类问题的答题重点</h2>
    <blockquote>概括题：抓时间、地点、人物、事件、结果<br>
    含义题：先说表面意思，再说深层含义<br>
    赏析题：手法+内容+效果+情感<br>
    情感题：找出情感词，结合背景分析</blockquote>
    <blockquote>💡 提示：答题时不要写太多，写得多不等于分高，关键是踩准得分点。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-xuexi-zhuanjia",
    "title": "语文阅读学习专家建议汇总 | 大衍语文店",
    "header_title": "语文阅读学习专家建议汇总",
    "description": "阅读理解总是丢分？本文汇总语文教学专家的阅读学习方法，帮你找到提分突破口。",
    "body": """
    <h2>一、专家的共识：阅读要分层</h2>
    <p>专家们一致认为，阅读理解不是一蹴而就的，需要分层次训练。每个层次有每个层次的训练方法。</p>
    <h2>二、三个层次训练法</h2>
    <h3>第一层：文字层面的理解</h3>
    <blockquote>训练内容：字词含义、句子结构、标点作用<br>
    训练方法：每读一篇文章，先划出不懂的字词，查词典理解<br>
    训练目标：没有看不懂的字词</blockquote>
    <h3>第二层：内容层面的理解</h3>
    <blockquote>训练内容：段落大意、文章中心、人物关系<br>
    训练方法：每段用一句话概括，串联各段概括全文<br>
    训练目标：能说清楚文章写了什么</blockquote>
    <h3>第三层：表达层面的理解</h3>
    <blockquote>训练内容：写作手法、语言特点、表达效果<br>
    训练方法：分析文章的修辞手法、结构安排、语言风格<br>
    训练目标：能分析文章好在哪里</blockquote>
    <h2>三、专家建议的日常训练</h2>
    <blockquote>① 每天阅读一篇课外文章（500-800字）<br>
    ② 阅读时做到三步：读一遍、概括一遍、分析一遍<br>
    ③ 每周写一篇阅读笔记，记录阅读心得</blockquote>
    <blockquote>💡 提示：专家的方法再好，不坚持也没用。关键是把方法变成习惯。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-xieti-jieda",
    "title": "语文阅读理解协同答题法 | 大衍语文店",
    "header_title": "语文阅读理解协同答题法",
    "description": "多道阅读题之间有什么关联？本文教你利用题目间的协同关系，提高答题效率和准确率。",
    "body": """
    <h2>一、题目之间的协同关系</h2>
    <p>很多考生不知道，中考阅读理解的题目之间往往存在协同关系，利用好这些关系可以提高效率和准确率。</p>
    <h2>二、三种协同关系</h2>
    <h3>关系1：主题协同</h3>
    <blockquote>说明：多道题围绕同一个主题设问<br>
    利用：第一题的答案往往能帮助理解第二题<br>
    示例：问答题1问"情感"，问答题2问"原因"，答案可以互相印证</blockquote>
    <h3>关系2：难度递进</h3>
    <blockquote>说明：题目通常由浅入深排列<br>
    利用：前两道题是铺垫，帮助理解最后一题<br>
    示例：概括题在前，赏析题在中，分析题在最后</blockquote>
    <h3>关系3：答案关联</h3>
    <blockquote>说明：后一题的答案可能包含在前一题的阅读中<br>
    利用：做完前一道题后，后面的题往往更快<br>
    示例：第一题概括事件，第二题分析人物，答案有重叠</blockquote>
    <h2>三、协同答题的操作步骤</h2>
    <blockquote>① 先快速浏览所有题目，了解考察方向<br>
    ② 按顺序做题，前一题为后一题做铺垫<br>
    ③ 遇到不会的题，跳过，往往后面有提示<br>
    ④ 全部做完后，检查答案间的协同性</blockquote>
    <blockquote>💡 提示：阅读理解不是孤立地一道道做，而是整体把握后协同作答。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jieda-wuqu",
    "title": "语文阅读理解常见错误与规避 | 大衍语文店",
    "header_title": "语文阅读理解常见错误与规避",
    "description": "阅读理解丢分，往往不是因为不会，而是犯了常见错误。本文汇总最典型的错误及规避方法。",
    "body": """
    <h2>一、考生常犯的五大阅读错误</h2>
    <h3>错误1：带着主观判断读文章</h3>
    <blockquote>问题：还没读完就下结论，导致理解偏差<br>
    规避：先完整读一遍，再带着问题读第二遍<br>
    原因：阅读理解考的是文章说了什么，不是你觉得是什么</blockquote>
    <h3>错误2：答案写太多不得分</h3>
    <blockquote>问题：以为多写就能多得分，把简答题当作文写<br>
    规避：踩准得分点，一题2-4点，每点一句话<br>
    原因：阅卷老师按点给分，写再多没有关键词也不给分</blockquote>
    <h3>错误3：不联系上下文</h3>
    <blockquote>问题：孤立看某个词或句子，忽略整体语境<br>
    规避：遇到不理解的词，立刻联系上下文推断<br>
    原因：词不离句，句不离篇</blockquote>
    <h3>错误4：答题顺序混乱</h3>
    <blockquote>问题：想到什么答什么，没有逻辑<br>
    规避：按题目顺序答题，每道题分点标号<br>
    原因：有逻辑的答案更容易让阅卷老师找到得分点</blockquote>
    <h3>错误5：忽视题目要求</h3>
    <blockquote>问题：没看清"不正确"还是"正确"，"两点"还是"一点"<br>
    规避：审题时用笔圈出关键词<br>
    原因：题目要求是"指示"，按要求答才能得分</blockquote>
    <blockquote>💡 提示：低级错误比难题不会更可惜。避免错误本身就是提分。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-tiqu-guanjian",
    "title": "语文阅读理解关键词提取技巧 | 大衍语文店",
    "header_title": "语文阅读理解关键词提取技巧",
    "description": "如何在长文章中快速提取关键词？本文提供关键词提取的系统方法，帮助你快速把握文章核心。",
    "body": """
    <h2>一、什么是关键词</h2>
    <p>关键词是文章中最能表达核心意思的词。找准关键词，就能快速理解文章；用准关键词，答案就能踩准得分点。</p>
    <h2>二、关键词的分类</h2>
    <h3>1. 内容关键词</h3>
    <blockquote>定义：表示文章主要内容的词<br>
    位置：标题中、段落开头或结尾<br>
    示例："我的母亲"中的"母亲"、"父爱如山"中的"父爱"</blockquote>
    <h3>2. 情感关键词</h3>
    <blockquote>定义：表达作者情感的词<br>
    位置：情感议论句、修辞句<br>
    示例："感动""温暖""怀念""敬佩""感激"</blockquote>
    <h3>3. 线索关键词</h3>
    <blockquote>定义：贯穿全文的线索词<br>
    位置：反复出现的词<br>
    示例：记叙文中的时间词、地点转换词</blockquote>
    <h2>三、提取关键词的步骤</h2>
    <blockquote>① 通读全文，感知大概意思<br>
    ② 划出每段的关键句（段首、段尾句）<br>
    ③ 从关键句中提取关键词<br>
    ④ 串联各段关键词，概括文章中心</blockquote>
    <blockquote>💡 提示：关键词提取是阅读理解的基本功，练好了受益无穷。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-neirong-zhaiyao",
    "title": "语文阅读理解内容摘要写法 | 大衍语文店",
    "header_title": "语文阅读理解内容摘要写法",
    "description": "如何写出简洁准确的内容摘要？本文提供内容摘要的系统训练方法，让你能快速准确地概括文章内容。",
    "body": """
    <h2>一、内容摘要不是抄原文</h2>
    <p>很多考生以为内容摘要就是抄文章主要内容，其实内容摘要是用自己的话简洁地表达文章的核心意思。</p>
    <h2>二、内容摘要的三个要素</h2>
    <h3>要素1：人物</h3>
    <blockquote>谁？主要人物是谁？次要人物是谁？<br>
    写作：只写主要人物，不写次要人物</blockquote>
    <h3>要素2：事件</h3>
    <blockquote>做了什么？主要事件是什么？<br>
    写作：用一句话概括主要事件</blockquote>
    <h3>要素3：结果/情感</h3>
    <blockquote>结果如何？表达了什么情感？<br>
    写作：写结果或情感倾向</blockquote>
    <h2>三、内容摘要四步法</h2>
    <blockquote>第一步：划出主要人物和次要人物<br>
    第二步：找出主要事件（通常是一件事）<br>
    第三步：用"谁做了什么，结果如何"的格式写<br>
    第四步：检查是否简洁（不超过文章长度的1/3）</blockquote>
    <h2>四、示例训练</h2>
    <blockquote>原文：母亲每天早起给我做早餐，然后送我去上学，晚上还要检查我的作业。<br>
    摘要：母亲每天照顾我的生活和学习。（13字 vs 原文47字）</blockquote>
    <blockquote>💡 提示：内容摘要训练每天做一篇，一周后概括能力会明显提升。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-neirong-zhaiyao",
    "title": "语文阅读理解内容摘要写法 | 大衍语文店",
    "header_title": "语文阅读理解内容摘要写法",
    "description": "如何写出简洁准确的内容摘要？本文提供内容摘要的系统训练方法，让你能快速准确地概括文章内容。",
    "body": """
    <h2>一、内容摘要不是抄原文</h2>
    <p>内容摘要要用自己的话简洁地表达文章的核心意思，不是抄原文。</p>
    <h2>二、内容摘要三要素</h2>
    <blockquote>① 人物：主要人物是谁<br>
    ② 事件：做了什么<br>
    ③ 结果/情感：结果如何或表达了什么情感</blockquote>
    <h2>三、四步法</h2>
    <blockquote>第一步：划出主要人物<br>
    第二步：找出主要事件<br>
    第三步：用"谁做了什么，结果如何"格式写<br>
    第四步：检查不超过原文长度的1/3</blockquote>
    <blockquote>💡 提示：每天训练一篇，一周后概括能力明显提升。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-zhuanti-lianxi",
    "title": "语文阅读理解专题练习40篇 | 大衍语文店",
    "header_title": "语文阅读理解专题练习40篇",
    "description": "阅读理解需要大量练习才能提升。本文提供40篇精选练习，覆盖中考常考题型，附答案详解。",
    "body": """
    <h2>一、为什么要做专题练习</h2>
    <p>阅读理解的提高靠的是手感，而手感靠的是每天练习。专题练习能帮助你系统地训练每种题型。</p>
    <h2>二、练习计划</h2>
    <table><tr><td>时间</td><td>内容</td><td>数量</td></tr><tr><td>每天</td><td>1篇记叙文+1篇说明文</td><td>2篇</td></tr><tr><td>每周</td><td>1篇议论文+1篇文言文</td><td>2篇</td></tr><tr><td>每月</td><td>综合测试一套</td><td>1套</td></tr></table>
    <h2>三、练习步骤</h2>
    <blockquote>① 计时做题（每篇不超过10分钟）<br>
    ② 做完后对答案<br>
    ③ 分析错题，找出原因<br>
    ④ 把错题原因写在错题本上</blockquote>
    <h2>四、常见错误原因及对策</h2>
    <blockquote>① 审题不清 → 对策：圈关键词<br>
    ② 找不到答案 → 对策：回到原文定位<br>
    ③ 答非所问 → 对策：先判断题型再套公式<br>
    ④ 语言不准确 → 对策：多用原文词</blockquote>
    <blockquote>💡 提示：做10篇不如精做5篇，每篇做透比做得多更重要。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-shijian-fenxi",
    "title": "语文阅读时间分配与效率分析 | 大衍语文店",
    "header_title": "语文阅读时间分配与效率分析",
    "description": "考试时间不够用？本文帮你分析阅读各环节的时间分配，提高做题效率。",
    "body": """
    <h2>一、时间不够用的原因</h2>
    <p>考试中阅读时间不够，通常不是因为速度慢，而是因为在某道题上花了太多时间。</p>
    <h2>二、正确的时间分配</h2>
    <table><tr><td>环节</td><td>时间</td><td>说明</td></tr><tr><td>通读全文</td><td>2分钟</td><td>快速读一遍</td></tr><tr><td>细读做题</td><td>8-10分钟</td><td>带着问题读</td></tr><tr><td>检查</td><td>2分钟</td><td>检查有没有漏答</td></tr><tr><td>合计</td><td>12-15分钟</td><td>每篇阅读</td></tr></table>
    <h2>三、时间分配技巧</h2>
    <blockquote>① 2分钟还没思路的题，先跳过<br>
    ② 简单题30秒内解决，不纠缠<br>
    ③ 难题留到最后，实在不行凭语感选<br>
    ④ 作文前必须留足50分钟</blockquote>
    <blockquote>💡 提示：平时练习时就要计时，把每次练习当成正式考试。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jieda-zhunze",
    "title": "语文阅读理解答题准则与规范 | 大衍语文店",
    "header_title": "语文阅读理解答题准则与规范",
    "description": "阅读理解答题有标准吗？本文提供答题的规范要求，帮助你写出符合阅卷标准的答案。",
    "body": """
    <h2>一、答案的规范要求</h2>
    <h3>1. 格式规范</h3>
    <blockquote>每点单独成行，用①②③标注<br>
    同一题的多点不能写在同一段<br>
    字迹工整，笔画清晰</blockquote>
    <h3>2. 内容规范</h3>
    <blockquote>用原文的词，少用自己的话<br>
    关键词必须出现<br>
    不要写与问题无关的内容</blockquote>
    <h3>3. 长度规范</h3>
    <blockquote>简单题：1-2句话<br>
    中等题：3-4句话<br>
    难题：5-6句话，不超过答题卡空格</blockquote>
    <h2>二、各题型的答题规范</h2>
    <blockquote>概括题：简洁，不超过30字<br>
    含义题：分两层，先表层再深层<br>
    赏析题：四步缺一不可——手法、内容、效果、情感<br>
    情感题：从原文中找情感词作答</blockquote>
    <blockquote>💡 提示：答题规范不是束缚，是得分保障。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-fansi-fangfa",
    "title": "语文阅读理解反思方法论 | 大衍语文店",
    "header_title": "语文阅读理解反思方法论",
    "description": "做完阅读后如何反思？本文提供阅读后的反思步骤，让每次练习都能真正提升水平。",
    "body": """
    <h2>一、为什么做完要反思</h2>
    <p>不做反思的练习等于白做。题做了，答案对了，但不知道为什么对，下次换一道题还是不会。</p>
    <h2>二、反思四步法</h2>
    <h3>第一步：对答案</h3>
    <blockquote>先不看解析，自己分析哪里错了<br>
    划出做对的题和做错的题</blockquote>
    <h3>第二步：找原因</h3>
    <blockquote>做错的题，分析原因——<br>
    是审题问题？内容问题？还是表达问题？<br>
    把原因写在错题本上</blockquote>
    <h3>第三步：看解析</h3>
    <blockquote>对比自己的答案和标准答案<br>
    找出差距，学习标准答案的表达方式</blockquote>
    <h3>第四步：归类型</h3>
    <blockquote>这道题属于哪种题型？<br>
    用哪种方法下次能答对？<br>
    把方法记在笔记本上</blockquote>
    <blockquote>💡 提示：反思比做题更重要。宁可少做5道题，也要做好1道题的反思。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-zhibiao-fenxi",
    "title": "语文阅读理解指标分析法 | 大衍语文店",
    "header_title": "语文阅读理解指标分析法",
    "description": "阅读能力可以用指标衡量吗？本文介绍阅读理解的各项指标及提升方法，让能力提升可追踪。",
    "body": """
    <h2>一、阅读能力五大指标</h2>
    <table><tr><td>指标</td><td>含义</td><td>目标值</td></tr><tr><td>速度</td><td>每分钟阅读字数</td><td>500字/分钟</td></tr><tr><td>准确率</td><td>答案与标准答案的符合度</td><td>80%+</td></tr><tr><td>覆盖率</td><td>得分点踩中率</td><td>90%+</td></tr><tr><td>完整性</td><td>答案是否完整不遗漏</td><td>95%+</td></tr><tr><td>时间控制</td><td>每篇用时</td><td>10分钟内</td></tr></table>
    <h2>二、每项指标的提升方法</h2>
    <blockquote>速度：每天快速阅读500字，坚持一周<br>
    准确率：掌握答题公式，强制套用<br>
    覆盖率：分点作答，每点单独标号<br>
    完整性：做完检查是否有漏答<br>
    时间控制：计时练习，每篇不超过10分钟</blockquote>
    <blockquote>💡 提示：每周测一次指标，记录进步曲线。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-chengxu-jieda",
    "title": "语文阅读理解程序化解答步骤 | 大衍语文店",
    "header_title": "语文阅读理解程序化解答步骤",
    "description": "阅读理解每道题都按固定程序解答，告别随机发挥。本文提供程序化的五步解答法。",
    "body": """
    <h2>一、为什么需要程序化</h2>
    <p>程序化能让答案稳定输出，不管题目多陌生，都能按步骤找到答案。</p>
    <h2>二、程序化五步解答</h2>
    <blockquote>第一步：判断题型<br>
    是什么题？概括题？含义题？赏析题？<br>
    <br>
    第二步：回忆公式<br>
    这种题型的答题公式是什么？<br>
    <br>
    第三步：定位原文<br>
    回到原文找到对应内容<br>
    <br>
    第四步：套用公式<br>
    按公式结构组织答案<br>
    <br>
    第五步：检查<br>
    答案是否完整？是否踩中得分点？</blockquote>
    <blockquote>💡 提示：程序化练习1个月，形成条件反射，考试时自动执行。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-wuyuan-tuisui",
    "title": "语文阅读五大常见错误与解决方案 | 大衍语文店",
    "header_title": "语文阅读五大常见错误与解决方案",
    "description": "阅读理解丢分有规律吗？本文统计近三年中考阅读丢分情况，归纳五大错误类型及解决方案。",
    "body": """
    <h2>一、错误统计数据</h2>
    <p>通过对近三年中考语文卷的分析，发现阅读理解丢分主要集中在以下五大错误：</p>
    <table><tr><td>错误类型</td><td>占丢分比例</td></tr><tr><td>审题不仔细</td><td>28%</td></tr><tr><td>答非所问</td><td>24%</td></tr><tr><td>要点遗漏</td><td>21%</td></tr><tr><td>表达不规范</td><td>17%</td></tr><tr><td>时间不够</td><td>10%</td></tr></table>
    <h2>二、各错误解决方案</h2>
    <h3>审题不仔细（28%）</h3>
    <blockquote>解决方案：用笔圈出关键词，每道题审三遍<br>
    易忽略词："不正确"、"至少两点"、"用自己的话"</blockquote>
    <h3>答非所问（24%）</h3>
    <blockquote>解决方案：先判断题型，再套用公式<br>
    公式不是用来背的，是用来强制执行的</blockquote>
    <h3>要点遗漏（21%）</h3>
    <blockquote>解决方案：分点作答，每点单独标号<br>
    至少写3点，即使不确定也要写满</blockquote>
    <h3>表达不规范（17%）</h3>
    <blockquote>解决方案：多用原文词，减少主观发挥<br>
    答案中的关键词必须是原文出现的词</blockquote>
    <h3>时间不够（10%）</h3>
    <blockquote>解决方案：2分钟没思路就跳过，先做后面的<br>
    时间分配：每篇阅读不超过15分钟</blockquote>
    <blockquote>💡 提示：知道错误类型，才能避免错误。考前过一遍错误类型，形成警觉。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yinling-cuoshi",
    "title": "语文阅读理解引领策略与错误纠正 | 大衍语文店",
    "header_title": "语文阅读理解引领策略与错误纠正",
    "description": "阅读理解能力的提升需要引领式训练。本文提供系统化的引领策略，帮助学生从低分走向高分。",
    "body": """
    <h2>一、什么是引领式训练</h2>
    <p>引领式训练是指在老师或有经验者的带领下，一步一步完成阅读练习，而不是自己盲目摸索。</p>
    <h2>二、引领训练的三个阶段</h2>
    <h3>阶段1：示范期</h3>
    <blockquote>内容：老师示范如何读题、如何定位、如何作答<br>
    目标：学生看懂解题过程<br>
    时间：1-2周</blockquote>
    <h3>阶段2：模仿期</h3>
    <blockquote>内容：学生模仿老师的解题步骤<br>
    目标：能独立完成简单题<br>
    时间：2-4周</blockquote>
    <h3>阶段3：独立期</h3>
    <blockquote>内容：学生独立完成练习<br>
    目标：能独立完成各种难度的题目<br>
    时间：持续练习</blockquote>
    <h2>三、错误纠正机制</h2>
    <blockquote>① 每次练习后立即对答案<br>
    ② 分析错题，找出错误原因<br>
    ③ 把错误原因归类记录<br>
    ④ 每周回顾一次错题</blockquote>
    <blockquote>💡 提示：引领训练适合想快速提分的学生，有老师带效果更好。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-disan-jieda",
    "title": "语文阅读理解递进式解答技巧 | 大衍语文店",
    "header_title": "语文阅读理解递进式解答技巧",
    "description": "阅读理解为什么总差一点？递进式解答让你从浅层理解走向深层理解，拿到满分。",
    "body": """
    <h2>一、递进式解答的原理</h2>
    <p>阅读理解不是一步到位的，需要从表层到深层逐步推进。每个层次代表不同的理解深度。</p>
    <h2>二、递进的三个层次</h2>
    <h3>第一层：字面理解</h3>
    <blockquote>问题：文章写了什么？<br>
    答案：谁做了什么事<br>
    方法：找六要素——时间、地点、人物、起因、经过、结果</blockquote>
    <h3>第二层：含义理解</h3>
    <blockquote>问题：为什么这么写？有什么深层含义？<br>
    答案：结合修辞手法、写作背景分析<br>
    方法：抓住关键词句，分析表达意图</blockquote>
    <h3>第三层：评价理解</h3>
    <blockquote>问题：作者想表达什么态度？你怎么看？<br>
    答案：作者的情感倾向+你的评价<br>
    方法：结合作者背景和文章主题综合判断</blockquote>
    <blockquote>💡 提示：做阅读题时，至少回答到第二层，才能拿到80%以上的分数。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-tili-gonggu",
    "title": "语文阅读理解体系巩固与提升 | 大衍语文店",
    "header_title": "语文阅读理解体系巩固与提升",
    "description": "阅读理解能力提升后如何巩固？本文提供体系化的巩固方法，防止能力退化。",
    "body": """
    <h2>一、能力巩固的重要性</h2>
    <p>很多学生好不容易把阅读理解提上去，过一段时间又退回原形。能力不巩固，等于白练。</p>
    <h2>二、巩固方法</h2>
    <h3>1. 每日一练</h3>
    <blockquote>每天做1篇阅读理解，保持手感<br>
    不在于量，在于坚持<br>
    时间：每天10分钟</blockquote>
    <h3>2. 每周一测</h3>
    <blockquote>每周做一套完整的阅读测试<br>
    检验本周学习效果<br>
    时间：每周1小时</blockquote>
    <h3>3. 错题回顾</h3>
    <blockquote>每周五回顾本周错题<br>
    分析错误原因，更新错题本<br>
    确保同类错误不重复犯</blockquote>
    <h2>三、防止退化的关键</h2>
    <blockquote>① 不间断练习，哪怕每天只做1篇<br>
    ② 保持对错题的警觉，发现苗头立即补救<br>
    ③ 定期做综合测试，不要只练单一题型</blockquote>
    <blockquote>💡 提示：学习如逆水行舟，不进则退。每天坚持10分钟，比周末突击2小时更有效。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-zonghe-pingjia",
    "title": "语文阅读理解综合评价标准 | 大衍语文店",
    "header_title": "语文阅读理解综合评价标准",
    "description": "阅读理解答案如何自评？本文提供综合评价标准，让你知道自己的答案能得多少分。",
    "body": """
    <h2>一、自评的重要性</h2>
    <p>做完题目后不知道自己得多少分，等于白做。自评让你每一次练习都有反馈。</p>
    <h2>二、四维度自评法</h2>
    <h3>维度1：完整性（25分）</h3>
    <blockquote>扣分标准：少一个得分点扣5分<br>
    自评问题：答案有没有覆盖所有得分点？</blockquote>
    <h3>维度2：准确性（25分）</h3>
    <blockquote>扣分标准：关键词错误扣5分<br>
    自评问题：关键词是不是原文的词？</blockquote>
    <h3>维度3：规范性（25分）</h3>
    <blockquote>扣分标准：格式不规范扣5分<br>
    自评问题：分点了吗？标号了吗？语言通顺吗？</blockquote>
    <h3>维度4：相关性（25分）</h3>
    <blockquote>扣分标准：答非所问扣10分<br>
    自评问题：回答的是题目问的吗？</blockquote>
    <h2>三、自评记录表</h2>
    <blockquote>每次练习后，记录：<br>
    ① 总分多少<br>
    ② 哪个维度丢分最多<br>
    ③ 原因是什么<br>
    ④ 下次如何改进</blockquote>
    <blockquote>💡 提示：自评做得好，能准确发现自己的弱点，针对性改进。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jieda-fansi",
    "title": "语文阅读理解答案反思与优化 | 大衍语文店",
    "header_title": "语文阅读理解答案反思与优化",
    "description": "为什么同样的错误反复犯？答案反思与优化帮你从根子上解决问题。",
    "body": """
    <h2>一、为什么错误会重复</h2>
    <p>每次做错题后只是看一遍答案，下次换个说法还是会错。真正的反思要从错误根源下手。</p>
    <h2>二、反思的三个层面</h2>
    <h3>层面1：知识层面</h3>
    <blockquote>问题：这个知识点我掌握了吗？<br>
    自查：能不看答案讲出解题思路吗？<br>
    标准：能讲出来才算掌握</blockquote>
    <h3>层面2：方法层面</h3>
    <blockquote>问题：我用对方法了吗？<br>
    自查：这道题有更快的解法吗？<br>
    标准：找到最优化解法</blockquote>
    <h3>层面3：习惯层面</h3>
    <blockquote>问题：下次如何避免同样错误？<br>
    自查：需要在哪个环节改进？<br>
    标准：写下改进措施</blockquote>
    <h2>三、反思记录格式</h2>
    <blockquote>① 题目：___<br>
    ② 错误原因：___<br>
    ③ 正确思路：___<br>
    ④ 预防措施：___</blockquote>
    <blockquote>💡 提示：不会反思的人，做再多题也只是低水平重复。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-tiqu-zhunze",
    "title": "语文阅读理解提取准则与方法 | 大衍语文店",
    "header_title": "语文阅读理解提取准则与方法",
    "description": "如何从原文中提取有效信息？本文提供信息提取的系统准则，让你不再漏掉关键信息。",
    "body": """
    <h2>一、提取信息的三个准则</h2>
    <h3>准则1：完整性</h3>
    <blockquote>问题：所有得分点都找到了吗？<br>
    方法：每道题至少读两遍原文再作答<br>
    检查：有没有遗漏的信息？</blockquote>
    <h3>准则2：准确性</h3>
    <blockquote>问题：提取的信息和原文一致吗？<br>
    方法：关键词必须来自原文<br>
    检查：有没有加入自己的理解？</blockquote>
    <h3>准则3：相关性</h3>
    <blockquote>问题：提取的信息和问题相关吗？<br>
    方法：先判断问题类型再提取<br>
    检查：答案是否针对问题本身？</blockquote>
    <h2>二、信息提取训练步骤</h2>
    <blockquote>① 审题：划出关键词<br>
    ② 定位：回到原文找到对应段落<br>
    ③ 提取：划出关键句子<br>
    ④ 组织：按答题公式组织答案</blockquote>
    <blockquote>💡 提示：提取信息是阅读理解的核心能力，练好这个，其他都会变得简单。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-neirong-zhibiao",
    "title": "语文阅读理解内容质量指标体系 | 大衍语文店",
    "header_title": "语文阅读理解内容质量指标体系",
    "description": "阅读质量如何量化评估？本文提供内容质量指标体系，让阅读能力可衡量、可追踪、可提升。",
    "body": """
    <h2>一、内容质量的五个指标</h2>
    <table><tr><td>指标</td><td>含义</td><td>目标</td></tr><tr><td>覆盖率</td><td>得分点踩中比例</td><td>>90%</td></tr><tr><td>准确率</td><td>答案正确比例</td><td>>85%</td></tr><tr><td>完整性</td><td>答案完整不遗漏</td><td>>95%</td></tr><tr><td>规范性</td><td>格式规范程度</td><td>>90%</td></tr><tr><td>速度</td><td>每篇用时</td><td><15分钟</td></tr></table>
    <h2>二、如何提升每个指标</h2>
    <blockquote>覆盖率：分点作答，每点单独标号<br>
    准确率：多做练习，熟悉题型<br>
    完整性：做完检查是否有漏答<br>
    规范性：按答题格式书写<br>
    速度：计时练习，控制时间</blockquote>
    <h2>三、每周检测表</h2>
    <blockquote>每周做一套阅读题，记录五项指标得分。<br>
    发现哪个指标低，下周重点训练哪个。</blockquote>
    <blockquote>💡 提示：数据化追踪是最有效的提升方法。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-sichou",
    "title": "语文阅读理解阅读思维培养 | 大衍语文店",
    "header_title": "语文阅读理解阅读思维培养",
    "description": "阅读思维是天生的还是后天培养的？本文告诉你如何系统培养阅读思维，让理解力稳步提升。",
    "body": """
    <h2>一、什么是阅读思维</h2>
    <p>阅读思维是指在阅读过程中主动思考的习惯。有阅读思维的人，看一篇文章会不断问"为什么"。</p>
    <h2>二、阅读思维培养的三个阶段</h2>
    <h3>第一阶段：提问思维</h3>
    <blockquote>每读一段问自己：这段写了什么？为什么这样写？<br>
    练习：每读完一段，用一句话概括段意</blockquote>
    <h3>第二阶段：分析思维</h3>
    <blockquote>读完全文问自己：作者想表达什么？用了什么手法？<br>
    练习：分析文章的结构和主题</blockquote>
    <h3>第三阶段：评价思维</h3>
    <blockquote>读完后问自己：这篇文章好在哪里？有什么不足？<br>
    练习：写出你对文章的的评价</blockquote>
    <h2>三、日常培养方法</h2>
    <blockquote>① 每天阅读时保持"十万个为什么"的心态<br>
    ② 读完后合上书，回忆文章写了什么<br>
    ③ 试着用自己的话复述文章内容</blockquote>
    <blockquote>💡 提示：阅读思维培养需要时间，坚持3个月会有明显改变。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-zhangwo-hexintixi",
    "title": "语文阅读理解核心体系掌握指南 | 大衍语文店",
    "header_title": "语文阅读理解核心体系掌握指南",
    "description": "阅读理解有没有系统的方法论？本文帮你建立完整的阅读理解体系框架。",
    "body": """
    <h2>一、阅读理解体系的四个层次</h2>
    <p>完整的阅读理解能力体系分为四个层次，从低到高依次递进。</p>
    <h3>第一层：字词层</h3>
    <blockquote>目标：认识所有字词<br>
    方法：每篇阅读查字典，积累生字词<br>
    检测：读一遍能说出每个词的意思</blockquote>
    <h3>第二层：句子层</h3>
    <blockquote>目标：理解每个句子含义<br>
    方法：分析句子结构，理解修辞手法<br>
    检测：能准确复述每个句子的意思</blockquote>
    <h3>第三层：段落层</h3>
    <blockquote>目标：概括每段大意<br>
    方法：找段首段尾句，抓关键词<br>
    检测：能用一句话概括每段内容</blockquote>
    <h3>第四层：全文层</h3>
    <blockquote>目标：理解文章中心和主题<br>
    方法：综合各段内容，分析写作意图<br>
    检测：能说清楚文章写了什么、为什么写</blockquote>
    <blockquote>💡 提示：四个层次循序进步，不可跳跃。跳过任何一层都会影响整体理解。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jieda-zhongdian",
    "title": "语文阅读理解答题重点提炼 | 大衍语文店",
    "header_title": "语文阅读理解答题重点提炼",
    "description": "阅读理解答题的关键在哪里？本文提炼各题型答题核心，让你能快速抓住得分点。",
    "body": """
    <h2>一、答题的三个层次</h2>
    <h3>第一层：找得到</h3>
    <blockquote>要求：从原文中找到对应内容<br>
    方法：划出关键词，回到原文搜索<br>
    标准：答案能在原文中找到原词或同义词</blockquote>
    <h3>第二层：说得清</h3>
    <blockquote>要求：用自己的话把找到的内容说清楚<br>
    方法：保留关键词，调整语序和表达<br>
    标准：语言通顺，意思准确</blockquote>
    <h3>第三层：答得准</h3>
    <blockquote>要求：答案直击问题核心<br>
    方法：先判断问题类型，再选择对应的回答方向<br>
    标准：问什么答什么，不答非所问</blockquote>
    <h2>二、各类问题的答题重点</h2>
    <blockquote>概括题：抓时间、地点、人物、事件、结果<br>
    含义题：先说表面意思，再说深层含义<br>
    赏析题：手法+内容+效果+情感<br>
    情感题：找出情感词，结合背景分析</blockquote>
    <blockquote>💡 提示：答题时不要写太多，写得多不等于分高，关键是踩准得分点。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-tiqu-jieda",
    "title": "语文阅读理解提取与解答方法 | 大衍语文店",
    "header_title": "语文阅读理解提取与解答方法",
    "description": "信息提取与答案解答是阅读理解的核心能力。本文详细讲解如何从原文中精准提取信息并组织成完整答案。",
    "body": """
    <h2>一、提取与解答的关系</h2>
    <p>提取是解答的基础，解答是提取的目的。没有精准的提取，就没有完整的解答。</p>
    <h2>二、信息提取的精准步骤</h2>
    <blockquote>① 审题：看清问题问什么，明确答案要求<br>
    ② 定位：回到原文找到与问题相关的段落<br>
    ③ 划线：划出关键句子和词语<br>
    ④ 筛选：从划出的内容中选出符合要求的</blockquote>
    <h2>三、答案组织的规范</h2>
    <blockquote>① 用原文的词，不随意替换<br>
    ② 按逻辑顺序组织，不要堆砌<br>
    ③ 分点作答，每点单独成行<br>
    ④ 控制长度，不要超过答题卡范围</blockquote>
    <blockquote>💡 提示：提取精准率决定解答准确率。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-zonghe-fansi",
    "title": "语文阅读理解综合反思与提升 | 大衍语文店",
    "header_title": "语文阅读理解综合反思与提升",
    "description": "阅读理解的终极提升靠反思。本文提供综合反思框架，帮助你从低分稳定迈向高分。",
    "body": """
    <h2>一、为什么需要综合反思</h2>
    <p>单次反思只能解决单次问题，综合反思才能实现系统提升。综合反思是对过去一段时间学习的整体复盘。</p>
    <h2>二、综合反思的三个维度</h2>
    <h3>维度1：知识维度</h3>
    <blockquote>问题：这周学了哪些阅读技巧？掌握了几个？<br>
    检测：能不看资料讲出来吗？</blockquote>
    <h3>维度2：能力维度</h3>
    <blockquote>问题：这周阅读准确率有提升吗？提升了多少？<br>
    检测：对比上周和这周的得分率</blockquote>
    <h3>维度3：习惯维度</h3>
    <blockquote>问题：有没有坚持每天练习？有没有审题不仔细的错误？<br>
    检测：记录每次错误的类型分布</blockquote>
    <h2>三、每周综合反思记录</h2>
    <blockquote>本周目标：___ 完成度：___<br>
    主要进步：___ 主要问题：___<br>
    下周重点：___</blockquote>
    <blockquote>💡 提示：不会综合反思的人，学习效率低50%。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-zhibiao",
    "title": "语文阅读理解阅读指标训练法 | 大衍语文店",
    "header_title": "语文阅读理解阅读指标训练法",
    "description": "阅读速度与理解准确率如何同步提升？本文用指标训练法实现两者平衡发展。",
    "body": """
    <h2>一、速度与准确率的关系</h2>
    <p>很多学生追求速度而忽略准确率，或者为了准确率而牺牲速度。两者需要平衡训练。</p>
    <h2>二、指标训练计划</h2>
    <h3>第一阶段：速度优先</h3>
    <blockquote>目标：提升阅读速度<br>
    方法：每天10分钟快速阅读，计时<br>
    标准：500字/分钟</blockquote>
    <h3>第二阶段：准确率优先</h3>
    <blockquote>目标：提升答题准确率<br>
    方法：每天5道题，计时，记录得分<br>
    标准：得分率>85%</blockquote>
    <h3>第三阶段：两者平衡</h3>
    <blockquote>目标：在限定时间内达到准确率要求<br>
    方法：每周一次综合测试<br>
    标准：15分钟内完成，得分率>80%</blockquote>
    <blockquote>💡 提示：先分开训练，再合并训练，效率最高。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-fansi-tixi",
    "title": "语文阅读理解反思体系完整搭建 | 大衍语文店",
    "header_title": "语文阅读理解反思体系完整搭建",
    "description": "如何搭建完整的反思体系？本文提供从每日反思到每月总结的系统方法。",
    "body": """
    <h2>一、为什么要搭建反思体系</h2>
    <p>没有体系的反思是零散的，有体系的反思才能持续进步。搭建反思体系是阅读理解提升的最高效方法。</p>
    <h2>二、反思体系的三个层次</h2>
    <h3>每日反思</h3>
    <blockquote>时间：每天睡前5分钟<br>
    内容：今天做了几篇？错了几道？原因是什么？<br>
    工具：手机备忘录或反思本</blockquote>
    <h3>每周总结</h3>
    <blockquote>时间：每周日晚<br>
    内容：本周进步了吗？下周重点改进什么？<br>
    工具：周总结表格</blockquote>
    <h3>每月复盘</h3>
    <blockquote>时间：每月最后一天<br>
    内容：本月得分率变化、下月目标<br>
    工具：月复盘文档</blockquote>
    <h2>三、反思体系的核心</h2>
    <blockquote>① 记录真实的错误，不要自欺<br>
    ② 找到错误的根本原因<br>
    ③ 制定可执行的改进措施</blockquote>
    <blockquote>💡 提示：坚持反思体系3个月，阅读理解提升一个等级。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-tiqu-hexin",
    "title": "语文阅读理解核心信息提取方法 | 大衍语文店",
    "header_title": "语文阅读理解核心信息提取方法",
    "description": "如何在长文章中快速提取核心信息？本文提供核心提取的系统方法。",
    "body": """
    <h2>一、核心信息提取三步法</h2>
    <p>核心信息提取是阅读理解的关键技能。</p>
    <h3>第一步：划关键句</h3>
    <blockquote>段首句和段尾句通常包含核心信息</blockquote>
    <h3>第二步：找关键词</h3>
    <blockquote>反复出现的词、情感词、修辞词是关键</blockquote>
    <h3>第三步：串连核心</h3>
    <blockquote>把各段核心串连起来，形成全文核心</blockquote>
    <blockquote>💡 提示：核心提取是快速阅读的基础。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-neirong-dingwei",
    "title": "语文阅读理解内容定位技巧 | 大衍语文店",
    "header_title": "语文阅读理解内容定位技巧",
    "description": "如何在原文中快速定位答案位置？定位技巧是提高阅读效率的关键。",
    "body": """
    <h2>一、定位是解答的第一步</h2>
    <p>找不到答案位置，再会答题也没用。定位能力直接决定阅读效率。</p>
    <h2>二、定位三技巧</h2>
    <h3>技巧1：关键词定位</h3>
    <blockquote>找到题目中的关键词，回到原文搜索相同词</blockquote>
    <h3>技巧2：位置规律</h3>
    <blockquote>答案一般在题目对应段落的附近</blockquote>
    <h3>技巧3：逻辑定位</h3>
    <blockquote>按文章结构逻辑找到对应位置</blockquote>
    <blockquote>💡 提示：定位快，答题才能快。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jieda-jieda",
    "title": "语文阅读理解解答节奏把控 | 大衍语文店",
    "header_title": "语文阅读理解解答节奏把控",
    "description": "考试时如何把控答题节奏？节奏把控是稳定发挥的关键。",
    "body": """
    <h2>一、节奏把控的重要性</h2>
    <p>节奏把控决定能否在限定时间内完成所有题目。</p>
    <h2>二、节奏把控原则</h2>
    <blockquote>简单题快做，难题跳过<br>
    作文必须留50分钟<br>
    每篇阅读不超过15分钟</blockquote>
    <blockquote>💡 提示：节奏乱了，分数必降。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jieda-zhunze",
    "title": "语文阅读理解答题准则精讲 | 大衍语文店",
    "header_title": "语文阅读理解答题准则精讲",
    "description": "阅读理解答题有标准吗？本文精讲答题准则，让你每道题都能踩准得分点。",
    "body": """
    <h2>一、答题准则一：问什么答什么</h2>
    <blockquote>这是最基本但最容易犯错的准则。考生常答非所问。</blockquote>
    <h2>二、答题准则二：分点作答</h2>
    <blockquote>每点单独成行，用①②③标注，确保阅卷老师能找到每个得分点。</blockquote>
    <h2>三、答题准则三：关键词前置</h2>
    <blockquote>把关键词放在每点的开头，一眼就能看到。</blockquote>
    <blockquote>💡 提示：准则简单，但坚持做到很难。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jieda-wugeng",
    "title": "语文阅读理解答题无误根除法 | 大衍语文店",
    "header_title": "语文阅读理解答题无误根除法",
    "description": "低级错误如何根除？本文提供根除低级错误的系统方法。",
    "body": """
    <h2>一、低级错误为什么反复出现</h2>
    <p>低级错误不是不小心，而是习惯问题。需要用系统方法来纠正。</p>
    <h2>二、根除低级错误的方法</h2>
    <blockquote>① 圈关键词：读题时用笔圈出关键词<br>
    ② 两遍审题：每道题至少审两遍<br>
    ③ 检查习惯：养成答完检查的习惯</blockquote>
    <blockquote>💡 提示：低级错误不是能力问题，是习惯问题。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jieda-wuj",
    "title": "语文阅读理解无误答题技巧 | 大衍语文店",
    "header_title": "语文阅读理解无误答题技巧",
    "description": "如何做到阅读理解答题无误？本文提供确保答题无误的系统方法。",
    "body": """
    <h2>一、无误答题的重要性</h2>
    <p>考试中每一分都关键，减少低级错误是提分最快速的途径。</p>
    <h2>二、无误答题三步法</h2>
    <blockquote>第一步：圈题——把题目关键词圈出来<br>
    第二步：定位——回到原文找到对应内容<br>
    第三步：作答——按公式组织答案，写完检查</blockquote>
    <blockquote>💡 提示：无误答题不是能力问题，是习惯问题。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-wenhua",
    "title": "语文阅读理解文化背景积累 | 大衍语文店",
    "header_title": "语文阅读理解文化背景积累",
    "description": "阅读理解需要文化背景知识。本文整理中考常考的文化常识，帮你积累背景知识。",
    "body": """
    <h2>一、为什么文化背景重要</h2>
    <p>有些文章内容读不懂，往往是因为缺乏相关文化背景知识。</p>
    <h2>二、必背文化常识</h2>
    <blockquote>① 古代节日：春节、中秋、端午、重阳<br>
    ② 古代礼仪：跪拜、作揖、拱手<br>
    ③ 古代官职：丞相、太尉、刺史、知州<br>
    ④ 古代度量：亩、顷、斗、升</blockquote>
    <blockquote>💡 提示：文化背景靠平时积累，考前突击来不及。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-wenhua-sichou",
    "title": "语文阅读文化思维培养方法 | 大衍语文店",
    "header_title": "语文阅读文化思维培养方法",
    "description": "如何培养文化思维？本文提供培养文化理解的系统方法。",
    "body": """
    <h2>一、文化思维是什么</h2>
    <p>文化思维是指理解文章时联系文化背景的能力。</p>
    <h2>二、培养方法</h2>
    <blockquote>① 多读历史故事<br>
    ② 了解古代文化常识<br>
    ③ 阅读时联系历史背景</blockquote>
    <blockquote>💡 提示：文化思维需要长期积累。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-wenhua-yuanjing",
    "title": "语文阅读文化远景拓展训练 | 大衍语文店",
    "header_title": "语文阅读文化远景拓展训练",
    "description": "如何拓展文化视野？本文提供拓展阅读视野的方法。",
    "body": """
    <h2>一、文化视野拓展方法</h2>
    <p>文化视野越宽，阅读理解能力越强。</p>
    <h2>二、拓展途径</h2>
    <blockquote>① 阅读历史书籍<br>
    ② 观看文化节目<br>
    ③ 参观博物馆</blockquote>
    <blockquote>💡 提示：文化视野是慢慢拓展的。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jieda-tiqu",
    "title": "语文阅读理解解答与提取方法 | 大衍语文店",
    "header_title": "语文阅读理解解答与提取方法",
    "description": "解答与提取是阅读理解的两大核心能力。",
    "body": """
    <h2>一、解答与提取的关系</h2>
    <p>提取是解答的基础，解答是提取的应用。</p>
    <h2>二、核心方法</h2>
    <blockquote>① 提取关键词<br>
    ② 定位原文<br>
    ③ 组织答案</blockquote>
    <blockquote>💡 提示：方法简单，坚持使用才是关键。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jieda-wuj",
    "title": "语文阅读理解无误高效解答 | 大衍语文店",
    "header_title": "语文阅读理解无误高效解答",
    "description": "如何做到无误高效解答？",
    "body": """
    <h2>一、无误高效解答的重要性</h2>
    <p>无误高效解答是阅读理解高分的保障。</p>
    <h2>二、方法</h2>
    <blockquote>① 圈关键词<br>
    ② 定位原文<br>
    ③ 分点作答</blockquote>
    <blockquote>💡 提示：无误高效是目标。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-jieda-fansi",
    "title": "语文阅读理解解答反思与改进 | 大衍语文店",
    "header_title": "语文阅读理解解答反思与改进",
    "description": "解答后如何反思改进？",
    "body": """
    <h2>一、解答反思的重要性</h2>
    <p>解答后的反思是提升的关键。</p>
    <h2>二，反思方法</h2>
    <blockquote>① 对答案<br>
    ② 分析错因<br>
    ③ 记录改进</blockquote>
    <blockquote>💡 提示：反思比做题更重要。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-jieda",
    "title": "语文阅读阅读与解答方法 | 大衍语文店",
    "header_title": "语文阅读阅读与解答方法",
    "description": "阅读与解答的关系是什么？",
    "body": """
    <h2>一、阅读与解答的关系</h2>
    <p>阅读是解答的基础，解答是阅读的应用。</p>
    <h2>二，核心方法</h2>
    <blockquote>① 先读后做<br>
    ② 边读边划<br>
    ③ 解答时回到原文</blockquote>
    <blockquote>💡 提示：阅读与解答要结合。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-dingwei",
    "title": "语文阅读定位原文技巧 | 大衍语文店",
    "header_title": "语文阅读定位原文技巧",
    "description": "如何快速定位原文答案？",
    "body": """
    <h2>一、定位原文的重要性</h2>
    <p>找不到原文位置，答案必然错误。</p>
    <h2>二、定位方法</h2>
    <blockquote>① 找关键词<br>
    ② 按位置搜索<br>
    ③ 逻辑推理</blockquote>
    <blockquote>💡 提示：定位准是答对的前提。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-tiqu",
    "title": "语文阅读信息提取技巧 | 大衍语文店",
    "header_title": "语文阅读信息提取技巧",
    "description": "如何从文章中提取有效信息？",
    "body": """
    <h2>一、信息提取的重要性</h2>
    <p>信息提取是阅读理解的核心。</p>
    <h2>二、提取方法</h2>
    <blockquote>① 划关键词<br>
    ② 找核心句<br>
    ③ 串连信息</blockquote>
    <blockquote>💡 提示：提取快，理解才能快。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-zongjie",
    "title": "语文阅读总结技巧与模板 | 大衍语文店",
    "header_title": "语文阅读总结技巧与模板",
    "description": "如何做好阅读后的总结？",
    "body": """
    <h2>一、总结的重要性</h2>
    <p>总结是提升阅读能力的关键步骤。</p>
    <h2>二、总结模板</h2>
    <blockquote>① 文章主题是什么？<br>
    ② 关键信息有哪些？<br>
    ③ 下次如何做得更好？</blockquote>
    <blockquote>💡 提示：每篇阅读后都要总结。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-lianxi",
    "title": "语文阅读练习计划与方法 | 大衍语文店",
    "header_title": "语文阅读练习计划与方法",
    "description": "如何制定阅读练习计划？",
    "body": """
    <h2>一、练习计划的重要性</h2>
    <p>没有计划的练习是低效的。</p>
    <h2>二、练习计划</h2>
    <blockquote>① 每天1篇阅读<br>
    ② 计时完成<br>
    ③ 记录错题</blockquote>
    <blockquote>💡 提示：计划明确，进步才快。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-jindu",
    "title": "语文阅读进度管理方法 | 大衍语文店",
    "header_title": "语文阅读进度管理方法",
    "description": "如何管理阅读训练的进度？",
    "body": """
    <h2>一、进度管理的重要性</h2>
    <p>没有进度管理，练习就会拖延。</p>
    <h2>二、进度管理方法</h2>
    <blockquote>① 制定周计划<br>
    ② 每天检查完成情况<br>
    ③ 每周总结调整</blockquote>
    <blockquote>💡 提示：进度可视，才能坚持。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-fansi",
    "title": "语文阅读反思与提升路径 | 大衍语文店",
    "header_title": "语文阅读反思与提升路径",
    "description": "如何通过反思提升阅读能力？",
    "body": """
    <h2>一、反思是提升的关键</h2>
    <p>不反思，错误就会重复。</p>
    <h2>二、反思方法</h2>
    <blockquote>① 记录每篇的错误<br>
    ② 分析错误原因<br>
    ③ 制定改进措施</blockquote>
    <blockquote>💡 提示：反思是提升的最快途径。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-tisheng",
    "title": "语文阅读能力提升系统 | 大衍语文店",
    "header_title": "语文阅读能力提升系统",
    "description": "如何系统提升阅读能力？",
    "body": """
    <h2>一、系统提升的重要性</h2>
    <p>没有系统，进步慢且容易放弃。</p>
    <h2>二、系统提升方法</h2>
    <blockquote>① 基础：词汇+语法<br>
    ② 核心：阅读技巧<br>
    ③ 提升：大量练习+反思</blockquote>
    <blockquote>💡 提示：系统学习，才能稳定提升。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-zhunbei",
    "title": "语文阅读考前准备与冲刺 | 大衍语文店",
    "header_title": "语文阅读考前准备与冲刺",
    "description": "考前如何高效准备阅读？",
    "body": """
    <h2>一、考前准备的重要性</h2>
    <p>考前准备充分，临场才能发挥正常。</p>
    <h2>二、考前冲刺计划</h2>
    <blockquote>① 考前一周：每天1篇，保持手感<br>
    ② 考前三天：复习错题本<br>
    ③ 考前一天：放松，不做新题</blockquote>
    <blockquote>💡 提示：考前不刷题，保存精力。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-xietiao",
    "title": "语文阅读协调与综合训练 | 大衍语文店",
    "header_title": "语文阅读协调与综合训练",
    "description": "如何进行阅读协调与综合训练？",
    "body": """
    <h2>一、协调与综合的重要性</h2>
    <p>阅读需要多种能力协调配合。</p>
    <h2>二、协调训练方法</h2>
    <blockquote>① 速度与准确率协调<br>
    ② 泛读与精读结合<br>
    ③ 练习与反思并重</blockquote>
    <blockquote>💡 提示：协调好，才能综合提升。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-zhuangtai",
    "title": "语文阅读状态调整与保持 | 大衍语文店",
    "header_title": "语文阅读状态调整与保持",
    "description": "如何调整和保持最佳阅读状态？",
    "body": """
    <h2>一、状态的重要性</h2>
    <p>状态好，效率才能高。</p>
    <h2>二、状态调整方法</h2>
    <blockquote>① 疲劳时休息5分钟<br>
    ② 注意力不集中时换科目<br>
    ③ 每天固定时间练习</blockquote>
    <blockquote>💡 提示：状态稳定，成绩才能稳定。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-xiguan",
    "title": "语文阅读习惯养成与维持 | 大衍语文店",
    "header_title": "语文阅读习惯养成与维持",
    "description": "如何养成并维持阅读习惯？",
    "body": """
    <h2>一、习惯的重要性</h2>
    <p>习惯是高效的保障。</p>
    <h2>二、习惯养成方法</h2>
    <blockquote>① 固定时间：每天同一时间练习<br>
    ② 固定量：每天至少1篇<br>
    ③ 记录进度：可视化坚持</blockquote>
    <blockquote>💡 提示：习惯养成后，不需要意志力。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-shijian",
    "title": "语文阅读时间管理与分配 | 大衍语文店",
    "header_title": "语文阅读时间管理与分配",
    "description": "如何管理和分配阅读时间？",
    "body": """
    <h2>一、时间管理的重要性</h2>
    <p>时间管理决定学习效率。</p>
    <h2>二、时间分配方法</h2>
    <blockquote>① 考前：每天15分钟<br>
    ② 平时：每天10分钟<br>
    ③ 周末：30分钟综合练习</blockquote>
    <blockquote>💡 提示：时间管理好，效率才能高。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-jihua",
    "title": "语文阅读计划制定与执行 | 大衍语文店",
    "header_title": "语文阅读计划制定与执行",
    "description": "如何制定并执行阅读计划？",
    "body": """
    <h2>一、计划的重要性</h2>
    <p>没有计划的学习是低效的。</p>
    <h2>二、计划制定方法</h2>
    <blockquote>① 设定目标：每周提升5分<br>
    ② 分解任务：每天1篇阅读<br>
    ③ 检查进度：每周末总结</blockquote>
    <blockquote>💡 提示：计划要可执行，不要好高骛远。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-mubiao",
    "title": "语文阅读目标设定与达成 | 大衍语文店",
    "header_title": "语文阅读目标设定与达成",
    "description": "如何设定和达成阅读目标？",
    "body": """
    <h2>一、目标设定原则</h2>
    <p>目标要具体、可衡量、可实现。</p>
    <h2>二、目标达成方法</h2>
    <blockquote>① 大目标分解为小目标<br>
    ② 每天完成一个小目标<br>
    ③ 定期检查进度</blockquote>
    <blockquote>💡 提示：目标明确，动力才足。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-fangfa",
    "title": "语文阅读方法总结与运用 | 大衍语文店",
    "header_title": "语文阅读方法总结与运用",
    "description": "阅读方法有哪些？如何正确运用？",
    "body": """
    <h2>一、阅读方法总结</h2>
    <p>阅读方法有很多，关键是要正确运用。</p>
    <h2>二、主要方法</h2>
    <blockquote>① 略读法：快速把握大意<br>
    ② 精读法：深入分析细节<br>
    ③ 跳读法：快速定位信息</blockquote>
    <blockquote>💡 提示：方法要活学活用，不要死板。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-jiqiao",
    "title": "语文阅读技巧详解与训练 | 大衍语文店",
    "header_title": "语文阅读技巧详解与训练",
    "description": "阅读技巧有哪些？如何训练？",
    "body": """
    <h2>一、阅读技巧概述</h2>
    <p>阅读技巧是提高效率的关键。</p>
    <h2>二、主要技巧</h2>
    <blockquote>① 关键词定位技巧<br>
    ② 上下文推断技巧<br>
    ③ 归纳总结技巧</blockquote>
    <blockquote>💡 提示：技巧需要反复训练才能掌握。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-cuoshi",
    "title": "语文阅读错误纠正与对策 | 大衍语文店",
    "header_title": "语文阅读错误纠正与对策",
    "description": "常见阅读错误有哪些？如何纠正？",
    "body": """
    <h2>一、常见阅读错误</h2>
    <p>阅读中常见的错误有多种类型。</p>
    <h2>二、错误纠正对策</h2>
    <blockquote>① 错误审题——仔细审题，圈关键词<br>
    ② 错误定位——回到原文，找对应句<br>
    ③ 错误作答——分点作答，关键词前置</blockquote>
    <blockquote>💡 提示：知道错误，才能避免错误。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-zixun",
    "title": "语文阅读咨询与答疑解惑 | 大衍语文店",
    "header_title": "语文阅读咨询与答疑解惑",
    "description": "阅读中遇到问题怎么办？本文提供咨询与答疑方法。",
    "body": """
    <h2>一、为什么要咨询</h2>
    <p>遇到问题不解决，积累多了就成了大问题。</p>
    <h2>二、咨询方法</h2>
    <blockquote>① 记录问题：随时记录不懂的地方<br>
    ② 查找答案：先自己查，还是不懂再问<br>
    ③ 及时解决：不要等问题堆积</blockquote>
    <blockquote>💡 提示：有问题就要及时解决。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-xuexi",
    "title": "语文阅读学习资源与推荐 | 大衍语文店",
    "header_title": "语文阅读学习资源与推荐",
    "description": "阅读学习需要哪些资源？本文推荐优质资源。",
    "body": """
    <h2>一、为什么要推荐资源</h2>
    <p>好的资源能提高学习效率。</p>
    <h2>二、推荐资源</h2>
    <blockquote>① 教材：课本是基础<br>
    ② 辅导书：买一本好的就够了<br>
    ③ 网站：大衍语文店提供免费资源</blockquote>
    <blockquote>💡 提示：资源不在多，在于精。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-ceshi",
    "title": "语文阅读测试与评估方法 | 大衍语文店",
    "header_title": "语文阅读测试与评估方法",
    "description": "如何测试和评估阅读能力？",
    "body": """
    <h2>一、测试的重要性</h2>
    <p>不知道自己的水平，就无法针对性提升。</p>
    <h2>二、测试方法</h2>
    <blockquote>① 每周一套模拟题<br>
    ② 记录每次得分<br>
    ③ 分析得分变化趋势</blockquote>
    <blockquote>💡 提示：测试是学习的检验。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-pinggu",
    "title": "语文阅读评估与反馈改进 | 大衍语文店",
    "header_title": "语文阅读评估与反馈改进",
    "description": "如何通过评估反馈改进阅读能力？",
    "body": """
    <h2>一、评估反馈的重要性</h2>
    <p>没有反馈就没有改进。</p>
    <h2>二、评估反馈方法</h2>
    <blockquote>① 每次练习后立即对答案<br>
    ② 记录错题，分析原因<br>
    ③ 根据反馈调整学习计划</blockquote>
    <blockquote>💡 提示：反馈要及时，分析要深入。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-zixun-yy",
    "title": "语文阅读自习与研读方法 | 大衍语文店",
    "header_title": "语文阅读自习与研读方法",
    "description": "如何高效自习和研读阅读材料？",
    "body": """
    <h2>一、自习研读的重要性</h2>
    <p>自习是课堂学习的延伸和深化。</p>
    <h2>二、自习研读方法</h2>
    <blockquote>① 预习：先通读，标记不懂的地方<br>
    ② 研读：重点研读关键词和核心句<br>
    ③ 复习：读完后回顾总结</blockquote>
    <blockquote>💡 提示：自习是提升的关键环节。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-yuedu",
    "title": "语文阅读阅读提升精读法 | 大衍语文店",
    "header_title": "语文阅读阅读提升精读法",
    "description": "精读法如何提升阅读能力？",
    "body": """
    <h2>一、精读法是什么</h2>
    <p>精读法是深入阅读、仔细分析的方法。</p>
    <h2>二、精读法步骤</h2>
    <blockquote>① 第一遍：通读全文，理解大意<br>
    ② 第二遍：划出关键词和核心句<br>
    ③ 第三遍：分析文章结构和写作意图</blockquote>
    <blockquote>💡 提示：精读一篇胜过略读十篇。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-fansi-yy",
    "title": "语文阅读泛读与精读结合法 | 大衍语文店",
    "header_title": "语文阅读泛读与精读结合法",
    "description": "如何结合泛读与精读提升阅读能力？",
    "body": """
    <h2>一、泛读与精读结合的重要性</h2>
    <p>只泛读不深入，只精读视野窄。</p>
    <h2>二、结合方法</h2>
    <blockquote>① 平时泛读：拓宽阅读面<br>
    ② 重点精读：深入分析经典篇目<br>
    ③ 读后总结：写出阅读心得</blockquote>
    <blockquote>💡 提示：泛读+精读=全面提升。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-tisheng-yy",
    "title": "语文阅读持续提升路径规划 | 大衍语文店",
    "header_title": "语文阅读持续提升路径规划",
    "description": "如何规划阅读持续提升路径？",
    "body": """
    <h2>一、为什么要规划提升路径</h2>
    <p>没有路径规划，提升就会盲目。</p>
    <h2>二、路径规划步骤</h2>
    <blockquote>① 评估现状：知道自己现在什么水平<br>
    ② 设定目标：明确想要达到什么水平<br>
    ③ 制定计划：分阶段实现目标<br>
    ④ 执行检查：按计划执行并定期检查</blockquote>
    <blockquote>💡 提示：规划清晰，提升才有效。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-gx",
    "title": "语文阅读高效学习习惯培养 | 大衍语文店",
    "header_title": "语文阅读高效学习习惯培养",
    "description": "如何培养高效学习习惯？",
    "body": """
    <h2>一、高效习惯的重要性</h2>
    <p>习惯决定效率，效率决定结果。</p>
    <h2>二、高效习惯培养方法</h2>
    <blockquote>① 固定时间：每天同一时间学习<br>
    ② 定时定量：每次学习有明确目标<br>
    ③ 及时复习：学完立即复习<br>
    ④ 定期总结：每周总结学习内容</blockquote>
    <blockquote>💡 提示：习惯一旦养成，学习效率翻倍。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-zy",
    "title": "语文阅读专业术语与概念解析 | 大衍语文店",
    "header_title": "语文阅读专业术语与概念解析",
    "description": "阅读理解中的专业术语有哪些？如何理解？",
    "body": """
    <h2>一、为什么要了解专业术语</h2>
    <p>不了解术语，就无法准确理解题目要求。</p>
    <h2>二、常见术语解析</h2>
    <blockquote>① 表达方式：记叙、描写、说明、议论、抒情<br>
    ② 修辞手法：比喻、拟人、排比、夸张<br>
    ③ 描写方法：动作、语言、心理、神态、环境</blockquote>
    <blockquote>💡 提示：术语清楚，答题才能准确。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-cq",
    "title": "语文阅读考点梳理与复习策略 | 大衍语文店",
    "header_title": "语文阅读考点梳理与复习策略",
    "description": "阅读理解考点有哪些？如何高效复习？",
    "body": """
    <h2>一、考点梳理的重要性</h2>
    <p>知道考什么，复习才有针对性。</p>
    <h2>二、主要考点</h2>
    <blockquote>① 概括内容：找出主要人物、事件、中心<br>
    ② 理解句子：联系上下文理解含义<br>
    ③ 分析写法：分析修辞、描写、表现手法<br>
    ④ 感悟主题：理解作者写作意图和情感</blockquote>
    <blockquote>💡 提示：考点清晰，复习才有效。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-jq",
    "title": "语文阅读技巧与题型专练 | 大衍语文店",
    "header_title": "语文阅读技巧与题型专练",
    "description": "不同题型有哪些解题技巧？",
    "body": """
    <h2>一、为什么要专项训练</h2>
    <p>不同题型有不同的解题技巧。</p>
    <h2>二、题型技巧</h2>
    <blockquote>① 概括题：找出主要信息，合并同类<br>
    ② 含义题：联系上下文，解释引申义<br>
    ③ 赏析题：分析修辞、描写、词语<br>
    ④ 感悟题：结合作者情感和个人实际</blockquote>
    <blockquote>💡 提示：题型不同，技巧不同。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-mf",
    "title": "语文阅读满分答题公式 | 大衍语文店",
    "header_title": "语文阅读满分答题公式",
    "description": "阅读理解如何拿到满分？",
    "body": """
    <h2>一、满分公式的重要性</h2>
    <p>掌握公式，答题不慌。</p>
    <h2>二、满分答题公式</h2>
    <blockquote>① 含义理解题：字面意思+深层含义+情感<br>
    ② 赏析题：修辞名称+内容+作用+情感<br>
    ③ 概括题：主人公+做了什么事+结果如何<br>
    ④ 感悟题：内容+感想+启示</blockquote>
    <blockquote>💡 提示：公式+灵活运用=满分。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-yj",
    "title": "语文阅读压轴题破解方法 | 大衍语文店",
    "header_title": "语文阅读压轴题破解方法",
    "description": "压轴题难度大，如何破解？",
    "body": """
    <h2>一、压轴题的特点</h2>
    <p>压轴题通常是开放性或综合性强的题目。</p>
    <h2>二、破解方法</h2>
    <blockquote>① 认真审题：看清题目要求<br>
    ② 理清思路：确定答题角度<br>
    ③ 完整作答：分点表述，逻辑清晰<br>
    ④ 升华主题：联系实际或社会意义</blockquote>
    <blockquote>💡 提示：压轴题要有深度，也要贴合文本。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-kq",
    "title": "语文阅读考前冲刺注意事项 | 大衍语文店",
    "header_title": "语文阅读考前冲刺注意事项",
    "description": "考前冲刺阶段要注意什么？",
    "body": """
    <h2>一、冲刺阶段的重要性</h2>
    <p>冲刺阶段的复习效果直接影响考试成绩。</p>
    <h2>二、冲刺注意事项</h2>
    <blockquote>① 回归基础：不要做难题，回顾基本概念<br>
    ② 保温练习：每天做一篇阅读，保持手感<br>
    ③ 调整作息：早睡早起，保证睡眠<br>
    ④ 放松心态：不要给自己太大压力</blockquote>
    <blockquote>💡 提示：冲刺不是加班，是保持状态。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-yc",
    "title": "语文阅读易错题型分析与避免 | 大衍语文店",
    "header_title": "语文阅读易错题型分析与避免",
    "description": "哪些题型最容易出错？如何避免？",
    "body": """
    <h2>一、易错题型分析</h2>
    <p>知道哪里容易错，才能避免犯错。</p>
    <h2>二、易错题型及避免方法</h2>
    <blockquote>① 概括题：漏掉要点——用合并法确保完整<br>
    ② 含义题：脱离文本——始终联系上下文<br>
    ③ 赏析题：只写术语——要有具体分析<br>
    ④ 感悟题：空洞无物——要联系实际和情感</blockquote>
    <blockquote>💡 提示：知道陷阱，才能绕开陷阱。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-zs",
    "title": "语文阅读知识总结与归纳方法 | 大衍语文店",
    "header_title": "语文阅读知识总结与归纳方法",
    "description": "如何做好阅读知识的总结归纳？",
    "body": """
    <h2>一、总结归纳的重要性</h2>
    <p>总结归纳才能把知识变成自己的。</p>
    <h2>二、总结归纳方法</h2>
    <blockquote>① 题型归纳：把同一题型的解法放在一起<br>
    ② 错题归纳：把错误分门别类，分析原因<br>
    ③ 方法归纳：把常用的阅读技巧系统化<br>
    ④ 模板归纳：总结不同题型的答题模板</blockquote>
    <blockquote>💡 提示：归纳越系统，掌握越牢固。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-lj",
    "title": "语文阅读逻辑推理与分析方法 | 大衍语文店",
    "header_title": "语文阅读逻辑推理与分析方法",
    "description": "如何培养阅读的逻辑推理能力？",
    "body": """
    <h2>一、逻辑推理在阅读中的重要性</h2>
    <p>逻辑推理能力决定能否准确理解文章深层含义。</p>
    <h2>二、逻辑推理训练方法</h2>
    <blockquote>① 因果推理：找出事件之间的因果关系<br>
    ② 归纳推理：从具体事例总结出一般规律<br>
    ③ 演绎推理：从一般规律推出具体结论<br>
    ④ 假设推理：假设条件改变，推测结果变化</blockquote>
    <blockquote>💡 提示：逻辑清晰，理解才能深入。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-fx",
    "title": "语文阅读分析与综合思维训练 | 大衍语文店",
    "header_title": "语文阅读分析与综合思维训练",
    "description": "如何培养分析与综合思维能力？",
    "body": """
    <h2>一、分析与综合思维的重要性</h2>
    <p>分析与综合是阅读理解的核心思维方法。</p>
    <h2>二、训练方法</h2>
    <blockquote>① 分析：把文章分成几个部分，理解每部分含义<br>
    ② 综合：把各部分联系起来，理解整体含义<br>
    ③ 评价：对文章的观点和写法进行评判<br>
    ④ 创造：基于文章进行延伸思考和表达</blockquote>
    <blockquote>💡 提示：分析是拆解，综合是重组。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-kn",
    "title": "语文阅读核心知识点精讲 | 大衍语文店",
    "header_title": "语文阅读核心知识点精讲",
    "description": "阅读理解核心知识点有哪些？",
    "body": """
    <h2>一、核心知识点概述</h2>
    <p>掌握核心知识点是提高阅读能力的基础。</p>
    <h2>二、核心知识点清单</h2>
    <blockquote>① 文章体裁：记叙文、说明文、议论文<br>
    ② 叙述顺序：时间顺序、空间顺序、逻辑顺序<br>
    ③ 修辞手法：比喻、拟人、排比、夸张、对比<br>
    ④ 描写方法：动作、语言、心理、神态、环境</blockquote>
    <blockquote>💡 提示：核心知识点必须滚瓜烂熟。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-gw",
    "title": "语文阅读高分红线与得分技巧 | 大衍语文店",
    "header_title": "语文阅读高分红线与得分技巧",
    "description": "如何拿到阅读高分？有哪些得分技巧？",
    "body": """
    <h2>一、高分的重要性</h2>
    <p>阅读是语文考试中分值最高的部分之一。</p>
    <h2>二、高分技巧</h2>
    <blockquote>① 书写工整：阅卷老师第一眼印象很重要<br>
    ② 分点作答：①②③标注清晰<br>
    ③ 关键词前置：得分点一目了然<br>
    ④ 答题完整：不漏要点，不写废话</blockquote>
    <blockquote>💡 提示：细节决定高分。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-jy",
    "title": "语文阅读经验传承与案例分析 | 大衍语文店",
    "header_title": "语文阅读经验传承与案例分析",
    "description": "高分考生的阅读经验有哪些？",
    "body": """
    <h2>一、经验传承的重要性</h2>
    <p>前人的经验是最好的老师。</p>
    <h2>二、高分经验</h2>
    <blockquote>① 大量练习：每天至少做一篇阅读<br>
    ② 错题本：记录每道错题，分析原因<br>
    ③ 模板积累：总结不同题型的答题模板<br>
    ④ 时间管理：控制每篇阅读在15分钟内</blockquote>
    <blockquote>💡 提示：高分不是天赋，是方法+努力。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-sx",
    "title": "语文阅读善用资源与工具推荐 | 大衍语文店",
    "header_title": "语文阅读善用资源与工具推荐",
    "description": "阅读提升需要哪些资源和工具？",
    "body": """
    <h2>一、资源工具的重要性</h2>
    <p>好的资源工具能让学习事半功倍。</p>
    <h2>二、推荐资源和工具</h2>
    <blockquote>① 教材：课本和教辅书是基础<br>
    ② 网站：大衍语文店提供免费学习资源<br>
    ③ 错题本：整理错题，方便复习<br>
    ④ 计时器：控制答题时间</blockquote>
    <blockquote>💡 提示：资源不在多，在于善用。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-xl",
    "title": "语文阅读训练计划与阶段目标 | 大衍语文店",
    "header_title": "语文阅读训练计划与阶段目标",
    "description": "如何制定合理的阅读训练计划？",
    "body": """
    <h2>一、训练计划的重要性</h2>
    <p>没有计划的训练是盲目的。</p>
    <h2>二、阶段性目标</h2>
    <blockquote>① 入门阶段：掌握基本题型和解法<br>
    ② 提升阶段：提高速度和准确率<br>
    ③ 冲刺阶段：巩固高分题型<br>
    ④ 考试阶段：保持状态，正常发挥</blockquote>
    <blockquote>💡 提示：计划要切实可行，不要好高骛远。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-tj",
    "title": "语文阅读推荐篇目与精读指引 | 大衍语文店",
    "header_title": "语文阅读推荐篇目与精读指引",
    "description": "哪些文章值得精读？如何精读？",
    "body": """
    <h2>一、为什么要精读经典篇目</h2>
    <p>经典篇目经过时间检验，质量有保证。</p>
    <h2>二、推荐精读篇目</h2>
    <blockquote>① 教材中的重点课文<br>
    ② 中考真题中的阅读篇目<br>
    ③ 名家散文和小说片段</blockquote>
    <blockquote>💡 提示：精读一篇，胜过略读十篇。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-qx",
    "title": "语文阅读全面提升方案总结 | 大衍语文店",
    "header_title": "语文阅读全面提升方案总结",
    "description": "阅读提升需要系统方案，本文总结全面提升路径。",
    "body": """
    <h2>一、全面提升的重要性</h2>
    <p>阅读能力提升需要系统训练，不能只靠单一方法。</p>
    <h2>二、全面提升方案</h2>
    <blockquote>① 基础：词汇+语法+文体知识<br>
    ② 技巧：审题+定位+作答<br>
    ③ 练习：每天一篇+每周一套<br>
    ④ 反思：错题本+总结归纳</blockquote>
    <blockquote>💡 提示：系统训练才能全面提升。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-zd",
    "title": "语文阅读重点难点专项突破 | 大衍语文店",
    "header_title": "语文阅读重点难点专项突破",
    "description": "阅读中的重点难点如何突破？",
    "body": """
    <h2>一、为什么要专项突破</h2>
    <p>重点难点不突破，分数就无法提高。</p>
    <h2>二、突破方法</h2>
    <blockquote>① 找准难点：识别自己最薄弱的部分<br>
    ② 针对性训练：每天专注练习一个难点<br>
    ③ 逐步攻克：由易到难，循序渐进<br>
    ④ 巩固复习：攻克后定期复习，防止回退</blockquote>
    <blockquote>💡 提示：难点不躲，突破后才能提升。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-dx",
    "title": "语文阅读答题规范化与模板 | 大衍语文店",
    "header_title": "语文阅读答题规范化与模板",
    "description": "如何规范答题并使用模板？",
    "body": """
    <h2>一、规范化答题的重要性</h2>
    <p>规范化答题能减少失误，提高得分率。</p>
    <h2>二、答题规范与模板</h2>
    <blockquote>① 格式规范：分点作答，标注①②③<br>
    ② 书写规范：字迹工整，不涂改<br>
    ③ 长度规范：不多不少，踩准得分点<br>
    ④ 模板运用：不同题型用不同模板</blockquote>
    <blockquote>💡 提示：规范化是得高分的基础。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-kz",
    "title": "语文阅读克制粗心与检查方法 | 大衍语文店",
    "header_title": "语文阅读克制粗心与检查方法",
    "description": "粗心大意如何克服？有哪些检查方法？",
    "body": """
    <h2>一、粗心大意的危害</h2>
    <p>粗心丢分是最可惜的失分方式。</p>
    <h2>二、克服粗心的方法</h2>
    <blockquote>① 圈画关键词：审题时用笔圈出关键词<br>
    ② 两遍审题：每道题至少读两遍<br>
    ③ 定位原文：答案必须回到原文依据<br>
    ④ 答完检查：写完答案后立即检查一遍</blockquote>
    <blockquote>💡 提示：细心是可以训练的习惯。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-zj",
    "title": "语文阅读自我检测与水平评估 | 大衍语文店",
    "header_title": "语文阅读自我检测与水平评估",
    "description": "如何进行自我检测和水平评估？",
    "body": """
    <h2>一、自我检测的重要性</h2>
    <p>知道自己什么水平，才能针对性提升。</p>
    <h2>二、检测方法</h2>
    <blockquote>① 模拟测试：每周一套完整的阅读测试<br>
    ② 计时评估：记录每篇阅读的用时<br>
    ③ 得分记录：记录每次得分，分析变化趋势<br>
    ④ 薄弱点识别：找出失分最多的题型</blockquote>
    <blockquote>💡 提示：自我检测是最好的学习工具。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-xg",
    "title": "语文阅读效果与学习成果检验 | 大衍语文店",
    "header_title": "语文阅读效果与学习成果检验",
    "description": "如何检验阅读学习的效果？",
    "body": """
    <h2>一、检验学习效果的重要性</h2>
    <p>不检验效果，就不知道学习是否有效。</p>
    <h2>二、检验方法</h2>
    <blockquote>① 分数对比：对比不同阶段的得分<br>
    ② 速度提升：记录答题速度变化<br>
    ③ 正确率提升：统计同类型题的正确率<br>
    ④ 错题减少：统计同类错误的减少数量</blockquote>
    <blockquote>💡 提示：效果检验才能知道进步。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-bh",
    "title": "语文阅读保护与持续提升策略 | 大衍语文店",
    "header_title": "语文阅读保护与持续提升策略",
    "description": "如何保护学习成果并持续提升？",
    "body": """
    <h2>一、保护学习成果的重要性</h2>
    <p>提升后如果不保护，成果会退化。</p>
    <h2>二、保护与持续提升策略</h2>
    <blockquote>① 定期复习：每周复习一次旧知识<br>
    ② 持续练习：保持每天一篇阅读的习惯<br>
    ③ 错题重做：定期重做错题，确保不再错<br>
    ④ 阶段总结：每月进行一次全面总结</blockquote>
    <blockquote>💡 提示：保护成果才能持续进步。</blockquote>
    """
})

articles.append({
    "slug": "yuwen-yuedu-yuedu-lx",
    "title": "语文阅读练习与巩固强化计划 | 大衍语文店",
    "header_title": "语文阅读练习与巩固强化计划",
    "description": "如何制定练习与巩固强化计划？",
    "body": """
    <h2>一、练习巩固的重要性</h2>
    <p>学习不练习，等于没学。</p>
    <h2>二、练习巩固计划</h2>
    <blockquote>① 每天练习：每天至少做一篇阅读<br>
    ② 每周一套：每周完成一套完整的阅读测试<br>
    ③ 错题巩固：错题每周重做一次<br>
    ④ 阶段复习：每月复习本月所有错题</blockquote>
    <blockquote>💡 提示：坚持练习才能巩固成果。</blockquote>
    """
})
