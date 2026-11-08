# 主题与页面地图

本表用于说明站点如何把相近搜索意图归并到可持续维护的主页面。它不是关键词堆砌清单；每个页面都应提供独立问题、可核对资料和明确边界。

统一入口：[专题导航](https://jiedianshouce.com/topics/)

| 主题 | 主要搜索意图 | 主页面 |
| --- | --- | --- |
| 免费节点 | 今日免费节点、Clash/Mihomo 配置、历史测试 | [免费节点](https://jiedianshouce.com/free-nodes/) |
| 免费节点历史 | 日期、数量、地区、丢包和测速证据 | [历史归档](https://jiedianshouce.com/free-nodes/archive/) |
| 机场推荐 | 价格、流量、倍率、周期与公开证据 | [机场评级](https://jiedianshouce.com/airports/) |
| 机场评级 | 品牌历史资料、评级口径与核验状态 | [机场评级](https://jiedianshouce.com/airports/) |
| 枫叶机场 | 枫叶 Maple Relay 品牌评测、套餐记录与公开入口 | [枫叶机场完整评测](https://jiedianshouce.com/airports/maple-relay/) |
| 机场选购方法 | 把最低付款额、倍率后流量、有效期和退款规则放到同一口径比较 | [机场推荐选购指南](https://jiedianshouce.com/articles/airport-recommendation-guide/) |
| 新手连接入口 | 从选择付费服务或临时免费节点，到客户端、订阅导入与首次验证 | [第一次连接](https://jiedianshouce.com/start/) |
| 机场历史条件筛选 | 按旧价格与流量缩小资料候选，现行套餐另行核对 | [节点罗盘](https://jiedianshouce.com/airport-selector/) |
| 家宽机场 | 住宅 IP、机房 IP、ASN 与标签核验 | [家宽住宅 IP 专题](https://jiedianshouce.com/articles/residential-ip-airports/) |
| 机场支付 | 支付宝、微信、USDT、PayPal 与退款风险 | [支付方式专题](https://jiedianshouce.com/articles/airport-payment-methods/) |
| 套餐选择 | 月付、按量付费、低倍率与总成本 | [按量付费专题](https://jiedianshouce.com/articles/monthly-or-usage/) |
| 地区节点 | 香港、日本、新加坡、美国节点怎么选 | [节点地区选择](https://jiedianshouce.com/articles/choose-node-region/) |
| 线路测试 | CN2、BGP、中转、直连、晚高峰、低延迟 | [晚高峰测试](https://jiedianshouce.com/articles/peak-hour-airport-test/) |
| 客户端导入 | Clash、Clash Verge、v2rayN 与订阅导入 | [客户端选择与导入](https://jiedianshouce.com/articles/clash-v2rayn-subscription-import/) |
| Clash Verge Rev 故障 | 无法选择配置、Socket错误、内核启动和端口占用 | [Clash Verge Rev Socket错误排查](https://jiedianshouce.com/articles/clash-verge-rev-cannot-select-profile-socket-error/) |
| Clash Verge Rev 系统 DNS 报错 | set system dns failed、exit code 1、系统代理开启失败 | [系统 DNS 写入失败排查](https://jiedianshouce.com/articles/clash-verge-rev-set-system-dns-failed-exit-code-1/) |
| Clash Verge Rev TUN接管后断网 | 同节点系统代理可用、仅TUN接管失败时排查服务、接口、路由与DNS | [TUN无法上网排查](https://jiedianshouce.com/articles/clash-verge-rev-tun-not-working/) |
| 订阅更新失败 | HTTP错误、空内容、格式不兼容与缓存问题 | [订阅更新失败排查](https://jiedianshouce.com/articles/subscription-update-errors/) |
| Clash Verge Rev 远程配置 YAML 精确报错 | 更新远程配置时 `the remote profile data is invalid yaml`，区分 HTTP、解析和缺字段阶段 | [Clash Verge Rev invalid yaml 排查](https://jiedianshouce.com/articles/clash-verge-rev-remote-profile-invalid-yaml/) |
| Hiddify WARP 精确报错 | 添加或连接 WARP 时 `netip.ParsePrefix("/24")`、空 IP 地址前缀解析失败 | [Hiddify WARP 地址前缀排查](https://jiedianshouce.com/articles/hiddify-warp-parseprefix-empty-ip/) |
| Hiddify 订阅后无节点 | 订阅获取、解析、保存与配置选择，不承接 WARP 前缀错误 | [Hiddify 订阅无节点排查](https://jiedianshouce.com/articles/hiddify-subscription-updated-no-nodes/) |
| Hiddify Linux TUN 启动精确故障 | 授权后 `Bad state: exit status 127`、帮助进程或共享库加载阶段；区别于订阅为空和一般安装 | [Hiddify Linux 127 错误排查](https://jiedianshouce.com/articles/hiddify-linux-tun-exit-status-127/) |
| Hiddify 常规使用 | 安装、导入、连接及 WARP 与普通订阅分流 | [Hiddify 完整教程](https://jiedianshouce.com/tools/hiddify/) |
| sing-box 远程规则集冷启动故障 | 核心 `route.rule_set` 远程文件在无缓存启动时下载或解析失败；区别于客户端订阅更新 | [sing-box 远程规则集启动失败排查](https://jiedianshouce.com/articles/sing-box-remote-rule-set-startup-failed/) |
| v2rayN精确报错 | ArgumentOutOfRange_Count、订阅成功但节点列表为空 | [v2rayN节点列表为空排查](https://jiedianshouce.com/articles/v2rayn-argumentoutofrange-count-subscription-empty/) |
| v2rayN内核启动故障 | 运行Core失败、内核进程无法启动 | [v2rayN运行Core失败排查](https://jiedianshouce.com/articles/v2rayn-core-start-failed/) |
| v2rayN macOS TUN跨核心切换端口占用 | 开启TUN期间从sing-box切到Xray后出现 `address already in use`，先核对实际监听端口和进程；一般Core启动故障仍由上页承接 | [v2rayN macOS端口占用排查](https://jiedianshouce.com/articles/v2rayn-macos-tun-core-switch-port-in-use/) |
| v2rayN Geo 文件精确故障 | Xray 启动日志明确显示 geosite.dat 缺失或 EOF；一般 Core 启动失败仍由上页承接 | [v2rayN geosite.dat 排查](https://jiedianshouce.com/articles/v2rayn-geosite-dat-missing/) |
| 2026-11-05 免费节点批次 | 当批公开来源、独立双端测试、下载与证据 | [11月5日测试记录](https://jiedianshouce.com/free-nodes/2026-11-05/) |
| 2026-11-06 免费节点批次 | 四轮公开候选、独立双端测试、最终复测、中文地区名与下载证据 | [11月6日测试记录](https://jiedianshouce.com/free-nodes/2026-11-06/) |
| 2026-11-07 免费节点批次 | 当批480条新候选、38条双端测试、13条初选与剔除失效节点后的12条最终下载 | [11月7日测试记录](https://jiedianshouce.com/free-nodes/2026-11-07/) |
| 2026-11-08 免费节点批次 | 8份公开来源、1338条去重候选、66条双端测试、27条最终下载及原编号20的剔除证据 | [11月8日测试记录](https://jiedianshouce.com/free-nodes/2026-11-08/) |
| FlClash空配置故障 | configuration file config.yaml is empty、切换配置失败、当前配置指针失效 | [FlClash空配置与切换失败排查](https://jiedianshouce.com/articles/flclash-config-yaml-empty-profile-switch/) |
| 订阅转换安全 | Clash订阅转换、V2Ray转Clash、在线转换信任边界 | [订阅转换安全](https://jiedianshouce.com/articles/subscription-conversion-safety/) |
| 移动与高级客户端 | Shadowrocket、Surge、sing-box、v2rayNG | [移动与高级客户端](https://jiedianshouce.com/articles/mobile-advanced-proxy-clients/) |
| AI 与流媒体 | ChatGPT、Claude、Gemini、Codex、Netflix 等逐平台核验 | [AI 与流媒体核验](https://jiedianshouce.com/articles/ai-streaming-airport-verification/) |
| 优惠与试用 | 优惠码、折扣、免费试用与长期付款风险 | [优惠与风险历史](https://jiedianshouce.com/articles/airport-deals-risk-history/) |
| IP 检测 | 出口 IP、ASN、地理位置、住宅标签、DNS 泄漏 | [IP 检测](https://jiedianshouce.com/ip-check/) |

## 维护原则

- 已有Google搜索证据的「机场评级」固定由`/airports/`承接，「枫叶机场」固定由`/airports/maple-relay/`承接。以后日更先对照Search Console和线上页面；没有用户明确要求与可核验事实，不改这两页的URL、标题主体、H1、canonical或主要搜索意图。11月8日按用户要求恢复枫叶原题，旧折扣是否生效仍以结算页为准；恢复标题不等于排名已恢复。
- 其他已有查询或页面展示证据的主页面见[`docs/PROTECTED-SEARCH-PAGES.json`](docs/PROTECTED-SEARCH-PAGES.json)。每次发布前对完整预览运行`python scripts/check_protected_search_pages.py <预览网站目录>`；检查不通过时先核对用户是否明确要求改变该主题，不把加新内容当作改动已有效标题的理由。正文可在证据充分时补答案、来源、FAQ和自然内链，并在7–14天后对照GSC观察。
- 2026-11-08复核：新v2rayN专项只承接macOS TUN跨核心切换后的端口占用，通用Core页保留其他启动失败；系统代理断网页补官方个案与阶段判断。固定免费节点入口展示8号27条，日期页承载当批证据。最近可用GSC仍为10月29日至11月4日268展示、7点击，索引截图67已收录仅是10月23日历史数；11月14日前后按查询、页面和索引状态复盘。
- 2026-11-07夜间聚焦修订：`/airports/`继续承接机场推荐及品牌资料查找，旧版评级顺序只作历史索引；`/articles/airport-recommendation-guide/`承接购买判断方法；`/start/`承接新手首次连接路径。原有免费节点、地区、套餐、线路与客户端故障主页面均保留。GSC最近完整7日为10月29日至11月4日的268展示、7点击；索引报告最后更新10月23日，不能用67已收录代表当前值。11月14日前后按页面及查询复查本次改进。

- 2026-11-07 复核：Clash Verge Rev 远程配置 `invalid yaml` 由新专项页承接，订阅更新失败总排查保留跨客户端阶段入口；更新成功但无节点和TUN断网继续由现有页面承接。7号节点日期页只记录本批双端证据，不替代固定 `/free-nodes/`。最新Search Console查询和索引报告缺失，不能把线上可访问当作已收录；下次取得报告后记录展示、点击、CTR、平均排名及网页索引状态。
- 2026-11-06 日更：Hiddify Linux `exit status 127` 由新专项页承接，安装与订阅为空继续由旧页承接；Clash订阅无节点旧页深修提供者获取阶段。11月6日日期页记录580条抽样配置、57条完成双端测试、44条最终双端复测通过并上线，覆盖13个国家和地区；固定免费节点页保留主入口。Search Console最新查询和索引数据仍缺，不声称新词已收录。
- 2026-11-06 复核：机场榜单现为历史资料参考排序，三家证据不足的品牌暂停参与普通排序；节点罗盘只按旧价格、流量及明示偏好筛选，不证明当前套餐或AI适用。TUN页与系统代理、服务安装故障页各承接不同阶段。无最新Search Console查询与索引数据，不声称本次修订已带来收录。
- 2026-11-05 复核：v2rayN Geo 文件精确故障与一般 Core 启动失败分工；11月5日日期页只记录本批360条去重候选、37条完成双端测试及发布前复测合格的13条，不替代固定免费节点入口。Search Console 当日查询与索引报表未取得，不声称新页面已收录。
- 2026-11-04 复核：sing-box 远程规则集冷启动故障由独立页面承接，移动与高级客户端旧页补配置对象分流；11月4日免费节点日期页记录14份公开来源文件、409条跨历史去重候选、67条完成双端测试、29条通过最终配置复测并上线，不替代固定 `/free-nodes/` 入口。没有完整 Search Console 查询和索引报告，不声称新词已收录。
- 2026-11-03 复核：WARP 前缀解析错误由独立精确页面承接，订阅无节点与完整教程保留各自主意图；11月3日免费节点日期帖只记当批 13/390/28/10 的来源、测试和下载，不替代固定入口。页面上线不等于已被 Google 收录，仍需 Search Console 数据核对。
- 2026-11-02 复核：新增的 `set system dns failed: exit code 1` 页面只承接配置验证后的系统 DNS 写入失败，通用 DNS、TUN 联网失败和服务安装失败继续由原页面承接；免费节点日期页只记录当批双探针事实，不替代固定入口。
- 2026-11-02 质量维护：月付与长期套餐、节点地区、晚高峰测速和优惠核验继续使用原有主页面，通过公开数据与FAQ加深，不拆分“好用机场、机场选择”等同义页面；免费节点固定页只说明当前方法和入口，日期页保留独立批次证据。
- 2026-11-01 复核：已有主页面能够访问，但“有页面”不代表已被 Google 收录。当天为套餐选择、地区节点、线路测试、优惠与试用、AI 与流媒体五个主页面补公开资料或当批证据及其边界；移动客户端页补官方资料和内链。实际结算与退款、四地区同条件对照、昼夜配对测试、AI 和流媒体账号功能测试仍缺证据，不把这些缺口写成结论。
- 每日先核对本表、已有页面和可用的 Search Console 查询；优先深修有展示但证据薄弱的旧页，每次新增文章必须回答另一种具体问题。
- 新文章与深修旧文都应给出可核对来源、核验日期、判断表或步骤、限制、FAQ 和自然内链；机场套餐、线路与免费节点的事实只用当批证据，不用机械换日期或关键词替代。
- 检查标题、描述、正文、结构化数据、站内搜索、RSS、站点地图、移动端与下载入口的一致性；发布后再同步更新记录和仓库。
- 同一搜索意图保留一个主页面，避免多个薄页面互相竞争。
- 新增页面前先确认它解决的是不同问题，并且有足够的公开资料、实测数据或诊断步骤。
- 页面标题、描述、H1、结构化数据、内部链接和移动端排版在发布后统一验收。
- 每次实质更新同步修改 [CHANGELOG.md](CHANGELOG.md)，但不承诺搜索引擎何时收录。
