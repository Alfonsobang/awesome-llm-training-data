# 金融评测数据来源治理

金融 Agent 评测不能只有 URL 列表，还需要数据来源治理层。每个任务都应该明确：允许使用哪些来源、必须保留哪些时间字段、需要哪些引用证据，以及第三方数据是否可以打包，还是只能作为 reference-only 来源。

当前公开 seed 已经包含一个机器可校验的 [source manifest](../examples/financial-agent-eval-seed/data-sources/source-manifest.json)。

## 核心规则

- 公开可访问不等于自动拥有再分发权。
- 外部来源默认使用 `reference_only`。
- 当许可证、隐私或市场数据条款不清楚时，合成 fixture 是更稳妥的默认选择。
- 对时间敏感的任务，必须保留来源日期、检索时间戳，以及适用的 vintage 或期间字段。
- Task spec 应引用受治理的 `source_id`，而不只依赖自然语言说明。
- 在采集或再分发第三方数据前，需要重新核对当前条款和访问要求。

这是一份工程清单，不是法律建议。

## Manifest 字段

| 字段 | 作用 |
| --- | --- |
| `source_id` | Task spec 使用的稳定来源标识。 |
| `source_type` | 监管机构 API、宏观 API、披露平台或合成 fixture。 |
| `official_url` | 官方文档或平台入口。 |
| `access_method` | 公开 API、注册 API key、人工检索或随仓库打包的 fixture。 |
| `packaging_policy` | 数据可否打包，还是只允许 reference-only，或需 review 后使用。 |
| `terms_review_required` | 标记使用前是否需要再次核对当前条款。 |
| `allowed_task_families` | 限定来源可用于哪些任务族。 |
| `temporal_fields` | 保证时间截点完整性所需的日期和 vintage 字段。 |
| `required_citation_fields` | 任务运行时至少应保留的证据字段。 |

## 当前公开来源索引

初始 manifest 以保守方式记录：

- [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
- [FRED Series Observations API](https://fred.stlouisfed.org/docs/api/fred/series_observations.html)
- [World Bank Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)
- [HKEXnews Listed Company Information Title Search](https://www1.hkexnews.hk/search/titlesearch.xhtml?lang=en)
- [CNINFO Disclosure Portal](https://www.cninfo.com.cn/new/index)
- 仓库自有合成 fixture

Manifest 不声称每个外部来源都可以被再分发。它刻意将来源发现和 benchmark 打包分开。

## 校验

运行：

```bash
python examples/financial-agent-eval-seed/validate_sources.py
```

Validator 会检查：

- `source_id` 唯一性，
- 必需治理字段，
- 外部来源是否使用 HTTPS 官方链接，
- 是否显式声明打包策略，
- 时间字段和引用字段，
- 任务与来源映射，
- 来源是否允许被对应任务族使用。

## 对 Harbor 任务的意义

Harbor task 可以校验输出并保留轨迹，但金融 benchmark 仍然需要来源策略。例如：

- 报表 QA 任务应保留文档期间和检索时间。
- 宏观预测任务应保留 vintage 或 real-time 字段。
- 玩具回测应优先使用合成 fixture，除非市场数据再分发条款清晰。
- 浏览器搜索任务应引用文档 URL、发布日期和检索时间。

这个来源治理层与 task verifier、ATIF 轨迹审计是互补关系。
